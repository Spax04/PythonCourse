#
# You are working on a project to analyze a large dataset containing information about online product reviews. The dataset is quite extensive, and processing it sequentially takes a significant amount of time. To speed up the analysis, you decide to utilize multiprocessing in Python.
#
# Here are the requirements for the program:
#
# 1.	Define a class called ReviewAnalyzer that inherits from multiprocessing.Process.
# 2.	The ReviewAnalyzer class should have an __init__ method that takes two parameters: review_data (a list) and process_id (an integer).
# 3.	Inside the __init__ method, store the review_data and process_id in instance variables.
# 4.	Implement the run method in the ReviewAnalyzer class. This method should process a subset of the review_data assigned to the process based on its process_id.
# 5.	The processing of the reviews can be a simple task, such as counting the number of positive and negative reviews.
# 6.	Create a list of ReviewAnalyzer instances, each with a different process_id and a subset of the review_data.
# 7.	Start each instance of the ReviewAnalyzer class using the start method.
# 8.	Join all the processes using the join method to wait for them to finish.
# 9.	Collect and aggregate the results from each process to obtain the final analysis.
#
# Your task is to implement the ReviewAnalyzer class and create instances of it to analyze the online product reviews dataset.


import multiprocessing

class ReviewAnalyzer(multiprocessing.Process):
    def __init__(self, review_data, process_id):
        super().__init__()
        self.review_data = review_data
        self.process_id = process_id

    def run(self):
        print(f"Starting process {self.process_id}...")
        positive_count = 0
        negative_count = 0
        for review in self.review_data:
            sentiment = analyze_sentiment(review)
            if sentiment == "positive":
                positive_count += 1
            elif sentiment == "negative":
                negative_count += 1
        print(f"Process {self.process_id} finished. Positive count: {positive_count}, Negative count: {negative_count}")

def analyze_sentiment(review):
    if "amazing" in review or "recommended" in review or "excellent" in review:
        return "positive"
    elif "subpar" in review or "not worth" in review:
        return "negative"
    else:
        return "neutral"

# Sample review dataset
reviews = [
    "This product is amazing!",
    "The quality is subpar.",
    "Highly recommended.",
    "Not worth the price.",
    "Excellent product!"
]

# Create instances of ReviewAnalyzer
processes = []
num_processes = 2  # Number of processes to create

chunk_size = len(reviews) // num_processes
for i in range(num_processes):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_processes - 1 else None
    process = ReviewAnalyzer(reviews[start:end], i)
    processes.append(process)

# Start each instance of the ReviewAnalyzer class
for process in processes:
    process.start()

# Join all the processes
for process in processes:
    process.join()

# Aggregate the results
positive_count = 0
negative_count = 0
for process in processes:
    positive_count += process.positive_count
    negative_count += process.negative_count

print(f"Total Positive count: {positive_count}, Total Negative count: {negative_count}")
