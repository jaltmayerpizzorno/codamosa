# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0

def test_case_0():
    try:
        str_0 = "Initialize self.\n\n        :param args: list of arguments. The exact content of this variable is\n                     dependent on the kind of docstring; it's used to distinguish between\n                     custom docstring meta information items.\n        :param description: associated docstring description.\n        "
        str_1 = 'B\x0bUc\x0cNIY)T\rX;LUP'
        deprecation_section_0 = module_0.DeprecationSection(str_0, str_1)
        str_2 = '`1'
        str_3 = 'mk]W{=*?u'
        str_4 = '5+>v\tkB{='
        section_0 = module_0.Section(str_3, str_4)
        iterable_0 = section_0.parse(str_2)
        numpydoc_parser_0 = module_0.NumpydocParser(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '2ZMx&D'
        str_1 = 'Jfb@C6,X\x0bLkhwbNsGVA\\'
        str_2 = 'uIt'
        str_3 = None
        numpydoc_parser_0 = module_0.NumpydocParser()
        docstring_0 = numpydoc_parser_0.parse(str_3)
        yields_section_0 = module_0.YieldsSection(str_2, str_2)
        str_4 = "dDm;aHy44n|w'L"
        k_v_section_0 = module_0._KVSection(str_1, str_4)
        str_5 = 'E'
        iterable_0 = k_v_section_0.parse(str_5)
        iterable_1 = k_v_section_0.parse(str_0)
        str_6 = '?'
        iterable_2 = k_v_section_0.parse(str_0)
        docstring_1 = module_0.parse(str_6)
        numpydoc_parser_1 = module_0.NumpydocParser(iterable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '%D:?#Kd8RR)++a %,;"('
        section_0 = module_0.Section(str_0, str_0)
        str_1 = "2-f</A@Zg]rS'"
        numpydoc_parser_0 = module_0.NumpydocParser(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '2ZMx&D'
        str_1 = '7_v9P{b!T*'
        str_2 = 'Returns'
        yields_section_0 = module_0.YieldsSection(str_2, str_2)
        k_v_section_0 = module_0._KVSection(str_2, str_1)
        str_3 = "dDm;aHy44n|w'L"
        str_4 = ''
        iterable_0 = k_v_section_0.parse(str_4)
        iterable_1 = k_v_section_0.parse(str_0)
        docstring_0 = module_0.parse(str_2)
        numpydoc_parser_0 = module_0.NumpydocParser(iterable_0)
        str_5 = None
        iterable_2 = k_v_section_0.parse(str_5)
        docstring_1 = numpydoc_parser_0.parse(str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'xC'
        str_1 = 'For sections like returns or yields.'
        section_0 = module_0.Section(str_0, str_1)
        str_2 = 'RNons&Co7&VZ5V'
        str_3 = ''
        str_4 = ' k:g%[si3PSC~I0\x0bl!'
        deprecation_section_0 = module_0.DeprecationSection(str_3, str_4)
        iterable_0 = deprecation_section_0.parse(str_2)
        numpydoc_parser_0 = module_0.NumpydocParser(iterable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'xmples'
        str_1 = '3j[\nP,V!tjrC(,7'
        str_2 = '$'
        str_3 = ':WR'
        yields_section_0 = module_0.YieldsSection(str_0, str_2)
        deprecation_section_0 = module_0.DeprecationSection(str_2, str_3)
        iterable_0 = deprecation_section_0.parse(str_1)
        numpydoc_parser_0 = module_0.NumpydocParser(iterable_0)
    except BaseException:
        pass