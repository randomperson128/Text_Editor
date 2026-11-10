try:
    from pathlib import Path
except ModuleNotFoundError:
    print("Install pathlib to delete docs (recomended)")

try:
    from  prompt_toolkit import prompt
except ModuleNotFoundError:
    print("Install prompt_toolkit to use autofill (recomended)")
    with open("Autofill.txt", "w") as file:
        file.write("0")

try:
    import pyperclip
except ModuleNotFoundError:
    print("Install pyperclip to use Copy to clipboard (recomended)")

from random import randint
from colorama import Fore, Back
import climage
import os

#check if autofill enabled 
with open("settings/Autofill.txt", "r") as file:
    Autofill = file.read()

def show_folder(name):
    for item in Path(name).iterdir():
        if item.is_file():
            print(item.name)

def clear_screen():
    os.system('cls')

def text_editor():
    try:
        with open(f"RECOVERY_{doc_name}", "r") as file:
            file.close
            print(f"Recovery file found for {doc_name}")
            RECOVERY_file = True
            RECOVERY_file_text = file.readlines()
    except: RECOVERY_file = False


    with open(f"docs/{doc_name}.txt", "r+") as file:
        if RECOVERY_file == False:
            lines = file.readlines()
        else:
            lines = RECOVERY_file_text

        if not lines:
            lines.append("\n")
        line = 0
        user_typed = ""
        while True:
            print(lines[line].rstrip("\n") + f" | line {line + 1} of {len(lines)}")

            if lines[line][:5] == "!IMG ":
                print(climage.convert(lines[line].rstrip("\n")[5:], is_unicode=True, width=50))

            if Autofill == "1":
                user_typed = prompt("", default=(lines[line].rstrip("\n")))
            elif Autofill == "0":
                user_typed = input("")
            else:
                print("Autofill file error")
                with open("settings/Autofill.txt", "w") as file:
                    file.write("1")
                    print("Please restart")

            
            if randint(1,10) == 1:
                with open(f"RECOVERY_{doc_name}", "w") as recovery:
                    recovery.truncate()
                    recovery.writelines(lines)

                
            if "!U" == user_typed.upper() and line > 0:
                line -= 1

            elif "!D" == user_typed.upper() and line < len(lines) - 1:
                line += 1

            elif "!GT" == user_typed.upper():
                target_line = input("goto: ")
                try:
                    target_line = int(target_line)
                    if target_line < len(lines) and target_line > 0:
                        line = target_line - 1
                    else: print("Invalid")

                except ValueError: print("Invalid")

            elif "!IMG" == user_typed.upper():
                input("Please insert image in images folder\nPress ENTER to continue")

                while True:
                    show_folder("images")
                    img = "images/" + input("\n Enter image name including (.png .jpg .jpeg .webp .bmp .gif): ")

                    if img == "images/":
                        break

                    try:
                        IMG = climage.convert(img, is_unicode=True, width=50)
                        print(IMG)
                        if input("Is this correct?(Y/n): ").lower() == "y":

                            lines[line] = f"!IMG {img}" + "\n"
                            if line == len(lines) - 1:
                                lines.append("\n")
                            line += 1
                            break

                    except FileNotFoundError:
                        print("Image not found")


                

            elif "!VA" == user_typed.upper():
                print("".join(lines).rstrip("\n"))

            elif "!QUIT" == user_typed.upper():
                clear_screen()
                try:
                    Path.unlink(f"RECOVERY_{doc_name}")
                except: pass
                break

            elif not user_typed.upper() == "!U" or not user_typed.upper() == "!D":
                lines[line] = user_typed + "\n"
                if line == len(lines) - 1:
                    lines.append("\n")
                line += 1

        file.seek(0)
        file.truncate()
        file.writelines(lines)



# =================================================

# MAIN MENU

# =================================================

while True:
    while True:
        while True:
            print("Select an option\n1. New doc\n2. Load doc\n3. Delete doc\n4. Copy doc\n5. Quit\n6. Settings")
            mode = input("")
            try:
                mode = int(mode)
                if mode <= 6 and mode >= 1:
                    break
                else: print("Invaild option\n")
            except ValueError:
                print("Invaild option\n")

        if mode == 1:
            while True:
                doc_name = input("Enter name for doc: ")
                try:
                    with open(f"docs/{doc_name}.txt", "r"): #should crash if file dosen't exist.
                        print(f"{doc_name} already exist!")
                except FileNotFoundError:
                    if doc_name == "":
                        break
                    if len(doc_name.split(" ")) > 1: #check for " "'s
                        print("Invalid name, please don't use spaces.")
                        break
                    
                    print(f"Creating {doc_name}.txt")
                    with open(f"docs/{doc_name}.txt", "w"):
                        pass
                    text_editor()
                    break
            break

        elif mode == 2:
            print("docs:\n")
            show_folder("docs")

            while True:
                doc_name = input("Enter doc name: ")
                try:
                    with open(f"docs/{doc_name}.txt", "r"): #should crash if file dosen't exist.
                        print(f"Opening {doc_name}.txt")
                    text_editor()
                    break
                except FileNotFoundError:
                    if doc_name == "":
                        break
                    print(f"{doc_name}.txt doesn't exist!")
            break

        elif mode == 3:
            while True:
                print("docs:\n")
                show_folder("docs")
                doc_name = input("Enter name of doc to delete: ")
                try:
                    with open(f"docs/{doc_name}.txt", "r"): #should crash if file dosen't exist.
                        pass
                    if input(f"Delete {doc_name}.txt?(y/N): ").lower() == "y":
                        Path(f"docs/{doc_name}.txt").unlink()
                        print(f"Deleted {doc_name}.txt")
                    break
                except FileNotFoundError:
                    if doc_name == "":
                        break
                    print(f"{doc_name}.txt doesn't exist!")

        elif mode == 4:
            show_folder("docs")
            doc_name = input("Enter doc name: ")
            try:
                with open(f"docs/{doc_name}.txt", "r") as ImLokeyKindaTired: #should crash if file dosen't exist.
                    print(f"Copying {doc_name}.txt")

                    text = ImLokeyKindaTired.read()
                    pyperclip.copy(text)
                break
            except FileNotFoundError:
                if doc_name == "":
                    break
                print(f"{doc_name}.txt doesn't exist!")   

        elif mode == 5:
            quit()

        elif mode == 6: #settings
            while True:
                print("Settings\n1. Autofill\n2. Background\n3. Foreground")
                mode = input("")
                if mode == "":
                    break
                try:
                    mode = int(mode)
                    if mode <= 3 and mode >= 1:
                        break
                    else: print("Invaild option\n")
                except ValueError:
                    print("Invaild option\n")

            if mode == 1:
                if Autofill == "1":

                    with open("settings/Autofill.txt", "w") as file:
                        file.write("0")
                    Autofill = "0"
                    print("turned off autofill.")

                elif Autofill == "0":

                    with open("settings/Autofill.txt", "w") as file:
                        file.write("1")
                    Autofill = "1"
                    print("turned on autofill.")

            elif mode == 2:
                
                while True:
                    print("1. Red   2. Blue   3. Green   4. Yellow    5. Black   6. White   7. Cancel")
                    mode = input("")
                    if mode == "":
                        break
                    try:
                        mode = int(mode)
                        if mode <= 7 and mode >= 1:
                            break
                        else: print("Invaild option\n")
                    except ValueError:
                        print("Invaild option\n")

                if mode == 1:
                    print(Back.RED +"")
                elif mode == 2:
                    print(Back.BLUE +"")
                if mode == 3:
                    print(Back.GREEN +"")
                if mode == 4:
                    print(Back.YELLOW +"")
                if mode == 5:
                    print(Back.BLACK +"")
                if mode == 6:
                    print(Back.WHITE +"")
                    print("What is wrong with you?")
                if mode == 7:
                    pass

            elif mode == 3:
                
                while True:
                    print("1. Red   2. Blue   3. Green   4. Yellow    5. Black   6. White   7. Cancel")
                    mode = input("")
                    if mode == "":
                        break
                    try:
                        mode = int(mode)
                        if mode <= 7 and mode >= 1:
                            break
                        else: print("Invaild option\n")
                    except ValueError:
                        print("Invaild option\n")

                if mode == 1:
                    print(Fore.RED +"")
                elif mode == 2:
                    print(Fore.BLUE +"")
                if mode == 3:
                    print(Fore.GREEN +"")
                if mode == 4:
                    print(Fore.YELLOW +"")
                if mode == 5:
                    print(Fore.BLACK +"")
                if mode == 6:
                    print(Fore.WHITE +"")
                if mode == 7:
                    pass
