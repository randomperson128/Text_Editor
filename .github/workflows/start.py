


with open("settings/a.txt", "r") as file:
    code = str(file.readline())
    file.close()

if code == "1":
        print("Here's a simple explination on how to use the program\n!GT - go to a desired line.\n!U - go up\n!D go down \n!VA to view all \n!QUIT to quit\n\nDO NOT EXIT WITHOUT TYPING !QUIT")
        if input("Don't show this message again (Y/n): ").lower == "y":
            with open("settings/a.txt", "w") as file:
                file.close()