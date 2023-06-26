# You are tasked with creating a Python program that interacts with environment variables and performs various operations on directories using the os module. The program should have the following functionality:
#
# Display the current working directory.
# Change the working directory to a specified path.
# Create a new directory at a specified path.
# Remove a directory or file at a specified path.
# You need to create a class called DirectoryManager that encapsulates these operations. The class should have the following methods:
#
# display_current_directory(): This method should use the os.getcwd() function to retrieve and print the current working directory.
#
# change_directory(path): This method should use the os.chdir(path) function to change the working directory to the specified path.
#
# create_directory(path): This method should use the os.mkdir(path) function to create a new directory at the specified path.
#
# remove_file_or_directory(path): This method should use the os.remove(path) function to remove the file or directory at the specified path.
#
# You should also provide a simple menu-driven program that allows the user to interact with the DirectoryManager class. The menu should have the following options:
#
# Display current directory
# Change directory
# Create directory
# Remove file or directory
# Exit

import os


class DirectoryManager:
    def display_current_directory(self):

    # Your code here

    def change_directory(self, path):

    # Your code here

    def create_directory(self, path):

    # Your code here

    def remove_file_or_directory(self, path):


# Your code here

# Menu-driven program
def main():


# Your code here


if __name__ == "__main__":
    main()

