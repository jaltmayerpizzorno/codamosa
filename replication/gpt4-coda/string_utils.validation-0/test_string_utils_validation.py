# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'y#eB~Tu'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)

def test_case_2():
    str_0 = '978-3-16-148410-0'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_13()
    bool_1 = module_0.is_isbn(str_0)

def test_case_3():
    bool_0 = None
    bool_1 = module_0.is_credit_card(bool_0)
    bool_2 = module_0.is_email(bool_0)
    bool_3 = module_0.is_ip_v4(bool_0)
    str_0 = 'is_snake_case'
    bool_4 = module_0.is_isbn_13(str_0)

def test_case_4():
    str_0 = 'GDG%ue'
    bool_0 = module_0.is_isbn_13(str_0)

def test_case_5():
    str_0 = 'qCX8/n9txS:&#'
    bool_0 = module_0.is_isbn_10(str_0)
    str_1 = 'PB/^Sagpu,'
    bool_1 = module_0.is_isbn(str_1, bool_0)

def test_case_6():
    str_0 = ']\tPFzC8'
    bool_0 = module_0.is_isbn_10(str_0)

def test_case_7():
    bytes_0 = None
    bool_0 = module_0.is_string(bytes_0)

def test_case_8():
    str_0 = 'R'
    bool_0 = module_0.is_isogram(str_0)

def test_case_9():
    str_0 = '+E.5olZRRaj'
    bool_0 = module_0.is_number(str_0)

def test_case_10():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_integer(str_0)
    bool_1 = module_0.is_email(str_0)

def test_case_11():
    str_0 = 'j#a\r$:(zBs"0n2x:B?`'
    bool_0 = module_0.is_decimal(str_0)

def test_case_12():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_url(str_0)

def test_case_13():
    str_0 = 'my.email@the-provider.com'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = module_0.is_url(str_0, list_0)

def test_case_14():
    str_0 = 'u)\ty.D78:|Sr_r<]y='
    bool_0 = module_0.is_ip(str_0)
    float_0 = -1475.5736
    bytes_0 = b'\x9f\x8a\xc0\xfc\x87r\\'
    bool_1 = module_0.is_url(float_0, bytes_0)

def test_case_15():
    str_0 = '+VZ!KB!%5S_'
    bool_0 = module_0.is_email(str_0)

def test_case_16():
    tuple_0 = ()
    bool_0 = module_0.is_email(tuple_0)

def test_case_17():
    str_0 = '4111111111111111'
    bool_0 = module_0.is_credit_card(str_0)

def test_case_18():
    bytes_0 = b"q'\xac\x12\x88\xfd\x12t"
    bool_0 = module_0.is_ip(bytes_0)
    bool_1 = module_0.is_credit_card(bool_0)
    str_0 = '255.200.100.75'
    bool_2 = module_0.is_ip(str_0)

def test_case_19():
    str_0 = 'p~BP i\nY`E2*kQt'
    bool_0 = module_0.is_credit_card(str_0)
    bool_1 = module_0.is_credit_card(str_0)
    bool_2 = module_0.is_decimal(str_0)

def test_case_20():
    str_0 = 'dma{g!'
    bool_0 = module_0.is_camel_case(str_0)

def test_case_21():
    tuple_0 = ()
    bool_0 = module_0.is_snake_case(tuple_0)

def test_case_22():
    str_0 = '7A,i=0KeF"'
    str_1 = ':IV~OSK.\rY2ilw'
    bool_0 = module_0.is_snake_case(str_0, str_1)

def test_case_23():
    str_0 = '{"name": "John", "age": 30}'
    bool_0 = module_0.is_json(str_0)

def test_case_24():
    float_0 = 1744.636037
    bool_0 = module_0.is_json(float_0)

def test_case_25():
    bool_0 = False
    bool_1 = module_0.is_uuid(bool_0)
    str_0 = 'p~BP i\nY`E2*kQt'
    bool_2 = module_0.is_credit_card(str_0)
    bool_3 = module_0.is_camel_case(bool_0)
    bool_4 = module_0.is_credit_card(str_0)
    bool_5 = module_0.is_decimal(str_0)

def test_case_26():
    str_0 = ''
    bool_0 = False
    bool_1 = module_0.is_isbn_10(str_0, bool_0)
    str_1 = '~Pq{x[]`2P;iw"i5~\x0c@ '
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_2 = module_0.is_snake_case(i_s_b_n_checker_0)
    str_2 = '|6\x0c'
    bool_3 = module_0.is_email(str_1)
    bool_4 = module_0.is_isogram(str_2)
    bool_5 = module_0.is_pangram(bool_0)
    bool_6 = True
    bool_7 = i_s_b_n_checker_0.is_isbn_13()
    bool_8 = i_s_b_n_checker_0.is_isbn_13()
    bool_9 = i_s_b_n_checker_0.is_isbn_10()
    bool_10 = module_0.is_credit_card(str_1)
    bool_11 = module_0.is_palindrome(str_2)
    bool_12 = i_s_b_n_checker_0.is_isbn_10()
    bool_13 = module_0.is_uuid(str_2)
    bool_14 = module_0.is_uuid(str_2, bool_6)
    bool_15 = i_s_b_n_checker_0.is_isbn_13()
    str_3 = "lG'@?fS|X\np"
    int_0 = module_0.words_count(str_3)
    bool_16 = module_0.is_isogram(i_s_b_n_checker_0)

def test_case_27():
    str_0 = 'jyGYDm4'
    bool_0 = module_0.is_ip_v4(str_0)

def test_case_28():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip(str_0)

def test_case_29():
    bytes_0 = b'\x9do>\x9d\xb1Rpj\xf4'
    bool_0 = module_0.is_ip(bytes_0)
    str_0 = '#_}'
    bool_1 = module_0.is_palindrome(str_0)
    str_1 = '>60T'
    int_0 = module_0.words_count(str_1)

def test_case_30():
    str_0 = '?8J}Z'
    bool_0 = module_0.is_uuid(str_0)
    bool_1 = None
    bool_2 = module_0.is_isbn_10(str_0, bool_1)
    bool_3 = module_0.is_isogram(str_0)
    bool_4 = module_0.is_ip_v6(str_0)
    bool_5 = module_0.is_decimal(str_0)
    bool_6 = True
    bool_7 = module_0.is_ip_v4(bool_6)
    bool_8 = module_0.is_palindrome(bool_5, bool_6)
    bool_9 = module_0.is_integer(str_0)
    bool_10 = module_0.is_email(str_0)

def test_case_31():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_isogram(str_0)
    bool_1 = True
    bool_2 = module_0.is_palindrome(str_0, bool_1)
    str_1 = 'r#E"FqR\'m\\P})|7|D_'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_3 = i_s_b_n_checker_0.is_isbn_13()
    bool_4 = module_0.is_ip(bool_3)
    str_2 = 'e\\}IpUu=/'
    bool_5 = i_s_b_n_checker_0.is_isbn_13()
    int_0 = -1968
    bool_6 = module_0.is_ip(bool_0)
    bool_7 = module_0.is_credit_card(bool_2)
    bool_8 = module_0.is_ip(str_2)
    int_1 = -1968
    bool_9 = module_0.is_json(int_1)
    bool_10 = module_0.is_camel_case(str_1)
    bool_11 = module_0.is_snake_case(str_2)
    bool_12 = module_0.is_ip_v4(int_0)
    bool_13 = module_0.is_email(int_1)

def test_case_32():
    bytes_0 = b'\x9do>\x9d\xb1Rpj\xf4'
    bool_0 = module_0.is_ip(bytes_0)
    str_0 = 'C'
    bool_1 = module_0.is_palindrome(str_0)
    str_1 = '>x0T'
    int_0 = module_0.words_count(str_1)

def test_case_33():
    str_0 = "+f,0/'0u?;lr?, Y"
    bool_0 = module_0.is_pangram(str_0)
    bool_1 = module_0.is_isbn(str_0)

def test_case_34():
    str_0 = 'ABWp6%PDNB'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    int_0 = 255
    str_1 = 'SAXON_GENITIVE'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_0 = module_0.is_pangram(int_0)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    bool_2 = i_s_b_n_checker_0.is_isbn_13()

def test_case_35():
    bool_0 = True
    str_0 = 'dLRY\\i$uySDkX80/Zo[!'
    bool_1 = module_0.is_isogram(bool_0)
    str_1 = 'roman_range'
    int_0 = module_0.words_count(str_0)
    list_0 = [str_0, str_1, str_1, str_0]
    bool_2 = module_0.is_isbn_10(str_1)
    str_2 = ">>u\tE\n?/\\ePjre '"
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_1)
    bool_3 = i_s_b_n_checker_0.is_isbn_13()
    bool_4 = module_0.is_slug(str_0)
    bool_5 = module_0.is_url(bool_0, list_0)
    str_3 = 'q0wa]O\x0cp~"8nM'
    bool_6 = True
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_3, bool_6)
    i_s_b_n_checker_2 = module_0.__ISBNChecker(str_1, bool_4)
    bool_7 = i_s_b_n_checker_1.is_isbn_10()
    bool_8 = module_0.is_ip(str_1)

def test_case_36():
    str_0 = 'Tc?'
    int_0 = module_0.words_count(str_0)
    float_0 = 4751.214968
    bool_0 = module_0.is_slug(float_0)
    str_1 = '7'
    bool_1 = module_0.is_isbn(str_1)

def test_case_37():
    str_0 = 'U2:u[p>o;u*-D({=ce'
    bool_0 = module_0.contains_html(str_0)

def test_case_38():
    str_0 = '|P'
    int_0 = module_0.words_count(str_0)

def test_case_39():
    str_0 = '&z$4Z'
    bool_0 = module_0.is_isbn(str_0)

def test_case_40():
    bytes_0 = b'\xaea\xe5\x80p'
    bool_0 = module_0.is_palindrome(bytes_0)
    bool_1 = module_0.is_isogram(bool_0)
    bool_2 = module_0.is_url(bytes_0)
    str_0 = '4'
    str_1 = 'NLf0|\\&\x0bye0}BZU91'
    bool_3 = module_0.is_decimal(str_1)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
    bool_4 = i_s_b_n_checker_0.is_isbn_13()
    bool_5 = i_s_b_n_checker_0.is_isbn_10()
    bool_6 = i_s_b_n_checker_0.is_isbn_13()
    str_2 = 't'
    bool_7 = module_0.contains_html(str_2)
    bool_8 = i_s_b_n_checker_0.is_isbn_10()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0)
    bool_9 = i_s_b_n_checker_1.is_isbn_13()
    str_3 = '`\x0cr|)<'
    bool_10 = module_0.is_decimal(str_3)
    bool_11 = module_0.is_camel_case(bool_10)
    bool_12 = module_0.is_uuid(bool_10)
    bool_13 = module_0.is_slug(bool_7)
    bool_14 = False
    bool_15 = i_s_b_n_checker_0.is_isbn_13()
    bool_16 = module_0.is_credit_card(bytes_0, str_3)
    bool_17 = module_0.is_isbn(str_3, bool_14)
    bool_18 = module_0.is_string(bool_17)
    bool_19 = module_0.is_uuid(i_s_b_n_checker_1)
    bool_20 = module_0.is_ip_v4(bytes_0)
    bool_21 = module_0.is_json(i_s_b_n_checker_0)
    bool_22 = i_s_b_n_checker_1.is_isbn_13()
    bool_23 = module_0.is_string(bytes_0)
    bool_24 = i_s_b_n_checker_1.is_isbn_13()
    str_4 = '/C=L<'
    bool_25 = True
    bool_26 = module_0.is_uuid(bool_1, bool_25)
    bool_27 = module_0.contains_html(str_4)
    bool_28 = module_0.is_decimal(str_0)
    bool_29 = i_s_b_n_checker_0.is_isbn_13()
    bool_30 = i_s_b_n_checker_1.is_isbn_10()

def test_case_41():
    str_0 = '411111111111S111'
    bool_0 = module_0.is_json(str_0)

def test_case_42():
    float_0 = -3401.43
    bool_0 = module_0.is_ip(float_0)

def test_case_43():
    str_0 = ''
    bool_0 = module_0.is_isogram(str_0)

def test_case_44():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)

def test_case_45():
    str_0 = 'J;b4+(f*LD)Y\x0c-9+pNSx'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'words_count'
    list_0 = [str_1, str_1, str_1]
    bool_1 = module_0.is_slug(str_1)
    bool_2 = module_0.is_snake_case(bool_1)
    bool_3 = None
    bool_4 = module_0.is_ip_v4(str_1)
    bool_5 = module_0.is_uuid(list_0, bool_3)
    bool_6 = module_0.is_full_string(str_1)
    bool_7 = module_0.is_email(list_0)
    str_2 = '|N(#].\x0cw\\pLA`'
    bool_8 = module_0.is_ip_v4(str_2)
    bool_9 = module_0.is_email(bool_7)
    bool_10 = False
    bool_11 = module_0.is_camel_case(bool_7)
    list_1 = [str_0]
    bool_12 = module_0.is_url(str_1, list_1)
    str_3 = '7'
    bool_13 = module_0.is_integer(str_3)
    bool_14 = module_0.is_isbn_13(str_2, bool_10)
    str_4 = '\nxwm65b3g&E[8MM'
    bool_15 = module_0.contains_html(str_4)
    str_5 = 'T:*SN LR'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_5, bool_2)
    bool_16 = i_s_b_n_checker_0.is_isbn_13()
    bool_17 = module_0.is_ip(bool_10)
    str_6 = 'e\\}IpUu=/'
    bool_18 = module_0.is_credit_card(str_4)
    bool_19 = module_0.is_json(bool_1)
    bool_20 = module_0.is_credit_card(bool_7, str_6)
    bool_21 = module_0.is_palindrome(bool_16)
    str_7 = '%:Czo}h'
    bool_22 = module_0.is_number(str_6)
    bool_23 = module_0.is_number(str_7)

def test_case_46():
    bool_0 = True
    list_0 = None
    str_0 = 'qCX8/n9txS:&#'
    bool_1 = module_0.is_isbn_10(str_0)
    bool_2 = module_0.is_url(bool_0, list_0)
    bool_3 = None
    str_1 = 'PB/^Sagpu,'
    bool_4 = module_0.is_isbn(str_1, bool_1)
    bool_5 = module_0.is_isbn(str_0)
    bool_6 = module_0.is_ip(bool_3)
    str_2 = '$W32h*x|\\.m(Ht'
    bool_7 = module_0.is_email(bool_6)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
    str_3 = '$'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_3, bool_4)
    bool_8 = i_s_b_n_checker_1.is_isbn_10()
    bool_9 = i_s_b_n_checker_1.is_isbn_13()
    bool_10 = i_s_b_n_checker_0.is_isbn_10()
    bool_11 = module_0.is_isogram(bool_2)
    bool_12 = False
    bool_13 = module_0.is_palindrome(str_0)
    str_4 = '[uc#`xM5"(4G<H&Z-o'
    i_s_b_n_checker_2 = module_0.__ISBNChecker(str_3)
    bool_14 = i_s_b_n_checker_1.is_isbn_13()
    bool_15 = module_0.is_ip(bool_12)
    bool_16 = module_0.is_ip(bool_15)
    bool_17 = module_0.is_credit_card(str_4)
    bool_18 = module_0.is_ip(i_s_b_n_checker_0)
    str_5 = "\n    Force string content to be ascii-only by translating all non-ascii chars into the closest possible representation\n    (eg: ó -> o, Ë -> E, ç -> c...).\n\n    **Bear in mind**: Some chars may be lost if impossible to translate.\n\n    *Example:*\n\n    >>> asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') # returns 'eeuuooaaeynAAACIINOE'\n\n    :param input_string: String to convert\n    :return: Ascii utf-8 string\n    "
    bool_19 = module_0.is_json(str_4)
    bool_20 = module_0.is_camel_case(bool_6)
    bool_21 = module_0.is_snake_case(i_s_b_n_checker_2)
    bool_22 = module_0.is_ip_v4(str_5)
    bool_23 = module_0.is_email(str_5)

def test_case_47():
    str_0 = 'http://www.example.com'
    bool_0 = module_0.is_url(str_0)
    list_0 = [str_0, str_0]
    bool_1 = module_0.is_url(str_0, list_0)
    bool_2 = module_0.is_url(bool_1)

def test_case_48():
    str_0 = '\nhF'
    bool_0 = False
    bool_1 = module_0.is_isbn_13(str_0)
    bool_2 = False
    bool_3 = True
    str_1 = 'k'
    bool_4 = module_0.is_slug(bool_3, str_1)
    str_2 = '7'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
    bool_5 = i_s_b_n_checker_0.is_isbn_10()
    bool_6 = module_0.is_palindrome(str_0, bool_2, bool_3)
    bool_7 = module_0.is_credit_card(bool_0)
    bool_8 = module_0.is_decimal(str_0)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0, bool_0)
    bool_9 = module_0.is_integer(str_0)
    bool_10 = i_s_b_n_checker_1.is_isbn_10()
    bool_11 = module_0.contains_html(str_0)
    bool_12 = module_0.is_ip_v6(str_0)

def test_case_49():
    str_0 = '4111111111111111'
    str_1 = 'VISA'
    bool_0 = module_0.is_credit_card(str_0, str_1)
    str_2 = '4012888888881881'
    bool_1 = module_0.is_credit_card(str_2, str_1)
    str_3 = '5555555555554444'
    str_4 = 'MASTERCARD'
    bool_2 = module_0.is_credit_card(str_3, str_4)
    str_5 = '5105105105105100'
    bool_3 = module_0.is_credit_card(str_5, str_4)
    bool_4 = module_0.is_ip(str_5)

def test_case_50():
    str_0 = '0471958697'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = i_s_b_n_checker_0.is_isbn_10()
    str_1 = '0-471-60695-2'
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
    bool_1 = module_0.is_ip(str_0)

def test_case_51():
    bytes_0 = b'\xae\xd2\\M\x88\xf6\xb4\x13s\xcb\xde\x02'
    str_0 = '>,9+'
    bool_0 = module_0.is_number(str_0)
    bool_1 = module_0.is_slug(bytes_0)
    str_1 = 'K[p0'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    bool_2 = i_s_b_n_checker_0.is_isbn_10()
    str_2 = 'cML^t-$Ha\r3kE"5'
    bool_3 = True
    bool_4 = i_s_b_n_checker_0.is_isbn_10()
    bool_5 = module_0.is_integer(str_2)
    bool_6 = module_0.is_snake_case(str_0)
    bool_7 = module_0.is_pangram(str_2)
    bool_8 = module_0.is_decimal(str_2)
    bool_9 = module_0.is_isbn_13(str_2, bool_3)
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
    bool_10 = i_s_b_n_checker_1.is_isbn_13()
    bool_11 = module_0.is_credit_card(bool_5, str_2)
    str_3 = ".'|P}N\roS57ka'"
    bool_12 = module_0.contains_html(str_3)
    bool_13 = i_s_b_n_checker_1.is_isbn_10()
    list_0 = [str_1]
    bool_14 = module_0.is_url(bool_9, list_0)
    bool_15 = module_0.is_json(bool_12)
    tuple_0 = (bytes_0,)
    str_4 = 'k!^AD<N$~L0#do)@CYO'
    bool_16 = module_0.contains_html(str_4)
    bool_17 = module_0.is_isbn_13(str_1)
    bool_18 = module_0.is_snake_case(tuple_0)
    bool_19 = module_0.is_json(tuple_0)
    bool_20 = module_0.is_email(str_3)
    bool_21 = module_0.contains_html(str_3)
    bool_22 = module_0.is_uuid(bool_5)
    bool_23 = i_s_b_n_checker_1.is_isbn_10()
    str_5 = '6xW2SF^"bj='
    bool_24 = module_0.is_slug(bool_0, str_5)
    bool_25 = module_0.is_pangram(tuple_0)
    str_6 = '?'
    bool_26 = module_0.is_isbn_10(str_6, bool_13)