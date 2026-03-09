import main
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
# 1
def test_low_access_hispanic_la():
    result = main.calculate_low_access(
        los_angeles_data,
        "Hispanic, low access to store (2019)"
    )
    assert result > 0


def test_low_access_children_orange():
    result = main.calculate_low_access(
        orange_data,
        "Children, low access to store (2019)"
    )
    assert result > 0

#2
def test_food_ratio_la():
    ratio = main.food_assistance_to_pop_ratio(los_angeles_data)
    assert ratio > 0


def test_food_ratio_orange():
    ratio = main.food_assistance_to_pop_ratio(orange_data)
    assert ratio > 0

#3
def test_food_vs_poverty_la():
    poverty, sites, ratio = main.compare_food_assistance_to_poverty(los_angeles_data)

    assert poverty > 0
    assert sites > 0
    assert ratio > 0


def test_food_vs_poverty_orange():
    poverty, sites, ratio = main.compare_food_assistance_to_poverty(orange_data)

    assert poverty > 0
    assert sites > 0
    assert ratio > 0

#4
def test_food_vs_income_la():
    income, sites, ratio = main.compare_food_assistance_to_income(los_angeles_data)

    assert income > 0
    assert sites > 0
    assert ratio > 0


def test_food_vs_income_orange():
    income, sites, ratio = main.compare_food_assistance_to_income(orange_data)

    assert income > 0
    assert sites > 0
    assert ratio > 0