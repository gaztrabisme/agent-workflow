import struct
import zlib

import numpy as np


def read_rgb16(path):
    data = open(path, "rb").read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    pos, chunks, dims = 8, [], None
    while pos < len(data):
        n = struct.unpack(">I", data[pos:pos+4])[0]
        if n > len(data)-pos-12:
            raise ValueError("truncated PNG chunk")
        kind, body = data[pos+4:pos+8], data[pos+8:pos+8+n]
        if kind == b"IHDR":
            dims = struct.unpack(">IIBBBBB", body)
        if kind == b"IDAT":
            chunks.append(body)
        pos += n+12
        if kind == b"IEND":
            break
    if not dims or dims[2] != 16:
        return None
    w, h, _, ctype, comp, filt, interlace = dims
    if ctype not in (0, 2, 4, 6) or comp or filt or interlace:
        raise ValueError("16-bit PNG must be non-interlaced grayscale, gray-alpha, RGB or RGBA")
    channels = {0: 1, 2: 3, 4: 2, 6: 4}[ctype]
    bpp = channels*2
    if w < 1 or h < 1:
        raise ValueError("PNG dimensions must be positive")
    stride = w*channels*2
    expected = h*(stride+1)
    if expected > 512*1024*1024:
        raise ValueError("16-bit PNG decoded data exceeds the 512 MiB safety limit")
    decoder = zlib.decompressobj()
    raw = decoder.decompress(b"".join(chunks), expected+1)
    if len(raw) != expected or decoder.unconsumed_tail or not decoder.eof:
        raise ValueError("invalid or oversized PNG image data")
    rows, prior, offset = [], bytearray(stride), 0
    for _ in range(h):
        ft, scan = raw[offset], bytearray(raw[offset+1:offset+1+stride])
        offset += stride+1
        for i in range(stride):
            a = scan[i-bpp] if i >= bpp else 0
            b = prior[i]
            c = prior[i-bpp] if i >= bpp else 0
            if ft == 1: scan[i] = (scan[i]+a)&255
            elif ft == 2: scan[i] = (scan[i]+b)&255
            elif ft == 3: scan[i] = (scan[i]+((a+b)//2))&255
            elif ft == 4:
                p = a+b-c
                pa, pb, pc = abs(p-a), abs(p-b), abs(p-c)
                predictor = a if pa <= pb and pa <= pc else b if pb <= pc else c
                scan[i] = (scan[i]+predictor)&255
            elif ft != 0: raise ValueError("unsupported PNG filter")
        rows.append(scan); prior = scan
    arr = np.frombuffer(b"".join(rows), dtype=">u2").reshape(h, w, channels)
    if channels <= 2:
        return np.repeat(arr[..., :1], 3, axis=-1).astype(np.uint16)
    return arr[..., :3].astype(np.uint16)


def _chunk(kind, body):
    payload = kind+body
    return struct.pack(">I", len(body))+payload+struct.pack(">I", zlib.crc32(payload)&0xffffffff)


def write_rgb16(path, rgb):
    rgb = np.clip(np.rint(rgb*65535), 0, 65535).astype(">u2")
    h, w = rgb.shape[:2]
    scan = b"".join(b"\0"+row.tobytes() for row in rgb)
    header = struct.pack(">IIBBBBB", w, h, 16, 2, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n"+_chunk(b"IHDR", header))
        f.write(_chunk(b"IDAT", zlib.compress(scan, 6))+_chunk(b"IEND", b""))
