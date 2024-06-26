# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1974
    str_0 = module_0.roman_encode(int_0)

def test_case_2():
    str_0 = 'J)q-C}&MUA,csfa'
    str_1 = module_0.compress(str_0)

def test_case_3():
    str_0 = 'This is a test'
    str_1 = module_0.compress(str_0)
    str_2 = module_0.decompress(str_1)

def test_case_4():
    str_0 = '9\x0c\\xf'
    str_1 = module_0.prettify(str_0)

def test_case_5():
    str_0 = 'Hi ALLa, my name  is... Stefano!! with $x$ and https://www.dapgs.it/example/string and info@dapgs.it'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()

def test_case_6():
    str_0 = 'V6?XfyAj]'
    str_1 = 'uuid'
    str_2 = '!)m]\\|Mg'
    str_3 = module_0.slugify(str_1, str_2)
    str_4 = module_0.prettify(str_0)

def test_case_7():
    str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
    bool_0 = True
    str_1 = module_0.strip_html(str_0, bool_0)
    str_2 = '\x0cD|7TnaF@'
    str_3 = module_0.snake_case_to_camel(str_0, str_2)
    str_4 = module_0.prettify(str_0)
    str_5 = module_0.asciify(str_4)
    str_6 = module_0.shuffle(str_5)
    str_7 = 'W\x0cIhK'
    str_8 = module_0.strip_margin(str_7)
    str_9 = module_0.reverse(str_0)
    str_10 = module_0.compress(str_7)

def test_case_8():
    str_0 = 'the_fnake_is_green'
    bool_0 = False
    str_1 = module_0.snake_case_to_camel(str_0, bool_0)

def test_case_9():
    str_0 = 'Z\x0cU9J}\t.z<;x1\t\nl'
    bool_0 = True
    str_1 = module_0.snake_case_to_camel(str_0, bool_0)
    str_2 = 'WhQLjv34'
    str_3 = module_0.snake_case_to_camel(str_2, str_2)
    str_4 = module_0.reverse(str_3)
    str_5 = module_0.compress(str_3)
    str_6 = 'EzOBw-J27Fo;'
    str_7 = module_0.shuffle(str_6)

def test_case_10():
    int_0 = 3999
    str_0 = '6Pep'
    str_1 = module_0.slugify(str_0)
    str_2 = module_0.roman_encode(int_0)

def test_case_11():
    str_0 = '@E7e=ES98hXsL+~98E'
    bool_0 = module_0.booleanize(str_0)

def test_case_12():
    str_0 = 'q$QiMa'
    str_1 = module_0.strip_margin(str_0)
    int_0 = 1974
    str_2 = module_0.roman_encode(int_0)

def test_case_13():
    str_0 = 'the_fnke_is_gree'
    bool_0 = True
    str_1 = module_0.snake_case_to_camel(str_0, bool_0)

def test_case_14():
    str_0 = '\rHo'
    str_1 = module_0.strip_margin(str_0)
    str_2 = module_0.strip_margin(str_0)
    str_3 = 'random_string'
    str_4 = 'Eq=!P(=V7.O'
    str_5 = 'G\x0bA|+_6nU_u93cat'
    str_6 = module_0.snake_case_to_camel(str_3, str_4)
    str_7 = module_0.prettify(str_4)
    roman_numbers_0 = module_0.__RomanNumbers()
    str_8 = module_0.slugify(str_5)
    str_9 = module_0.reverse(str_7)
    str_10 = module_0.reverse(str_7)
    str_11 = 'J'
    str_12 = module_0.compress(str_11)
    var_0 = module_0.camel_case_to_snake(str_9)
    int_0 = 2002
    str_13 = module_0.roman_encode(int_0)

def test_case_15():
    str_0 = '\rHo'
    str_1 = module_0.strip_margin(str_0)
    str_2 = 'random_string'
    str_3 = 'G\x0bA|+_6nU_u93cat'
    str_4 = module_0.snake_case_to_camel(str_2, str_1)
    str_5 = module_0.prettify(str_1)
    roman_numbers_0 = module_0.__RomanNumbers()
    str_6 = module_0.slugify(str_3)
    str_7 = 'zL)ieu*hB&*utS5+1'
    str_8 = module_0.snake_case_to_camel(str_7, str_6)
    str_9 = module_0.reverse(str_5)
    str_10 = module_0.reverse(str_5)
    str_11 = 'J'
    str_12 = module_0.compress(str_11)
    var_0 = module_0.camel_case_to_snake(str_9)
    int_0 = 1973
    str_13 = module_0.roman_encode(int_0)

def test_case_16():
    str_0 = 'hello-one-test'
    str_1 = '^\\s*\\w'
    bool_0 = True
    str_2 = '\n\t7%|JEJ/:T6e|'
    str_3 = module_0.snake_case_to_camel(str_1, bool_0, str_2)
    str_4 = module_0.snake_case_to_camel(str_1, bool_0)
    str_5 = '_fc'
    str_6 = module_0.snake_case_to_camel(str_5)
    str_7 = module_0.snake_case_to_camel(str_0)