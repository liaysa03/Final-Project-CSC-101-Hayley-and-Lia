import main
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
# 1
def test_low_access_hispanic_la():
    result = main.calculate_low_access(
        los_angeles_dict,
        "Hispanic, low access to store (2019)"
    )
    assert result > 0


def test_low_access_children_orange():
    result = main.calculate_low_access(
        orange_dict,
        "Children, low access to store (2019)"
    )
    assert result > 0

#2
def test_food_ratio_la():
    ratio = main.food_assistance_to_pop_ratio(san_diego_dict)
    assert ratio > 0


def test_food_ratio_orange():
    ratio = main.food_assistance_to_pop_ratio(riverside_dict)
    assert ratio > 0

#3
def test_food_vs_poverty_la():
    poverty, sites, ratio = main.compare_food_assistance_to_poverty(san_bernardino_dict)

    assert poverty > 0
    assert sites > 0
    assert ratio > 0


def test_food_vs_poverty_orange():
    poverty, sites, ratio = main.compare_food_assistance_to_poverty(ventura_dict)

    assert poverty > 0
    assert sites > 0
    assert ratio > 0

#4
def test_food_vs_income_la():
    income, sites, ratio = main.compare_food_assistance_to_income(santa_barbara_dict)

    assert income > 0
    assert sites > 0
    assert ratio > 0


def test_food_vs_income_orange():
    income, sites, ratio = main.compare_food_assistance_to_income(kern_dict)

    assert income > 0
    assert sites > 0
    assert ratio > 0

#5
def test_resource_mix_la():
    total, breakdown = main.resource_mix_breakdown(imperial_dict)

    assert total > 0
    assert isinstance(breakdown, dict)


def test_resource_mix_orange():
    total, breakdown = main.resource_mix_breakdown(san_luis_obispo_dict)

    assert total > 0
    assert "SNAP Authorized Stores" in breakdown

#6
def test_compare_multiple_poverty():
    counties = ["Los Angeles", "Orange"]
    metrics = ["poverty"]

    result = main.compare_multiple_counties_with_metrics(counties, metrics)

    assert "Los Angeles" in result
    assert "poverty" in result["Los Angeles"]


def test_compare_multiple_sites():
    counties = ["San Diego", "Riverside"]
    metrics = ["total_sites"]

    result = main.compare_multiple_counties_with_metrics(counties, metrics)

    assert result["San Diego"]["total_sites"] > 0

#7
def test_filter_threshold_poverty():
    counties = ["San Bernardino", "Ventura"]

    result = main.filter_counties_by_threshold(counties, "poverty", 5)

    assert isinstance(result, list)


def test_filter_threshold_sites():
    counties = ["Santa Barbara", "Kern"]

    result = main.filter_counties_by_threshold(counties, "total_sites", 100)

    assert len(result) >= 0

#8
def test_filter_thresholdless_income():
    counties = ["Imperial", "San Luis Obispo"]

    result = main.filter_counties_by_thresholdless(counties, "income", 100000)

    assert isinstance(result, list)


def test_filter_thresholdless_sites():
    counties = ["Los Angeles", "Orange"]

    result = main.filter_counties_by_thresholdless(counties, "total_sites", 10000)

    assert isinstance(result, list)

#9
def test_print_county_website_la():
    main.print_county_website("San Diego")


def test_print_county_website_orange():
    main.print_county_website("Riverside")
