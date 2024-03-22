# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    int_0 = -1329
    bool_0 = module_0.is_string(int_0)

def test_case_1():
    str_0 = '|'
    bool_0 = module_0.is_isbn(str_0)

def test_case_2():
    str_0 = '9780312498580'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '1506715214'
    bool_1 = module_0.is_isbn(str_1)

def test_case_3():
    str_0 = 'n+t$olUCh\ntJE'
    bool_0 = True
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_13()
    bool_2 = i_s_b_n_checker_0.is_isbn_10()

def test_case_4():
    str_0 = '0-306-40615-2'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = '161729134X'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_1 = i_s_b_n_checker_1.is_isbn_10()

def test_case_5():
    float_0 = None
    bool_0 = module_0.is_ip(float_0)

def test_case_6():
    str_0 = "6{@r}r'$p\x0bfAQz/+!"
    bool_0 = module_0.is_integer(str_0)

def test_case_7():
    float_0 = 1420.861304
    bool_0 = module_0.is_ip_v6(float_0)
    bool_1 = module_0.is_slug(float_0)
    str_0 = 'fI7Y3"8Q#II%'
    bool_2 = module_0.is_decimal(str_0)
    str_1 = 'QCF6dtfA.'
    str_2 = 'T$>U^'
    int_0 = module_0.words_count(str_2)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_3 = module_0.is_url(str_1)
    dict_0 = {i_s_b_n_checker_0: str_1, str_1: str_1, i_s_b_n_checker_0: str_1}
    bool_4 = module_0.is_json(dict_0)
    int_1 = module_0.words_count(str_0)
    bool_5 = i_s_b_n_checker_0.is_isbn_13()

def test_case_8():
    str_0 = 'https://www.google.com'
    bool_0 = module_0.is_url(str_0)

def test_case_9():
    set_0 = set()
    bool_0 = module_0.is_url(set_0)
    bool_1 = module_0.is_ip_v4(set_0)
    bytes_0 = b'0\x1a\x1aE\xdf\x9cs|a\xe8e\x10;\xd6\xf4\x9b\x05'
    tuple_0 = (bytes_0,)
    bool_2 = module_0.is_camel_case(set_0)
    bool_3 = module_0.is_credit_card(tuple_0)

def test_case_10():
    str_0 = 'john@gmail.com'
    bool_0 = module_0.is_email(str_0)

def test_case_11():
    str_0 = '978-3-16-148410-0'
    bool_0 = module_0.is_email(str_0)

def test_case_12():
    str_0 = 'l.~b|9'
    bool_0 = module_0.is_ip(str_0)
    bool_1 = module_0.is_email(bool_0)
    bool_2 = module_0.is_palindrome(bool_0)
    str_1 = 'l'
    int_0 = module_0.words_count(str_1)

def test_case_13():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip(str_0)
    str_1 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_1 = module_0.is_ip(str_1)
    bool_2 = module_0.is_credit_card(str_1)
    str_2 = 'MASTERCARD'
    bool_3 = module_0.is_credit_card(str_2)

def test_case_14():
    dict_0 = {}
    bool_0 = module_0.is_uuid(dict_0)
    float_0 = -576.363
    bool_1 = module_0.is_snake_case(float_0)
    none_type_0 = None
    bool_2 = module_0.is_credit_card(float_0, none_type_0)
    bool_3 = module_0.is_slug(dict_0)

def test_case_15():
    str_0 = 'E^Zmz4!&01des'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_snake_case(bool_0)

def test_case_16():
    str_0 = ')'
    bool_0 = module_0.is_slug(str_0)
    bool_1 = module_0.is_pangram(str_0)
    bool_2 = module_0.is_snake_case(str_0)
    bool_3 = module_0.is_uuid(bool_2)
    bool_4 = module_0.is_decimal(str_0)
    bool_5 = module_0.is_slug(bool_4, str_0)
    bool_6 = module_0.is_ip_v4(str_0)
    str_1 = 'DK"L*'
    bool_7 = module_0.is_integer(str_1)
    str_2 = ')MW*V+J`:%\x0cFE'
    bool_8 = module_0.is_slug(bool_5)
    bool_9 = module_0.is_isbn(str_2)
    bool_10 = module_0.is_pangram(bool_7)
    bool_11 = module_0.is_palindrome(bool_2)

def test_case_17():
    str_0 = '["foo", "bar", "kaz"]'
    bool_0 = module_0.is_json(str_0)

def test_case_18():
    str_0 = '["foo", "bar" "a"]'
    bool_0 = module_0.is_json(str_0)

def test_case_19():
    str_0 = 'john.doe.jr@gmail.com'
    bool_0 = module_0.is_uuid(str_0)
    bool_1 = module_0.is_email(str_0)

def test_case_20():
    str_0 = 'aQ^\tMw7vV xxC)^Rs^'
    bool_0 = module_0.is_json(str_0)
    bool_1 = module_0.is_email(str_0)
    str_1 = 'Qfo<dB(RS((sXq'
    bool_2 = True
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_2)
    bool_3 = module_0.is_ip(str_0)
    bool_4 = module_0.is_full_string(str_0)
    str_2 = 'w\\A 0>ghHF'
    bool_5 = module_0.is_credit_card(str_2)
    int_0 = module_0.words_count(str_2)
    bool_6 = module_0.is_slug(str_2)
    bool_7 = True
    bool_8 = module_0.is_uuid(bool_2, bool_7)
    bool_9 = module_0.is_isbn(str_1)
    str_3 = 'mN0?2m~Q{mF\x0b\x0b'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_3)
    bool_10 = i_s_b_n_checker_1.is_isbn_10()
    bool_11 = module_0.is_json(bool_5)
    list_0 = [bool_7]
    bool_12 = module_0.is_credit_card(list_0)
    bool_13 = module_0.is_email(bool_7)
    bool_14 = i_s_b_n_checker_1.is_isbn_13()
    bool_15 = module_0.is_ip_v6(bool_11)
    bool_16 = module_0.is_json(bool_14)
    bool_17 = module_0.is_url(str_2)

def test_case_21():
    str_0 = '5j\tX\\7\t+FJ@gyL\x0cd.rvp'
    bool_0 = module_0.is_integer(str_0)
    str_1 = 'y1EKbIcU]>ZSCz!0+'
    bool_1 = module_0.is_palindrome(str_1)
    str_2 = 'Ju&*l+_\ndhCcc:T;qc'
    bool_2 = module_0.is_number(str_2)
    bool_3 = module_0.is_url(str_1)
    bool_4 = module_0.is_slug(str_2)

def test_case_22():
    int_0 = None
    bool_0 = module_0.is_palindrome(int_0)

def test_case_23():
    str_0 = "'Zm*<39"
    bool_0 = module_0.is_camel_case(str_0)
    str_1 = '((?<=[^\\s\\d]),(?=[^\\s\\d])|\\s,\\s|\\s,(?=[^\\s\\d])|\\s,(?!.)|(?<=[^\\s\\d.])\\.+(?=[^\\s\\d.])|\\s\\.+\\s|\\s\\.+(?=[^\\s\\d])|\\s\\.+(?!\\.)|(?<=\\S);(?=\\S)|\\s;\\s|\\s;(?=\\S)|\\s;(?!.)|(?<=\\S):(?=\\S)|\\s:\\s|\\s:(?=\\S)|\\s:(?!.)|(?<=[^\\s!])!+(?=[^\\s!])|\\s!+\\s|\\s!+(?=[^\\s!])|\\s!+(?!!)|(?<=[^\\s?])\\?+(?=[^\\s?])|\\s\\?+\\s|\\s\\?+(?=[^\\s?])|\\s\\?+(?!\\?)|\\d%(?=\\S)|(?<=\\d)\\s%\\s|(?<=\\d)\\s%(?=\\S)|(?<=\\d)\\s%(?!.))'
    str_2 = 'cBAtvvM>>~w7AE@'
    bool_1 = module_0.is_slug(str_2)
    bool_2 = True
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_2)
    bool_3 = True
    bool_4 = module_0.is_palindrome(str_1, bool_3)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_5 = i_s_b_n_checker_1.is_isbn_10()

def test_case_24():
    str_0 = '(63,`H+?24'
    bool_0 = True
    bool_1 = module_0.is_pangram(str_0)
    bool_2 = module_0.is_isbn(str_0, bool_0)
    str_1 = '\\W0xe\x0bP5'
    bool_3 = module_0.is_integer(str_0)
    bool_4 = module_0.is_ip(str_1)
    str_2 = '[VOUZX\rOg'
    bool_5 = module_0.is_number(str_2)

def test_case_25():
    str_0 = 'r-pLk#;nG,\\W1dd '
    bool_0 = module_0.contains_html(str_0)
    str_1 = '(63,`H+?24'
    bool_1 = module_0.is_pangram(bool_0)
    bool_2 = True
    bool_3 = module_0.is_pangram(str_0)
    bool_4 = module_0.is_slug(bool_0, str_0)
    bool_5 = module_0.is_isbn(str_1, bool_2)
    bool_6 = module_0.is_uuid(bool_0)
    str_2 = '\\W0xe\x0bP5'
    bool_7 = module_0.is_integer(str_1)
    bool_8 = module_0.is_ip(str_2)
    str_3 = '[VOUZX\rOg'
    bool_9 = module_0.is_number(str_3)

def test_case_26():
    str_0 = 'SJ7Q&}\x0cpoP,|Nn`fG'
    bool_0 = module_0.is_json(str_0)
    bool_1 = module_0.is_isbn_10(str_0)
    bool_2 = module_0.is_credit_card(str_0)
    bool_3 = module_0.is_email(str_0)
    str_1 = '(B!>Q/;D3Pi'
    bool_4 = module_0.is_json(bool_1)
    str_2 = 'g'
    list_0 = [str_2, str_1, str_0, str_0]
    bool_5 = module_0.is_url(str_1, list_0)
    bool_6 = module_0.is_isogram(bool_5)

def test_case_27():
    str_0 = '978-1-63345-649-7'
    str_1 = "7)#|\t'a'/mgp7gK3P=\\J"
    bool_0 = module_0.is_slug(str_0, str_1)
    bool_1 = module_0.is_isbn(str_0)
    str_2 = '1506715214'
    bool_2 = module_0.is_isbn(str_2)

def test_case_28():
    str_0 = 'R\n;( 8<OR(}~eS'
    bool_0 = module_0.contains_html(str_0)

def test_case_29():
    float_0 = None
    bool_0 = module_0.is_ip(float_0)
    str_0 = 'qVpF\\H-R'
    int_0 = module_0.words_count(str_0)

def test_case_30():
    str_0 = '5"NjVhbxM&FP.~;1,)41'
    bool_0 = module_0.is_ip_v6(str_0)
    bool_1 = False
    bool_2 = module_0.is_isbn_10(str_0, bool_1)

def test_case_31():
    str_0 = '~eGXx'
    bool_0 = module_0.is_pangram(str_0)
    str_1 = 'ed\x0cL0zuxYF\rn!'
    bool_1 = module_0.is_isbn_13(str_0)
    str_2 = '0V^qU74k!aydCV'
    bool_2 = module_0.is_camel_case(str_2)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
    str_3 = 'L8DYwr\t4@(*w,0N'
    bool_3 = module_0.is_uuid(str_3)
    bool_4 = module_0.is_credit_card(str_1)
    bool_5 = module_0.is_isbn_13(str_1)

def test_case_32():
    str_0 = 'john@gmail.com'
    bool_0 = module_0.is_ip_v4(str_0)

def test_case_33():
    str_0 = '|'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = module_0.is_palindrome(i_s_b_n_checker_0)
    bool_1 = module_0.is_json(str_0)

def test_case_34():
    str_0 = 'g'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = module_0.is_json(i_s_b_n_checker_0)

def test_case_35():
    str_0 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_0 = module_0.is_ip(str_0)

def test_case_36():
    str_0 = 'AMERICAN_EXPRESS'
    bool_0 = module_0.is_integer(str_0)
    bytes_0 = b'\xfe\xffW<`\xd2\x1f\x9b7\x11k\xf4\x98\xa1\xc9'
    bool_1 = module_0.is_email(bytes_0)
    str_1 = '\n    Converts a string into a "slug" using provided separator.\n    The returned string has the following properties:\n\n    - it has no spaces\n    - all letters are in lower case\n    - all punctuation signs and non alphanumeric chars are removed\n    - words are divided using provided separator\n    - all chars are encoded as ascii (by using `asciify()`)\n    - is safe for URL\n\n    *Examples:*\n\n    >>> slugify(\'Top 10 Reasons To Love Dogs!!!\') # returns: \'top-10-reasons-to-love-dogs\'\n    >>> slugify(\'Mönstér Mägnët\') # returns \'monster-magnet\'\n\n    :param input_string: String to convert.\n    :type input_string: str\n    :param separator: Sign used to join string tokens (default to "-").\n    :type separator: str\n    :return: Slug string\n    '
    bool_2 = module_0.is_ip(bytes_0)
    bool_3 = module_0.is_credit_card(bool_1)
    list_0 = None
    bool_4 = module_0.is_url(str_1, list_0)
    bool_5 = module_0.is_snake_case(bytes_0)
    str_2 = 'roman_decode'
    bool_6 = module_0.is_isbn(str_2)
    bool_7 = module_0.is_camel_case(bool_5)
    bool_8 = module_0.is_number(str_0)
    str_3 = 'A^G*vxxuf}UC\rXz0I'
    bool_9 = module_0.is_isbn_13(str_3)
    bool_10 = module_0.is_isogram(str_3)
    bool_11 = module_0.is_decimal(str_3)
    int_0 = module_0.words_count(str_3)
    bool_12 = module_0.is_pangram(bool_5)
    bool_13 = module_0.is_ip(bool_3)

def test_case_37():
    str_0 = '978-3-16-148410-0'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    str_1 = '"test@test.com"@test.com'
    bool_1 = module_0.is_email(str_1)
    bool_2 = module_0.is_email(str_0)
    str_2 = '"aaaa"@test.com'
    bool_3 = module_0.is_email(bool_1)
    bool_4 = module_0.is_email(bool_1)
    bool_5 = module_0.is_email(str_2)

def test_case_38():
    str_0 = '1'
    bool_0 = module_0.is_decimal(str_0)
    int_0 = 744
    str_1 = ';neSaV  Y@j7r%x_cK'
    bool_1 = module_0.is_slug(int_0, str_1)
    bool_2 = module_0.is_json(str_0)
    str_2 = '"asd"'
    bool_3 = module_0.is_json(str_2)
    str_3 = '{}'
    bool_4 = module_0.is_json(str_3)
    bool_5 = module_0.is_email(str_2)
    bool_6 = module_0.is_email(str_0)
    bool_7 = module_0.is_ip(str_3)
    bool_8 = module_0.is_ip_v4(bool_5)
    bool_9 = module_0.is_email(str_0)
    str_4 = ''
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_4)
    bool_10 = i_s_b_n_checker_0.is_isbn_13()
    bool_11 = module_0.is_json(i_s_b_n_checker_0)
    bool_12 = module_0.is_url(bool_11)

def test_case_39():
    str_0 = '1'
    bool_0 = module_0.is_json(str_0)
    str_1 = '"asd"'
    bool_1 = module_0.is_json(str_1)
    str_2 = 'john@gmail.'
    bool_2 = module_0.is_email(bool_0)
    str_3 = '@gmail.com'
    bool_3 = module_0.is_email(bool_2)
    str_4 = 'john@.com'
    bool_4 = module_0.is_palindrome(str_2)
    str_5 = 'a'
    bool_5 = module_0.is_email(str_3)
    bool_6 = module_0.is_credit_card(str_4)
    bool_7 = module_0.is_email(bool_2)
    str_6 = 'john234.doe@gmail.cm'
    bool_8 = module_0.is_email(str_6)
    bool_9 = module_0.is_palindrome(str_1, bool_8)
    bool_10 = module_0.is_ip(bool_1)
    bool_11 = module_0.is_email(str_5)
    bool_12 = module_0.is_ip_v4(str_0)
    bool_13 = module_0.is_email(str_5)

def test_case_40():
    float_0 = 672.151201
    str_0 = '..'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.contains_html(str_0)
    str_1 = '@|"]1]HF'
    bool_2 = module_0.is_integer(str_1)
    bool_3 = module_0.is_isogram(str_1)
    bool_4 = module_0.is_full_string(bool_2)
    bool_5 = False
    bool_6 = module_0.is_ip_v4(bool_5)
    bytes_0 = b'D}\x8c\xac\x85\xc7\x81<\xb0\xfdX\xd7\xc8:p'
    str_2 = '"$?:$TY^Sn'
    bool_7 = module_0.is_isbn(str_2)
    bool_8 = module_0.is_full_string(bytes_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_5)
    bool_9 = module_0.is_decimal(str_1)
    bool_10 = i_s_b_n_checker_0.is_isbn_10()
    bool_11 = module_0.is_email(float_0)
    bool_12 = module_0.is_json(str_2)

def test_case_41():
    str_0 = 'xzIJR`Zz2qOK=6]TH'
    bool_0 = True
    bool_1 = True
    bool_2 = module_0.is_isbn_10(str_0)
    bool_3 = module_0.is_palindrome(str_0, bool_0, bool_1)
    bool_4 = module_0.is_decimal(str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_5 = i_s_b_n_checker_0.is_isbn_10()
    bool_6 = i_s_b_n_checker_0.is_isbn_10()
    bool_7 = True
    bool_8 = module_0.contains_html(str_0)
    bool_9 = i_s_b_n_checker_0.is_isbn_10()
    bytes_0 = b'\x9bLF\x15L\xec\xbe'
    str_1 = 'K'
    bool_10 = module_0.is_slug(bytes_0, str_1)
    bool_11 = module_0.is_palindrome(bool_7)
    int_0 = 829
    bool_12 = module_0.is_uuid(bool_4)
    list_0 = None
    str_2 = ' V['
    bool_13 = module_0.is_number(str_2)
    set_0 = {int_0, list_0, list_0}
    bool_14 = module_0.is_snake_case(bool_12)
    str_3 = 'ow-vjm+\nW 5'
    bool_15 = module_0.is_uuid(str_3)
    bool_16 = module_0.is_slug(set_0, str_3)
    str_4 = 'I3" {VMRkO5!'
    bool_17 = i_s_b_n_checker_0.is_isbn_10()
    bool_18 = module_0.is_url(bool_6, str_4)
    str_5 = '{W.\x0b&J:`u89Z['
    bool_19 = module_0.is_uuid(str_5)
    bool_20 = module_0.is_camel_case(int_0)
    str_6 = ''
    bool_21 = module_0.is_number(str_6)
    bool_22 = module_0.contains_html(str_5)

def test_case_42():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)

def test_case_43():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = 'nope'
    bool_1 = module_0.is_ip_v4(str_1)
    str_2 = '255.200.100.999'
    bool_2 = module_0.is_ip_v4(str_2)

def test_case_44():
    str_0 = '1.1'
    bool_0 = module_0.is_integer(str_0)
    str_1 = '-1.1'
    bool_1 = module_0.is_integer(str_1)
    str_2 = '1e3'
    bool_2 = module_0.is_integer(str_2)

def test_case_45():
    str_0 = '1'
    bool_0 = module_0.is_json(str_0)
    str_1 = '"asd"'
    bool_1 = module_0.is_json(str_1)
    str_2 = "{'}"
    bool_2 = module_0.is_json(str_2)
    bool_3 = module_0.is_email(str_1)
    bool_4 = module_0.is_email(bool_2)
    bool_5 = module_0.is_email(bool_1)
    str_3 = 'Q'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_3)
    bool_6 = module_0.is_ip_v6(bool_2)
    bool_7 = i_s_b_n_checker_0.is_isbn_13()
    bool_8 = module_0.is_ip(str_0)
    str_4 = '\n    Convert a snake case string into a camel case one.\n    (The original string is returned if is not a valid snake case string)\n\n    *Example:*\n\n    >>> snake_case_to_camel(\'the_snake_is_green\') # returns \'TheSnakeIsGreen\'\n\n    :param input_string: String to convert.\n    :type input_string: str\n    :param upper_case_first: True to turn the first letter into uppercase (default).\n    :type upper_case_first: bool\n    :param separator: Sign to use as separator (default to "_").\n    :type separator: str\n    :return: Converted string\n    '
    bool_9 = module_0.is_isbn_10(str_3)
    bool_10 = module_0.is_email(str_4)

def test_case_46():
    str_0 = 'VISA'
    bool_0 = module_0.is_credit_card(str_0)
    str_1 = '4532 2428 9905 3534'
    bool_1 = module_0.is_credit_card(str_1)
    bool_2 = module_0.is_credit_card(bool_1)
    bool_3 = module_0.is_credit_card(bool_1, str_1)
    tuple_0 = ()
    bool_4 = module_0.is_credit_card(tuple_0, str_0)
    str_2 = '4024007188084288'
    bool_5 = module_0.is_credit_card(bool_0)
    bool_6 = module_0.is_credit_card(str_2)
    bool_7 = module_0.is_credit_card(bool_6)

def test_case_47():
    str_0 = 'http://www.mysite.com'
    bool_0 = module_0.is_url(str_0)
    str_1 = 'https://mysite.com'
    str_2 = '.mysite.com'
    bool_1 = module_0.is_url(str_2)
    str_3 = 'http'
    str_4 = 'https'
    bool_2 = module_0.is_url(str_0, str_1)
    str_5 = 'ftp://www.mysite.com'
    str_6 = [str_3, str_4]
    bool_3 = module_0.is_url(str_5, str_6)
    bool_4 = module_0.is_email(str_5)

def test_case_48():
    str_0 = '55.200.100.75'
    str_1 = '2ehkP|SFH8'
    bool_0 = False
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    bool_2 = module_0.contains_html(str_0)
    bool_3 = module_0.is_ip_v4(str_0)
    str_2 = 'v+ph'
    bool_4 = module_0.is_camel_case(str_0)
    bool_5 = module_0.is_json(str_2)
    str_3 = '~,a-XK$05My=\x0cq'
    bool_6 = i_s_b_n_checker_0.is_isbn_13()
    bool_7 = module_0.is_isbn(str_3)
    bool_8 = module_0.is_email(bool_2)
    str_4 = '"a.aM@test.c#m'
    bool_9 = i_s_b_n_checker_0.is_isbn_10()
    bool_10 = module_0.is_email(bool_8)
    str_5 = '"aaaa"@test.com'
    bool_11 = module_0.is_email(str_4)
    str_6 = 'h'
    int_0 = module_0.words_count(str_6)
    bool_12 = module_0.is_email(str_5)
    bool_13 = module_0.is_email(str_6)

def test_case_49():
    str_0 = '978-3-16-148410-0'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = '978-3-16-148410-1'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_2 = i_s_b_n_checker_1.is_isbn_13()
    bool_3 = module_0.is_email(str_0)
    bool_4 = module_0.is_email(bool_1)
    bool_5 = module_0.is_email(i_s_b_n_checker_1)
    str_2 = 'john..doe@example.com'
    bool_6 = module_0.is_email(str_2)
    str_3 = 'john.doe@example..com'
    bool_7 = module_0.is_email(bool_2)
    bool_8 = module_0.is_email(str_3)