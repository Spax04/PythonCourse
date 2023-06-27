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
import zipfile

class FileCompressor:
    def __init__(self, file_path, compression_algorithm):
        self.file_path = file_path
        self.compression_algorithm = compression_algorithm

    def compress(self):
        if self.compression_algorithm == "zip":
            try:
                subprocess.run(["C:/Program Files/7-Zip/7z.exe", "a", self.file_path + ".zip", self.file_path + ".txt"],
                               check=True)
                return f"Compression successful. File {self.file_path} was compressed using ZIP."
            except subprocess.CalledProcessError:
                return f"Compression failed. An error occurred during the compression process."
        else:
            return f"Compression failed. Unsupported compression algorithm: {self.compression_algorithm}."

    def decompress(self):
        if self.compression_algorithm == "zip":
            try:
                with zipfile.ZipFile(self.file_path, "r") as zip_ref:
                    zip_ref.extractall()
                return f"Decompression successful. File {self.file_path} was decompressed using ZIP."
            except zipfile.BadZipFile:
                return f"Decompression failed. The ZIP file is invalid or corrupted."
            except Exception as e:
                print(e)
                return f"Decompression failed. An unknown error occurred during the decompression process."
        else:
            return f"Decompression failed. Unsupported compression algorithm: {self.compression_algorithm}."



# Example usage
compressor = FileCompressor("my_file", "zip")
print(compressor.compress())

decompressor = FileCompressor("my_file.zip", "zip")
print(decompressor.decompress())

