# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    try:
        int_0 = -3428
        str_0 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '2Sw5'
        str_1 = module_0.strip_margin(str_0)
        str_2 = module_0.compress(str_0)
        str_3 = module_0.roman_encode(str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'MF5ay~?A&<H'
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'camel_case_to_snake'
        int_0 = -3088
        str_1 = module_0.compress(str_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'I?'
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = module_0.slugify(str_0)
        str_3 = module_0.reverse(str_1)
        str_4 = module_0.decompress(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 57
        str_0 = '3=nlC^KG'
        str_1 = module_0.reverse(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = module_0.compress(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = '8'
        str_6 = module_0.snake_case_to_camel(str_5)
        str_7 = module_0.prettify(str_5)
        str_8 = module_0.snake_case_to_camel(str_2)
        str_9 = module_0.decompress(str_4)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -159
        string_formatter_0 = module_0.__StringFormatter(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = " \n,nl.+R]&PI\x0c^0.'"
        str_1 = '[sD\\_'
        bool_0 = False
        str_2 = module_0.strip_html(str_1, bool_0)
        bool_1 = module_0.booleanize(str_0)
        str_3 = 'Invalid compression_level: it must be an "int" between 0 and 9'
        str_4 = ';Sg:\n#U'
        bool_2 = False
        str_5 = module_0.strip_html(str_4, bool_2)
        str_6 = '$%tH-VVR\r<XHx5Kej~3o'
        str_7 = module_0.strip_margin(str_4)
        str_8 = module_0.strip_margin(str_6)
        str_9 = module_0.prettify(str_3)
        bool_3 = False
        string_formatter_0 = module_0.__StringFormatter(bool_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        str_1 = 'D'
        int_0 = module_0.roman_decode(str_1)
        str_2 = module_0.reverse(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 1471.6
        var_0 = module_0.camel_case_to_snake(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        str_1 = module_0.snake_case_to_camel(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -3428
        str_0 = '"kG'
        bool_0 = False
        str_1 = module_0.snake_case_to_camel(str_0, bool_0, str_0)
        str_2 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'BtcO7Q7_d88sz3R'
        bool_0 = False
        str_1 = module_0.strip_margin(str_0)
        str_2 = module_0.snake_case_to_camel(str_0, bool_0)
        bool_1 = module_0.booleanize(str_1)
        str_3 = 's_ip'
        str_4 = module_0.strip_html(str_3, bool_1)
        str_5 = None
        str_6 = module_0.shuffle(str_5)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        bool_0 = True
        str_1 = module_0.strip_html(str_0, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'true'
        int_0 = 962
        str_1 = module_0.roman_encode(int_0)
        bool_0 = module_0.booleanize(str_0)
        str_2 = 'True'
        bool_1 = module_0.booleanize(str_2)
        str_3 = None
        bool_2 = module_0.booleanize(str_3)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = None
        str_1 = module_0.strip_margin(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'D'
        str_1 = ''
        str_2 = module_0.strip_html(str_1)
        bool_0 = module_0.booleanize(str_0)
        str_3 = module_0.compress(str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = ''
        str_1 = module_0.strip_margin(str_0)
        bool_0 = module_0.booleanize(str_1)
        int_0 = module_0.roman_decode(str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '}Ut\t&(2Meh;<;.PC'
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = None
        str_1 = module_0.compress(str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'I?'
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = '6Fv4_?b2#zA'
        str_3 = module_0.slugify(str_2)
        str_4 = ';r*cf\t\nz^'
        str_5 = module_0.reverse(str_4)
        str_6 = None
        str_7 = module_0.slugify(str_6)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'this_is_a_snake'
        str_1 = 'a_long_snake_for_testing'
        int_0 = 501
        str_2 = module_0.compress(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = ' %]'
        str_1 = module_0.strip_margin(str_0)
        str_2 = None
        str_3 = module_0.asciify(str_2)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '*L\x0c5&vxe!H[W\x0bPT6<bE'
        int_0 = None
        str_1 = module_0.shuffle(str_0)
        str_2 = module_0.compress(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_24():
    try:
        int_0 = 2859
        str_0 = '\\i>C9/!VlZ#h!|npiV'
        str_1 = 'dJVWAc)\x0c\nwDgVR!C'
        str_2 = module_0.slugify(str_1)
        str_3 = 'JZQ=bs0'
        str_4 = module_0.roman_encode(int_0)
        str_5 = module_0.strip_margin(str_4)
        str_6 = module_0.snake_case_to_camel(str_0)
        str_7 = module_0.prettify(str_3)
        int_1 = module_0.roman_decode(str_5)
        int_2 = module_0.roman_decode(str_1)
    except BaseException:
        pass

def test_case_25():
    try:
        int_0 = 56
        str_0 = module_0.roman_encode(int_0)
        str_1 = module_0.compress(str_0)
        str_2 = module_0.prettify(str_0)
        str_3 = module_0.snake_case_to_camel(str_0)
        str_4 = module_0.decompress(str_1)
        roman_numbers_0 = None
        string_formatter_0 = module_0.__StringFormatter(roman_numbers_0)
    except BaseException:
        pass

def test_case_26():
    try:
        int_0 = 56
        str_0 = module_0.roman_encode(int_0)
        str_1 = 'wT\tzQBf'
        str_2 = module_0.compress(str_1)
        str_3 = 'zR'
        var_0 = module_0.camel_case_to_snake(str_3)
        str_4 = module_0.prettify(str_2)
        str_5 = module_0.decompress(str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'true'
        str_1 = module_0.asciify(str_0)
        int_0 = 989
        str_2 = module_0.roman_encode(int_0)
        str_3 = module_0.reverse(str_0)
        bool_0 = module_0.booleanize(str_0)
        str_4 = 'True'
        bool_1 = module_0.booleanize(str_4)
        str_5 = 'TUE'
        bool_2 = module_0.booleanize(str_5)
        str_6 = "|]I,\teh\n'l\x0blXHVYF"
        bool_3 = True
        str_7 = module_0.strip_html(str_6, bool_3)
        str_8 = 'wC"-D\'RyxoN ~Z1!\x0cH<N'
        str_9 = '6o*M< gHk2;*B}[!8PQ'
        str_10 = module_0.compress(str_8, str_9)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '-6<_'
        str_1 = module_0.reverse(str_0)
        str_2 = module_0.compress(str_0)
        str_3 = module_0.snake_case_to_camel(str_2)
        str_4 = None
        str_5 = module_0.roman_encode(str_4)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'true'
        bool_0 = module_0.booleanize(str_0)
        str_1 = 'True'
        bool_1 = module_0.booleanize(str_1)
        str_2 = 'TU('
        bool_2 = module_0.booleanize(str_2)
        str_3 = 'YpwM[7'
        int_0 = -2
        str_4 = module_0.compress(str_2, str_3, int_0)
    except BaseException:
        pass