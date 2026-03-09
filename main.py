from dataBuilder import *

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
        # for racial/ethnic groups, remove ', low access to store (2019)' and append 'alone (%)' or 'or Latino (%)'
        group_name = low_access_key.replace(", low access to store (2019)", "")
        # handle Hispanic special case
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

def start():
    print("SoCal Counties: Los Angeles, Orange, San Diego, Riverside, San Bernardino, Ventura, Santa Barbara, Kern, Imperial, San Luis Obispo")
    input_county = input("Which SoCal County would you like to learn about?: ").strip()
    county_name = " ".join(word.capitalize() for word in input_county.split())

    if county_name not in foodSecurity:
        print(f"Sorry, data for {county_name} is not available.")
        return

    county_data = foodSecurity[county_name]

    # List all keys that have low access data
    low_access_keys = [k for k in county_data if "low access to store (2019)" in k]

    print("\nGroups available for low access statistics:")
    for key in low_access_keys:
        print("-", key.replace(", low access to store (2019)", "").strip())

    input_group = input("Which group would you like to see low access statistics for?: ").strip()

    # match user input to a low access key
    matched_key = None
    for key in low_access_keys:
        if input_group.lower() in key.lower():
            matched_key = key
            break

    if not matched_key:
        print(f"Sorry, group '{input_group}' is not available.")
        return

    count = calculate_low_access(county_data, matched_key)
    print(f"Estimated number of {input_group} with low access to stores in {county_name}: {count}")

if __name__ == "__main__":
    start()