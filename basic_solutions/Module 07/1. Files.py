#
# You are a data analyst working for a retail company. Your manager has assigned you a task to analyze the sales data of various products. You have been provided with a file named "sales_data.txt" that contains the sales data in the following format:
#
# Product Name,Quantity,Price
#
# Your task is to create a Python class called "SalesDataAnalyzer" that performs the following operations:
#
# 1.	Read the sales data from the file using a file iterator.
# 2.	Calculate the total revenue generated from the sales data.
# 3.	Find the product with the highest quantity sold.
# 4.	Find the average price of all products.
# 5.	Write the calculated statistics to a new file named "sales_summary.txt".

class SalesDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze_sales_data(self):
        sales_data = []
        total_revenue = 0
        max_quantity = 0
        max_quantity_product = None
        total_products = 0

        # Read the sales data from the file
        with open(self.file_path, 'r') as file:
            for line in file:
                product_name, quantity, price = line.strip().split(',')
                quantity = int(quantity)
                price = float(price)

                # Calculate total revenue
                revenue = quantity * price
                total_revenue += revenue

                # Check if current product has highest quantity sold
                if quantity > max_quantity:
                    max_quantity = quantity
                    max_quantity_product = product_name

                total_products += 1

        # Calculate average price
        average_price = total_revenue / total_products

        # Write the calculated statistics to a new file
        summary = f"Total Revenue: {total_revenue:.2f}\n"
        summary += f"Product with Highest Quantity Sold: {max_quantity_product}\n"
        summary += f"Average Price of Products: {average_price:.2f}\n"

        with open('sales_summary.txt', 'w') as file:
            file.write(summary)

# Usage example:
analyzer = SalesDataAnalyzer('sales_data.txt')
analyzer.analyze_sales_data()
