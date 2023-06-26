# You are working as a data engineer for a social media platform. Your task is to analyze user engagement data for posts. You have been provided with a file named "user_engagement.txt" that contains the user engagement data in the following format:
#
# Post ID | Likes | Comments | Shares
#
# Your goal is to create a Python class called "EngagementAnalyzer" that performs the following operations:
#
# 1.	Read the user engagement data from the file using a file iterator.
# 2.	Calculate the total number of likes, comments, and shares across all posts.
# 3.	Find the post with the highest engagement (sum of likes, comments, and shares).
# 4.	Determine the average engagement per post.
# 5.	Write the analysis results to a new file named "engagement_analysis.txt".
# 6.	Provide a function to search for a specific post by its ID and retrieve its engagement metrics.
# 7.	Implement a function to calculate the engagement rate, defined as the average engagement per post divided by the number of followers.
# 8.	Add a function to calculate the engagement ratio, defined as the number of comments divided by the sum of likes and shares for each post.
# 9.	Write the engagement metrics of all posts to a separate file named "post_engagement_metrics.txt".

class EngagementAnalyzer:
    def __init__(self, engagement_file_path):

    # Your code here

    def load_engagement_data(self):

    # Your code here

    def calculate_total_engagement(self):

    # Your code here

    def find_highest_engagement_post(self):

    # Your code here

    def calculate_average_engagement(self):

    # Your code here

    def search_post_by_id(self, post_id):

    # Your code here

    def calculate_engagement_rate(self, followers):

    # Your code here

    def calculate_engagement_ratio(self):

    # Your code here

    def write_analysis_results(self):

    # Your code here

    def write_post_engagement_metrics(self):


# Your code here


# Usage example:
analyzer = EngagementAnalyzer('user_engagement.txt')
analyzer.write_analysis_results()
analyzer.write_post_engagement_metrics()

# Example usage of additional functions
post_id = '123456'
post_metrics = analyzer.search_post_by_id(post_id)
if post_metrics:
    print(f"Engagement metrics for post ID {post_id}: {post_metrics}")
else:
    print(f"Post with ID {post_id} not found.")

followers_count = 1000
engagement_rate = analyzer.calculate_engagement_rate(followers_count)
print(f"Engagement rate: {engagement_rate:.2f}")

engagement_ratios = analyzer.calculate_engagement_ratio()
print(f"Engagement ratios: {engagement_ratios}")
