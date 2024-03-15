def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
    except Exception as e:
        print("Error occurred while creating file:", e)

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File Contents:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access file.")
    except Exception as e:
        print("Error occurred while reading file:", e)

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("67890\n")
            file.write("Appending another line here\n")
    except Exception as e:
        print("Error occurred while appending to file:", e)

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()
    read_and_display()
