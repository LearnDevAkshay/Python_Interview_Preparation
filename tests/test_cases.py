import pytest

from Assigments.character_repetition import first_non_repeating_character, max_occurring_character
from Assigments.check_rotation import check_rotation
from Assigments.check_string_anagram import check_anagram
from Assigments.count_word_frequency import count_word_frequency
from Assigments.duplicate_in_list import duplicate_in_list
from Assigments.factorial import find_factorial
from Assigments.fibonaci_series import create_fibonaci_series
from Assigments.longest_sub_string import longest_substring
from Assigments.move_all_zeros_to_last import move_zeros_to_last
from Assigments.prime_number import check_prime
from Assigments.remove_duplicates import remove_duplicates
from Assigments.reverse_string import reverse_string
from Assigments.reverse_word_in_sentence import reverse_sentence
from Assigments.rotation_of_list import rotate_list
from Assigments.sum_of_all_digits import calculate_sum_of_digits
from Assigments.swap_two_numbers import swap_num


def test_reverse_string():
    assert reverse_string(input_string="Automation") == "noitamotuA"


def test_reverse_word_in_sentence():
    assert reverse_sentence("my name is Akshay") == "Akshay is name my"

def test_count_word_frequency():
    assert count_word_frequency("test automation test pytest")=={'automation': 1,'test': 2,'pytest': 1}

def test_duplicate_in_list():
    assert duplicate_in_list(['hi','akshay','test','read','test','read','test','write','hi'])==['hi', 'test', 'read']

def test_remove_duplicate_with_maintaining_order():
    assert remove_duplicates([1,2,3,4,1,2,3,5])==[1, 2, 3, 4, 5]

def test_first_non_repeating_character():
    assert first_non_repeating_character("test") == 'e'

def test_max_occurring_character():
    assert max_occurring_character("testautomation") == 't'

def test_check_anagram():
    assert check_anagram("Listen","Silent") == True


def test_move_all_zeros_to_last():
   my_list = [0, 1, 0, 3, 12]
   expected_list = [1, 3, 12, 0, 0]
   assert move_zeros_to_last(my_list) == expected_list

def test_rotation_of_list():
    my_list = [1, 2, 3, 4, 5]
    expected_list = [4, 5, 1, 2, 3]
    input_rotation  = 7
    assert rotate_list(my_list,input_rotation) == expected_list



def test_swap_two_numbers_without_temp():
    a = 10
    b = 20
    assert swap_num(a,b) == (20,10)

def test_factorial():
    a = 5
    assert find_factorial(a)== 120

def test_prime_number():
    a =  6
    assert check_prime(a) == True

def test_fibonaci_series():
    a =  5
    exp_series =[0, 1, 1, 2, 3]
    assert create_fibonaci_series(5) == exp_series

def test_of_all_digits():
    num =  1234
    print(calculate_sum_of_digits(num))

def test_reverse_words_in_sentence():
    str = " hi this is akshay"

def test_longest_sub_string():
    print(longest_substring('abcabcbb'))


def test_string_rotation():
   s1= 'abcd'
   s2 = 'cdab'
   s5 = 'test'
   s3 ='test'
   s4 = 'test2'
   assert check_rotation(s1,s2) == True

