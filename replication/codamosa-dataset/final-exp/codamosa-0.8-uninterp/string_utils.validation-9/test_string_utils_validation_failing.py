# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        list_0 = None
        bool_0 = module_0.is_ip(list_0)
        bool_1 = module_0.is_snake_case(list_0)
        str_0 = None
        bool_2 = True
        bool_3 = module_0.is_isbn_13(str_0, bool_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '+zM#q}Ow^|'
        bool_0 = module_0.is_json(str_0)
        bool_1 = False
        bool_2 = True
        bool_3 = module_0.is_uuid(bool_1, bool_2)
        bool_4 = module_0.is_palindrome(str_0, bool_1)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_5 = None
        bool_6 = module_0.is_palindrome(str_0, bool_5)
        bool_7 = i_s_b_n_checker_0.is_isbn_10()
        str_1 = '\n\x0bq:7E\x0b4WUh'
        bool_8 = module_0.is_isbn_13(str_1)
        str_2 = None
        bool_9 = module_0.is_number(str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        complex_0 = None
        bool_0 = module_0.is_ip_v6(complex_0)
        str_0 = 'RfW\x0c\\g&7^ '
        bool_1 = module_0.is_integer(str_0)
        bool_2 = module_0.is_camel_case(complex_0)
        str_1 = 'Q'
        bool_3 = module_0.contains_html(str_1)
        str_2 = 'HVVXVR\x0b3'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
        bool_4 = module_0.is_pangram(bool_2)
        bool_5 = module_0.is_json(bool_4)
        bool_6 = module_0.is_string(str_1)
        bool_7 = module_0.is_isbn_13(str_0)
        bool_8 = module_0.is_snake_case(bool_5)
        bool_9 = module_0.is_ip(complex_0)
        bool_10 = module_0.is_pangram(bool_4)
        bool_11 = module_0.is_uuid(bool_2)
        str_3 = '|'
        bool_12 = module_0.is_credit_card(str_3, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '(?%bs$I)3I /qmu;M9'
        bool_0 = module_0.is_ip(str_0)
        bool_1 = True
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_1)
        str_1 = None
        bool_2 = module_0.contains_html(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '&}yf9!'
        bool_0 = module_0.is_full_string(str_0)
        bool_1 = False
        bool_2 = module_0.is_snake_case(bool_0)
        bool_3 = module_0.is_camel_case(bool_0)
        bool_4 = module_0.is_isbn_13(str_0)
        str_1 = 'gVumq}ETC\rE&'
        bool_5 = module_0.is_ip_v6(str_1)
        str_2 = None
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_1)
        int_0 = module_0.words_count(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xfb\xd1\xe4\xbd\x86\xd4*M\x98\xd2\xf3\x0f\xaf\x1e\x81'
        bool_0 = module_0.is_ip_v6(bytes_0)
        str_0 = 'n'
        str_1 = '7'
        bool_1 = module_0.is_full_string(str_1)
        bool_2 = module_0.is_decimal(str_1)
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_3 = module_0.is_snake_case(dict_0)
        str_2 = '!?'
        bool_4 = module_0.is_ip_v6(str_2)
        str_3 = None
        bool_5 = module_0.is_url(dict_0)
        bool_6 = module_0.is_integer(str_2)
        bool_7 = module_0.is_url(bool_4)
        bool_8 = module_0.is_isbn(str_3)
    except BaseException:
        pass