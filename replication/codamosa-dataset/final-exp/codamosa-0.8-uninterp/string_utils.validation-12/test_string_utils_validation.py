# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'y\tj6\n.'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)

def test_case_2():
    bool_0 = True
    str_0 = 'p{|.\n"@(yBQap'
    bool_1 = True
    bool_2 = module_0.is_isbn(str_0, bool_1)
    bool_3 = module_0.is_ip_v6(bool_0)

def test_case_3():
    str_0 = 'dFpW'
    bool_0 = module_0.is_isbn(str_0)

def test_case_4():
    str_0 = '123456789X'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0)
    bool_1 = i_s_b_n_checker_1.is_isbn_10()

def test_case_5():
    str_0 = '3TBUC[\\SUPM'
    bool_0 = module_0.is_isogram(str_0)

def test_case_6():
    str_0 = 'u~$:'
    bool_0 = module_0.is_decimal(str_0)

def test_case_7():
    bool_0 = False
    bool_1 = module_0.is_pangram(bool_0)
    str_0 = 'RhxJR;9<m(=`#~R]'
    bool_2 = module_0.is_integer(str_0)
    str_1 = ''
    bool_3 = module_0.is_number(str_1)
    str_2 = '\n    Check if a string is a valid json.\n\n    *Examples:*\n\n    >>> is_json(\'{"name": "Peter"}\') # returns true\n    >>> is_json(\'[1, 2, 3]\') # returns true\n    >>> is_json(\'{nope}\') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if json, false otherwise\n    '
    bool_4 = module_0.is_number(str_2)

def test_case_8():
    str_0 = '\ny.mail@the-provOder.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    str_2 = 'ha}0T1'
    bool_1 = module_0.is_url(str_2)
    bool_2 = module_0.is_email(str_1)

def test_case_9():
    str_0 = '&Z\'iQYp"alaA'
    bool_0 = module_0.is_isbn_13(str_0)
    str_1 = 'x^sXm;OO?USsC,'
    bool_1 = module_0.is_pangram(str_1)
    str_2 = '_qz-T,E~tVF_|2Z'
    bool_2 = module_0.is_isbn_10(str_2, bool_1)
    bool_3 = True
    str_3 = None
    list_0 = [str_0, str_3]
    bool_4 = module_0.is_url(str_0, list_0)
    bool_5 = module_0.is_isbn_13(str_1, bool_3)
    bool_6 = module_0.is_ip(bool_1)

def test_case_10():
    str_0 = "'otsbN"
    bool_0 = module_0.is_email(str_0)

def test_case_11():
    float_0 = 2165.585
    set_0 = {float_0, float_0, float_0}
    bool_0 = module_0.is_email(set_0)

def test_case_12():
    str_0 = 'xF4'
    bool_0 = module_0.is_credit_card(str_0)

def test_case_13():
    bytes_0 = None
    bool_0 = module_0.is_credit_card(bytes_0)

def test_case_14():
    str_0 = ')Qu7'
    bool_0 = True
    bool_1 = module_0.is_isbn_10(str_0, bool_0)
    str_1 = '-{)tA:k'
    bool_2 = module_0.is_email(str_1)
    bool_3 = module_0.is_camel_case(str_1)
    bool_4 = module_0.is_pangram(bool_2)

def test_case_15():
    str_0 = '\n4\n'
    bool_0 = module_0.is_number(str_0)
    bool_1 = module_0.is_snake_case(bool_0)

def test_case_16():
    str_0 = "{'name': 'Peter'}"
    bool_0 = module_0.is_json(str_0)

def test_case_17():
    str_0 = '^[a-z]{2}_[a-z]{2}$'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    str_1 = 'ascii'
    bool_0 = module_0.is_snake_case(i_s_b_n_checker_0, str_1)
    str_2 = ''
    bool_1 = module_0.is_uuid(str_2)
    bool_2 = module_0.is_palindrome(bool_1)
    bool_3 = i_s_b_n_checker_0.is_isbn_10()
    bool_4 = i_s_b_n_checker_0.is_isbn_10()
    bool_5 = module_0.is_isbn(str_2)

def test_case_18():
    bytes_0 = b'\xb3'
    bool_0 = module_0.is_ip(bytes_0)

def test_case_19():
    bool_0 = True
    bool_1 = module_0.is_ip_v6(bool_0)

def test_case_20():
    bool_0 = False
    str_0 = '/`[}+Rn$h[<NMOA_m'
    bool_1 = module_0.is_ip_v6(bool_0)
    bool_2 = module_0.is_pangram(bool_0)
    str_1 = '>*Zf'
    bool_3 = module_0.is_integer(str_1)
    bool_4 = module_0.is_string(bool_0)
    bool_5 = module_0.is_palindrome(str_0)

def test_case_21():
    bytes_0 = b'~\n\xb1\x93\x85vf\xc1\xba\x1a\xc7\xfeK\xf1\xbf\x9d\x92'
    bool_0 = False
    bool_1 = False
    bool_2 = module_0.is_palindrome(bytes_0, bool_0, bool_1)

def test_case_22():
    str_0 = 'x^sXm;OO?USsC,'
    bool_0 = module_0.is_pangram(str_0)
    str_1 = '_qz-T,E~tVF_|2Z'
    bool_1 = module_0.is_isbn_10(str_1, bool_0)
    bool_2 = True
    bool_3 = module_0.is_isbn_13(str_0, bool_2)
    bool_4 = module_0.is_ip(bool_0)

def test_case_23():
    float_0 = -1226.4
    str_0 = 'R\x0bv\nZGI=ku*f8PMTz\\j'
    bool_0 = module_0.is_camel_case(float_0)
    bool_1 = module_0.is_isbn_13(str_0)
    bool_2 = module_0.is_email(str_0)
    str_1 = 'P)NK4X\x0b`[LZ&oI8H-iAR'
    bool_3 = True
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_3)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0)
    bool_4 = module_0.is_slug(str_0)
    bool_5 = module_0.is_credit_card(float_0, str_0)

def test_case_24():
    bytes_0 = b'\x85\xb4o\xf4\xc8l-'
    str_0 = 'k{wA+A\tE?y?5FDR[N)<.'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    bool_1 = module_0.is_slug(bytes_0)
    bool_2 = module_0.is_ip(bytes_0)

def test_case_25():
    str_0 = '%" jE6)$Y0X'
    bool_0 = module_0.contains_html(str_0)

def test_case_26():
    str_0 = 'CQ ]!j{nMEY?KzVeM'
    int_0 = module_0.words_count(str_0)

def test_case_27():
    str_0 = '&'
    bool_0 = module_0.is_ip_v4(str_0)
    int_0 = module_0.words_count(str_0)
    set_0 = None
    bool_1 = module_0.is_isbn_10(str_0)
    bool_2 = module_0.is_ip_v6(set_0)

def test_case_28():
    str_0 = '>{9rA6cN];=;'
    bool_0 = True
    bool_1 = module_0.is_isbn_13(str_0, bool_0)

def test_case_29():
    float_0 = -2528.56
    bool_0 = module_0.is_camel_case(float_0)
    optional_0 = None
    str_0 = '` #p67TH6T=Mv\n[twQYV'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_1 = module_0.is_isogram(i_s_b_n_checker_0)
    bool_2 = module_0.is_credit_card(float_0, optional_0)
    bool_3 = module_0.is_snake_case(float_0)
    str_1 = 'oViHy-9,::'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)

def test_case_30():
    str_0 = 'cJ\t\nr|JT2~C6\r)6\x0bU'
    bool_0 = module_0.is_decimal(str_0)
    bool_1 = module_0.is_json(str_0)

def test_case_31():
    str_0 = '\x0b/Czm*#bjyL/8'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '[1,2,3]'
    bool_1 = module_0.is_json(str_1)
    bool_2 = module_0.is_json(bool_0)

def test_case_32():
    str_0 = '&'
    bool_0 = module_0.is_ip_v4(str_0)

def test_case_33():
    str_0 = '127.0.0.1'
    bool_0 = module_0.is_ip(str_0)

def test_case_34():
    str_0 = 'VISA'
    bool_0 = module_0.is_ip(str_0)
    bool_1 = module_0.is_ip(str_0)
    bool_2 = True
    bool_3 = module_0.is_snake_case(bool_2)
    bool_4 = module_0.is_uuid(str_0, bool_2)
    str_1 = 'a2Q2#Oc(P|-k$Eu-'
    bool_5 = module_0.is_email(str_1)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_6 = i_s_b_n_checker_0.is_isbn_10()
    bool_7 = i_s_b_n_checker_0.is_isbn_10()

def test_case_35():
    str_0 = 'a'
    bool_0 = module_0.is_palindrome(str_0)
    bool_1 = module_0.is_palindrome(str_0)
    bool_2 = True
    bool_3 = module_0.is_palindrome(str_0, bool_2)
    bool_4 = module_0.is_palindrome(str_0, bool_2, bool_2)
    bool_5 = module_0.is_palindrome(str_0, bool_1, bool_2)
    bool_6 = module_0.is_ip_v4(bool_4)

def test_case_36():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)

def test_case_37():
    str_0 = '.my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'my.email@the-provider.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'my..email@the-provider.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'my@.email@the-provider.com'
    bool_3 = module_0.is_email(str_3)
    bool_4 = module_0.is_json(bool_3)
    bool_5 = module_0.is_json(bool_0)
    bool_6 = module_0.is_json(bool_0)
    float_0 = 3.14
    bool_7 = module_0.is_json(float_0)

def test_case_38():
    str_0 = '1'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_full_string(str_0)
    bool_2 = module_0.is_string(str_0)
    bool_3 = module_0.is_json(str_0)
    bool_4 = module_0.is_integer(str_0)
    bool_5 = module_0.is_credit_card(bool_1, str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_6 = module_0.is_isbn_10(str_0)
    bool_7 = False
    bool_8 = i_s_b_n_checker_0.is_isbn_13()
    bool_9 = module_0.is_isbn(str_0)
    bool_10 = module_0.is_credit_card(str_0)
    list_0 = [bool_6]
    bool_11 = module_0.is_snake_case(list_0)
    bool_12 = module_0.is_email(bool_5)
    bool_13 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = 'z '
    bool_14 = False
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1, bool_14)
    bool_15 = module_0.is_url(i_s_b_n_checker_1)
    list_1 = None
    bool_16 = module_0.is_url(bool_15)
    str_2 = ',[EUCUL'
    str_3 = 'SPACES_AROUND'
    bool_17 = module_0.is_isbn_13(str_3)
    bool_18 = module_0.is_number(str_0)
    str_4 = 'O'
    bool_19 = module_0.is_slug(list_1, str_2)
    bool_20 = True
    bool_21 = module_0.is_palindrome(str_4, bool_20)
    dict_0 = {bool_12: str_3, str_1: bool_9, bool_10: bool_2, bool_7: bool_6}
    bool_22 = module_0.is_ip_v6(dict_0)

def test_case_39():
    str_0 = '0Y.@D<O/J\\V}-z}**'
    bool_0 = module_0.is_integer(str_0)
    bytes_0 = b'@P\x08t\x97\xd4\xbe:\xd1\xfc'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_1 = module_0.is_url(bytes_0)
    bytes_1 = b'D\x81'
    bool_2 = module_0.is_ip_v6(bytes_1)
    bytes_2 = b'$\x9e\x88qkd\xb8-\xf6'
    bool_3 = module_0.is_url(bytes_2)
    bool_4 = module_0.is_isogram(bytes_2)
    bool_5 = module_0.is_email(str_0)
    bool_6 = i_s_b_n_checker_0.is_isbn_10()
    bool_7 = module_0.is_isogram(bytes_2)
    bool_8 = module_0.is_number(str_0)
    bool_9 = module_0.is_json(bool_6)

def test_case_40():
    str_0 = '192.168.1.1'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = '192.168.1.abc'
    bool_1 = module_0.is_ip_v4(str_1)
    str_2 = '978-0312498580'
    str_3 = '('
    bool_2 = module_0.is_isbn(str_3, bool_0)
    bool_3 = module_0.is_isbn(str_2, bool_0)

def test_case_41():
    str_0 = '6'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_string(str_0)
    bool_2 = module_0.is_json(str_0)
    bool_3 = module_0.is_credit_card(bool_2, str_0)
    bool_4 = module_0.is_url(bool_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_5 = module_0.is_isbn_10(str_0)
    bool_6 = module_0.is_integer(str_0)
    bool_7 = module_0.is_ip_v6(bool_3)
    bool_8 = module_0.is_email(bool_3)
    bool_9 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = 'p9xD^klVY\n'
    bool_10 = module_0.is_decimal(str_0)
    bool_11 = module_0.is_isbn(str_1)
    bool_12 = i_s_b_n_checker_0.is_isbn_10()
    str_2 = '5&,KD_R^C'
    str_3 = '^([a-z\\d]+'
    str_4 = '<'
    bool_13 = module_0.is_snake_case(bool_5, str_4)
    bool_14 = module_0.is_decimal(str_3)
    bool_15 = module_0.is_ip_v4(str_2)
    bool_16 = module_0.is_uuid(bool_1, bool_1)
    bool_17 = module_0.is_ip(bool_14)
    str_5 = 'Sd<@FcHKi\\GL4'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_5)
    bool_18 = module_0.is_email(i_s_b_n_checker_1)
    bool_19 = module_0.is_isogram(bool_0)
    bool_20 = i_s_b_n_checker_1.is_isbn_13()
    bool_21 = module_0.is_credit_card(str_1)
    bool_22 = module_0.contains_html(str_1)
    bool_23 = module_0.is_uuid(bool_11)
    bool_24 = module_0.is_palindrome(str_3, bool_8)
    bool_25 = module_0.is_ip_v6(bool_3)

def test_case_42():
    str_0 = '1506715214'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '9780312498580'
    bool_1 = module_0.is_json(str_0)
    str_2 = '[1,2,3]'
    bool_2 = module_0.is_json(str_1)
    bool_3 = module_0.is_json(str_1)
    bool_4 = module_0.is_json(str_2)

def test_case_43():
    str_0 = '4111-1111-1111-1111'
    bool_0 = module_0.is_credit_card(str_0)
    str_1 = '4111 1111 1111 1111'
    bool_1 = module_0.is_credit_card(str_1)
    str_2 = '4111111111111111'
    bool_2 = module_0.is_credit_card(str_2)
    str_3 = '5105-1051-0510-5100'
    bool_3 = module_0.is_credit_card(str_3)
    bool_4 = module_0.is_ip_v4(bool_1)
    bool_5 = module_0.is_ip_v4(bool_1)
    bool_6 = module_0.is_ip_v4(str_2)

def test_case_44():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = 'nope'
    bool_1 = module_0.is_ip_v4(str_1)
    str_2 = '255.200.100.999'
    bool_2 = module_0.is_ip_v4(str_2)

def test_case_45():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'disposable.style.email.with+symbol@example.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'other.email-with-dash@example.com'
    bool_2 = module_0.is_email(bool_1)
    str_3 = '"much.more unusual"@example.com'
    bool_3 = module_0.is_email(str_2)
    bool_4 = module_0.is_email(str_3)

def test_case_46():
    str_0 = ''
    bool_0 = module_0.is_email(str_0)
    str_1 = 'hello@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'abcdefghijklmnopqrstuvwxyz23456789abcdefghijklmnopqrstuvwxyz2@gmail.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'hello@gmail.com.cn'
    bool_3 = module_0.is_email(str_3)
    str_4 = '.hello@gmail.com'
    bool_4 = module_0.is_email(str_4)
    bool_5 = module_0.is_json(str_4)
    bool_6 = module_0.is_json(bool_2)

def test_case_47():
    str_0 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_0 = module_0.is_ip(str_0)

def test_case_48():
    str_0 = 'http://www.google.com'
    bool_0 = module_0.is_url(str_0)
    str_1 = 'https://www.google.com'
    bool_1 = module_0.is_url(str_1)
    str_2 = 'http://www.google.com/some/path'
    bool_2 = module_0.is_url(str_2)
    str_3 = 'https'
    str_4 = 'http'
    str_5 = [str_3, str_4]
    bool_3 = module_0.is_url(str_2, str_5)
    str_6 = 'http://user:password@www.google.com'
    bool_4 = module_0.is_url(str_6)
    str_7 = [str_3, str_4]
    bool_5 = module_0.is_url(str_6, str_7)

def test_case_49():
    str_0 = 'my.name@example.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'name@example.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = '@example.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'my.name@example.'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'my.name@exam ple.com'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'my.name@.com'
    bool_5 = module_0.is_email(str_5)
    str_6 = 'my.name@example..com'
    bool_6 = module_0.is_email(str_6)
    str_7 = '"my name@example.com"'
    bool_7 = module_0.is_email(str_7)
    str_8 = '"my name@example'
    bool_8 = module_0.is_email(str_8)
    str_9 = 'my name@example.com"'
    bool_9 = module_0.is_email(str_9)
    bool_10 = module_0.is_email(bool_5)

def test_case_50():
    str_0 = '4111111111111111'
    str_1 = 'VISA'
    bool_0 = module_0.is_credit_card(str_0, str_1)
    str_2 = 'MASTERCARD'
    bool_1 = module_0.is_credit_card(str_0, str_2)
    str_3 = 'AMERICAN_EXPRESS'
    bool_2 = module_0.is_credit_card(str_0, str_3)
    str_4 = 'DINERS_CLUB'
    bool_3 = module_0.is_credit_card(str_0, str_4)
    str_5 = 'DISCOVER'
    bool_4 = module_0.is_credit_card(str_0, str_5)
    bool_5 = module_0.is_ip_v4(bool_4)