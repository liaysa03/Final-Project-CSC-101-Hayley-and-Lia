from data import foodSecurity

# main.py
from dataBuilder import (
    los_angeles_data, orange_data, san_diego_data, riverside_data,
    san_bernardino_data, ventura_data, santa_barbara_data, kern_data,
    imperial_data, san_luis_obispo_data
)

# Map county names (user-friendly) to the actual data dictionaries
foodSecurity = {
    "Los Angeles": los_angeles_data,
    "Orange": orange_data,
    "San Diego": san_diego_data,
    "Riverside": riverside_data,
    "San Bernardino": san_bernardino_data,
    "Ventura": ventura_data,
    "Santa Barbara": santa_barbara_data,
    "Kern": kern_data,
    "Imperial": imperial_data,
    "San Luis Obispo": san_luis_obispo_data
}


def high_risk_groups(county_data):
    """
    Calculate the number of seniors with low access to stores in a county.
    """
    total_pop = county_data["Population estimates (July 1, 2024)"]
    senior_percent = county_data["Persons 65 years and over (%)"]
    low_access_percent = county_data["Seniors, low access to store (2019)"]

    num_seniors = total_pop * (senior_percent / 100)
    seniors_low_access = num_seniors * (low_access_percent / 100)

    return int(seniors_low_access)


def start():
    print(
        "SoCal Counties: Los Angeles, Orange, San Diego, Riverside, San Bernardino, Ventura, Santa Barbara, Kern, Imperial, San Luis Obispo")
    input_answer = input("Which SoCal County would you like to learn about?: ").strip()

    # Normalize capitalization to match keys
    county_name = " ".join(word.capitalize() for word in input_answer.split())

    if county_name in foodSecurity:
        seniors = high_risk_groups(foodSecurity[county_name])
        print(f"Estimated number of seniors with low access to stores in {county_name}: {seniors}")
    else:
        print(f"Sorry, data for {county_name} is not available.")


# Run the program
if __name__ == "__main__":
    start()