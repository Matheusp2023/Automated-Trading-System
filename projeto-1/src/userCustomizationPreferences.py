# User Customization and Preferences: Allowing users to customize settings according to their preferences
# author: Matheus Pedro

import ctypes

class UserPreferences:
    def __init__(self):
        # Dictionary to store user preferences
        self.preferences = {}

    def set_preference(self, key, value):
        # Set user preference
        self.preferences[key] = value
        print(f"Preference '{key}' set to '{value}'.")
        self.update_console_color(value)

    def get_preference(self, key):
        # Get user preference
        return self.preferences.get(key, None)

    def update_console_color(self, color):
        # Update console color (Windows specific)
        if color.lower() == 'red':
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 12)  # Red
        elif color.lower() == 'green':
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 10)  # Green
        elif color.lower() == 'blue':
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 9)  # Blue
        else:
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 7)  # Default

def userCustomizationPreferencesFunctionalities():
    user = UserPreferences()

    print("Choose an option:")
    print("1. Set background color")
    print("2. Get background color")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        color = input("Enter the background color (e.g., 'red', 'blue', 'green'): ")
        user.set_preference('background_color', color)
    elif choice == "2":
        color = user.get_preference('background_color')
        if color is not None:
            print(f"Background color: {color}")
        else:
            print("Background color not set.")
    elif choice == "3":
        print("Exiting...")
        return
    else:
        print("Invalid option. Please try again.")