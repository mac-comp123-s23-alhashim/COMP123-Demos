"""
Test for Question 1 of Quiz 2

To activate pytest on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Expand Python Integrated Tools
> under Testing section: Default test runner, select pytest
> click Fix to install the module if prompted

Auther: Amin G. Alhashim (aalhashi@maclester.edu)
"""

from Question1 import *

def test_list_tuple() -> None:
    """
    A unit test for the list_tuple variable

    :return: None
    """
    # a list containing 3 items
    assert type(list_tuple) == list
    assert len(list_tuple) == 3

    # all the elements are tuples with 2 integer items each
    for e in list_tuple:
        assert type(e) == tuple
        assert len(e) == 2
        for i in e:
            assert type(i) == int

def test_dict_tuple() -> None:
    """
    A unit test for the dict_tuple variable

    :return: None
    """
    # a dict of 3 items
    assert type(dict_tuple) == dict
    assert len(dict_tuple) == 3

    # all the elements are tuples-string with tuples made up of 2 integers
    for e in dict_tuple:
        assert type(e) == tuple
        assert len(e) == 2
        for i in e:
            assert type(i) == int
        assert type(dict_tuple[e]) == str


def test_tuple_dict() -> None:
    """
    A unit test for the tuple_dict variable

    :return: None
    """
    # a tuple of 3 items
    assert type(tuple_dict) == tuple
    assert len(tuple_dict) == 3

    # all the elements are dictionaires each is made up of 2 string-integer
    # items
    for e in tuple_dict:
        assert type(e) == dict
        assert len(e) == 2
        for i in e:
            assert type(i) == str
            assert type(e[i]) == int


def test_list_dict() -> None:
    """
    A unit test for the list_dict variable

    :return: None
    """
    # a list of 3 items
    assert type(list_dict) == list
    assert len(list_dict) == 2

    # all the elements are dictionaries, each made up of 2 integer-tuple item
    # and each tuple contains 3 strings
    for e in list_dict:
        assert type(e) == dict
        assert len(e) == 2
        for i in e:
            assert type(i) == int
            assert type(e[i]) == tuple
            assert len(e[i]) == 2
            for m in e[i]:
                assert type(m) == str
