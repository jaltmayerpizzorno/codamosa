# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    roman_numbers_0 = module_0.__RomanNumbers()

def test_case_1():
    str_0 = '([a-z]|[A-Z]+)(?=[A-Z])'
    str_1 = module_0.compress(str_0)
    str_2 = module_0.decompress(str_1)

def test_case_2():
    str_0 = '~ |_xlle/h;mlc'
    str_1 = 'i?xCJ5cUD0\rd@0'
    str_2 = module_0.prettify(str_1)
    bool_0 = module_0.booleanize(str_0)

def test_case_3():
    str_0 = '0h\t9E}x(|^'
    str_1 = module_0.reverse(str_0)

def test_case_4():
    str_0 = 'nf}{4h!U\rjq$a'
    str_1 = module_0.compress(str_0)
    str_2 = module_0.strip_html(str_1)
    str_3 = module_0.reverse(str_0)
    str_4 = 'yA@J(%f&r0^#nFc'
    str_5 = '@8CTWH})0\x0b&%('
    str_6 = module_0.prettify(str_5)
    str_7 = module_0.shuffle(str_4)
    str_8 = module_0.asciify(str_7)
    var_0 = module_0.camel_case_to_snake(str_7)

def test_case_5():
    str_0 = ',={l\x0c?@5\\\x0bM4MX5;'
    str_1 = module_0.snake_case_to_camel(str_0)

def test_case_6():
    str_0 = '^3(?:0[0-5]|[68]\\d)\\d{11}$'
    str_1 = module_0.shuffle(str_0)

def test_case_7():
    str_0 = '<w*\x0b!+(;O&'
    str_1 = module_0.strip_html(str_0)

def test_case_8():
    str_0 = 'uA)w3M$epe'
    str_1 = module_0.slugify(str_0)

def test_case_9():
    str_0 = 'V'
    str_1 = module_0.strip_margin(str_0)

def test_case_10():
    str_0 = 'contains_html'
    str_1 = module_0.snake_case_to_camel(str_0)

def test_case_11():
    str_0 = 'the_snake_is_green'
    bool_0 = False
    str_1 = module_0.snake_case_to_camel(str_0, bool_0)

def test_case_12():
    str_0 = ')UWL0.;E\x0bKSb)3J\n~bG\\'
    bool_0 = True
    str_1 = module_0.strip_html(str_0, bool_0)
    str_2 = 'jjf'
    bool_1 = module_0.booleanize(str_2)

def test_case_13():
    int_0 = 1858
    str_0 = module_0.roman_encode(int_0)
    roman_numbers_0 = module_0.__RomanNumbers()
    str_1 = 'is_camel_case'
    str_2 = module_0.shuffle(str_1)
    string_formatter_0 = module_0.__StringFormatter(str_1)

def test_case_14():
    str_0 = 'test'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()
    str_2 = 'testTest'
    string_formatter_1 = module_0.__StringFormatter(str_2)
    str_3 = string_formatter_1.format()
    str_4 = 'test@test'
    string_formatter_2 = module_0.__StringFormatter(str_4)
    str_5 = string_formatter_2.format()
    str_6 = 'test1.test2'
    string_formatter_3 = module_0.__StringFormatter(str_6)
    str_7 = string_formatter_3.format()
    str_8 = 'test@test.com'
    string_formatter_4 = module_0.__StringFormatter(str_8)
    str_9 = string_formatter_4.format()
    str_10 = 'test+test@test.test'
    string_formatter_5 = module_0.__StringFormatter(str_10)
    str_11 = string_formatter_5.format()

def test_case_15():
    str_0 = 'p_'
    str_1 = module_0.snake_case_to_camel(str_0)