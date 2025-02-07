def display_title():
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))

def display_menu():
    print("\n[A] View Data\n[B] Visualise Data\n[X] Exit")
    return input("Enter your choice: ").strip().upper()

def display_sub_menu_a():
    print("\n[A] View reviews by Park\n[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per Year by Park\n[X] Return to Main Menu")
    return input("Enter your choice: ").strip().upper()

def display_sub_menu_b():
    print("\n[A] Most Reviewed Parks\n[B] Average Scores")
    print("[C] Park Ranking by Nationality\n[D] Most Popular Month by Park\n[X] Return to Main Menu")
    return input("Enter your choice: ").strip().upper()
