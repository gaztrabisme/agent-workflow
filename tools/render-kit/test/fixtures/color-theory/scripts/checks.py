import sys

mode = sys.argv[1]
focal = sys.argv[sys.argv.index('--focal') + 1]
x0, y0, x1, y1 = [int(n) for n in focal.split(',')]
share = max(0, x1 - x0) * max(0, y1 - y0)
if mode == 'value':
    print(f'Focal box covers {share} pixels and holds 30.0% of the value-edge energy (0.75x its area share of value edges).')
    print('T1 FAIL (default: focal box holds at least 2x its area share of value edges).')
elif mode == 'chroma':
    if x1 - x0 > 320:
        print('ring 5 (distance 120-160px): mean OKLCH C 0.001')
        print('Focal box mean C 0.002; outermost ring 0.000.')
        print('T5 CHECK (default: the focal box is at least as chromatic as every ring outside it).')
    else:
        print('Focal box mean C 0.020; outermost ring 0.000.')
        print('T5 PASS (default: the focal box is at least as chromatic as every ring outside it).')
