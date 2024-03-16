fail_handli = "fail_handlin.txt"
def write_to_file (fail_handli, content):
    """
    Writes content to a file in a write mode
    
    Args:
    filename: the name of the file to write to.
    content: the content to be written to the file (string or list of strings).
    
    """
    if isinstance(content, str): #handle single string input
        with open(fail_handli, "w") as file:
            try:
                file.write(content)
            except FileNotFoundError:
                print(f"Error: File '{fail_handli}' not found.")
            except PermissionError:
                print(f"Error: Insufficient permissions to write to '{fail_handli}'.")
            except Exception as e: #Catch other unexpected errors
                print(f"An Error occurred: {e}")

    else: #Handle list of strings
        with open(fail_handli, "w") as file:
            for line in content:
                file.write(line) #Adds a newline after each line
                print(f"Successfully wrote to {fail_handli}")
   

def read_from_file(fail_handli):
    """
    Reads the contents of a file and displays them on the console.

    Args:
        filename: The name of the file to read from.
    """
    with open(fail_handli, "r") as file:
        try:
            content = file.read()
            print(f"Contents of '{fail_handli}':\n{content}")
        except FileNotFoundError:
            print(f"Error: File '{fail_handli}' not found.")
        except PermissionError:
            print(f"Error: Insufficient permissions to read from '{fail_handli}'.")
        except Exception as e:  # Catch other unexpected errors
            print(f"An error occurred: {e}")
    
def append_to_file (fail_handli, content):
    """
    Appends content to a file in append mode (a).

    Args:
        filename: the name of the file to append to.
        content: the content to be appendend to the file (String or List of Strings).
    """
    if isinstance(content, str): #Handle single string input
        with open(fail_handli, "a") as file:
            try:
                file.write(content)
                    # else: #Handle list of strings
                    #     for line in content:
                    #         file.write(line + "\n") #Add newline after each line
                    # print(f"Successfully appended to '{fail_handli}'") 
            except FileNotFoundError:
                print(f"Error: File '{fail_handli}' not found.")
            except PermissionError:
                print(f"Error: Insufficient permissions to append to '{fail_handli}'.")
            except Exception as e:  # Catch other unexpected errors
                print(f"An error occurred: {e}") 
    else:  # Handle list of strings
        with open(fail_handli, "a") as file:
                for line in content:
                    file.write(line + "\n")  # Add newline after each line
                    print(f"Successfully appended to '{fail_handli}'")


#Create the file
write_to_file(fail_handli, ["Line 1: This is some text.\n", "Line 2: You can write numbers too: 67.\n", "Line 3: And mixed data types.\n"])


#Read and display the contents
read_from_file(fail_handli)
      

# File Appending
content_to_append = ["Appended line 1\n", "Appended line 2\n", "Appended line 3\n"]
append_to_file(fail_handli, content_to_append)

# Read the final contents
read_from_file(fail_handli)