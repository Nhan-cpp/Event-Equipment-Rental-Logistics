from ui.mainMenu import mainMenu
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    Menu = mainMenu()
    Menu.display()
    Menu.saveAll()

if __name__ == "__main__":
    main()