# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '%\x0c6"11Wl\x0b~_$:'
    bool_0 = module_0.is_isbn(str_0)

def test_case_2():
    str_0 = '123456789X'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()

def test_case_3():
    int_0 = 1130
    bool_0 = module_0.is_email(int_0)

def test_case_4():
    str_0 = 'CsU=zO-S oxT-x^'
    bool_0 = module_0.is_integer(str_0)

def test_case_5():
    str_0 = 'I'
    bool_0 = module_0.is_full_string(str_0)
    str_1 = '=0+\tmu<60\t'
    bool_1 = module_0.is_isbn(str_1)
    bool_2 = module_0.is_snake_case(str_0)
    bool_3 = module_0.is_decimal(str_0)

def test_case_6():
    str_0 = '.?\t{0(:\x0co\\bX@>z0>'
    str_1 = 'rz='
    str_2 = [str_1]
    bool_0 = module_0.is_url(str_0, str_2)
    str_3 = 'https://mysite.com'
    str_4 = 'https'
    str_5 = [str_4]
    bool_1 = module_0.is_url(str_3, str_5)
    bool_2 = module_0.is_url(str_5)

def test_case_7():
    str_0 = 'words_count'
    str_1 = 'is_isbn_13'
    bool_0 = module_0.is_isbn(str_1)
    bool_1 = module_0.is_url(str_0)
    bool_2 = module_0.is_full_string(bool_0)
    bool_3 = module_0.is_integer(str_0)
    str_2 = '9lhD`6s'
    bool_4 = module_0.is_isogram(bool_0)
    bool_5 = module_0.is_snake_case(bool_2)
    bool_6 = module_0.is_integer(str_2)
    bool_7 = module_0.is_camel_case(str_0)
    bool_8 = module_0.is_number(str_0)

def test_case_8():
    str_0 = 'eS*5f*(*E4'
    bool_0 = module_0.is_slug(str_0, str_0)
    str_1 = ')BwK8 S\\a<z:S+#mB~Wt'
    bool_1 = module_0.is_url(bool_0)
    bool_2 = module_0.is_credit_card(str_1)
    int_0 = module_0.words_count(str_1)
    str_2 = 'q+~q5sDaHx[,62;Ul&kg'
    int_1 = module_0.words_count(str_2)
    bool_3 = module_0.is_ip_v6(str_2)

def test_case_9():
    str_0 = 'Input must be >= 1 and <= 3999'
    bool_0 = module_0.is_ip(str_0)
    bool_1 = module_0.is_email(str_0)
    bool_2 = module_0.is_number(str_0)

def test_case_10():
    str_0 = ' 9/*'
    bool_0 = module_0.is_credit_card(str_0)
    float_0 = -2817.5782
    bool_1 = module_0.is_json(float_0)

def test_case_11():
    bool_0 = True
    bool_1 = module_0.is_ip_v6(bool_0)
    str_0 = '\n        :param input_data: Any received object\n        '
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_1)
    bool_2 = module_0.is_email(i_s_b_n_checker_0)
    str_1 = ''
    str_2 = 'iFY]&O'
    bool_3 = module_0.contains_html(str_2)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_4 = module_0.is_credit_card(i_s_b_n_checker_1)

def test_case_12():
    str_0 = 'I&}'
    str_1 = '}f\rX'
    bool_0 = module_0.is_isbn(str_1)
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_camel_case(bool_1)

def test_case_13():
    str_0 = '{"a":"b"} {"b":"c"}'
    bool_0 = module_0.is_json(str_0)

def test_case_14():
    str_0 = 'CotJG_k\n|<S[&'
    bool_0 = module_0.is_integer(str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    tuple_0 = (i_s_b_n_checker_0, i_s_b_n_checker_0)
    bool_1 = module_0.is_isogram(tuple_0)
    str_1 = '<&w\n}jVP*'
    bool_2 = module_0.is_isogram(str_1)
    bool_3 = module_0.is_json(str_0)
    bool_4 = module_0.is_credit_card(bool_2)
    bool_5 = module_0.is_slug(str_1)
    bool_6 = module_0.is_camel_case(bool_5)
    bool_7 = True
    bool_8 = i_s_b_n_checker_0.is_isbn_10()
    bool_9 = module_0.is_ip_v4(str_1)
    bool_10 = i_s_b_n_checker_0.is_isbn_10()
    bool_11 = module_0.is_uuid(bool_2, bool_7)
    bool_12 = module_0.is_isbn_13(str_1, bool_7)
    set_0 = {bool_5, str_1, str_1, str_1}
    bool_13 = module_0.contains_html(str_1)
    bool_14 = module_0.is_camel_case(set_0)
    bool_15 = False
    bool_16 = module_0.is_isogram(bool_14)
    bool_17 = module_0.is_credit_card(str_1)
    bool_18 = module_0.is_uuid(set_0)
    bool_19 = module_0.is_integer(str_1)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1, bool_15)
    bool_20 = module_0.is_snake_case(set_0)
    bool_21 = i_s_b_n_checker_1.is_isbn_13()
    str_2 = ''
    bool_22 = module_0.is_isbn(str_2)
    bool_23 = module_0.is_isbn_13(str_1, bool_13)
    bool_24 = module_0.is_ip(bool_5)

def test_case_15():
    str_0 = 'M+am'
    bool_0 = module_0.is_ip(str_0)

def test_case_16():
    str_0 = "u|2Hl~TN9)'<K$b&"
    bool_0 = module_0.is_camel_case(str_0)
    bool_1 = module_0.is_palindrome(str_0)
    str_1 = '4VS~j\x0c'
    int_0 = module_0.words_count(str_1)
    bool_2 = module_0.is_number(str_0)
    bool_3 = module_0.is_ip_v4(int_0)

def test_case_17():
    float_0 = 663.0
    bool_0 = module_0.is_palindrome(float_0)
    bool_1 = module_0.is_ip_v6(float_0)
    str_0 = '6GSaEYBvD&'
    bool_2 = module_0.is_slug(str_0)
    bool_3 = module_0.is_credit_card(float_0, str_0)
    str_1 = '2 cCPz\x0b@|Awz">YZE1q#'
    bool_4 = module_0.is_isbn(str_1)
    str_2 = 'ON\t2$Ra,s/3`o'
    bool_5 = module_0.is_ip(str_2)
    bool_6 = module_0.is_snake_case(float_0, str_2)
    bool_7 = True
    bool_8 = module_0.is_isbn_13(str_2, bool_7)
    int_0 = module_0.words_count(str_0)

def test_case_18():
    float_0 = 1938.09865
    bool_0 = module_0.is_email(float_0)
    str_0 = 'wjT,,RW>6.\x0bugj(SD'
    bool_1 = module_0.is_pangram(str_0)

def test_case_19():
    int_0 = -1839
    bool_0 = module_0.is_camel_case(int_0)
    str_0 = 'ieo&#jkD'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_1 = module_0.is_pangram(i_s_b_n_checker_0)
    complex_0 = None
    int_1 = 2
    complex_1 = None
    set_0 = {complex_1}
    tuple_0 = (complex_0, int_1, complex_0, set_0)
    bool_2 = module_0.is_isogram(tuple_0)
    bool_3 = module_0.contains_html(str_0)

def test_case_20():
    str_0 = 'Dk^;'
    str_1 = '\\ '
    bool_0 = module_0.is_string(str_0)
    bool_1 = module_0.is_json(str_1)
    bool_2 = module_0.is_number(str_0)
    bool_3 = module_0.is_isogram(str_1)

def test_case_21():
    dict_0 = None
    bool_0 = module_0.is_slug(dict_0)

def test_case_22():
    str_0 = 'Q}J@?Z5\x0b=j'
    bool_0 = module_0.contains_html(str_0)

def test_case_23():
    str_0 = '$<C8'
    int_0 = module_0.words_count(str_0)

def test_case_24():
    str_0 = '\x0br4,Np'
    bool_0 = module_0.is_isbn_10(str_0)
    bytes_0 = b'\xe7\x19\xd6l\xc8\x1b\x90'
    set_0 = {bytes_0, bytes_0, bytes_0}
    str_1 = 'p5r-}7Q\r}3:'
    bool_1 = module_0.is_decimal(str_1)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_2 = False
    bool_3 = module_0.is_full_string(bool_2)
    bool_4 = i_s_b_n_checker_0.is_isbn_13()
    bool_5 = module_0.is_uuid(set_0)
    str_2 = '<LPd95y<\r[F\rX'
    bool_6 = module_0.is_slug(str_2)

def test_case_25():
    str_0 = 'AmNhO=Z,\n^F^B@5;'
    bool_0 = False
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()

def test_case_26():
    str_0 = ' Mg,Wa'
    bool_0 = True
    bool_1 = module_0.is_isbn(str_0, bool_0)

def test_case_27():
    str_0 = 'N42t9dLMuNpr^g7'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = '09'
    str_2 = '\n    Checks if the given string represents a valid ISBN 13 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_13(\'9780312498580\') # returns true\n    >>> is_isbn_13(\'978-0312498580\') # returns true\n    >>> is_isbn_13(\'978-0312498580\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 13, false otherwise.\n    '
    bool_1 = module_0.is_camel_case(str_2)
    bool_2 = module_0.is_integer(str_1)

def test_case_28():
    str_0 = '##L'
    bool_0 = module_0.is_string(str_0)
    bool_1 = module_0.is_json(str_0)
    bool_2 = False
    bool_3 = module_0.is_string(bool_2)
    bool_4 = module_0.is_ip_v6(bool_2)

def test_case_29():
    str_0 = '##L'
    bool_0 = module_0.is_string(str_0)
    bool_1 = False
    bool_2 = module_0.is_ip(str_0)
    bool_3 = module_0.is_ip_v6(bool_1)

def test_case_30():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'my.email@gmail.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'my.email@gmail'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'my.email@gmail.'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'my.email@gmail.com.'
    bool_5 = module_0.is_email(str_5)
    str_6 = 'my.email@gmail.com.es'
    bool_6 = module_0.is_email(str_6)
    str_7 = 'my.email@gmail.com.es.uk.co.fr'
    bool_7 = module_0.is_email(str_7)
    str_8 = 'myemail@gmail.com.es.uk.co.fr.org'
    bool_8 = module_0.is_email(str_8)
    str_9 = 'a'
    int_0 = 320
    int_1 = 1
    var_0 = int_0 + int_1
    var_1 = str_9 * var_0
    str_10 = '@gmail.com.es'
    var_2 = var_1 + str_10
    bool_9 = module_0.is_email(var_2)

def test_case_31():
    str_0 = '\n{\n  "name": "Peter",\n  "age": 23,\n  "address": {\n    "street": "2 main st.",\n    "zip": "90210"\n  },\n  "references": [\n    {"name": "Annie", "phone": "212-555-1212"},\n    {"name": "Petey", "phone": "212-555-1212"}\n  ]\n}\n    '
    bool_0 = module_0.is_email(str_0)
    str_1 = 'test@test.a'
    bool_1 = module_0.is_email(str_1)

def test_case_32():
    bytes_0 = b'\xe6GD\x914'
    str_0 = 'y\t_m~>"*QjF?x\';qL}'
    str_1 = '{h3\x0c+d$KmNO)WTX*tH'
    list_0 = [str_0, str_1]
    bool_0 = module_0.is_url(bytes_0, list_0)
    str_2 = 'i'
    str_3 = '))LgC*wV1'
    bool_1 = module_0.is_isbn_10(str_2, bool_0)
    bool_2 = False
    str_4 = "@')W4`I\ryJc2t34s"
    bool_3 = True
    bool_4 = module_0.is_credit_card(str_2)
    bool_5 = module_0.is_isbn_13(str_4, bool_3)
    str_5 = 'Yl'
    bool_6 = module_0.is_integer(str_5)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_3, bool_2)
    str_6 = '\rz'
    int_0 = module_0.words_count(str_6)
    bool_7 = i_s_b_n_checker_0.is_isbn_13()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
    bool_8 = module_0.is_json(bytes_0)
    str_7 = 'NcbV@1"Tx\\h^H/b'
    bool_9 = module_0.is_ip_v4(bool_8)
    i_s_b_n_checker_2 = module_0.__ISBNChecker(str_7)
    bool_10 = module_0.is_palindrome(str_2)

def test_case_33():
    str_0 = 'is_(ip_v4'
    bool_0 = module_0.is_integer(str_0)
    str_1 = '\'mW@4Rj2\\zq%NT\t&pO!"'
    int_0 = module_0.words_count(str_1)
    bool_1 = module_0.is_palindrome(str_1)
    bool_2 = True
    bool_3 = module_0.is_full_string(str_1)
    bool_4 = module_0.is_email(bool_2)
    str_2 = '!E/XD%O}:'
    str_3 = 'is_isbn_10'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_3)
    bool_5 = True
    bool_6 = module_0.is_palindrome(str_0, bool_2, bool_5)
    bool_7 = module_0.is_url(str_3)
    bool_8 = i_s_b_n_checker_0.is_isbn_13()
    bool_9 = module_0.is_integer(str_0)
    str_4 = '`'
    bool_10 = i_s_b_n_checker_0.is_isbn_10()
    str_5 = '!'
    bool_11 = module_0.is_isbn_10(str_5)
    bool_12 = module_0.is_integer(str_4)
    bool_13 = module_0.is_email(bool_6)
    str_6 = 'A'
    bool_14 = module_0.is_isbn_13(str_6)
    bool_15 = module_0.is_email(bool_4)
    bool_16 = i_s_b_n_checker_0.is_isbn_10()
    bool_17 = module_0.is_slug(str_0)
    bool_18 = i_s_b_n_checker_0.is_isbn_10()
    bool_19 = i_s_b_n_checker_0.is_isbn_13()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2, bool_19)
    bool_20 = i_s_b_n_checker_1.is_isbn_13()
    bool_21 = module_0.is_credit_card(str_0)

def test_case_34():
    bytes_0 = b'\x1b\xcaRR\x7f\t\x9f\xd7u\xef\xfbn!'
    str_0 = None
    bool_0 = module_0.is_credit_card(bytes_0, str_0)
    str_1 = 'mGt>'
    bool_1 = module_0.is_isbn_10(str_1)
    str_2 = 'B[y\\)Sz&5^7'
    int_0 = module_0.words_count(str_2)
    str_3 = '@\tDJ|ef"A\x0c?N9or'
    bool_2 = module_0.is_isbn_13(str_3)
    str_4 = '\n    Remove html code contained into the given string.\n\n    *Examples:*\n\n    >>> strip_html(\'test: <a href="foo/bar">click here</a>\') # returns \'test: \'\n    >>> strip_html(\'test: <a href="foo/bar">click here</a>\', keep_tag_content=True) # returns \'test: click here\'\n\n    :param input_string: String to manipulate.\n    :type input_string: str\n    :param keep_tag_content: True to preserve tag content, False to remove tag and its content too (default).\n    :type keep_tag_content: bool\n    :return: String with html removed.\n    '
    str_5 = '1'
    bool_3 = module_0.is_decimal(str_5)
    int_1 = module_0.words_count(str_4)
    bool_4 = module_0.is_slug(str_4)
    bool_5 = module_0.is_uuid(bool_2)
    bool_6 = module_0.is_decimal(str_3)
    bool_7 = module_0.is_slug(int_1)

def test_case_35():
    str_0 = '.test@gmail.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'test@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'test@test.test.test'
    bool_2 = module_0.is_email(str_2)
    str_3 = ' test@test'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'test@test.test..test'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'test@test.a.test'
    bool_5 = module_0.is_email(str_5)
    bool_6 = module_0.is_email(str_2)
    str_6 = 'test@test.test.test.test'
    bool_7 = module_0.is_email(str_6)
    str_7 = 'test@@test.test.test'
    bool_8 = module_0.is_email(str_7)
    str_8 = '(0`"d@LXipF<"`('
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_8)
    bool_9 = i_s_b_n_checker_0.is_isbn_13()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_3, bool_0)
    bool_10 = i_s_b_n_checker_1.is_isbn_13()
    i_s_b_n_checker_2 = module_0.__ISBNChecker(str_0)
    bool_11 = i_s_b_n_checker_2.is_isbn_13()

def test_case_36():
    str_0 = 'test@gmail.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'test@gmail.com.'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'test@gmail.com...'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'test@gmail.com..'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'test..@gmail.com'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'test.test@gmail.com'
    bool_5 = module_0.is_email(str_5)
    str_6 = 'test.test@gmail..com'
    bool_6 = module_0.is_email(str_6)

def test_case_37():
    float_0 = -1306.64
    bool_0 = module_0.is_ip_v4(float_0)
    bool_1 = module_0.is_json(bool_0)
    str_0 = "G..'L`C}@2lv"
    bool_2 = module_0.is_slug(float_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_3 = module_0.is_palindrome(bool_1, bool_0)
    str_1 = 'j;"G)A(M\n`A\\GaAPY~\'t'
    bool_4 = module_0.is_decimal(str_1)
    bool_5 = module_0.is_url(bool_4)
    str_2 = '\\I&Fl4\\zX'
    bool_6 = module_0.is_integer(str_2)
    str_3 = ''
    str_4 = '[a~C.1s;OJLy_V'
    str_5 = ')!3GR$'
    bool_7 = module_0.is_isbn_10(str_5)
    bool_8 = module_0.is_ip(bool_4)
    str_6 = ';Z,?@\x0c^2J!!i$dbFm ='
    bool_9 = module_0.is_isbn(str_6, bool_3)
    bool_10 = i_s_b_n_checker_0.is_isbn_10()
    bool_11 = i_s_b_n_checker_0.is_isbn_10()
    bool_12 = module_0.is_email(str_0)
    bool_13 = module_0.is_email(str_3)
    bool_14 = module_0.is_ip_v4(str_0)
    bool_15 = None
    bool_16 = module_0.is_isbn_13(str_5, bool_15)
    bool_17 = module_0.is_slug(str_3)
    bool_18 = i_s_b_n_checker_0.is_isbn_10()
    bool_19 = i_s_b_n_checker_0.is_isbn_13()
    str_7 = "0JLF{L5Gyj'9x|\x0cS"
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_4, bool_17)
    bool_20 = i_s_b_n_checker_1.is_isbn_13()
    bool_21 = i_s_b_n_checker_0.is_isbn_13()
    bool_22 = module_0.is_credit_card(str_7)

def test_case_38():
    str_0 = '978-3-662-48339-5'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0)
    bool_1 = i_s_b_n_checker_1.is_isbn_13()
    str_1 = '978-3-662-48339'
    i_s_b_n_checker_2 = module_0.__ISBNChecker(str_1)
    bool_2 = i_s_b_n_checker_2.is_isbn_13()
    str_2 = '978-3-662-483391'
    i_s_b_n_checker_3 = module_0.__ISBNChecker(str_2)
    bool_3 = i_s_b_n_checker_3.is_isbn_13()
    str_3 = '978-3-662-48339 5'
    bool_4 = module_0.is_email(str_3)
    bool_5 = module_0.is_email(str_3)
    bool_6 = i_s_b_n_checker_2.is_isbn_13()

def test_case_39():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = 'nope'
    bool_1 = module_0.is_ip_v4(str_1)

def test_case_40():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = 'nope'
    bool_1 = module_0.is_ip_v4(str_1)
    str_2 = '255.200.100.999'
    bool_2 = module_0.is_ip_v4(str_2)

def test_case_41():
    str_0 = '0316666343'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    bool_1 = module_0.is_email(bool_0)
    str_1 = 'example-indeed@strange-example.com'
    bool_2 = module_0.is_email(str_1)
    bool_3 = True
    bool_4 = module_0.is_email(bool_3)
    bool_5 = module_0.is_email(bool_0)
    bool_6 = module_0.is_email(bool_1)
    bool_7 = module_0.is_email(bool_0)

def test_case_42():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = '"very.(),:;<>[]".VERY."very@\\ "very".unusual"@gmail.com'
    bool_2 = module_0.is_email(str_2)

def test_case_43():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip(str_0)
    str_1 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_1 = module_0.is_ip(str_1)
    str_2 = '1.2.3'
    bool_2 = module_0.is_ip(str_2)
    str_3 = ''
    bool_3 = module_0.is_ip(str_3)
    int_0 = 1
    bool_4 = module_0.is_ip(int_0)
    var_0 = None
    bool_5 = module_0.is_ip(var_0)

def test_case_44():
    str_0 = '9780312498580'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '1506715214'
    bool_1 = module_0.is_isbn(str_1)
    str_2 = '1234567890123'
    bool_2 = module_0.is_isbn(str_2)
    str_3 = '123456789012345'
    bool_3 = module_0.is_isbn(str_3)
    bool_4 = False
    bool_5 = module_0.is_isbn(str_0, bool_4)
    bool_6 = module_0.is_isbn(str_1, bool_4)
    str_4 = '978-0312498580'
    bool_7 = module_0.is_isbn(str_4, bool_4)
    str_5 = '150-6715214'
    bool_8 = module_0.is_isbn(str_5, bool_4)
    str_6 = '123-456789012-3'
    bool_9 = module_0.is_isbn(str_6, bool_4)
    str_7 = '123-456789012345'
    bool_10 = module_0.is_isbn(str_7, bool_4)

def test_case_45():
    str_0 = 'OV$5HZwIAKMVq~+L'
    bool_0 = True
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    bool_2 = module_0.is_email(str_0)
    bool_3 = module_0.is_email(str_0)
    bool_4 = i_s_b_n_checker_0.is_isbn_13()
    str_1 = '"my.addess@gmal.com"gmail.com'
    bool_5 = module_0.is_email(str_1)
    int_0 = module_0.words_count(str_1)
    bool_6 = module_0.is_ip_v4(bool_5)
    str_2 = 'is_decimal'
    str_3 = 'test@gmail.com.com'
    bool_7 = module_0.is_email(str_3)
    bool_8 = i_s_b_n_checker_0.is_isbn_13()
    bool_9 = module_0.is_isbn(str_3)
    bool_10 = module_0.is_credit_card(str_2)
    bool_11 = i_s_b_n_checker_0.is_isbn_13()

def test_case_46():
    str_0 = '4111 1111 1111 1111'
    bool_0 = module_0.is_credit_card(str_0)
    str_1 = '4111-1111-1111-1111'
    bool_1 = module_0.is_credit_card(str_1)
    str_2 = '4111111111111111'
    bool_2 = module_0.is_credit_card(str_2)
    str_3 = 'VISA'
    bool_3 = module_0.is_credit_card(str_1, str_3)
    bool_4 = module_0.is_json(str_1)
    bool_5 = module_0.is_json(str_3)