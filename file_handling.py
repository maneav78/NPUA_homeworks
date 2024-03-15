import os


def get_name():
    while True:
        file_name = input("Give the file name you want to open: ")
        if is_valid(file_name):
            return file_name
        else:
            print("Please enter a valid file name.")


def is_valid(file):
    full_path = "./" + file
    if os.path.exists(full_path):
        return True
    else:
        return False


file_name = get_name()
try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file you want to open doesn't exist! Please give a valid file.")
except ValueError:
    print("Please enter a valid file name")
except Exception as e:
    print("An error occurred", e)
    print("Please enter a valid file name")

is_same = bool(int(input("Do you want to write in the same file or you want to change the file?(Enter 0 for changing file and 1 for opposite choice): ")))
if not is_same:
    file_name = get_name()
content = "\n" + input("Give a content: ")
try:
    with open(file_name, "a") as file:
        file.write(content)
except FileNotFoundError:
    print("The file you want to open doesn't exist! Please give a valid file.")
except Exception as e:
    print("An error occurred", e)
    print("Please enter a valid file name")
else:
    print("The writing is successful")
finally:
    print("The file was closed")
    #I dont close the file because in with statement it isn't necessary