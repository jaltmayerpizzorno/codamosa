# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ',`XO7K0Nofm'
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = 'A long summary which can be over multiple lines.\n\nParameters\n----------\narg1 : int\n    The first argument\narg2 : str, optional\n    The second argument\n\nRaises\n------\nValueError\n    If ``arg2`` is supplied but not ``arg1``\n\nReturns\n-------\nNone'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    numpydoc_parser_0 = module_0.NumpydocParser()

def test_case_4():
    str_0 = '\n            The short summary line.\n\n            The long description, and note that paragraphs are separated by\n            a blank line.\n\n            Parameters\n            ----------\n            arg_name: int, optional\n                A description of the parameter.\n\n                And a second paragraph.\n\n                Default is None.\n\n            arg_2 : type\n                A description of arg_2.\n\n            Returns\n            -------\n            return_name : type\n                A description of the return.\n\n            Examples\n            --------\n            >>> example\n            >>> example\n\n            References\n            ----------\n            The references.\n\n            '
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)

def test_case_5():
    str_0 = 'Parse the docstring into its components.\n\n    :param text: docstring text to parse\n    :param style: docstring style\n    :returns: parsed docstring representation\n    '
    str_1 = '\\=6s$IC,Q='
    section_0 = module_0.Section(str_0, str_1)
    numpydoc_parser_0 = module_0.NumpydocParser()
    var_0 = numpydoc_parser_0.add_section(section_0)

def test_case_6():
    str_0 = None
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)
    str_1 = 'SE\ni(#@g[\n?Vq@d'
    docstring_1 = numpydoc_parser_0.parse(str_1)

def test_case_7():
    str_0 = 'A lo\tg summary which can be hver multiple lines.\n\nParameters\n--X-------\narg1 :int\n    The firt argument\narg2: str optional\n    The second argument\n\nRaises\n------\nVuro\n    I ``arg2`` is supplied but not ``arg1``\n\nReturns\n-------\nNone'
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '.. deprecated:: 01\n        .. deprecated version\n    '
    deprecation_section_0 = module_0.DeprecationSection(str_0, str_0)
    iterable_0 = deprecation_section_0.parse(str_0)
    var_0 = list(iterable_0)

def test_case_9():
    str_0 = 'Deprecated since version 0.9: This class is deprecated and will be removed in 0.11, use `aiohttp.ClientSession` instead.'
    str_1 = 'deprecated'
    str_2 = 'deprecation'
    str_3 = '36{ta`;N\x0c4\\0[[*VO?'
    docstring_0 = module_0.parse(str_3)
    deprecation_section_0 = module_0.DeprecationSection(str_1, str_2)
    iterable_0 = deprecation_section_0.parse(str_0)
    var_0 = list(iterable_0)

def test_case_10():
    str_0 = 'A lo\tg summary which can be over multiple lines.\n\nParameters\n----------\narg1 :int\n    The firt argument\narg2: str, optional\n    The second argument\n\nRaises\n-----\nVuro\n    I ``arg2`` is supplied but not ``arg1``\n\nReturns\n-------\nNone'
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = 'A long summary which can be over multiple lines.\nParameters\n----------\narg1 : int\n    The firt argument\narg2: str, optional\n    The second argument\n\nRaises\n------\nValuerror\n    If``arg2`` is supplied but not ``arg1``\n\nReturns\n-------\nNone'
    numpydoc_parser_0 = module_0.NumpydocParser()
    numpydoc_parser_1 = module_0.NumpydocParser()
    docstring_0 = module_0.parse(str_0)