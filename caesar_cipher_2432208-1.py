import os


def box(text):
    """
       Create a box with the specified text centered inside.

       Parameters:
       text : str
           The text to be displayed inside the box.

       Returns:
       str
           A string representing the box with the specified text centered inside.
       """
    width = len(text) + 4  # Calculate the width of the box
    box_element = "┌" + "─" * (width - 2) + "┐\n"  # Top edge of the box
    # Middle part of the box with the text
    box_element += "│ " + text + " │\n"
    box_element += "└" + "─" * (width - 2) + "┘"  # Bottom edge of the box
    return box_element


# color code variables
red = '\033[91m'  # for error
cyan = '\033[36m'  # welcome and thankyou
GREEN = '\033[92m'  # result
reset = '\033[0m'  # reset to default white



def welcome():
    """
       Print a welcome message for the Caesar Cipher program.

       This function prints a welcome message for the Caesar Cipher program,
       including the program title and a brief description.

    """
    print(cyan + box("     *** Welcome to the Caesar Cipher By Aryan Neupane ***     ") + reset)
    print(cyan + box("This program encrypts and decrypts text with the Caesar Cipher.") + reset)


def encrypt(shift_code, input_text):
    """
      Encrypt the input text using the Caesar Cipher algorithm.

      Parameters
      shift_code : int
          The shift code to be used for encryption.
      input_text : str
          The text to be encrypted.

      Returns
      str
          The encrypted text.

      """
    return decrypt(-shift_code, input_text)


def decrypt(shift_code, input_text):
    """
       Decrypt the input text using the Caesar Cipher algorithm.

       Parameters
       shift_code : int
           The shift code to be used for decryption.
       input_text : str
           The text to be decrypted.

       Returns
       str
           The decrypted text.

       """
    resultant_text = ''
    for char in input_text:
        if char.isalpha():
            x = ord(char) - ord('a')
            y = (x - shift_code) % 26
            resultant_text += chr(y + ord('a'))
        else:
            resultant_text += char
    return resultant_text.upper()


def process_file(file_name, mode="encrypt or decrypt"):
    """
        Process the specified file for encryption or decryption.

        This function prompts the user to enter a shifting code and then processes the
        contents of the specified file for encryption or decryption based on the provided mode.

        Parameters
        file_name : str
            The name of the file to be processed.
        mode : str, optional
            The mode for processing the file, either "encrypt" or "decrypt". Default is "encrypt".

    """
    while True:
            print(box("Enter Shifting code"))
            print("Enter Your Shifting Code >>> ", end="")
            shift = input()
            if shift.isdigit():
                shift=int(shift)
                with open(file_name, "r") as file:
                    file_content = (file.read()).lower()
                    if mode == "d":
                        write_message(decrypt(shift, file_content))
                        print(GREEN+box("File Decryption Successful Check result.txt")+reset)
                    else:
                        write_message(encrypt(shift, file_content))
                        print(GREEN+box("File Encryption Successful Check result.txt")+reset)

                break
            else:
                print(red + box("Shifting code must be a numeric value") + reset)

def is_file(file):
    """
       Check if the specified file exists.

       Parameters
       file : str
           The path of the file to be checked.

       Returns
       bool
           True if the file exists, False otherwise.
       """
    return os.path.exists(file)


def write_message(string):
    """
       Write a string to a file named "result.txt".

       Parameters
       string : str
           The string to be written to the file.
       """
    with open("result.txt", "w") as file:
        file.write(string)


def enter_message(mode):
    """
       Prompt the user to enter text and a shifting code for encryption or decryption.

       This function prompts the user to enter text and a shifting code for encryption or decryption.
       It then performs the encryption or decryption operation based on the provided mode.

       Parameters
       mode : str
           The mode for encryption or decryption, either "e" for encryption or "d" for decryption.
       """
    print(box("Enter text you wand to input"))
    print("Enter your Text >>>", end="")
    input_text = (input()).lower()
    while True:
        print(box("Enter Shifting code"))
        print("Enter your Code >>>", end="")
        shift = input()
        if shift.isdigit():
            shift=int(shift)
            if mode == "e":
                print(GREEN + "Result >>> " + reset)
                print(GREEN + box(encrypt(shift, input_text)) + reset)
            elif mode == "d":
                print(GREEN + "Result >>> " + reset)
                print(GREEN + box(decrypt(shift, input_text)) + reset)
            else:
                print(red + box("Invalid Input given PLease choose correct mode") + reset)
                # print(box("Would you like to encrypt (e) console message or decrypt (d) console message or exit(x) to exit"))
                # print("Enter your Choice >>>", end="")
                # mode = input()
            break
        else:
            print(red+box("Shifting code must be a numeric value")+reset)


def message_or_file():
    """
       Prompt the user to choose between encrypting or decrypting text, and selecting input method (console or file).

       This function continuously prompts the user to choose between encrypting or decrypting text,
       and then selecting the input method (console or file) for the chosen operation.
       It then calls the appropriate function based on the user's choices.

    """
    while True:
        print(box("Would you like to encrypt (e) or decrypt (d) or exit(x) to exit"))
        print("Enter Your Choice >>> ", end="")
        mode = input().lower()
        if mode == "e" or mode == "d":
            while True:
                print(box("Enter (c) for console or (f) for file"))
                print("Enter your Choice >>>", end="")
                file_or_message = (input()).lower()
                if file_or_message == "c":
                    enter_message(mode)
                    break
                elif file_or_message == "f":
                    while True:
                        print(box(f"Enter File: {red}Name{reset} if same  Directiory {red}Path{reset} if another directory"))
                        print("Enter your desired file name >>> ", end="")
                        file_name = input()
                        if is_file(file_name):
                            process_file(file_name, mode)
                            break
                        else:
                            print(red + box("*** File not found please enter correct file name ***") + reset)
                    break
                else:
                    print(red + box("*** Please Choose correct mode ***") + reset)

        elif mode == "x":
            break
        else:
            print(red + box("*** please choose correct mode ***") + reset)


def main():
    """
      Run the Caesar Cipher program.

      This function starts the Caesar Cipher program by displaying a welcome message,
      prompting the user to choose between encrypting or decrypting text and selecting the input method.
      After each operation, it asks the user if they want to continue using the cipher.
      If the user chooses not to continue, it displays a thank you message and exits the program.

      """
    welcome()
    while True:
        message_or_file()
        print(cyan + box("Do You Want To Use The Cipher Again y to continue or any keys to exit") + reset)
        print("Enter your Choice >>>", end="")
        r = (input().lower())
        if r != "y":
            print(cyan + box("*** Thankyou ***") + reset)
            break


if __name__ == "__main__":
    main()
