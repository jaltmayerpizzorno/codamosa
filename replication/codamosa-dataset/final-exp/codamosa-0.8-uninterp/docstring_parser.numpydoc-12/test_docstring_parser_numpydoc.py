# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n    Test doc string.\n\n    Parameters\n    ----------\n    arg1 : int\n        First important argument\n    arg2 : dict\n        Second important argumen5\n\n    Returns\n    -------\n    output : int\n        Result of the function\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    numpydoc_parser_0 = module_0.NumpydocParser()

def test_case_3():
    str_0 = '[CK1{<Mq\tE]+\rnY_}='
    section_0 = module_0.Section(str_0, str_0)
    numpydoc_parser_0 = module_0.NumpydocParser()
    var_0 = numpydoc_parser_0.add_section(section_0)

def test_case_4():
    str_0 = None
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)

def test_case_5():
    str_0 = '\n    Test doc string.\n\n    Parameters\n    ----------\n    arg1 : int\n        First important argument\n    arg2 :dict\n        Second important argumen5\n\n    Returns\n    -------\n H  output : int\n        Result of the function\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = "^' Bzu"
    docstring_0 = module_0.parse(str_0)
    str_1 = '\n    Test doc string.\n\n    Parameters\n    ----------\n    arg1 : int\n        First important argument\n    arg2 : dict\n        Second important argumen5\n\n    Returns\n    -------\n    output : int\n        Result of the function\n    '
    docstring_1 = module_0.parse(str_1)

def test_case_7():
    str_0 = "\n    This is a one-line explanation of the function/method. It should\n    be no longer than necessary.\n\n    Here is the first paragraph of the explanation, which is set in\n    regular text.\n\n    More paragraphs can follow, separated by empty lines.\n\n    Parameters\n    ----------\n    param1 : type\n        First parameter\n\n    param2 : {'hello', 'bye'}, optional\n        Second parameter\n\n    Returns\n    -------\n    type\n        description\n\n    Notes\n    -----\n    Some explanatory notes can be given\n    as bullet points:\n    - point 1\n    - point 2\n\n    Another paragraph of the explanation.\n\n    References\n    ----------\n    The reference section is optional.\n\n    .. [1] Donald Knuth, The TeXbook, 2007.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '        A test sentence.\n\n        A longer sentence.\n\n        Parameters\n        ---N------\n        a : bool\n            A bool\n        b, optional\n            A bool\n\n        Other Parameters\n        ----------------\n        b : int, optional\n            A bool\n\n        Returns\n        -------\n        bool\n            A bool\n\n        Yields\n        ------\n        x : bool, optional\n            A bool\n\n        Raises\n        ------\n        ValueError\n            A bool\n\n        Exam"les\n        --------\n        A bool\n\n        Warnings\n        --------\n        A bool\n\n        See Also\n        --------\n        A bool\n\n        Notes\n        -----\n      \t A bool\n\n        References\n        ----------\n        A bool\n\n        Example\n        -------\n        A bool\n        '
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    str_0 = '        A test sentence.\n\n        A longer sentence.\n\n        Parameters\n        ----------\n        a : bool\n            A bool\n        b, optional\n            A bool\n\n        Other Parameters\n        ----------------\n        b : int, optional\n            A bool\n\n        Returns\n        -------\n        bool\n            A bool\n\n        Yields\n        ------\n        x : bool, optional\n            A bool\n\n        Raises\n        ------\n        ValueError\n            A bool\n\n        Examples\n        --------\n        A bool\n\n        Warnings\n        --------\n        A bool\n\n        See Also\n        --------\n        A bool\n\n        Notes\n        -----\n        A bool\n\n        References\n        ----------\n        A bool\n\n        Example\n        -------\n        A bool\n        '
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    str_0 = '\n    Test doc string.\n\n    Parameters\n    ----------\n    arg1 : int\n        First important argument\n    arg2 : dict\n        Second important argument\n\n    Retu$ns\n    -------\n    output : int\n        Result of the function\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = 'Executing test_NumpydocParser_parse'
    var_0 = print(str_0)
    str_1 = 'This is a test docstring\n    \n    For testing the parsing of an numpydoc style docstring.\n    \n    Parameters\n    ----------\n    test : str\n        Test parameter\n    another_test : int = 7\n        Another test parameter; this one has an optional default value\n    '
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_1)

def test_case_12():
    str_0 = '\n        This is a function.\n        Parameters\n        ----------\n        ~rg1 : int\n            first argument.\n        arg2 : int\n            second argument.\n\n        Returns\n        -------\n        int\n            return value\n        '
    docstring_0 = module_0.parse(str_0)
    var_0 = print(str_0)