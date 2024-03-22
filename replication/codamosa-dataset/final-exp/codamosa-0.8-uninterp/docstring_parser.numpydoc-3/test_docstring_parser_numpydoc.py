# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "^jj'oC-2\x0b;!~uy"
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    numpydoc_parser_0 = module_0.NumpydocParser()

def test_case_3():
    str_0 = 'Yield'
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)
    section_0 = module_0.Section(str_0, str_0)
    var_0 = numpydoc_parser_0.add_section(section_0)

def test_case_4():
    str_0 = 'Method to convert response to array\n    Parameters\n    ----------\n    data: sequence\n        to be converted\n    Returns\n    -------\n    ndarray\n        length of data\n    Raises\n    ------\n    ValueError\n        For zero length input.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = None
    section_0 = module_0.Section(str_0, str_0)
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = '\n        Short description.\n\n        Docstrings may extend over multiple lines. Sections start with a header\n        and are followed by a body, which are divided by a single newline.\n        Everything is optional, including having multiple paragraphs.\n\n        Parameters\n        ----------\n        arg1 : int\n            The first argument.\n\n        arg2 : str\n            The second argument.\n\n        Returns\n        -------\n        int\n            The return value.\n        '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = '\n    Arguments\n    ---------\n    arg1 : int\n        The first argument.\n    arg2 : str\n        The second argument.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '.. deprecated:: 1.0\n   Use deprecation section instead.\n'
    int_0 = 0
    str_1 = 'deprecated'
    deprecation_section_0 = module_0.DeprecationSection(str_1, str_1)
    iterable_0 = deprecation_section_0.parse(str_0)
    var_0 = list(iterable_0)[int_0]
    var_1 = var_0.description

def test_case_9():
    var_0 = None
    k_v_section_0 = module_0._KVSection(var_0, var_0)
    str_0 = ''
    iterable_0 = k_v_section_0.parse(str_0)
    var_1 = list(iterable_0)
    str_1 = 'key'
    iterable_1 = k_v_section_0.parse(str_1)
    var_2 = list(iterable_1)
    str_2 = 'key\n    value'
    iterable_2 = k_v_section_0.parse(str_2)
    var_3 = list(iterable_2)
    iterable_3 = k_v_section_0.parse(str_0)
    var_4 = list(iterable_3)
    str_3 = 'key 1\n    value 1\nkey 2'
    iterable_4 = k_v_section_0.parse(str_3)
    var_5 = list(iterable_4)

def test_case_10():
    str_0 = 'Method to convert response to array\n    Parameters\n    ----------\n    data: sequence\n       to be converted\n    Returns\n    ------\n    ndarray\n        length of data\n    Raises\n    ------\n    VleErro\n       For zero length input.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = 'One line summary.\n    Longer description.\n    Parameters\n    ----------\n    param1 : int\n        The first parameter.\n    param2 : str\n        The second parameter.\n    param3 : {\'hi\', \'lo\'}, optional\n        The third parameter.  Defaults to \'hi\'.\n    Returns\n    -------\n    description\n        description\n    """\n    '
    numpydoc_parser_0 = module_0.NumpydocParser()
    docstring_0 = numpydoc_parser_0.parse(str_0)
    var_0 = docstring_0.meta