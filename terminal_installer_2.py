import os
import subprocess

commands = {"terminal": {"dependencies": None,
                          "command": [ "winget install Microsoft.WindowsTerminal --accept-source-agreements" ]
                    },
            "git": {"dependencies": None,
                    "command": [ "winget install git --accept-source-agreements" ]
                    },
            "nvim": {"dependencies": [ "git" ],
                     "command": [ "winget install nvim --accept-source-agreements",
                                  "git clone --depth 1 https://github.com/AstroNvim/AstroNvim $env:LOCALAPPDATA\\nvim" ]
                    },
            "rust": {"dependencies": None,
                     "command": [ "winget install -e --id Rustlang.Rustup --accept-source-agreements",
                                     "rustup toolchain install stable-x86_64-pc-windows-gnu",
                                     "rustup default stable-x86_64-pc-windows-gnu" ]
                    },
            "python_custom_modules": {"dependencies": None,
                                      "command": [ "pip install -r requirements.txt" ]
                    },
            "python_default_modules": {"dependencies": None,
                                       "command": [ "pip install numpy matplotlib pandas pygame" ]
                    },
            "curseforge": {"dependencies": None,
                           "command": [ "winget install CurseForge --accept-source-agreements" ]
                    },
            "vscode": {"dependencies": None,
                       "command": [ 'winget install "Microsoft Visual Studio Code" --accept-package-agreements --accept-source-agreements' ]
                    },
            "vscode2": {"dependencies": None,
                       "command": [ 'winget install "XP9KHM4BK9FZ7Q" --accept-package-agreements --accept-source-agreements' ]
                    },
            "copilot": {"dependencies": [ "vscode" ],
                        "command": [ "code --install-extension github.copilot" ]
                    },
            
            }

def run_command(command_list):
    for command in command_list:
        os.system('powershell -Command "' + command + '"')

def run_command2(command_list):
    for command in command_list:
        print(subprocess.run(["powershell", "-Command", command], capture_output=True, text=True))
        print("done")

def install_dependencies(name):
    if commands[name]["dependencies"]:
        print("has dependencies")
        for dependency in commands[name]["dependencies"]:
            print("installing " + dependency)
            install_dependencies(dependency)
    run_command2(commands[name]["command"])

def show_commands():
    print("commands: dependencies")
    for command in commands:
        print(command + ": " + str(commands[command]["dependencies"]))
    print("exit")

def main():
    show_commands()
    while True:
        command = input("Enter command: ")
        if command == "exit":
            print("Exiting")
            break
        elif command in commands:
            install_dependencies(command)
        else:
            print("Command not found")


if __name__ == "__main__":
    main()
