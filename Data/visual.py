import matplotlib.pyplot as plt

def plot_reviews_pie_chart(review_counts):
    plt.pie(review_counts.values(), labels=review_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Distribution of Reviews per Park")
    plt.show()

def plot_average_scores_bar_chart(average_scores):
    plt.bar(average_scores.keys(), average_scores.values(), color='blue')
    plt.title("Average Review Scores per Park")
    plt.show()
def plot_top_10_locations_bar_chart(top_10_locations, park_name):
    """
    Plot a bar chart for the top 10 locations with the highest average ratings for a given park.

    Args:
        top_10_locations (dict): Dictionary of locations and their average ratings.
        park_name (str): Name of the park.
    """
   # import matplotlib.pyplot as plt

    locations = list(top_10_locations.keys())
    scores = list(top_10_locations.values())

    plt.figure(figsize=(10, 6))
    plt.barh(locations, scores, color='purple')
    plt.xlabel("Average Rating")
    plt.ylabel("Reviewer Location")
    plt.title(f"Top 10 Locations for {park_name}")
    plt.gca().invert_yaxis()  # Highest ratings on top
    plt.show()
def plot_average_rating_by_month_bar_chart(average_ratings, park_name):
    """
    Plot a bar chart for the average rating per month for a given park.

    Args:
        average_ratings (dict): Dictionary of months and their average ratings.
        park_name (str): Name of the park.
    """
   # import matplotlib.pyplot as plt

    months = list(average_ratings.keys())
    scores = list(average_ratings.values())

    plt.figure(figsize=(10, 6))
    plt.bar(months, scores, color='orange')
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Average Rating per Month for {park_name}")
    plt.xticks(rotation=45)  # Rotate month labels for readability
    plt.ylim(0, 5)  # Assuming rating scale is 1-5
    plt.show()
