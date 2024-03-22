# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    try:
        str_0 = 'A'
        google_parser_0 = module_0.GoogleParser(str_0)
        str_1 = 'Expected paramenter name.'
        str_2 = 'deprecation'
        docstring_0 = module_0.parse(str_2)
        docstring_1 = module_0.parse(str_2)
        str_3 = 'V,1\r,PYS<%%vd]'
        docstring_2 = module_0.parse(str_3)
        list_0 = [docstring_0, str_1, google_parser_0]
        section_0 = module_0.Section(*list_0)
        var_0 = google_parser_0.add_section(section_0)
        section_1 = module_0.Section()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "shot_descri|tion\n        long_description\n\n        Arguments:\n            arg0: arg0's description.\n            arg1 (int): arg1's description. Defaults to 1.\n        Returns:\n            returns description"
        docstring_0 = module_0.parse(str_0)
        list_0 = [docstring_0, docstring_0, docstring_0]
        google_parser_0 = module_0.GoogleParser(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        bytes_0 = b'{\x17\xad\xa9b\xcd\xf3[.\xc4P(zM\\\xc1n'
        list_0 = [tuple_0, tuple_0, bytes_0, tuple_0]
        list_1 = None
        float_0 = None
        google_parser_0 = module_0.GoogleParser(list_1, float_0)
        section_0 = module_0.Section(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\nStandard Google-style docstring.\n\nArgs:\n    arg_name: description.\n    arg2 (str): description.\n    arg3 (str, optional): description. Defaults to `None`.\nReturns:\n    description of return value\nRaises:\n}   KeyError: When a key error\n    ValueError: When a value error\n    TypeError: When a type error\nExample:\n    eNamples of usage\nAttributes:\n    attr_name: description of attribute\n'
        google_parser_0 = module_0.GoogleParser()
        docstring_0 = google_parser_0.parse(str_0)
    except BaseException:
        pass