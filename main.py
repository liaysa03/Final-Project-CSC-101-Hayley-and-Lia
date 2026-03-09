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

    total_food_sites = (
        county_data["FDPIR Sites(2015)"]
        + county_data["Food Banks (2021)"]
        + county_data["SNAP Authorized Stores"]
        + county_data["WIC Authorized Stores"]
    )

    ratio = total_food_sites / total_pop
    return ratio


def compare_food_assistance_to_poverty(county_data):

    poverty_percent = county_data["Persons in poverty (%)"]
    total_pop = county_data["Population estimates (July 1, 2024)"]

    total_food_sites = (
        county_data["FDPIR Sites(2015)"]
        + county_data["Food Banks (2021)"]
        + county_data["SNAP Authorized Stores"]
        + county_data["WIC Authorized Stores"]
    )

    people_in_poverty = total_pop * (poverty_percent / 100)

    sites_per_1000_poverty = (total_food_sites / people_in_poverty) * 1000

    return poverty_percent, total_food_sites, sites_per_1000_poverty

def compare_food_assistance_to_income(county_data):

    income = county_data["Per capita income (2024 dollars)"]
    total_pop = county_data["Population estimates (July 1, 2024)"]

    total_food_sites = (
        county_data["FDPIR Sites(2015)"]
        + county_data["Food Banks (2021)"]
        + county_data["SNAP Authorized Stores"]
        + county_data["WIC Authorized Stores"]
    )

    # normalize by population so counties can be compared fairly
    sites_per_100k = (total_food_sites / total_pop) * 100000

    return income, total_food_sites, sites_per_100k

def select_county():

    print("\nSoCal Counties:")
    for name in foodSecurity:
        print("-", name)

    input_county = input("\nWhich SoCal County would you like to analyze?: ").strip()
    county_name = " ".join(word.capitalize() for word in input_county.split())

    if county_name not in foodSecurity:
        print("County not found.")
        return None

    return county_name


def select_group(county_data):

    low_access_keys = [k for k in county_data if "low access to store (2019)" in k]

    print("\nGroups available:")
    for key in low_access_keys:
        print("-", key.replace(", low access to store (2019)", ""))

    input_group = input("\nWhich group?: ").strip()

    for key in low_access_keys:
        if input_group.lower() in key.lower():
            return key

    print("Group not found.")
    return None


def which_method():

    print("\nWhich information would you like to know?")
    print("1 - Calculate number of people with low access to stores")
    print("2 - Food assistance to population ratio")
    print("3 - Compare food assistance availability to poverty level")
    print("4 - Compare food assistance availability to per capita income")

    choice = input("\nEnter the number of the method: ").strip()

    county_name = select_county()
    if not county_name:
        return

    county_data = foodSecurity[county_name]

    if choice == "1":

        group_key = select_group(county_data)
        if not group_key:
            return

        count = calculate_low_access(county_data, group_key)

        print(
            f"\nEstimated number of {group_key.replace(', low access to store (2019)','')} with low access in {county_name}: {count}"
        )

    elif choice == "2":

        ratio = food_assistance_to_pop_ratio(county_data)

        print(f"\nFood assistance to population ratio in {county_name}: {ratio:.6f}")

    elif choice == "3":

        poverty_percent, total_food_sites, sites_per_1000 = compare_food_assistance_to_poverty(county_data)

        print(f"\n{county_name} Poverty Rate: {poverty_percent}%")
        print(f"Total Food Assistance Sites: {total_food_sites}")
        print(f"Food Assistance Sites per 1000 People in Poverty: {sites_per_1000:.2f}")

    elif choice == "4":

        income, total_food_sites, sites_per_100k = compare_food_assistance_to_income(county_data)

        print(f"\n{county_name} Per Capita Income: ${income}")
        print(f"Total Food Assistance Sites: {total_food_sites}")
        print(f"Food Assistance Sites per 100,000 People: {sites_per_100k:.2f}")

    else:
        print("Invalid selection.")


if __name__ == "__main__":
    which_method()
# amount of food assistance, poverty
# amount of food assistance, median income
# total employment, poverty, and total population