# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        str_0 = None
        bool_0 = module_0.is_isbn_10(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'V'
        bool_0 = module_0.is_full_string(str_0)
        bool_1 = module_0.is_decimal(str_0)
        bool_2 = module_0.is_palindrome(str_0, bool_1)
        bool_3 = module_0.is_decimal(str_0)
        bytes_0 = b'\xed?e\x06\xb6\x12 \xfa\x9e[#\x81'
        bool_4 = module_0.is_url(bytes_0, bytes_0)
        bool_5 = module_0.is_string(bytes_0)
        str_1 = None
        bool_6 = module_0.is_decimal(str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'http://www.mysite.com'
        bool_0 = module_0.is_url(str_0)
        bool_1 = module_0.is_url(str_0)
        str_1 = 'l'
        bool_2 = module_0.is_credit_card(str_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '255.2.100.75'
        bool_0 = module_0.is_snake_case(str_0)
        str_1 = 'nope'
        str_2 = 'nope'
        bool_1 = module_0.is_ip_v4(str_0)
        bool_2 = module_0.is_email(str_0)
        bool_3 = module_0.is_email(bool_1)
        bool_4 = True
        bool_5 = module_0.is_uuid(str_2, bool_4)
        str_3 = 'J,wsqO(:Yjv"\\unq*~0'
        str_4 = 'z'
        bool_6 = module_0.is_decimal(str_4)
        str_5 = "B$4D<&69 A'.W"
        bool_7 = module_0.is_ip_v6(str_0)
        bool_8 = module_0.is_isbn(str_5)
        bool_9 = module_0.is_credit_card(str_3, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1Pdn\\SL4YW`UR'
        str_1 = 'q'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
        bool_0 = i_s_b_n_checker_0.is_isbn_13()
        str_2 = None
        bool_1 = module_0.is_ip(str_0)
        bool_2 = module_0.contains_html(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'h\x98\x1c\xc7\xc1^\x8d\x123\x99\x1b]N\xcae\xc6'
        bool_0 = None
        bool_1 = module_0.is_uuid(bytes_0, bool_0)
        str_0 = 'k/*^YE]\t4]m<.0yC!I'
        bool_2 = module_0.is_isbn_10(str_0)
        bool_3 = module_0.is_ip_v4(bytes_0)
        bool_4 = module_0.is_credit_card(bool_3)
        bytes_1 = b'\xaf\x92\xdb=\x147\xfc\x8f2'
        bool_5 = module_0.is_ip(bool_3)
        list_0 = [bytes_1, bytes_1, bytes_1, bytes_1]
        bool_6 = module_0.is_uuid(list_0, bool_3)
        bool_7 = module_0.is_pangram(list_0)
        str_1 = None
        bool_8 = module_0.is_pangram(list_0)
        str_2 = 'LM Hb0'
        str_3 = '>Qt\n'
        bool_9 = module_0.is_decimal(str_3)
        str_4 = '4)&X5f@@?!&V?&.;>A'
        bool_10 = module_0.is_number(str_4)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_7)
        bool_11 = i_s_b_n_checker_0.is_isbn_10()
        bool_12 = module_0.is_full_string(bool_7)
        int_0 = module_0.words_count(str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_credit_card(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '255.20.100.75'
        bool_0 = module_0.is_ip(str_0)
        bool_1 = module_0.is_email(bool_0)
        bool_2 = module_0.is_isbn_13(str_0)
        str_1 = '"\\ has space"@the-provider.com\\ has space'
        bool_3 = module_0.is_email(str_1)
        str_2 = 'J,wsqO(:Yjv"\\unq*~0'
        str_3 = '\ns+D+>'
        str_4 = 'compress'
        str_5 = '5'
        bool_4 = module_0.is_integer(str_5)
        str_6 = 'coLHB5B'
        bool_5 = module_0.is_decimal(str_6)
        bool_6 = False
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_6)
        bool_7 = module_0.is_isbn(str_4, bool_0)
        bool_8 = module_0.is_credit_card(str_2, str_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '9780312498580'
        bool_0 = module_0.is_isbn(str_0)
        str_1 = '1506715214'
        bool_1 = module_0.is_isbn(str_1)
        str_2 = '9780000000000'
        bool_2 = module_0.is_isbn(str_2)
        str_3 = '150715214'
        bool_3 = module_0.is_isbn(str_3)
        str_4 = 'hello'
        bool_4 = module_0.is_isbn(str_4)
        str_5 = ''
        bool_5 = module_0.is_isbn(str_5)
        var_0 = None
        bool_6 = module_0.is_isbn(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '255.20.100.75'
        bool_0 = module_0.is_ip(str_0)
        bool_1 = module_0.is_email(bool_0)
        bool_2 = module_0.is_isbn_13(str_0)
        str_1 = '"\\ has spaceC@the-providvr.com\\ hasBspace'
        bool_3 = module_0.is_email(str_1)
        str_2 = '\ns+D+>'
        str_3 = 'compress'
        str_4 = 'TKej@e#(0zc3+\\O\r'
        bool_4 = module_0.is_decimal(str_4)
        bool_5 = module_0.is_decimal(str_1)
        bool_6 = module_0.is_ip_v6(bool_3)
        bool_7 = module_0.is_isbn(str_2)
        bool_8 = module_0.is_credit_card(str_0, str_3)
    except BaseException:
        pass