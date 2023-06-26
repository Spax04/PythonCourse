# In this exercise, you will create a Python class that utilizes the subprocess module and the Popen function to create a simple file compression tool. The class will provide methods to compress and decompress files using the popular compression tool called "gzip." The gzip command-line tool will be executed using the Popen function from the subprocess module.
#
# Your task is to implement the FileCompressor class, which should have the following methods:
#
# 1.	compress_file(input_file, output_file): This method takes an input file path and an output file path as parameters. It compresses the input file using the gzip command-line tool and saves the compressed file to the specified output file path.
#
# 2.	decompress_file(input_file, output_file): This method takes a compressed file path and an output file path as parameters. It decompresses the input file using the gzip command-line tool and saves the decompressed file to the specified output file path.
#
# Note: Ensure that the gzip command-line tool is installed on your system before attempting this exercise. You can check if it's installed by running the command gzip --version in your terminal or command prompt.

import subprocess

class FileCompressor:
    @staticmethod
    def compress_file(input_file, output_file):
        try:
            subprocess.run(['gzip', '-c', input_file], stdout=open(output_file, 'wb'), check=True)
        print(f"Compression successful. File {input_file} was compressed and saved as {output_file}.")
        except subprocess.CalledProcessError:
        print(f"Compression failed. An error occurred during the compression process.")

    @staticmethod
    def decompress_file(input_file, output_file):
        try:
            subprocess.run(['gzip', '-d', '-c', input_file], stdout=open(output_file, 'wb'), check=True)
            print(f"Decompression successful. File {input_file} was decompressed and saved as {output_file}.")
        except subprocess.CalledProcessError:
            print(f"Decompression failed. An error occurred during the decompression process.")

# Example usage
compressor = FileCompressor()

# Compressing a file
compressor.compress_file('input.txt', 'compressed.gz')

# Decompressing a file
compressor.decompress_file('compressed.gz', 'decompressed.txt')
