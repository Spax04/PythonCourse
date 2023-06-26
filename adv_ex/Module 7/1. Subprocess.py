# In this exercise, you will create a Python class that utilizes the subprocess module to compress a file using a specific compression algorithm. The class will provide methods to compress and decompress a file using either the ZIP or GZIP algorithm. You will implement these methods using the appropriate subprocess functions.
#
# Instructions:
#
# 1.	Create a Python class named FileCompressor.
# 2.	The class should have the following attributes:
# •	file_path: A string representing the path to the file that needs to be compressed.
# •	compression_algorithm: A string indicating the compression algorithm to be used. It can be either "zip" or "gzip".
# 1.	The class should have the following methods:
# •	compress(): This method should compress the file using the specified compression algorithm. It should check if the provided compression algorithm is supported (either "zip" or "gzip"). If the algorithm is supported, it should use the corresponding subprocess function to compress the file. After the compression is complete, the method should return a message indicating the success of the compression process.
# •	decompress(): This method should decompress the file using the specified compression algorithm. It should perform the necessary checks similar to the compress() method. If the algorithm is supported, it should use the corresponding subprocess function to decompress the file. After the decompression is complete, the method should return a message indicating the success of the decompression process.
# •	Note: Make sure to handle any potential errors that may occur during the compression or decompression process.

import subprocess

class FileCompressor:
    def __init__(self, file_path, compression_algorithm):

	# Your code here

    def compress(self):

	# Your code here


    def decompress(self):

	# Your code here


# Example usage
compressor = FileCompressor("my_file.txt", "zip")
print(compressor.compress())

decompressor = FileCompressor("compressed.zip", "zip")
print(decompressor.decompress())

