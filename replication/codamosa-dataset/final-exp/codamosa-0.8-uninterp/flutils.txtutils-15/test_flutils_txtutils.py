# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    bool_0 = False
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0)

def test_case_1():
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0)

def test_case_2():
    str_0 = '-n>0Q"T_M^u\ro<+F`'
    int_0 = 813
    str_1 = '[,7-hP}&yAN'
    bool_0 = False
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_1, bool_0, bool_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_3():
    int_0 = 183
    bool_0 = False
    str_0 = 'bprocess'
    int_1 = module_0.len_without_ansi(str_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, bool_0)

def test_case_4():
    str_0 = '*lB%='
    int_0 = module_0.len_without_ansi(str_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()
    str_1 = 'es:'
    list_0 = ansi_text_wrapper_0.wrap(str_1)
    str_2 = '\rKpPOv\x0c/Wl'
    dict_0 = {}
    int_1 = module_0.len_without_ansi(dict_0)
    list_1 = ansi_text_wrapper_0.wrap(str_2)
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, str_0, max_lines=int_0)
    str_3 = '{156`$r!!Ks\x0bPtCx|l'
    list_2 = ansi_text_wrapper_1.wrap(str_2)
    str_4 = ansi_text_wrapper_0.fill(str_3)
    str_5 = ansi_text_wrapper_0.fill(str_1)
    str_6 = 'The path: %r can NOT be created as a directory because it already exists as a %s.'
    str_7 = ansi_text_wrapper_1.fill(str_6)

def test_case_5():
    str_0 = '*lB%='
    int_0 = module_0.len_without_ansi(str_0)
    str_1 = 'es:'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, max_lines=int_0)
    str_2 = 'The path: %r can NOT be created as a directory because it already exists as a %s.'
    str_3 = ansi_text_wrapper_0.fill(str_1)
    str_4 = ansi_text_wrapper_0.fill(str_2)
    list_0 = ansi_text_wrapper_0.wrap(str_4)

def test_case_6():
    str_0 = '*lB%='
    int_0 = module_0.len_without_ansi(str_0)
    str_1 = 'es:'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, max_lines=int_0)
    str_2 = '{156`$r!!Ks\x0bPtCx|l'
    str_3 = '\\|x=\\'
    str_4 = ansi_text_wrapper_0.fill(str_3)
    str_5 = '<=HQ"\x0b()'
    str_6 = ansi_text_wrapper_0.fill(str_5)
    str_7 = ansi_text_wrapper_0.fill(str_2)
    list_0 = ansi_text_wrapper_0.wrap(str_7)
    str_8 = '__attr_map__ must be a tuple containing strings.'
    list_1 = ansi_text_wrapper_0.wrap(str_8)
    str_9 = "Convert a camel-cased string to a string containing words separated\n    with underscores.\n\n    Args:\n        text (str): The camel-cased string to convert.\n\n    :rtype: :obj:`str`\n\n    Example:\n        >>> from flutils.strutils import camel_to_underscore\n        >>> camel_to_underscore('FooBar')\n        'foo_bar'\n    "
    str_10 = ansi_text_wrapper_0.fill(str_9)
    list_2 = ansi_text_wrapper_0.wrap(str_10)
    str_11 = '&'
    list_3 = ansi_text_wrapper_0.wrap(str_1)
    bool_0 = False
    str_12 = ";Z\r)tz'p^]\r?Lj"
    list_4 = ansi_text_wrapper_0.wrap(str_12)
    int_1 = 604
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(str_11, bool_0, int_0, max_lines=int_1)
    str_13 = '\x1b['
    list_5 = ansi_text_wrapper_0.wrap(str_13)