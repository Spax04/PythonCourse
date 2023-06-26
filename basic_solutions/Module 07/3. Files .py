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
        self.engagement_file_path = engagement_file_path
        self.engagement_data = []

    def load_engagement_data(self):
        with open(self.engagement_file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter='|')
            next(csv_reader)  # Skip header row
            self.engagement_data = [row for row in csv_reader]

    def calculate_total_engagement(self):
        total_likes = 0
        total_comments = 0
        total_shares = 0

        for row in self.engagement_data:
            likes = int(row[1])
            comments = int(row[2])
            shares = int(row[3])

            total_likes += likes
            total_comments += comments
            total_shares += shares

        return total_likes, total_comments, total_shares

    def find_highest_engagement_post(self):
        max_engagement = 0
        highest_engagement_post = None

        for row in self.engagement_data:
            post_id = row[0]
            likes = int(row[1])
            comments = int(row[2])
            shares = int(row[3])

            engagement = likes + comments + shares

            if engagement > max_engagement:
                max_engagement = engagement
                highest_engagement_post = post_id

        return highest_engagement_post

    def calculate_average_engagement(self):
        total_likes, total_comments, total_shares = self.calculate_total_engagement()
        total_posts = len(self.engagement_data)

        average_likes = total_likes / total_posts
        average_comments = total_comments / total_posts
        average_shares = total_shares / total_posts

        return average_likes, average_comments, average_shares

    def search_post_by_id(self, post_id):
        for row in self.engagement_data:
            if row[0] == post_id:
                return row[1], row[2], row[3]

        return None

    def calculate_engagement_rate(self, followers):
        total_likes, total_comments, total_shares = self.calculate_total_engagement()
        total_engagement = total_likes + total_comments + total_shares

        if followers == 0:
            return 0

        engagement_rate = total_engagement / followers
        return engagement_rate

    def calculate_engagement_ratio(self):
        engagement_ratios = []

        for row in self.engagement_data:
            likes = int(row[1])
            comments = int(row[2])
            shares = int(row[3])

            engagement_ratio = comments / (likes + shares)
            engagement_ratios.append(engagement_ratio)

        return engagement_ratios

    def write_analysis_results(self):
        total_likes, total_comments, total_shares = self.calculate_total_engagement()
        average_likes, average_comments, average_shares = self.calculate_average_engagement()
        highest_engagement_post = self.find_highest_engagement_post()

        analysis_result = f"Total Likes: {total_likes}\n"
        analysis_result += f"Total Comments: {total_comments}\n"
        analysis_result += f"Total Shares: {total_shares}\n"
        analysis_result += f"Average Likes: {average_likes:.2f}\n"
        analysis_result += f"Average Comments: {average_comments:.2f}\n"
        analysis_result += f"Average Shares: {average_shares:.2f}\n"
        analysis_result += f"Highest Engagement Post: {highest_engagement_post}\n"

        with open('engagement_analysis.txt', 'w') as file:
            file.write(analysis_result)

    def write_post_engagement_metrics(self):
        with open('post_engagement_metrics.txt', 'w') as file:
            for row in self.engagement_data:
                post_id = row[0]
                likes = row[1]
                comments = row[2]
                shares = row[3]

                metrics_line = f"Post ID: {post_id}, Likes: {likes}, Comments: {comments}, Shares: {shares}\n"
                file.write(metrics_line)


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
