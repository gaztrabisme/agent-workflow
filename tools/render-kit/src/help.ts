const common = `Render options:
  --root <dir>             Serve local relative assets from this root
  --width <px>             Viewport width
  --height <px>            Viewport height
  --scale <n>              Device pixel ratio
  --at <ms|end>            Scene time to render
  --settle <ms>             Settle time when --at end
  --boot <ms>               Page time to run after load
  --media <screen|print>   Media type for PDF output
  --wait-for <selector>    Wait for a selector after load
  --timeout <ms>            Load and wait timeout
  --allow-network           Allow requests to other origins`;

const help: Record<string, string> = {
  global: `Usage: rk <command> [options]

Commands:
  render <input> --out <file.png|file.pdf> [render options] [--simulate <type>]
  check <input> [render options] [--checks <ids>] [--threshold <id.name=n>] [--pdf] [--out-dir <dir>] [--strict]
  text measure --font <css font> --text <string> [--font-file <path>]
  text wrap --font <css font> --text <string> --width <px> [--line-height <n>] [--max-lines <n>] [--format json|svg] [--x <n> --y <n>] [--font-file <path>]
  brief <input> --questions <file> --out-dir <dir> [--purpose <text>] [--simulate <types>] [--checks <ids>] [--threshold <id.name=n>] [render options]
  brief --verify <answers.json> [--strict]
  selftest [--strict]

Global option: --help
Run rk <command> --help for that command's flags. Use rk text <measure|wrap> --help for text flags.
Use rk help <command> for the same help, or rk help for this list.

${common}`,
  render: `Usage: rk render <input> --out <file.png|file.pdf> [render options] [--simulate <type>]

  --out <file>              Output PNG or PDF path
  --simulate <type>         PNG vision simulation: protanopia, deuteranopia, tritanopia, achromatopsia

${common}`,
  check: `Usage: rk check <input> [render options] [--checks <ids>] [--pdf] [--out-dir <dir>] [--strict]

  --checks <ids>            Comma-separated check ids
  --threshold <id.name=n>   Override a named check threshold (repeatable)
  --pdf                     Also render and check PDF fonts
  --out-dir <dir>           Output directory (default: temporary directory)
  --strict                  Treat skipped checks as failures

${common}`,
  brief: `Usage: rk brief <input> --questions <file> --out-dir <dir> [--purpose <text>] [--simulate <types>] [--checks <ids>] [--threshold <id.name=n>] [--pdf] [render options]
       rk brief --verify <answers.json> [--strict]

  --questions <file>        Question set for the reviewer
  --out-dir <dir>           Directory for the brief, report, and images
  --purpose <text>          Short description of the artifact
  --simulate <types>        Comma-separated vision simulations
  --pdf                     Also render the PDF and one PNG per PDF page
  --checks <ids>            Comma-separated check ids
  --threshold <id.name=n>   Override a named check threshold (repeatable)
  --verify <file>           Verify a completed answers file
  --strict                  Treat unsure and not-judged answers as failures

${common}`,
  selftest: `Usage: rk selftest [--strict]

  --strict                  Treat skipped checks as failures`,
  text: `Usage: rk text <measure|wrap> [options]

Subcommands:
  measure --font <css font> --text <string> [--font-file <path>]
  wrap --font <css font> --text <string> --width <px> [--line-height <n>] [--max-lines <n>] [--format json|svg] [--x <n> --y <n>] [--font-file <path>]

Use rk text measure --help or rk text wrap --help for details.`,
  'text measure': `Usage: rk text measure --font <css font> --text <string> [--font-file <path>]

  --font <css font>         CSS font shorthand
  --text <string>           Text to measure
  --font-file <path>        Register a font file before measuring`,
  'text wrap': `Usage: rk text wrap --font <css font> --text <string> --width <px> [options]

  --font <css font>         CSS font shorthand
  --text <string>           Text to wrap
  --width <px>              Maximum line width
  --line-height <n>         Line-height multiplier (default 1.2)
  --max-lines <n>           Maximum line count
  --format <json|svg>       Output format
  --x <n> --y <n>           SVG text position
  --font-file <path>        Register a font file before wrapping`,
};

export function helpText(command?: string, subcommand?: string) {
  if (!command) return help.global;
  if (command === 'text') return help[subcommand ? `text ${subcommand}` : 'text'] ?? help.text;
  return help[command] ?? help.global;
}
