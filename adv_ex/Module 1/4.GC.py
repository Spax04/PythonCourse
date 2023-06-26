# You are tasked with creating a class called GarbageBin that simulates a garbage bin in a residential area. The GarbageBin class should have the following functionalities:
#
# 1.	Initialize the GarbageBin object with a capacity (maximum number of items it can hold) and an empty list to store the items.
# 2.	Implement a method called add_item(item) that adds a new item to the garbage bin. The method should check if the bin is already full. If it is full, print a message indicating that the bin is full and the item cannot be added. Otherwise, add the item to the bin.
# 3.	Implement a method called empty_bin() that removes all the items from the bin.
# 4.	Implement a method called print_contents() that prints the list of items currently in the bin.
# 5.	Implement the __del__() method to display a message when the garbage bin object is being deleted by the garbage collector.

import gc

class GarbageBin:
    def __init__(self, capacity):

	# Your code here


    def add_item(self, item):

	# Your code here


    def empty_bin(self):

	# Your code here

    def print_contents(self):

	# Your code here


    def __del__(self):

	# Your code here

# Testing the GarbageBin class
bin1 = GarbageBin(5)
bin1.add_item("Banana peel")
bin1.add_item("Plastic bottle")
bin1.add_item("Food wrapper")
bin1.print_contents()

bin1.add_item("Crisp packet")
bin1.add_item("Paper cup")
bin1.print_contents()

bin1.empty_bin()
bin1.print_contents()

# Deleting the object manually to trigger __del__()
del bin1

# Forcing garbage collection
gc.collect()
