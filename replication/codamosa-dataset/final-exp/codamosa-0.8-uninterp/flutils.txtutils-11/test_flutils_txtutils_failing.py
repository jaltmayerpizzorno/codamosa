# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        ansi_text_wrapper_0 = None
        int_0 = module_0.len_without_ansi(ansi_text_wrapper_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '(UD'
        bool_0 = True
        int_0 = -579
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "The given 'cmd', %r, must be of type: str, bytes, list or tuple.  Got: %r"
        bool_0 = False
        bool_1 = False
        int_0 = 388
        str_1 = '\tY6ANJRh68>?Rh`qQHg'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_1, bool_0, int_0, max_lines=int_0, placeholder=str_1)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'0"
        bool_0 = True
        int_0 = 1950
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, int_0)
        str_1 = ''
        str_2 = ansi_text_wrapper_0.fill(str_1)
        str_3 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '-dts"cK:v~\\z>YQT?y\\'
        int_0 = -2569
        str_1 = ''
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_1)
        str_2 = ansi_text_wrapper_0.fill(str_0)
        str_3 = '[_6'
        set_0 = set()
        bool_0 = False
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_1, max_lines=int_0)
        int_1 = module_0.len_without_ansi(set_0)
        str_4 = 'D9{1RZjpT#3hRh2.vNFm'
        list_0 = ansi_text_wrapper_0.wrap(str_4)
        str_5 = 'IQ_$0S!yI['
        int_2 = module_0.len_without_ansi(str_5)
        bool_2 = False
        str_6 = 'A simple callable that simplifies many calls to :obj:`subprocess.run`.\n\n    Args:\n        raise_error (bool, optional): A value of :obj:`True` will raise\n            a :obj:`ChildProcessError` if the process,\n            exits with a non-zero return code. Default: :obj:`True`\n        output_encoding (str, optional): If set, the returned ``stdout``\n            and ``stderr`` will be converted to from bytes to a Python\n            string using this given ``encoding``.  Defaults to:\n            :obj:`None` which will use the value from\n            :obj:`locale.getpreferredencoding` or, if not set, the value\n            from :obj:`sys.getdefaultencoding` will be used. If the given\n            encoding does NOT exist the default will be used.\n        **default_kwargs: Any :obj:`subprocess.Popen` keyword argument.\n\n    Attributes:\n        default_kwargs (:obj:`NamedTuple <typing.NamedTuple>`): The\n            ``default_kwargs`` passed into the constructor which may be\n            passed on to :obj:`subprocess.run`.\n        output_encoding (str): The encoding used to decode the process\n            output\n\n    '
        int_3 = -3390
        str_7 = 'pESww\tuv#\td}JAGb'
        list_1 = ansi_text_wrapper_0.wrap(str_6)
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_3, str_3, str_7, bool_2, bool_2)
        str_8 = ansi_text_wrapper_2.fill(str_6)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_0 = 1342
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, bool_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass