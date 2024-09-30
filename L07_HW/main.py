from menu import Menu
from run_bash_cmd_function import run_bash_cmd

def main():
    menu = Menu()
    menu.addOption("Checking available memory")
    menu.addOption("Viewing network connections")
    menu.addOption("Displaying free RAM and swap")
    menu.addOption("Quit")

    while True:
        choice = menu.getInput()
        if choice == 4: 
            break
        else:
            run_bash_cmd(choice)

main()