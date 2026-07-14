RESET       = "\033[0m"
BOLD        = "\033[1m"

RED         = "\033[31m"
GREEN       = "\033[32m"
YELLOW      = "\033[33m"
MAGENTA     = "\033[35m"
CYAN        = "\033[36m"
WHITE       = "\033[37m"

def UI_Header(title : str, color=CYAN):

    width = 50
    print(f"\n{color}╭{'─' * width}╮{RESET}")
    print(f"{color}│{BOLD}{WHITE} {title:<{width - 1}}{RESET}{color}│{RESET}")
    print(f"{color}╰{'─' * width}╯{RESET}")

def UI_Card_Start(title, color=CYAN):

    width = 50
    title_len = len(title)
    side = (width - title_len - 2) // 2
    remainder = width - title_len - 2 - side
    print(f"\n{color}╭{'─' * side} {BOLD}{WHITE}{title}{RESET}{color} {'─' * remainder}╮{RESET}")

def UI_Card_End(color=CYAN):

    width = 50
    print(f"{color}╰{'─' * width}╯{RESET}")

def UI_Menu_Item(index, label, color=CYAN):

    width = 50
    if index >= 0:
        text = f"[{index}] {label}"
    else:
        text = label
    print(f"{color}│ {BOLD}{WHITE}{text:<{width - 1}}{RESET}{color}│{RESET}")

def UI_Divider(color=CYAN):

    width = 50
    print(f"{color}├{'─' * width}┤{RESET}")

def UI_Prompt(label):

    print(f"{BOLD}{YELLOW}  ❯ {label:<15} {RESET}: ", end="")

def UI_Return_Prompt():

    input(f"\n{BOLD}{YELLOW}  ❯ Press Enter to return... {RESET}")

def UI_Success(message):
    print(f"{BOLD}{GREEN}  ✔ {message}{RESET}")

def UI_Error(message):
    print(f"{BOLD}{RED}  ✖ {message}{RESET}")

def UI_Warning(message):
    print(f"{BOLD}{YELLOW}  [!] {message}{RESET}")

def UI_Table_Header(headers, widths, color=CYAN):

    top = f"  {color}╭"
    for i, w in enumerate(widths):
        top += "─" * (w + 2)
        top += "┬" if i < len(widths) - 1 else "╮"
    print(f"{top}{RESET}")

    row = f"  {color}│{RESET}"
    for i, h in enumerate(headers):
        row += f" {BOLD}{WHITE}{h:<{widths[i]}}{RESET} {color}│{RESET}"
    print(row)

    sep = f"  {color}├"
    for i, w in enumerate(widths):
        sep += "─" * (w + 2)
        sep += "┼" if i < len(widths) - 1 else "┤"
    print(f"{sep}{RESET}")

def UI_Table_Row(values, widths, color=CYAN):

    row = f"  {color}│{RESET}"
    for i, v in enumerate(values):
        row += f" {WHITE}{v:<{widths[i]}}{RESET} {color}│{RESET}"
    print(row)

def UI_Table_End(widths, color=CYAN):

    bottom = f"  {color}╰"
    for i, w in enumerate(widths):
        bottom += "─" * (w + 2)
        bottom += "┴" if i < len(widths) - 1 else "╯"
    print(f"{bottom}{RESET}")

def UI_Table_Total(count):
    print(f"  {BOLD}{WHITE}Total: {count} record(s){RESET}")
