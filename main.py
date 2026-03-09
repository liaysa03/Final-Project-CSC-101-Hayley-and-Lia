# main.py
from dataBuilder import (
    los_angeles_data,
    orange_data,
    san_diego_data,
    riverside_data,
    san_bernardino_data,
    ventura_data,
    santa_barbara_data,
    kern_data,
    imperial_data,
    san_luis_obispo_data
)

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

def get_population_key(low_access_key):
    if "Seniors" in low_access_key:
        return "Persons 65 years and over (%)"
    elif "Children" in low_access_key:
        return "Persons under 18 years (%)"
    else:
        group_name = low_access_key.replace(", low access to store (2019)", "")
        if group_name == "Hispanic":
            return "Hispanic or Latino (%)"
        elif group_name == "American Indian or Alaska Native":
            return "American Indian and Alaska Native alone (%)"
        elif group_name == "Hawaiian or Pacific Islander":
            return "Native Hawaiian and Other Pacific Islander alone (%)"
        else:
            return f"{group_name} alone (%)"

def calculate_low_access(county_data, low_access_key):
    total_pop = county_data["Population estimates (July 1, 2024)"]
    pop_key = get_population_key(low_access_key)
    group_percent = county_data[pop_key]
    low_access_percent = county_data[low_access_key]

    group_count = total_pop * (group_percent / 100)
    low_access_count = group_count * (low_access_percent / 100)
    return int(low_access_count)

def food_assistance_to_pop_ratio(county_data):
    total_pop = county_data["Population estimates (July 1, 2024)"]
    food_keys = [
        "FDPIR Sites(2015)",
        "Food Banks (2021)",
        "SNAP Authorized Stores",
        "WIC Authorized Stores"
    ]
    total_food_sites = sum(county_data.get(k, 0) for k in food_keys)
    ratio = total_food_sites / total_pop
    return ratio

def select_county():
    print("\nSoCal Counties:")
    for name in foodSecurity:
        print("-", name)
    input_county = input("\nWhich SoCal County would you like to analyze?: ").strip()
    county_name = " ".join(word.capitalize() for word in input_county.split())
    if county_name not in foodSecurity:
        print(f"Sorry, data for {county_name} is not available.")
        return None
    return county_name

def select_group(county_data):
    low_access_keys = [k for k in county_data if "low access to store (2019)" in k]
    print("\nGroups available for low access statistics:")
    for key in low_access_keys:
        print("-", key.replace(", low access to store (2019)", "").strip())
    input_group = input("\nWhich group would you like to analyze?: ").strip()

    for key in low_access_keys:
        if input_group.lower() in key.lower():
            return key
    print(f"Sorry, group '{input_group}' is not available.")
    return None

def which_method():
    print("Which information would you like to know about?")
    print("1 - Calculate number of people with low access to stores")
    print("2 - Food assistance to population ratio")
    # Add more methods here as you create them

    choice = input("\nEnter the number of the method you want to use: ").strip()

    county_name = select_county()
    if not county_name:
        return
    county_data = foodSecurity[county_name]

    if choice == "1":
        group_key = select_group(county_data)
        if not group_key:
            return
        count = calculate_low_access(county_data, group_key)
        print(f"\nEstimated number of {group_key.replace(', low access to store (2019)','')} with low access to stores in {county_name}: {count}")
    elif choice == "2":
        ratio = food_assistance_to_pop_ratio(county_data)
        print(f"\nFood assistance to population ratio in {county_name}: {ratio:.6f}")
    else:
        print("Invalid selection. Please try again.")

if __name__ == "__main__":
    which_method()