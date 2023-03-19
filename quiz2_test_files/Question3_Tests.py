"""
Test for Question 3 of Quiz 2

To activate pytest on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Expand Python Integrated Tools
> under Testing section: Default test runner, select pytest
> click Fix to install the module if prompted

Auther: Amin G. Alhashim (aalhashi@maclester.edu)
"""

from Question3 import  *


def test_empty_dict() -> None:
    """
    A unit test when the input is empty

    :return: None
    """
    input_dict = {}
    expected = {}
    assert clean_dict(input_dict) == expected


def test_return_new_dict() -> None:
    """
    A unit test to check if new dict is created

    :return: None
    """
    input_dict = {}
    expected = clean_dict(input_dict)
    assert input_dict is not expected


def test_one_neg() -> None:
    """
    A unit test when the input contains one item with negative quantity

    :return: None
    """
    input_dict = {'a': -3}
    expected = {}
    assert clean_dict(input_dict) == expected


def test_one_pos() -> None:
    """
    A unit test when the input contains one item with positive quantity

    :return: None
    """
    input_dict = {'a': 3}
    expected = {'a': 3}
    assert clean_dict(input_dict) == expected


def test_one_zero() -> None:
    """
    A unit test when the input contains one item with zero quantity

    :return: None
    """
    input_dict = {'a': 0}
    expected = {}
    assert clean_dict(input_dict) == expected


def test_all_neg() -> None:
    """
    A unit test when the input contains only item with negative quantities

    :return: None
    """
    input_dict = {'a': -1, 'b': -2, 'c': -3}
    expected = {}
    assert clean_dict(input_dict) == expected


def test_all_pos() -> None:
    """
    A unit test when the input contains only items with positive quantities

    :return: None
    """
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = {'a': 1, 'b': 2, 'c': 3}
    assert clean_dict(input_dict) == expected


def test_all_zeros() -> None:
    """
    A unit test when the input contains only items with zero quantities

    :return: None
    """
    input_dict = {'a': 0, 'b': 0, 'c': 0}
    expected = {}
    assert clean_dict(input_dict) == expected


def test_neg_first() -> None:
    """
    A unit test when the input contains items with negative quantities
    followed by items with positive quantities

    :return: None
    """
    input_dict = {'a': -1, 'b': -2, 'c': -3, 'd': 1, 'e': 2, 'f': 3}
    expected = {'d': 1, 'e': 2, 'f': 3}
    assert clean_dict(input_dict) == expected


def test_pos_first() -> None:
    """
    A unit test when the input contains items with positive quantities
    followed by items with negative quantities

    :return: None
    """
    input_dict = {'d': 1, 'e': 2, 'f': 3, 'a': -1, 'b': -2, 'c': -3}
    expected = {'d': 1, 'e': 2, 'f': 3}
    assert clean_dict(input_dict) == expected


def test_neg_pos_mixed() -> None:
    """
    A unit test when the input contains items with negative and positive
    quantities mixed togother

    :return: None
    """
    input_dict = {'a': -1, 'd': 1, 'b': -2, 'e': 2, 'c': -3, 'f': 3}
    expected = {'d': 1, 'e': 2, 'f': 3}
    assert clean_dict(input_dict) == expected
