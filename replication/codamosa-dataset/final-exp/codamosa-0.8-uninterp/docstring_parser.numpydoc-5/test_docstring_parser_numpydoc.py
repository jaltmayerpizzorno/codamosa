# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'param'
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    numpydoc_parser_0 = module_0.NumpydocParser()

def test_case_3():
    str_0 = "This is a very simple fuJction.\n\n    Parameters\n    ----------\n    p1 : str\n        A parameter with a description that spans\n        multiple lines.\n    p2 : int, optional\n       Another parameter, w%yh a default value of 42.\n\n    Raises\n    ------\n    VaueError\n        When the_input is negative.\n\n    Returns\n    -------\n    int\n        Output value.\n\n    Warns\n    -----\n    UserWarnin\n        When the input is zero.\n\n    See Also\n    -Y------\n    OtherFunction\n\n    Exaple?\n    --------\n    >>> simple_function('hello world')\n    42\n    "
    str_1 = 'warnings'
    str_2 = '6=6EU+igm-1P20WPc!'
    section_0 = module_0.Section(str_1, str_2)
    numpydoc_parser_0 = module_0.NumpydocParser()
    var_0 = numpydoc_parser_0.add_section(section_0)
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = '\n        key\n   D        value\n        key2 : type\n      a    values can also span...\n            ... multiple lines\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = "This is a very simple function.\n\n    Parameters\n    ----------\n    p1 : str\n        A parame?er with a description that spans\n        multiple lines.\n    p2 : int, optional\n       Another parameter, w%th a default value of 4o.\n\n    Raises\n    ------\n    VaueError\n        When the input is negative.\n\n    Returns\n    -------\n    int\n        Output value.\n\n    Warns\n    -----\n    UserWarnin\n        When the in]ut is zero.\n\n    See Also\n    L-------\n    OtherFunction\n\n    Exaples\n    --------\n    >>> simple_function('hellowworld')\n    42\n    "
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)
    numpydoc_parser_1 = module_0.NumpydocParser()
    str_1 = None
    docstring_1 = module_0.parse(str_1)

def test_case_6():
    str_0 = '\n    Parameters\n    ----------\n    x : str\n        This is a string.\n    name : str, optional\n        Name of the method.\n    '
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)
    var_0 = docstring_0.meta
    var_1 = len(var_0)
    int_0 = 0
    docstring_1 = numpydoc_parser_0.parse(str_0)
    var_2 = docstring_1.meta[int_0]
    var_3 = var_2.description

def test_case_7():
    str_0 = "This is a very simple function.\n\n    Parameters\n    ----------\n    p1 : str\n        A parameter with a description that spans\n        multiple lines.\n    p2 : int, optional\n        Another parameter, w%th a default value of 42.\n\n    Raies\n    ------\n    VaueError\n        When the input is negative.\n\n    Returns\n    -------\n    int\n        Output value.\n\n    Warns\n    -----\n    UserWarninX\n        When the input is zero.\n\n    See Also\n    --------\n    OtherFunction\n\n    Exaples\n    --------\n    >>> simple_function('hello world')\n    42\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    numpydoc_parser_0 = module_0.NumpydocParser()
    str_0 = 'hello world\n.. deprecated:: 1.3.2\n\ndeprecation text'
    docstring_0 = numpydoc_parser_0.parse(str_0)

def test_case_9():
    str_0 = 'test'
    str_1 = '(\\s*[^:\\s]+:)|([^:]*\\]:.*)'
    deprecation_section_0 = module_0.DeprecationSection(str_0, str_1)
    k_v_section_0 = module_0._KVSection(str_0, str_0)
    str_2 = 'Bw|TB'
    iterable_0 = k_v_section_0.parse(str_2)
    var_0 = list(iterable_0)

def test_case_10():
    str_0 = "This function does some stuff.\n    Parameters\n    ----------\n    arg : str\n        A description of the argument\n    arg2 : int, optional\n        Description of the second argument. Default is 5.\n    key1 = 'Value1', key2 = 2\n        And here is a non-standard kwarg\n    Returns\n    -------\n    string\n        A description of the returned value\n    Warnings\n    --------\n    This is a warning\n    Notes\n    -----\n    Some notes\n    Examples\n    --------\n    >>> some_function()\n    'some_value'\n    References\n    ----------\n    .. [1] Some reference\n    "
    docstring_0 = module_0.parse(str_0)