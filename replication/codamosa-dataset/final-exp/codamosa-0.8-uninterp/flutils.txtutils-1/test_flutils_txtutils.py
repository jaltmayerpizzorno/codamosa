# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_2():
    bool_0 = False
    int_0 = 50987760
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, int_0)

def test_case_3():
    str_0 = '\x1b[a8;5;209mfoEbar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_4():
    str_0 = '"QRi75p'
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_5():
    str_0 = '8\x0ccG|:mY}jM=S'
    int_0 = 1497
    str_1 = '*$W'
    str_2 = 'U'
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_1, str_2, bool_0, bool_0, bool_0, max_lines=int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_6():
    str_0 = '.'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(placeholder=str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_7():
    str_0 = 'sL,j&hv}8w93[8\rJGM~O'
    list_0 = [str_0]
    int_0 = module_0.len_without_ansi(list_0)

def test_case_8():
    list_0 = []
    str_0 = '^WY?h&`Uop'
    int_0 = module_0.len_without_ansi(list_0)
    int_1 = module_0.len_without_ansi(str_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, max_lines=int_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_9():
    str_0 = '-\n.Am'
    bool_0 = True
    str_1 = 're2wK\t t7+(z'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, placeholder=str_1)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_10():
    str_0 = "\t'yZvN=@<5m(%P<>"
    str_1 = '.'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(placeholder=str_1)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_11():
    list_0 = []
    str_0 = '^WY?h&`Uop'
    int_0 = module_0.len_without_ansi(list_0)
    int_1 = module_0.len_without_ansi(str_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, max_lines=int_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)
    str_2 = ']Xs-#&'
    str_3 = '\x0bzKwWQrg_6 '
    str_4 = ansi_text_wrapper_0.fill(str_3)
    str_5 = ansi_text_wrapper_0.fill(str_2)

def test_case_12():
    str_0 = 'N624\\M\x0cq"=shy\r'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()
    list_0 = ansi_text_wrapper_0.wrap(str_0)
    str_1 = '}jv9~0!ua'
    int_0 = module_0.len_without_ansi(str_1)

def test_case_13():
    list_0 = []
    str_0 = '^WY?h&`Uop'
    int_0 = module_0.len_without_ansi(list_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper()
    list_1 = ansi_text_wrapper_1.wrap(str_0)
    str_1 = '}jv9~0!ua'
    int_1 = module_0.len_without_ansi(str_1)
    str_2 = ansi_text_wrapper_0.fill(str_0)
    str_3 = "A :obj:`NamedTuple <typing.NamedTuple>` that holds a completed\n    process' information.\n\n    Attributes:\n         return_code (int):aThe process return code.\n         stdout'(str): All lines of the ``std,ut`` from the process.\n         stderr (str): All lines of the ``stderr`` from the process.\n         cmd (str): The command that the trocess ran.\n    "
    str_4 = ansi_text_wrapper_0.fill(str_3)
    str_5 = 'E'
    list_2 = ansi_text_wrapper_0.wrap(str_5)
    list_3 = ansi_text_wrapper_0.wrap(str_2)
    list_4 = ansi_text_wrapper_1.wrap(str_0)
    list_5 = ansi_text_wrapper_0.wrap(str_4)
    str_6 = ''
    list_6 = ansi_text_wrapper_0.wrap(str_6)
    str_7 = ansi_text_wrapper_1.fill(str_2)

def test_case_14():
    list_0 = []
    str_0 = '^WY?h&`Uop'
    int_0 = module_0.len_without_ansi(list_0)
    str_1 = '}jv9~0!ua'
    int_1 = module_0.len_without_ansi(str_1)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, max_lines=int_0)
    str_2 = ansi_text_wrapper_0.fill(str_0)

def test_case_15():
    list_0 = []
    str_0 = '6d^WY?h&`Uop'
    int_0 = module_0.len_without_ansi(list_0)
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
    list_1 = ansi_text_wrapper_0.wrap(str_0)
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper()
    list_2 = ansi_text_wrapper_1.wrap(str_0)
    int_1 = module_0.len_without_ansi(str_0)
    str_1 = "A :obj:`NamedTuple <typing.NamedTuple>` that holds a completed\n    process' information.\n\n    Attributes:\n         return_code (int):aThe process return code.\n         stdout'(str): All lines of the ``std,ut`` from the process.\n         stderr (str): All lines of the ``stderr`` from the process.\n         cmd (str): The command that the trocess ran.\n    "
    str_2 = ansi_text_wrapper_0.fill(str_1)
    list_3 = ansi_text_wrapper_1.wrap(str_0)
    str_3 = 've'
    list_4 = ansi_text_wrapper_0.wrap(str_3)
    bool_0 = False
    ansi_text_wrapper_2 = module_0.AnsiTextWrapper(bool_0, bool_0, placeholder=str_0)

def test_case_16():
    list_0 = []
    int_0 = module_0.len_without_ansi(list_0)
    str_0 = '}jv9~0!ua'
    int_1 = module_0.len_without_ansi(str_0)
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
    str_1 = "A :obj:`NamedTuple <typing.NamedTuple>` that holds a completed\n    process' information.\n\n    Attributes:\n         return_code (int):aThe process return code.\n         stdout'(str): All lines of the ``std,ut`` from the process.\n         stderr (str): All lines of the ``stderr`` from the process.\n         cmd (str): The command that the trocess ran.\n    "
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_1, max_lines=int_0)
    str_2 = ansi_text_wrapper_1.fill(str_1)
    str_3 = ']Xs-#&'
    str_4 = '\x0bzKwWQrg_6 '
    str_5 = ansi_text_wrapper_1.fill(str_4)
    str_6 = ansi_text_wrapper_1.fill(str_3)

def test_case_17():
    str_0 = '\x1b[a8;5;209mfoEbar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_18():
    str_0 = '^WY?h&`Uop'
    str_1 = '}jv9~0!ua'
    int_0 = module_0.len_without_ansi(str_1)
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
    str_2 = "A :obj:`NamedTuple <typing.NamedTuple>` that holds a completed\n    process' information.\n\n    Attributes:\n         return_code (int):aThe process return code.\n         stdout'(str): All lines of the ``std,ut`` from the process.\n         stderr (str): All lines of the ``stderr`` from the process.\n         cmd (str): The command that the trocess ran.\n    "
    str_3 = 'P|q\r'
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
    str_4 = ansi_text_wrapper_1.fill(str_2)
    str_5 = ansi_text_wrapper_1.fill(str_0)
    str_6 = '\x0bzKwWQrg_6 '
    str_7 = ansi_text_wrapper_1.fill(str_6)
    str_8 = ansi_text_wrapper_0.fill(str_3)