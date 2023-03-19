"""
Test for Question 2 of Quiz 2

To activate pytest on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Expand Python Integrated Tools
> under Testing section: Default test runner, select pytest
> click Fix to install the module if prompted

Auther: Amin G. Alhashim (aalhashi@maclester.edu)
"""

from Question2 import *


def test_empty_list() -> None:
    """
    A unit test when the input is empty

    :return: None
    """

    input_list = []
    expected = 0
    assert sum_even(input_list) == expected


def test_one_even_list() -> None:
    """
    A unit test when the input contains a single even number

    :return: None
    """

    input_list = [4]
    expected = 4
    assert sum_even(input_list) == expected


def test_one_odd_list() -> None:
    """
    A unit test when the input contains a single odd number

    :return: None
    """

    input_list = [5]
    expected = 0
    assert sum_even(input_list) == expected


def test_one_zero_list() -> None:
    """
    A unit test when the input contains a single zero

    :return: None
    """

    input_list = [0]
    expected = 0
    assert sum_even(input_list) == expected


def test_evens_first_list() -> None:
    """
    A unit test when the input contains even numbers followed by odd numbers

    :return: None
    """

    input_list = [2, 2, 2, 3, 3, 3]
    expected = 6
    assert sum_even(input_list) == expected


def test_odd_first_list() -> None:
    """
    A unit test when the input contains odd numbers followed by even numbers

    :return: None
    """

    input_list = [3, 3, 3, 2, 2, 2]
    expected = 6
    assert sum_even(input_list) == expected


def test_all_even_list() -> None:
    """
    A unit test when the input contains only even numbers

    :return: None
    """

    input_list = [2, 2, 2]
    expected = 6
    assert sum_even(input_list) == expected


def test_all_odd_list() -> None:
    """
    A unit test when the input contains only odd numbers

    :return: None
    """

    input_list = [3, 3, 3]
    expected = 0
    assert sum_even(input_list) == expected


def test_even_mix_odd_list() -> None:
    """
    A unit test when the input contains even and odd numbers

    :return: None
    """

    input_list = [2, 3, 2, 3, 2, 3]
    expected = 6
    assert sum_even(input_list) == expected

