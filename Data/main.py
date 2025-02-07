import tui
import process
import visual

def main():
    print("Starting program...")  # Debug: Program start
    tui.display_title()

    file_path = "disneyland_reviews.csv"
    print(f"Loading data from {file_path}...")  # Debug: File loading step
    data = process.load_data(file_path)
    print(f"Data loaded successfully. Number of rows: {len(data)}")  # Debug: Confirm data loaded

    if data:
        print("Entering the main menu...")  # Debug: Before the main menu loop
        while True:
            user_choice = tui.display_menu()
            print(f"User selected: {user_choice}")  # Debug: Confirm user choice

            if user_choice == 'A':  # View Data Sub-menu
                print("Entering submenu A (View Data)...")  # Debug: Submenu A start
                while True:
                    sub_choice = tui.display_sub_menu_a()
                    print(f"Submenu A - User selected: {sub_choice}")  # Debug: Submenu choice

                    if sub_choice == 'A':  # View Reviews by Park
                        print("Option A in submenu selected: View Reviews by Park")  # Debug
                        park_name = input("Enter the name of the park: ").strip()
                        reviews = process.get_reviews_by_park(data, park_name)
                        if reviews:
                            print(f"Found {len(reviews)} reviews for park: {park_name}")  # Debug
                        else:
                            print(f"No reviews found for park: {park_name}")  # Debug

                    elif sub_choice == 'X':
                        print("Exiting submenu A...")  # Debug
                        break

            elif user_choice == 'X':
                print("Exiting program. Goodbye!")  # Debug: Exit message
                break


if __name__ == "__main__":
    main()
