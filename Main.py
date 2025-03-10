import pyfiglet
import shutil
import os
import subprocess  # Import subprocess for executing external scripts

# Define colors using ANSI escape codes
bold = "\033[1m"
cyan = "\033[36m"
green = "\033[32m"
yellow = "\033[33m"
red = "\033[31m"
blue = "\033[34m"
reset = "\033[0m"

# Get terminal width for centering
terminal_width = shutil.get_terminal_size().columns

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    """Display the welcome banner."""
    banner = pyfiglet.figlet_format("Welcome to MalBuster", font="slant")
    banner_lines = banner.split("\n")
    centered_banner = "\n".join(line.center(terminal_width) for line in banner_lines)
    print(f"{bold}{cyan}╔{'═' * (terminal_width - 2)}╗{reset}")
    print(f"{bold}{green}{centered_banner}{reset}")
    print(f"{bold}{cyan}╚{'═' * (terminal_width - 2)}╝{reset}")

def display_info():
    """Display developer information."""
    print(f"{bold}{yellow}Developer:{reset} Khalid Alabsi")
    print(f"{bold}{yellow}Contact:{reset} khaled.s.alabsi@gmail.com")
    print(f"{bold}{yellow}GitHub:{reset} https://github.com/b0yx")
    print(f"{bold}{cyan}─{'─' * (terminal_width - 2)}─{reset}")

def display_menu():
    """Display the menu options."""
    print(f"{bold}{blue}1- Malware Analysis:{reset}")
    print(f"{bold}{blue}2- System Analysis:{reset}")
    print(f"{bold}{blue}3- Network Analysis:{reset}")
    print(f"{bold}{blue}4- Log Analysis:{reset}")
    print(f"{bold}{blue}5- Threat Intelligence:{reset}")
    print(f"{bold}{blue}6- Settings:{reset}")
    print(f"{bold}{red}0- Exit:{reset}")

def display_footer():
    """Display the footer."""
    print(f"{bold}{cyan}─{'─' * (terminal_width - 2)}─{reset}")
    print(f"{bold}{green} Thank you for using Malbuster!{reset}")
    print(f"{bold}{cyan}─{'─' * (terminal_width - 2)}─{reset}")

def launch_script(script_name):
    """Launch an external script using subprocess."""
    try:
        subprocess.run(["python", script_name], check=True)
    except FileNotFoundError:
        print(f"{bold}{red}Error: {script_name} not found!{reset}")
    except Exception as e:
        print(f"{bold}{red}An error occurred: {e}{reset}")

def submenu(choice):
    """Handle the user's choice by launching the corresponding script."""
    clear_screen()  # Clear the screen before launching the script
    if choice == 1:
        print(f"{bold}{blue}Launching Malware Analysis...{reset}")
        launch_script("MalwareAnalysis/MalwareAnalysis.py")
    elif choice == 2:
        print(f"{bold}{blue}Launching System Analysis...{reset}")
        launch_script("SystemAnalysis.py")
    elif choice == 3:
        print(f"{bold}{blue}Launching Network Analysis...{reset}")
        launch_script("NetworkAnalysis.py")
    elif choice == 4:
        print(f"{bold}{blue}Launching Log Analysis...{reset}")
        launch_script("LogAnalysis.py")
    elif choice == 5:
        print(f"{bold}{blue}Launching Threat Intelligence...{reset}")
        launch_script("ThreatIntelligence.py")
    elif choice == 6:
        print(f"{bold}{blue}Launching Settings...{reset}")
        launch_script("Settings.py")
    elif choice == 0:
        print(f"{bold}{red}Exiting...{reset}")
        exit()
    else:
        print(f"{bold}{red}Invalid choice. Please try again.{reset}")

    input(f"{bold}{yellow}Press Enter to return to the main menu...{reset}")
    clear_screen()
    menu()  # Return to the main menu

def menu():
    """Display the main menu and handle user input."""
    display_banner()
    display_info()
    display_menu()
    display_footer()

    try:
        choice = int(input(f"{bold}{yellow}Enter your choice (0-6):{reset} "))
        if choice > 6 or choice < 0:
            print("\n")
            print(f"{red}{bold}---------------------------------")
            print(f"{bold}{red}Wrong Choice. Please try again.... ")
            print(f"{red}{bold}----------------------------------")
            input(f"{bold}{yellow}Press Enter to continue...{reset}")
            clear_screen()
            menu()
        else:
            submenu(choice)
    except ValueError:
        print(f"{bold}{red}Invalid input. Please enter a number.{reset}")
        input(f"{bold}{yellow}Press Enter to continue...{reset}")
        clear_screen()
        menu()
    except KeyboardInterrupt:
        print(f"{bold}{red}\nExiting...{reset}")
        exit()

if __name__ == "__main__":
    clear_screen()
    menu()
