# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    bytes_0 = b'\xd85\xac\x03\xab\xca\xd9UK\xe5z \xfd\x19z\xc8'
    bool_0 = module_0.is_credit_card(bytes_0)

def test_case_1():
    str_0 = 'Z'
    bool_0 = module_0.is_isbn(str_0)

def test_case_2():
    str_0 = 'r`\x0br[xj~YRypl'
    bool_0 = False
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_13()
    float_0 = -456.634247
    bool_2 = module_0.is_isogram(float_0)

def test_case_3():
    str_0 = '^xgfZC0q^/'
    bool_0 = module_0.is_snake_case(str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_1 = module_0.is_palindrome(i_s_b_n_checker_0)
    bool_2 = i_s_b_n_checker_0.is_isbn_10()

def test_case_4():
    str_0 = '\\u/'
    bool_0 = module_0.is_integer(str_0)

def test_case_5():
    str_0 = 'A'
    bool_0 = module_0.is_uuid(str_0)
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_email(str_0)
    bool_3 = module_0.is_snake_case(bool_1)
    bool_4 = module_0.is_decimal(str_0)

def test_case_6():
    str_0 = "4o'6J6"
    set_0 = {str_0, str_0, str_0, str_0}
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    bool_1 = module_0.is_url(str_0, set_0)
    bool_2 = module_0.is_isbn_13(str_0, bool_1)

def test_case_7():
    str_0 = 'A\x0b15%6dVzz"5|5 }HRJ'
    list_0 = []
    str_1 = '`'
    bool_0 = module_0.is_isbn_10(str_1)
    bool_1 = module_0.is_isbn(str_0, bool_0)
    bool_2 = module_0.is_json(str_0)
    bool_3 = module_0.is_url(str_0, list_0)
    bool_4 = module_0.is_number(str_0)
    bool_5 = module_0.is_snake_case(str_0)

def test_case_8():
    str_0 = 'V\x0ckQc|h,#cv'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    str_1 = 'Y\rUj&U_4\ru-d'
    list_0 = [str_1]
    bool_0 = module_0.is_url(i_s_b_n_checker_0, list_0)

def test_case_9():
    str_0 = '\n    Restore a previously compressed string (obtained using `compress()`) back to its original state.\n\n    :param input_string: String to restore.\n    :type input_string: str\n    :param encoding: Original string encoding.\n    :type encoding: str\n    :return: Decompressed string.\n    '
    bool_0 = module_0.is_email(str_0)

def test_case_10():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '.gmail.com'
    bool_1 = module_0.is_email(str_1)

def test_case_11():
    bool_0 = False
    str_0 = '&djicih/{#_pH>n"Ke'
    bool_1 = module_0.is_ip_v6(bool_0)
    bool_2 = module_0.is_decimal(str_0)
    bool_3 = module_0.is_isogram(bool_0)
    bool_4 = module_0.is_camel_case(bool_0)

def test_case_12():
    str_0 = 'ioO@c?^g1pg@'
    str_1 = 'Invalid encoding'
    bool_0 = module_0.is_snake_case(str_0, str_1)
    bool_1 = module_0.is_isogram(str_0)
    bool_2 = module_0.is_isbn(str_0)

def test_case_13():
    str_0 = '[1, 2, 3]'
    bool_0 = module_0.is_json(str_0)

def test_case_14():
    str_0 = 'e\x0b8+g0[\t\x0cH]p'
    bool_0 = module_0.is_json(str_0)

def test_case_15():
    list_0 = None
    str_0 = None
    bool_0 = module_0.is_uuid(str_0)
    bool_1 = module_0.is_slug(list_0, str_0)
    bool_2 = module_0.is_isogram(list_0)

def test_case_16():
    bytes_0 = b'\x8d\xdd\xd1\x9a\x84\x83\xabaq\x98\xb8\xa5\xbc\xfa\xfe\xba\xe6\xc5C'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = module_0.is_snake_case(list_0)
    str_0 = '({})'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_1 = module_0.is_email(i_s_b_n_checker_0)
    list_1 = [i_s_b_n_checker_0]
    bool_2 = True
    bool_3 = module_0.is_uuid(list_1, bool_2)
    bool_4 = module_0.is_credit_card(list_1)

def test_case_17():
    int_0 = -818
    bool_0 = module_0.is_ip(int_0)

def test_case_18():
    str_0 = 'Ai6Xh$MQ'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = module_0.is_uuid(i_s_b_n_checker_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    float_0 = -644.802
    bool_2 = module_0.is_credit_card(float_0)
    str_1 = '\x0cMXpmE]9'
    bool_3 = module_0.is_palindrome(str_1)

def test_case_19():
    str_0 = 'user@domain.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'user@domain.info'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'user.lastname@domain.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'user.lastname+tag@domain.com.au'
    bool_3 = module_0.is_email(str_3)
    bool_4 = module_0.is_ip_v4(bool_1)
    str_4 = '0.0.0.256'
    bool_5 = module_0.is_ip_v4(str_2)
    str_5 = '6^|1PY'
    bool_6 = module_0.is_pangram(str_4)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_5)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2, bool_5)
    bool_7 = i_s_b_n_checker_0.is_isbn_13()
    bool_8 = i_s_b_n_checker_0.is_isbn_13()
    bool_9 = module_0.is_credit_card(bool_5)
    str_6 = '@`1@xqU6@hVsACA'
    int_0 = module_0.words_count(str_6)
    bool_10 = module_0.is_credit_card(bool_4)
    bool_11 = i_s_b_n_checker_0.is_isbn_10()

def test_case_20():
    str_0 = '255.200.100.75'
    bytes_0 = b'\x99'
    bool_0 = module_0.is_ip_v4(bytes_0)
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_ip_v4(str_0)
    bool_3 = module_0.is_pangram(bool_1)
    bool_4 = module_0.is_isbn(str_0)

def test_case_21():
    set_0 = set()
    bool_0 = module_0.is_isogram(set_0)

def test_case_22():
    int_0 = 4314
    str_0 = 'b1uNXbA\t"5p\''
    bool_0 = module_0.is_isbn_13(str_0)
    str_1 = ''
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    bool_2 = module_0.is_json(int_0)
    bool_3 = module_0.is_slug(int_0)
    bool_4 = module_0.is_decimal(str_1)
    bool_5 = i_s_b_n_checker_0.is_isbn_13()
    int_1 = module_0.words_count(str_1)
    bool_6 = module_0.is_email(int_0)
    bool_7 = i_s_b_n_checker_0.is_isbn_13()
    bool_8 = module_0.contains_html(str_1)

def test_case_23():
    str_0 = '\n    Restore a previously compressed string (obtained using `compress()`) back to its original state.\n\n    :param input_string: String to restore.\n    :type input_string: str\n    :param encoding: Original string encoding.\n    :type encoding: str\n    :return: Decompressed string.\n    '
    int_0 = module_0.words_count(str_0)

def test_case_24():
    str_0 = '9=v;>MD1V7mcW'
    bool_0 = module_0.is_isbn_10(str_0)

def test_case_25():
    str_0 = 'q\rrJK=SR'
    bool_0 = False
    bool_1 = module_0.is_isbn_10(str_0, bool_0)

def test_case_26():
    str_0 = 'Invalid encoding'
    bool_0 = module_0.is_isogram(str_0)

def test_case_27():
    str_0 = 'hq}lr\n*O'
    bool_0 = module_0.is_isogram(str_0)
    bool_1 = module_0.is_ip_v4(str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_2 = True
    bool_3 = module_0.is_email(bool_2)
    bool_4 = module_0.is_isogram(str_0)
    bool_5 = module_0.is_pangram(bool_2)

def test_case_28():
    float_0 = -1247.383854
    bool_0 = module_0.is_ip_v4(float_0)
    int_0 = -1594
    bool_1 = module_0.is_ip_v6(int_0)
    bool_2 = module_0.is_pangram(int_0)
    bool_3 = module_0.is_ip(int_0)
    set_0 = {int_0, float_0, int_0, int_0}
    bool_4 = module_0.is_palindrome(set_0)
    str_0 = 'strip_html'
    bool_5 = module_0.is_camel_case(str_0)
    float_1 = 4601.121
    bool_6 = module_0.is_isogram(float_1)
    bool_7 = module_0.is_slug(bool_0)
    str_1 = 'ZcI'
    bool_8 = module_0.is_ip(float_1)
    bool_9 = module_0.is_snake_case(float_1, str_1)

def test_case_29():
    str_0 = 'my.ema.il@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_json(str_0)
    bool_2 = module_0.is_json(bool_0)

def test_case_30():
    str_0 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_0 = module_0.is_ip(str_0)
    bool_1 = module_0.is_ip_v4(str_0)

def test_case_31():
    str_0 = '#<R7l1-Rp\\x'
    str_1 = '9f6\\|T=E'
    bool_0 = False
    bool_1 = module_0.is_isbn(str_1, bool_0)
    bool_2 = module_0.is_decimal(str_0)
    bool_3 = True
    dict_0 = {str_0: bool_3, str_0: bool_3}
    bool_4 = module_0.is_url(str_1, dict_0)
    bool_5 = module_0.is_ip(bool_3)
    bool_6 = module_0.is_palindrome(str_0, bool_3)
    bool_7 = module_0.is_ip(bool_5)
    bool_8 = module_0.is_json(bool_6)
    bool_9 = module_0.is_json(str_0)

def test_case_32():
    str_0 = '9780312498580'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '1506715214'
    bool_1 = module_0.is_credit_card(str_1)
    str_2 = '4929847580391231'
    bool_2 = module_0.is_credit_card(str_1)
    bool_3 = module_0.is_credit_card(str_2)
    bool_4 = module_0.is_credit_card(bool_0)

def test_case_33():
    str_0 = "\n    Checks if the string is an isogram (https://en.wikipedia.org/wiki/Isogram).\n\n    *Examples:*\n\n    >>> is_isogram('dermatoglyphics') # returns true\n    >>> is_isogram('hello') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if isogram, false otherwise.\n    "
    bool_0 = True
    bool_1 = module_0.is_isbn(str_0, bool_0)
    str_1 = '-'
    bool_2 = module_0.is_palindrome(str_1, bool_1)
    str_2 = '\nu*G#@L5>XL$|`HcY'
    bool_3 = module_0.is_ip_v4(bool_0)
    bool_4 = module_0.is_integer(str_2)
    bool_5 = module_0.is_email(str_2)
    bool_6 = module_0.is_credit_card(str_2)
    str_3 = ';(F^'
    bool_7 = module_0.is_number(str_3)
    bool_8 = module_0.is_ip_v6(bool_5)
    str_4 = ')h'
    str_5 = ".@\\\nf0'mcW["
    bool_9 = module_0.is_isbn_13(str_5, bool_7)
    bool_10 = module_0.is_isbn(str_4)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_11 = i_s_b_n_checker_0.is_isbn_13()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_4)
    bool_12 = i_s_b_n_checker_0.is_isbn_13()
    bool_13 = module_0.is_isbn(str_0, bool_5)
    str_6 = '-&=t1uU'
    int_0 = module_0.words_count(str_6)
    tuple_0 = ()
    bool_14 = module_0.is_credit_card(tuple_0, str_4)

def test_case_34():
    int_0 = 20
    var_0 = range(int_0)
    str_0 = '4556134642424246'
    bool_0 = module_0.is_credit_card(str_0)
    str_1 = '4929847580391230'
    bool_1 = module_0.is_credit_card(str_1)
    str_2 = '4929847580391231'
    bool_2 = module_0.is_credit_card(str_2)
    str_3 = 'VISA'
    bool_3 = module_0.is_credit_card(str_1, str_3)
    str_4 = '4444444444444444'
    bool_4 = module_0.is_credit_card(str_4, str_3)

def test_case_35():
    str_0 = '978-0-306-40615-7'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    str_1 = '979-10-90636-00-2'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_1 = i_s_b_n_checker_1.is_isbn_13()

def test_case_36():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)

def test_case_37():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = '"very.unusual.@.unusual.com"@example.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = '"very.(),:;<>[]".VERY."very@\\ "very".unusual"@strange.example.com'
    bool_3 = module_0.is_email(str_3)
    str_4 = '"()<>[]:,;@\\"!#$%&*+-/=?^_`{}| ~.a"@example.org'
    bool_4 = module_0.is_email(str_4)
    str_5 = '" "@example.org'
    bool_5 = module_0.is_email(str_5)
    str_6 = '!def!xyz%abc@example.com'
    bool_6 = module_0.is_email(str_6)
    str_7 = 'example@localhost'
    bool_7 = module_0.is_email(str_7)

def test_case_38():
    str_0 = "&'0b5Os4l$P/+p"
    bool_0 = module_0.is_camel_case(str_0)
    str_1 = '#<R7l1-Rp\\x'
    bool_1 = module_0.is_decimal(str_1)
    bool_2 = True
    bool_3 = module_0.is_ip(bool_2)
    bool_4 = module_0.is_palindrome(str_0, bool_2)
    str_2 = '\nu*G#@L5>XL$|`HcY'
    bool_5 = module_0.is_integer(str_2)
    bool_6 = module_0.is_email(str_0)
    bool_7 = module_0.is_url(str_0)
    bool_8 = module_0.is_credit_card(str_0)
    str_3 = '^([a-z\\d]{0,4}:){7}[az\\d]{0,4}$'
    str_4 = "'BWwF.<;0Z.>)"
    bool_9 = module_0.is_number(str_4)
    bool_10 = module_0.is_ip_v6(bool_3)
    bool_11 = module_0.is_uuid(bool_5, bool_1)
    str_5 = '&#vitKv'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_5, bool_10)
    bool_12 = module_0.is_json(str_3)
    bool_13 = i_s_b_n_checker_0.is_isbn_13()
    bool_14 = i_s_b_n_checker_0.is_isbn_10()
    bool_15 = module_0.is_snake_case(str_0)
    str_6 = '9'
    bool_16 = module_0.is_integer(str_6)
    str_7 = None
    bool_17 = module_0.is_snake_case(bool_14, str_7)
    bool_18 = i_s_b_n_checker_0.is_isbn_13()

def test_case_39():
    str_0 = "&'0b5Os4l$P/+p"
    bool_0 = module_0.is_camel_case(str_0)
    str_1 = '#<R7l1-Rp\\x'
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_json(str_1)
    str_2 = "zg1&s<-X}Nk'3b0A"
    bool_3 = module_0.is_ip(str_0)
    bool_4 = False
    bool_5 = True
    bool_6 = module_0.is_palindrome(str_1, bool_4, bool_5)
    str_3 = ':?t{Rv[i8'
    str_4 = '\nu*G#@L5>XL$|`HcY'
    bool_7 = module_0.is_integer(str_4)
    bytes_0 = b'\xf3\x08\x1a'
    bool_8 = module_0.is_email(bytes_0)
    bool_9 = module_0.is_credit_card(bool_7)
    bool_10 = False
    bool_11 = module_0.is_number(str_0)
    bool_12 = module_0.is_ip_v6(str_3)
    str_5 = 'DUPLICATES'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_4)
    bool_13 = module_0.is_credit_card(bool_2)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_5)
    bool_14 = i_s_b_n_checker_1.is_isbn_10()
    str_6 = '38\rq3Z\x0brTh~'
    bool_15 = module_0.is_isbn_13(str_6)
    bool_16 = module_0.is_string(str_2)
    str_7 = 'U%\n!JR'
    bool_17 = module_0.contains_html(str_7)
    bool_18 = module_0.is_snake_case(str_4)
    bool_19 = module_0.is_credit_card(bool_10)

def test_case_40():
    str_0 = '9780312498580'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '1506715214'
    bool_1 = module_0.is_isbn(str_1)
    bool_2 = module_0.is_ip_v4(bool_0)

def test_case_41():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_isbn(str_0)

def test_case_42():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_ip_v4(str_0)
    str_1 = '255.200.100.999'
    bool_2 = module_0.is_ip_v4(str_1)

def test_case_43():
    str_0 = '1.0'
    bool_0 = module_0.is_decimal(str_0)
    bool_1 = module_0.is_ip(bool_0)
    bool_2 = module_0.is_ip(str_0)

def test_case_44():
    str_0 = '[1, 2, 3]'
    bool_0 = module_0.is_json(str_0)
    str_1 = '{nope}'
    bool_1 = module_0.is_json(str_1)

def test_case_45():
    str_0 = '{"name": "Peter"}'
    bool_0 = module_0.is_json(str_0)
    bool_1 = module_0.is_email(str_0)
    str_1 = 'my.email@the+provider.com'
    str_2 = '\n    Turns a string into a boolean based on its content (CASE INSENSITIVE).\n\n    A positive boolean (True) is returned if the string value is one of the following:\n\n    - "true"\n    - "1"\n    - "yes"\n    - "y"\n\n    Otherwise False is returned.\n\n    *Examples:*\n\n    >>> booleanize(\'true\') # returns True\n    >>> booleanize(\'YES\') # returns True\n    >>> booleanize(\'nope\') # returns False\n\n    :param input_string: String to convert\n    :type input_string: str\n    :return: True if the string contains a boolean-like positive value, false otherwise\n    '
    bool_2 = module_0.is_email(str_2)
    bool_3 = module_0.is_email(str_1)
    bool_4 = module_0.is_email(str_2)
    bool_5 = module_0.is_email(str_0)

def test_case_46():
    str_0 = 'user@example.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'name@localhost'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'm...m@example.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'm.m@example.com'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'name@example.co.uk'
    bool_4 = module_0.is_email(str_4)
    bool_5 = module_0.is_url(bool_2)
    str_5 = 'www.mysite.com'
    bool_6 = module_0.is_url(str_5)

def test_case_47():
    str_0 = 'http://www.mysite.com'
    bool_0 = module_0.is_url(str_0)
    str_1 = 'https://mysite.com'
    bool_1 = module_0.is_url(str_1)
    str_2 = 'w>eRp@H(\\b#Yd\\F*'
    bool_2 = module_0.is_url(str_2)
    bool_3 = module_0.is_url(bool_1)
    str_3 = ';deELjRT-f81#<r/'
    str_4 = "Kmpe2b.D'!N|H"
    list_0 = [str_3, str_4]
    bool_4 = module_0.is_url(str_1, list_0)
    bool_5 = module_0.is_url(bool_3)

def test_case_48():
    str_0 = ''
    bool_0 = module_0.is_email(str_0)
    str_1 = ' '
    bool_1 = module_0.is_email(str_1)
    str_2 = '@gmail.com'
    bool_2 = module_0.is_email(str_2)
    bool_3 = module_0.is_email(str_0)
    str_3 = 'jen.@gmail.com'
    bool_4 = module_0.is_email(str_3)
    str_4 = 'jen..@gmail.com'
    bool_5 = module_0.is_email(str_4)
    str_5 = 'jen.a@gmail.com'
    bool_6 = module_0.is_email(str_5)
    bool_7 = module_0.is_email(str_3)
    bool_8 = module_0.is_email(str_4)
    bool_9 = module_0.is_email(str_5)
    str_6 = 'jen@a.@gmail.com'
    bool_10 = module_0.is_email(str_6)
    str_7 = 'jen@a..@gmail.com'
    bool_11 = module_0.is_email(str_7)

def test_case_49():
    str_0 = '{"name\\: "P8ter"}'
    bool_0 = module_0.is_json(str_0)
    bool_1 = module_0.is_email(str_0)
    str_1 = '(my.email@the-provider.com)'
    bool_2 = module_0.is_json(str_1)
    bool_3 = module_0.is_email(str_1)
    bool_4 = False
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_4)
    bool_5 = i_s_b_n_checker_0.is_isbn_10()
    str_2 = "9MH;)txYT'"
    bool_6 = module_0.is_number(str_2)
    bool_7 = module_0.is_uuid(bool_4)
    bool_8 = module_0.is_email(bool_1)
    bool_9 = module_0.is_email(bool_7)
    bool_10 = module_0.is_email(bool_9)
    int_0 = 201
    bool_11 = module_0.is_email(int_0)
    bool_12 = module_0.is_email(int_0)
    bool_13 = module_0.is_email(bool_4)
    bool_14 = module_0.is_email(bool_0)
    str_3 = '"\x0bP@b$.?pejLY'
    bool_15 = module_0.is_email(str_3)