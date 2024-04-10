# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    string_compressor_0 = module_0.__StringCompressor()

def test_case_1():
    str_0 = '/G!p-$wJX\tK3][[;hq'
    str_1 = module_0.prettify(str_0)

def test_case_2():
    str_0 = "\n    Check if a string is not empty (it must contains at least one non space character).\n\n    *Examples:*\n\n    >>> is_full_string(None) # returns false\n    >>> is_full_string('') # returns false\n    >>> is_full_string(' ') # returns false\n    >>> is_full_string('hello') # returns true\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if not empty, false otherwise.\n    "
    str_1 = module_0.prettify(str_0)

def test_case_3():
    str_0 = 'ThisIsACamelStringTest'
    var_0 = module_0.camel_case_to_snake(str_0)

def test_case_4():
    str_0 = '_'
    str_1 = module_0.snake_case_to_camel(str_0, str_0)

def test_case_5():
    str_0 = 'ThiYIsACame$StringTest'
    str_1 = ''
    str_2 = module_0.prettify(str_1)
    str_3 = module_0.strip_html(str_0)
    var_0 = module_0.camel_case_to_snake(str_0)

def test_case_6():
    str_0 = 'WBV'
    str_1 = module_0.asciify(str_0)

def test_case_7():
    dict_0 = {}
    roman_numbers_0 = module_0.__RomanNumbers(**dict_0)
    roman_numbers_1 = module_0.__RomanNumbers()
    str_0 = '.AoO[\tJ=}_Xd,\x0c'
    str_1 = module_0.slugify(str_0)

def test_case_8():
    str_0 = '((?<=\\S)\\+(?=\\S)|(?<=\\S)\\+\\s|\\s\\+(?=\\S)|(?<=\\S)-(?=\\S)|(?<=\\S)-\\s|\\s-(?=\\S)|(?<=\\S)/(?=\\S)|(?<=\\S)/\\s|\\s/(?=\\S)|(?<=\\S)\\*(?=\\S)|(?<=\\S)\\*\\s|\\s\\*(?=\\S)|(?<=\\S)=(?=\\S)|(?<=\\S)=\\s|\\s=(?=\\S)|\\s"[^"]+"(?=[^\\s?.:!,;])|(?<=\\S)"[^"]+"\\s|(?<=\\S)"[^"]+"(?=[^\\s?.:!,;])|\\s\\([^)]+\\)(?=[^\\s?.:!,;])|(?<=\\S)\\([^)]+\\)\\s|(?<=\\S)(\\([^)]+\\))(?=[^\\s?.:!,;]))'
    str_1 = module_0.compress(str_0)
    str_2 = ";N%'k,iWu9]\x0c'2/6 )"
    str_3 = '4[}'
    str_4 = module_0.snake_case_to_camel(str_2, str_3)
    str_5 = module_0.shuffle(str_3)
    roman_numbers_0 = module_0.__RomanNumbers()
    bool_0 = module_0.booleanize(str_3)
    str_6 = module_0.slugify(str_4)
    str_7 = module_0.prettify(str_5)
    str_8 = module_0.strip_html(str_3)
    int_0 = 3999
    str_9 = module_0.roman_encode(int_0)
    int_1 = module_0.roman_decode(str_9)

def test_case_9():
    str_0 = '((?<=\\S)\\+(?=\\S)|(?<=\\S)\\+\\s|\\s\\+(?=\\S)|(?<=\\S)-(?=\\S)|(?<=\\S)-\\s|\\s-(?=\\S)|(?<=\\S)/(?=\\S)|(?<=\\S)/\\s|\\s/(?=\\S)|(?<=\\S)\\*(?=\\S)|(?<=\\S)\\*\\s|\\s\\*(?=\\S)|(?<=\\S)=(?=\\S)|(?<=\\S)=\\s|\\s=(?=\\S)|\\s"[^"]+"(?=[^\\s?.:!,;])|(?<=\\S)"[^"]+"\\s|(?<=\\S)"[^"]+"(?=[^\\s?.:!,;])|\\s\\([^)]+\\)(?=[^\\s?.:!,;])|(?<=\\S)\\([^)]+\\)\\s|(?<=\\S)(\\([^)]+\\))(?=[^\\s?.:!,;]))'
    str_1 = "EN%'k,iWu9]\x0c'2/6 )"
    str_2 = module_0.snake_case_to_camel(str_1, str_0)
    str_3 = 'O`Q<w'
    str_4 = module_0.shuffle(str_1)
    str_5 = module_0.strip_html(str_3)
    str_6 = '795Q#tXw6\r}'
    str_7 = module_0.prettify(str_6)
    int_0 = 2894
    str_8 = module_0.roman_encode(int_0)
    str_9 = module_0.asciify(str_8)

def test_case_10():
    str_0 = "\n            Hello,     my name is     Stefano...\n            I'm 25 years    old and\n            I'm a student   at the\n             university.\n             my email is\n            stefano@email.it\n            and my website is http://www.stefano.it\n            "
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()

def test_case_11():
    str_0 = '((?<=\\S)\\+(?=\\S)|(?<=\\S)\\+\\s|\\s\\+(?=\\S)|(?<=\\S)-(?=\\S)|(?<=\\S)-\\s|\\s-(?=\\S)|(?<=\\S)/(?=\\S)|(?<=\\S)/\\s|\\s/(?=\\S)|(?<=\\S)\\*(?=\\S)|(?<=\\S)\\*\\s|\\s\\*(?=\\S)|(?<=\\S)=(?=\\S)|(?<=\\S)=\\s|\\s=(?=\\S)|\\s"[^"]+"(?=[^\\s?.:!,;])|(?<=\\S)"[^"]+"\\s|(?<=\\S)"[^"]+"(?=[^\\s?.:!,;])|\\s\\([^)]+\\)(?=[^\\s?.:!,;])|(?<=\\S)\\([^)]+\\)\\s|(?<=\\S)(\\([^)]+\\))(?=[^\\s?.:!,;]))'
    str_1 = module_0.compress(str_0)
    int_0 = 2855
    str_2 = "EN%'k,iWu9]\x0c'2/6 )"
    str_3 = '4[}'
    str_4 = module_0.snake_case_to_camel(str_2, str_3)
    str_5 = 'O`Q<iw'
    str_6 = module_0.strip_margin(str_5)
    str_7 = '\t]Ab?_0DbtAg!P'
    str_8 = module_0.strip_html(str_7)
    str_9 = module_0.prettify(str_6)
    str_10 = module_0.roman_encode(int_0)

def test_case_12():
    str_0 = 'ThisIsACamelStringTest'
    var_0 = module_0.camel_case_to_snake(str_0)
    str_1 = ' '
    str_2 = module_0.snake_case_to_camel(str_1)
    str_3 = 'is_this_a_s7akb'
    str_4 = module_0.snake_case_to_camel(str_3, str_2)
    str_5 = module_0.snake_case_to_camel(str_1)