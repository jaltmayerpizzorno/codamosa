# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    str_0 = 'Fm^@jZ<6?("#'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_1():
    bool_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)

def test_case_2():
    int_0 = 62
    str_0 = 'T|4X2\t=\x0c'
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_3():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    list_0 = [str_0]
    int_0 = module_0.len_without_ansi(list_0)
    str_1 = ' i${hsBu4y'
    str_2 = '9 !A&'
    str_3 = ';]tj};8{e8NCS0oY'
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_2, str_3, bool_0, bool_0)
    str_4 = ansi_text_wrapper_0.fill(str_1)
    bool_1 = False
    str_5 = 'I'
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, bool_1, placeholder=str_5)

def test_case_4():
    str_0 = '\x0bERd/;H'
    int_0 = -16
    bool_0 = False
    int_1 = 67
    bool_1 = False
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, str_0, bool_0, bool_0, bool_1, bool_0, max_lines=int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)
    str_1 = "Only the 'minor' or 'patch' parts of the version number can get a prerelease bump."
    str_2 = ansi_text_wrapper_0.fill(str_1)
    list_1 = ansi_text_wrapper_0.wrap(str_2)

def test_case_5():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_6():
    str_0 = 'N>t<g\x0c-b*~_'
    int_0 = 62
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_7():
    str_0 = '\x0bERd/;H'
    bool_0 = True
    int_0 = -16
    bool_1 = False
    int_1 = 67
    str_1 = ''
    int_2 = 933
    bool_2 = False
    bool_3 = True
    bool_4 = False
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_2, str_0, bool_0, bool_2, bool_3, bool_4, max_lines=int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_1)
    str_2 = "f1vy&A<GQ\nk' ICvwta"
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_1, str_2, max_lines=int_1)
    str_3 = ansi_text_wrapper_1.fill(str_0)
    bool_5 = False
    ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_0, int_0)
    ansi_text_wrapper_3 = module_0.AnsiTextWrapper(bool_1, bool_5, bool_1)
    str_4 = '$I}?r\x0csR\x0cKt\n['
    list_1 = ansi_text_wrapper_0.wrap(str_4)

def test_case_8():
    str_0 = '\x1b[38;5;20Amfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_9():
    str_0 = '\x0bERd/;H'
    bool_0 = True
    int_0 = -61
    str_1 = 'Yox-H\x0b~c^\\OLp^5G,rHE'
    int_1 = module_0.len_without_ansi(str_1)
    bool_1 = False
    bool_2 = False
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, str_0, bool_0, bool_1, bool_2, bool_0, max_lines=int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)
    str_2 = "Only the 'minor' or 'patch' parts of the version number can get a prerelease bump."
    str_3 = ansi_text_wrapper_0.fill(str_2)
    bool_3 = False
    str_4 = ansi_text_wrapper_0.fill(str_3)
    list_1 = ansi_text_wrapper_0.wrap(str_4)
    str_5 = "Check that given ``obj`` acts like a list and is iterable.\n\n    List-like objects are instances of:\n\n    - :obj:`UserList <collections.UserList>`\n    - :obj:`Iterator <collections.abc.Iterator>`\n    - :obj:`KeysView <collections.abc.KeysView>`\n    - :obj:`ValuesView <collections.abc.ValuesView>`\n    - :obj:`deque <collections.deque>`\n    - :obj:`frozenset`\n    - :obj:`list`\n    - :obj:`set`\n    - :obj:`tuple`\n\n    List-like objects are **NOT** instances of:\n\n    - :obj:`None`\n    - :obj:`bool`\n    - :obj:`bytes`\n    - :obj:`ChainMap <collections.ChainMap>`\n    - :obj:`Counter <collections.Counter>`\n    - :obj:`OrderedDict <collections.OrderedDict>`\n    - :obj:`UserDict <collections.UserDict>`\n    - :obj:`UserString <collections.UserString>`\n    - :obj:`defaultdict <collections.defaultdict>`\n    - :obj:`Decimal <decimal.Decimal>`\n    - :obj:`dict`\n    - :obj:`float`\n    - :obj:`int`\n    - :obj:`str`\n    - etc...\n\n    Args:\n        obj (:obj:`Any <typing.Any>`): The object to check.\n\n    :rtype:\n        :obj:`bool`\n\n        * :obj:`True` if the given ``obj`` is list-like; :\n        * :obj:`False` otherwise.\n\n    Examples:\n        >>> from flutils.objutils import is_list_like\n        >>> is_list_like([1, 2, 3])\n        True\n        >>> is_list_like(reversed([1, 2, 4]))\n        True\n        >>> is_list_like('hello')\n        False\n        >>> is_list_like(sorted('hello'))\n        True\n    "
    str_6 = ansi_text_wrapper_0.fill(str_5)
    bool_4 = False
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(str_1, bool_3, bool_4, int_1, placeholder=str_6)
    str_7 = ansi_text_wrapper_0.fill(str_6)