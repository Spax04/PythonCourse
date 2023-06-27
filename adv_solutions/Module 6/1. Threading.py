# In this exercise, you will implement a program that performs concurrent file processing using threading and synchronization in Python. The program will read multiple files concurrently, process their contents, and store the results in a shared data structure. To ensure thread safety and prevent conflicts, you will use synchronization techniques, taking into account the Global Interpreter Lock (GIL) limitations.
#
# Instructions:
#
# 1.	Create a Python class called FileProcessor that has the following attributes and methods:
# •	Attribute: results (a list) - stores the processed results.
# •	Method: process_file(filename) - reads and processes the contents of a file. The processing can be as simple as counting the number of lines in the file and appending the result to the results list.
#
# 2.	Create a function called worker that takes a FileProcessor object and a filename as parameters. This function will simulate the behavior of a thread processing a file. Inside the function, do the following:
# •	Acquire a lock to ensure exclusive access to the shared data structure (results list).
# •	Call the process_file method of the FileProcessor object to process the file.
# •	Print a message indicating the thread ID and the filename being processed.
# •	Release the lock.
#
# 3.	In the main part of your code, do the following:
# •	Create an instance of the FileProcessor class.
# •	Create a list of filenames that you want to process concurrently.
# •	Create multiple threads (at least 3) that will execute the worker function, passing the FileProcessor object and a filename from the list as parameters.
# •	Start the threads and wait for them to complete.
#
# 4.	After all the threads have finished processing, print the contents of the results list to verify that the files were processed correctly.

import threading


class FileProcessor:
    def __init__(self):
        self.results = []

    def process_file(self, filename):
        with open(filename, 'r') as file:
            lines_count = len(file.readlines())
            self.results.append({filename: lines_count})


def worker(processor, filename, lock):
    lock.acquire()
    try:
        processor.process_file(filename)
        print(f"Thread ID: {threading.get_ident()}, Processing file: {filename}")
    finally:
        lock.release()


def main():
    processor = FileProcessor()
    filenames = ["file1.txt", "file2.txt", "file3.txt"]  # List of filenames to process
    threads = []

    # Create a lock for synchronization
    lock = threading.Lock()

    # Create and start multiple threads
    for filename in filenames:
        thread = threading.Thread(target=worker, args=(processor, filename, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the results
    print(processor.results)


if __name__ == '__main__':
    main()