import csv  # For reading the CSV file
from collections import Counter  # For counting reviews per park
import calendar  # For sorting months


def load_data(file_path):
    """Load the CSV file into a list of dictionaries."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Error: File not found. Please ensure 'disneyland_reviews.csv' is in the same folder as 'main.py'.")
        return []


def get_reviews_by_park(data, park_name):
    """
    Get all reviews for a specific park.

    Args:
        data (list): The dataset loaded from the CSV file.
        park_name (str): The name of the park.

    Returns:
        list: A list of reviews for the specified park.
    """
    return [row for row in data if row["Park Name"].strip().lower() == park_name.strip().lower()]


def count_reviews_by_park_and_location(data, park_name, location):
    """
    Count the number of reviews a specific park received from a given location.

    Args:
        data (list): The dataset loaded from the CSV file.
        park_name (str): The name of the park.
        location (str): The location of the reviewer.

    Returns:
        int: The number of reviews.
    """
    return sum(1 for row in data if row["Park Name"].strip().lower() == park_name.strip().lower()
               and row["Reviewer Location"].strip().lower() == location.strip().lower())


def get_average_score_by_park_and_year(data, park_name, year):
    """
    Calculate the average rating for a specific park in a given year.

    Args:
        data (list): The dataset loaded from the CSV file.
        park_name (str): The name of the park.
        year (str): The year.

    Returns:
        float or None: The average rating, or None if no data is available.
    """
    ratings = [float(row["Rating"]) for row in data if row["Park Name"].strip().lower() == park_name.strip().lower()
               and row["Year"].strip() == year.strip()]
    return sum(ratings) / len(ratings) if ratings else None


def count_reviews_per_park(data):
    """
    Count the number of reviews per park.

    Args:
        data (list): The dataset loaded from the CSV file.

    Returns:
        dict: A dictionary with park names as keys and review counts as values.
    """
    return dict(Counter(row["Park Name"].strip() for row in data))


def calculate_average_score_per_park(data):
    """
    Calculate the average review score for each park.

    Args:
        data (list): The dataset loaded from the CSV file.

    Returns:
        dict: A dictionary with park names as keys and average scores as values.
    """
    scores, counts = {}, {}
    for row in data:
        current_park = row["Park Name"].strip()
        scores[current_park] = scores.get(current_park, 0) + float(row["Rating"])
        counts[current_park] = counts.get(current_park, 0) + 1
    return {park: scores[park] / counts[park] for park in scores}


def get_top_10_locations_by_average_rating(data, park_name):
    """
    Calculate the top 10 locations with the highest average ratings for a given park.

    Args:
        data (list): The dataset loaded from the CSV file.
        park_name (str): The name of the park.

    Returns:
        dict: Top 10 locations with their average ratings.
    """
    location_scores, location_counts = {}, {}
    for row in data:
        if row["Park Name"].strip().lower() == park_name.strip().lower():
            location = row["Reviewer Location"].strip()
            rating = float(row["Rating"])
            if location in location_scores:
                location_scores[location] += rating
                location_counts[location] += 1
            else:
                location_scores[location] = rating
                location_counts[location] = 1
    average_ratings = {loc: location_scores[loc] / location_counts[loc] for loc in location_scores}
    return dict(sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)[:10])


def get_average_rating_by_month(data, park_name):
    """
    Calculate the average review score for each month for a given park.

    Args:
        data (list): Dataset loaded from the CSV file.
        park_name (str): The name of the park.

    Returns:
        dict: Average ratings for each month (sorted by month order).
    """
    month_scores = {}
    month_counts = {}

    # Loop through the data to calculate total scores and counts for each month
    for row in data:
        # Filter rows for the specified park
        if row["Park Name"].strip().lower() == park_name.strip().lower():
            month = row["Month"].strip()  # Get the month
            rating = float(row["Rating"])  # Convert rating to a float

            # Accumulate scores and counts for the month
            if month in month_scores:
                month_scores[month] += rating
                month_counts[month] += 1
            else:
                month_scores[month] = rating
                month_counts[month] = 1

    # Calculate average scores for each month
    average_ratings = {month: month_scores[month] / month_counts[month] for month in month_scores}

    # Sort months in calendar order (January to December)
    sorted_months = sorted(average_ratings.keys(), key=lambda m: list(calendar.month_name).index(m))

    # Return the sorted average ratings
    return {month: average_ratings[month] for month in sorted_months}
