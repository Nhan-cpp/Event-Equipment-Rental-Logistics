# ─────────────────────────────────────────────────
# ANSI Color Constants
# ─────────────────────────────────────────────────
RESET       = "\033[0m"
BOLD        = "\033[1m"

# Normal colors
RED         = "\033[31m"
GREEN       = "\033[32m"
YELLOW      = "\033[33m"
BLUE        = "\033[34m"
MAGENTA     = "\033[35m"
CYAN        = "\033[36m"
WHITE       = "\033[37m"

# Bright colors
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"
BRIGHT_BLACK   = "\033[90m"

# ─────────────────────────────────────────────────
# UI Component Functions (inspired by fcode-violation-management-system)
# ─────────────────────────────────────────────────

def UI_Header(title, color=CYAN):
    """
    ╭────────────────────────────────────────────────╮
    │ TITLE                                          │
    ╰────────────────────────────────────────────────╯
    """
    width = 50
    print(f"\n{color}╭{'─' * width}╮{RESET}")
    print(f"{color}│{BOLD}{BRIGHT_WHITE} {title:<{width - 1}}{RESET}{color}│{RESET}")
    print(f"{color}╰{'─' * width}╯{RESET}")

def UI_Card_Start(title, color=CYAN):
    """
    ╭──────────── TITLE ─────────────╮
    """
    width = 50
    title_len = len(title)
    side = (width - title_len - 2) // 2
    remainder = width - title_len - 2 - side
    print(f"\n{color}╭{'─' * side} {BOLD}{BRIGHT_WHITE}{title}{RESET}{color} {'─' * remainder}╮{RESET}")

def UI_Card_End(color=CYAN):
    """
    ╰────────────────────────────────────────────────╯
    """
    width = 50
    print(f"{color}╰{'─' * width}╯{RESET}")

def UI_Menu_Item(index, label, color=CYAN):
    """
    │ [1] LABEL                                      │
    """
    width = 50
    if index >= 0:
        text = f"[{index}] {label}"
    else:
        text = label
    print(f"{color}│ {BOLD}{BRIGHT_CYAN}{text:<{width - 1}}{RESET}{color}│{RESET}")

def UI_Divider(color=CYAN):
    """
    ├────────────────────────────────────────────────┤
    """
    width = 50
    print(f"{color}├{'─' * width}┤{RESET}")

def UI_Prompt(label, glyph="❯"):
    """
      ❯ Label          : 
    """
    print(f"{BOLD}{YELLOW}  {glyph} {label:<15} {RESET}: ", end="")

def UI_Return_Prompt():
    """
      ❯ Press Enter to return... 
    """
    input(f"\n{BOLD}{YELLOW}  ❯ Press Enter to return... {RESET}")

def UI_Success(message):
    print(f"{BRIGHT_GREEN}  ✔ {message}{RESET}")

def UI_Error(message):
    print(f"{BOLD}{RED}  ✖ {message}{RESET}")

def UI_Warning(message):
    print(f"{BOLD}{BRIGHT_YELLOW}  [!] {message}{RESET}")

# ─────────────────────────────────────────────────
# Table Components
# ─────────────────────────────────────────────────

def UI_Table_Header(headers, widths, color=CYAN):
    """
      ╭──────┬────────────┬─────────╮
      │ H1   │ H2         │ H3      │
      ├──────┼────────────┼─────────┤
    """
    # Top border
    top = f"  {color}╭"
    for i, w in enumerate(widths):
        top += "─" * (w + 2)
        top += "┬" if i < len(widths) - 1 else "╮"
    print(f"{top}{RESET}")

    # Header row
    row = f"  {color}│{RESET}"
    for i, h in enumerate(headers):
        row += f" {BOLD}{h:<{widths[i]}}{RESET} {color}│{RESET}"
    print(row)

    # Separator
    sep = f"  {color}├"
    for i, w in enumerate(widths):
        sep += "─" * (w + 2)
        sep += "┼" if i < len(widths) - 1 else "┤"
    print(f"{sep}{RESET}")

def UI_Table_Row(values, widths, color=CYAN):
    """
      │ V1   │ V2         │ V3      │
    """
    row = f"  {color}│{RESET}"
    for i, v in enumerate(values):
        row += f" {v:<{widths[i]}} {color}│{RESET}"
    print(row)

def UI_Table_End(widths, color=CYAN):
    """
      ╰──────┴────────────┴─────────╯
    """
    bottom = f"  {color}╰"
    for i, w in enumerate(widths):
        bottom += "─" * (w + 2)
        bottom += "┴" if i < len(widths) - 1 else "╯"
    print(f"{bottom}{RESET}")

def UI_Table_Total(count):
    print(f"  {BRIGHT_WHITE}Total: {count} record(s){RESET}")
