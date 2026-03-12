
from dataBuilder import (
    los_angeles_dict,
    orange_dict,
    san_diego_dict,
    riverside_dict,
    san_bernardino_dict,
    ventura_dict,
    santa_barbara_dict,
    kern_dict,
    imperial_dict,
    san_luis_obispo_dict
)

from data import County as CountyObj


County = {
    "Los Angeles": los_angeles_dict,
    "Orange": orange_dict,
    "San Diego": san_diego_dict,
    "Riverside": riverside_dict,
    "San Bernardino": san_bernardino_dict,
    "Ventura": ventura_dict,
    "Santa Barbara": santa_barbara_dict,
    "Kern": kern_dict,
    "Imperial": imperial_dict,
    "San Luis Obispo": san_luis_obispo_dict
}

# helper function to retrieve population data for a specific group
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

# helper function to retrieve specific metric data
def get_metric_value(county_obj, metric, low_access_key=None):

    total_pop = county_obj.popEst

    total_food_sites = (
        county_obj.FDPIR
        + county_obj.foodbank
        + county_obj.SNAP
        + county_obj.WIC
    )

    if metric == "poverty":
        return float(county_obj.poverty)

    elif metric == "income":
        return float(county_obj.incomeI)

    elif metric == "total_sites":
        return float(total_food_sites)

    elif metric == "sites_per_100k":
        return (total_food_sites / total_pop) * 100000

    elif metric == "low_access_rate":
        if not low_access_key:
            raise ValueError("low_access_key required for low_access_rate")
        return float(county_obj.data[low_access_key])

    elif metric == "low_access_count":
        if not low_access_key:
            raise ValueError("low_access_key required for low_access_count")
        return float(calculate_low_access(county_obj, low_access_key))

    else:
        raise ValueError("Unknown metric.")

# method 1
# purpose is to return the number of people in a group that have low access to stores, so we retrieve the group
# percentage and population from our county data and calculate the number of people
def calculate_low_access(county_obj, low_access_key):

    total_pop = county_obj.popEst
    pop_key = get_population_key(low_access_key)

    group_percent = county_obj.data[pop_key]
    low_access_percent = county_obj.data[low_access_key]

    group_count = total_pop * (group_percent / 100)
    low_access_count = group_count * (low_access_percent / 100)

    return int(low_access_count)

# method 2
# purpose = calculate the food assistance resources to the population, retrieve the food sources available and total
# them then divide by total population of that county
def food_assistance_to_pop_ratio(county_obj):

    total_pop = county_obj.popEst

    total_food_sites = (
        county_obj.FDPIR
        + county_obj.foodbank
        + county_obj.SNAP
        + county_obj.WIC
    )

    ratio = total_food_sites / total_pop
    return ratio

# method 3
# purpose = calculate the food assistance to poverty ratio, similar to last method we totaled the food assistance
# resources in each county, then calculated the total people in poverty and finally calculated ratio of total food
# assistance over people in poverty per 1000 people to give a clearer comparison for other counties
def compare_food_assistance_to_poverty(county_obj):

    poverty_percent = county_obj.poverty
    total_pop = county_obj.popEst

    total_food_sites = (
        county_obj.FDPIR
        + county_obj.foodbank
        + county_obj.SNAP
        + county_obj.WIC
    )

    people_in_poverty = total_pop * (poverty_percent / 100)

    sites_per_1000_poverty = (total_food_sites / people_in_poverty) * 1000

    return poverty_percent, total_food_sites, sites_per_1000_poverty

# method 4
# purpose = calculate the ratio of food assistance to income
def compare_food_assistance_to_income(county_obj):

    income = county_obj.incomeI
    total_pop = county_obj.popEst

    total_food_sites = (
        county_obj.FDPIR
        + county_obj.foodbank
        + county_obj.SNAP
        + county_obj.WIC
    )

    # using a standard ratio of per 100,000 to compare other counties fairly
    sites_per_100k = (total_food_sites / total_pop) * 100000

    return income, total_food_sites, sites_per_100k

# method 5
# purpose = to return the composition of available food assistance resources
def resource_mix_breakdown(county_obj):

    fdpir = getattr(county_obj, "FDPIR", 0) or 0
    food_banks = getattr(county_obj, "foodbank", 0) or 0
    snap = getattr(county_obj, "SNAP", 0) or 0
    wic = getattr(county_obj, "WIC", 0) or 0

    total = fdpir + food_banks + snap + wic

    if total == 0:
        return 0, {
            "FDPIR Sites": 0.0,
            "Food Banks": 0.0,
            "SNAP Authorized Stores": 0.0,
            "WIC Authorized Stores": 0.0,
        }

    breakdown = {
        "FDPIR Sites": (fdpir / total) * 100,
        "Food Banks": (food_banks / total) * 100,
        "SNAP Authorized Stores": (snap / total) * 100,
        "WIC Authorized Stores": (wic / total) * 100,
    }

    return total, breakdown

# method 6
# purpose = compare multiple counties metrics at the same time
def compare_multiple_counties_with_metrics(county_names, metrics, low_access_key=None):

    if any(m in ("low_access_rate", "low_access_count") for m in metrics) and not low_access_key:
        raise ValueError("low_access_key required for low-access metrics.")

    results = {}

    for county in county_names:
        data = County[county]
        cobj = CountyObj(data)
        row = {}

        total_pop = cobj.popEst

        total_food_sites = (
            cobj.FDPIR
            + cobj.foodbank
            + cobj.SNAP
            + cobj.WIC
        )

        if "poverty" in metrics:
            row["poverty"] = float(cobj.poverty)

        if "income" in metrics:
            row["income"] = float(cobj.incomeI)

        if "total_sites" in metrics:
            row["total_sites"] = float(total_food_sites)

        if "sites_per_100k" in metrics:
            row["sites_per_100k"] = (total_food_sites / total_pop) * 100000

        if "low_access_rate" in metrics:
            row["low_access_rate"] = float(cobj.data[low_access_key])

        if "low_access_count" in metrics:
            row["low_access_count"] = float(calculate_low_access(cobj, low_access_key))

        if "resource_mix" in metrics:
            _, breakdown = resource_mix_breakdown(cobj)
            row["resource_mix"] = breakdown

        results[county] = row

    return results

# method 7
# purpose = to filter counties based on a greater than threshold for selected metric
def filter_counties_by_threshold(county_names, metric, threshold, low_access_key=None):

    passed = []

    for county in county_names:
        county_data = County[county]
        cobj = CountyObj(county_data)
        value = get_metric_value(cobj, metric, low_access_key=low_access_key)

        if value > threshold:
            passed.append((county, value))

    # sort highest to lowest so output is nicer
    passed.sort(key=lambda x: x[1], reverse=True)
    return passed

# method 8
# purpose = to filter counties based on a less than threshold for selected metric
def filter_counties_by_thresholdless(county_names, metric, threshold, low_access_key=None):

    passed = []

    for county in county_names:
        county_data = County[county]
        cobj = CountyObj(county_data)
        value = get_metric_value(cobj, metric, low_access_key=low_access_key)

        if value < threshold:
            passed.append((county, value))

    # sort highest to lowest so output is nicer
    passed.sort(key=lambda x: x[1], reverse=True)
    return passed

# method 9
# purpose = to print available food assistance websites for selected county
def print_county_website(county_name):
    county_websites = {
        "Los Angeles": ["https://www.getcalfresh.org/", "https://www.lafoodbank.org/",
                        "http://publichealth.lacounty.gov/nut/resources/food-assistance-programs.htm"],
        "Orange": ["https://www.getcalfresh.org/",
                   "https://www.capoc.org/oc-food-bank/?gad_source=1&gad_campaignid=1478494483&gbraid=0AAAAADPi94o78G52ORG7OYMYGXbiTjwKP&gclid=Cj0KCQjw37nNBhDkARIsAEBGI8Mqm-zLUVwpdzDXCnVPiQhUwT_PgNWFF0JloIcOxcvNWYixDhkNAqwaAhQ3EALw_wcB",
                   "https://ocfoodhelp.org/", "https://feedoc.org/need-food/"],
        "San Diego": ["https://www.getcalfresh.org/",
                      "https://www.sandiegocounty.gov/content/sdc/hhsa/programs/ssp/food_stamps.html",
                      "https://feedingsandiego.org/find-food/",
                      "https://www.sandiegofoodbank.org/programs/emergency-food-assistance-program/"],
        "Riverside": ["https://www.getcalfresh.org/", "https://riversideca.gov/hhs/get-help/food-supportive-resources"],
        "San Bernardino": ["https://www.getcalfresh.org/",
                           "https://www.feedingamericaie.org/get-help?utm_source=feeding_america_riverside_san_bernardino&utm_medium=paid_search&utm_campaign=google_grant&utm_content=ca&utm_term=san%20bernardino%20food%20bank&gad_source=1",
                           "https://www.capsbc.org/food-bank"],
        "Ventura": ["https://www.getcalfresh.org/", "https://foodshare.com/",
                    "https://venturacounty.gov/health-and-human-services/food-assistance-and-healthy-eating/"],
        "Santa Barbara": ["https://www.getcalfresh.org/",
                          "https://foodbanksbc.org/get-help/?srsltid=AfmBOoql7WdjMbedRIhkAIYXxilQ8bI5ywmdQY7qcTfbbZKbONb_mNPZ",
                          "https://sbparksandrec.santabarbaraca.gov/programs-services/food-distributions"],
        "Kern": ["https://www.getcalfresh.org/", "https://www.capk.org/food-bank/",
                 "https://www.kerncounty.com/government/aging-adult-services/services/senior-nutrition/supplemental-food-assistance"],
        "Imperial": ["https://www.getcalfresh.org/", "https://www.ivfoodbank.com/"],
        "San Luis Obispo": ["https://www.getcalfresh.org/", "https://slofoodbank.org/en/food-locator/",
                            "https://www.slocounty.ca.gov/departments/health-agency/public-health/all-public-health-services/health-promotion/nutrition-education-calfresh-healthy-living/food-assistance"],

    }
    urls = county_websites.get(county_name, [])
    if not urls:
            print(f"\nNo websites set for {county_name} yet.")
            return

    print(f"\nFood assistance websites for {county_name}:")
    for i, url in enumerate(urls, start=1):
            print(f"{i}. {url}")

# user input functions for user interface
def select_county():

    print("\nSoCal Counties:")
    for name in County:
        print("-", name)

    input_county = input("\nWhich SoCal County would you like to analyze?: ").strip()

    # chatgpt formating of print output
    county_name = " ".join(word.capitalize() for word in input_county.split())

    if county_name not in County:
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

def select_multiple_counties():
    print("\nSoCal Counties:")
    for name in County:
        print("-", name)

    raw = input(
        "\nEnter counties to compare (comma-separated, e.g. Los Angeles, Orange, San Diego): "
    ).strip()

    counties = []
    for part in raw.split(","):
        county_name = " ".join(word.capitalize() for word in part.strip().split())
        if county_name:
            counties.append(county_name)

    # validate
    valid = []
    for c in counties:
        if c in County:
            valid.append(c)
        else:
            print(f"County not found (skipping): {c}")

    if len(valid) < 2:
        print("Need at least 2 valid counties to compare.")
        return None

    return valid


def select_metrics():

    options = [
        ("poverty", "Poverty rate (%) "),
        ("income", "Per capita income "),
        ("sites_per_100k", "Food assistance sites per 100,000 people "),
        ("total_sites", "Total food assistance sites "),
        ("low_access_rate", "Low-access rate (%) for a selected group "),
        ("low_access_count", "Low-access count (estimated people) for a selected group "),
        ("resource_mix", "Food assistance composition "),
    ]

    print("\nMetrics available (choose multiple by number, comma-separated):")
    for i, (_, label) in enumerate(options, start=1):
        print(f"{i} - {label}")

    raw = input("\nEnter metric numbers (e.g. 1,3,5): ").strip()

    picks = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            picks.append(int(part))

    chosen = []
    for idx in picks:
        if 1 <= idx <= len(options):
            chosen.append(options[idx - 1][0])

    out = []
    for m in chosen:
        if m not in out:
            out.append(m)

    if not out:
        print("No valid metrics selected.")
        return None

    return out

# call to functions based on user input
def which_method():

    print("\nWhich information would you like to know?")
    print("1 - Calculate number of people with low access to stores")
    print("2 - Food assistance to population ratio")
    print("3 - Calculate food assistance availability to poverty level")
    print("4 - Calculate food assistance availability to per capita income")
    print("5 - Food Assistance Composition")
    print("6 - Compare multiple metrics across counties")
    print("7 - Filter counties with metrics > threshold")
    print("8 - Filter counties with metrics < threshold")
    print("9 - View food assistance websites for selected county")

    choice = input("\nEnter the number of the method: ").strip()

    if choice == "6":
        county_names = select_multiple_counties()
        if not county_names:
            return

        metrics = select_metrics()
        if not metrics:
            return

        low_access_key = None
        if any(m in ("low_access_rate", "low_access_count") for m in metrics):
            first_county_data = County[county_names[0]]
            low_access_key = select_group(first_county_data)
            if not low_access_key:
                return

        try:
            results = compare_multiple_counties_with_metrics(
                county_names, metrics, low_access_key=low_access_key
            )
        except (KeyError, ValueError) as e:
            print(f"\nError: {e}")
            return

        labels = {
            "poverty": "Poverty (%)",
            "income": "Income ($)",
            "sites_per_100k": "Sites per 100k",
            "total_sites": "Total Sites",
            "low_access_rate": "Low-Access Rate (%)",
            "low_access_count": "Low-Access Count",
            "resource_mix": "Composition",
        }

        group_label = ""
        if low_access_key:
            group_label = low_access_key.replace(", low access to store (2019)", "")

        def fmt(metric, val):
            if metric in ("poverty", "low_access_rate"):
                return f"{val:.2f}%"
            if metric == "income":
                return f"${val:,.0f}"
            if metric == "sites_per_100k":
                return f"{val:.2f}"
            if metric in ("total_sites", "low_access_count"):
                return f"{int(val):,}"
            return str(val)

        print("\nComparison:")
        header = ["County"] + [labels[m] for m in metrics]
        if group_label and any(m in ("low_access_rate", "low_access_count") for m in metrics):
            print(f"(Low-access group: {group_label})")

        print(" | ".join(header))
        print("-" * (len(" | ".join(header)) + 5))

        for county in county_names:
            row = [county]
            for m in metrics:
                if m == "resource_mix":
                    mix = results[county]["resource_mix"]
                    row.append(
                        f"SNAP {mix['SNAP Authorized Stores']:.1f}%, "
                        f"WIC {mix['WIC Authorized Stores']:.1f}%, "
                        f"FoodBanks {mix['Food Banks']:.1f}%, "
                        f"FDPIR {mix['FDPIR Sites']:.1f}%"
                    )
                else:
                    row.append(fmt(m, results[county][m]))
            print(" | ".join(row))

        print("\nRankings by metric (high to low):")
        for m in metrics:
            if m == "resource_mix":
                continue

            ranking = sorted(
                [(c, results[c][m]) for c in county_names],
                key=lambda x: x[1],
                reverse=True
            )

            title = labels[m]
            if m in ("low_access_rate", "low_access_count") and group_label:
                title += f" ({group_label})"

            print(f"\n{title}:")
            for i, (c, v) in enumerate(ranking, start=1):
                print(f"{i}. {c}: {fmt(m, v)}")

        return

    if choice == "7":
        county_names = list(County.keys())
        if not county_names:
            return

        print("\nWhich metric do you want to filter on?")
        print("1 - Poverty rate (%)")
        print("2 - Per capita income")
        print("3 - Total food assistance sites")
        print("4 - Sites per 100,000 people")
        print("5 - Low-access rate (%) for a group")
        print("6 - Low-access count for a group")

        metric_choice = input("\nEnter metric number: ").strip()

        metric_map = {
            "1": "poverty",
            "2": "income",
            "3": "total_sites",
            "4": "sites_per_100k",
            "5": "low_access_rate",
            "6": "low_access_count",
        }

        if metric_choice not in metric_map:
            print("Invalid metric selection.")
            return

        metric = metric_map[metric_choice]

        low_access_key = None
        if metric in ("low_access_rate", "low_access_count"):
            first_county_data = County[county_names[0]]
            low_access_key = select_group(first_county_data)
            if not low_access_key:
                return

        thresh_raw = input("\nEnter threshold value: ").strip()
        try:
            threshold = float(thresh_raw)
        except ValueError:
            print("Invalid threshold.")
            return

        try:
            passed = filter_counties_by_threshold(
                county_names, metric, threshold, low_access_key=low_access_key
            )
        except (KeyError, ValueError) as e:
            print(f"\nError: {e}")
            return

        if not passed:
            print("\nNo counties passed the threshold.")
            return

        def fmt(metric, val):
            if metric in ("poverty", "low_access_rate"):
                return f"{val:.2f}%"
            if metric == "income":
                return f"${val:,.0f}"
            if metric in ("total_sites", "low_access_count"):
                return f"{int(val):,}"
            return f"{val:.2f}"

        label = metric
        if low_access_key and metric in ("low_access_rate", "low_access_count"):
            group_label = low_access_key.replace(", low access to store (2019)", "")
            label += f" ({group_label})"

        print(f"\nCounties where {label} > {threshold}:")
        for county, value in passed:
            print(f"- {county}: {fmt(metric, value)}")

        return
    if choice == "8":
        county_names = list(County.keys())
        if not county_names:
            return

        print("\nWhich metric do you want to filter on?")
        print("1 - Poverty rate (%)")
        print("2 - Per capita income")
        print("3 - Total food assistance sites")
        print("4 - Sites per 100,000 people")
        print("5 - Low-access rate (%) for a group")
        print("6 - Low-access count for a group")

        metric_choice = input("\nEnter metric number: ").strip()

        metric_map = {
            "1": "poverty",
            "2": "income",
            "3": "total_sites",
            "4": "sites_per_100k",
            "5": "low_access_rate",
            "6": "low_access_count",
        }

        if metric_choice not in metric_map:
            print("Invalid metric selection.")
            return

        metric = metric_map[metric_choice]

        low_access_key = None
        if metric in ("low_access_rate", "low_access_count"):
            first_county_data = County[county_names[0]]
            low_access_key = select_group(first_county_data)
            if not low_access_key:
                return

        thresh_raw = input("\nEnter threshold value: ").strip()
        try:
            threshold = float(thresh_raw)
        except ValueError:
            print("Invalid threshold.")
            return

        try:
            passed = filter_counties_by_thresholdless(
                county_names, metric, threshold, low_access_key=low_access_key
            )
        except (KeyError, ValueError) as e:
            print(f"\nError: {e}")
            return

        if not passed:
            print("\nNo counties passed the threshold.")
            return

        def fmt(metric, val):
            if metric in ("poverty", "low_access_rate"):
                return f"{val:.2f}%"
            if metric == "income":
                return f"${val:,.0f}"
            if metric in ("total_sites", "low_access_count"):
                return f"{int(val):,}"
            return f"{val:.2f}"

        label = metric
        if low_access_key and metric in ("low_access_rate", "low_access_count"):
            group_label = low_access_key.replace(", low access to store (2019)", "")
            label += f" ({group_label})"

        print(f"\nCounties where {label} < {threshold}:")
        for county, value in passed:
            print(f"- {county}: {fmt(metric, value)}")

        return
    # ---------- Options 1–5: single-county ----------
    county_name = select_county()
    if not county_name:
        return

    county_data = County[county_name]
    county_obj = CountyObj(county_data)

    if choice == "1":
        group_key = select_group(county_data)
        if not group_key:
            return

        count = calculate_low_access(county_obj, group_key)
        print(
            f"\nEstimated number of {group_key.replace(', low access to store (2019)','')} with low access in {county_name}: {count}"
        )

    elif choice == "2":
        ratio = food_assistance_to_pop_ratio(county_obj)
        print(f"\nFood assistance to population ratio in {county_name}: {ratio:}")

    elif choice == "3":
        poverty_percent, total_food_sites, sites_per_1000 = compare_food_assistance_to_poverty(county_obj)
        print(f"\n{county_name} Poverty Rate: {poverty_percent}%")
        print(f"Total Food Assistance Sites: {total_food_sites}")
        print(f"Food Assistance Sites per 1000 People in Poverty: {sites_per_1000:}")

    elif choice == "4":
        income, total_food_sites, sites_per_100k = compare_food_assistance_to_income(county_obj)
        print(f"\n{county_name} Per Capita Income: ${income}")
        print(f"Total Food Assistance Sites: {total_food_sites}")
        print(f"Food Assistance Sites per 100,000 People: {sites_per_100k:}")

    elif choice == "5":
        total_sites, breakdown = resource_mix_breakdown(county_obj)
        print(f"\n{county_name} Total Food Assistance Sites: {total_sites}")
        print("Resource mix (% of total sites):")
        for label, pct in breakdown.items():
            print(f"- {label}: {pct:}%")
    elif choice == "9":
        if not county_name:
            return
        print_county_website(county_name)
        return
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    which_method()