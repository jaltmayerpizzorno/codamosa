# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        str_0 = '\n\\pc5`{U\x0b'
        int_0 = 3716
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, bool_0, bool_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = 76
        str_0 = "f1vy&A<GQ\nk'Cvwta"
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, max_lines=int_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_1, bool_0)
        list_0 = ansi_text_wrapper_1.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
        str_0 = '_literal_utf8'
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1301
        str_0 = ''
        int_1 = 50855936
        bool_0 = True
        str_1 = ':\tMj;[H KkYeC4y/d+/{'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, int_0, max_lines=int_1, placeholder=str_1)
        str_2 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '#XLnduCi=cs%wQF$'
        int_0 = -2586
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        sequence_0 = None
        int_0 = module_0.len_without_ansi(sequence_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_0 = module_0.len_without_ansi(str_0)
        str_1 = '\x1b[38;5;209mfoo\x1b[0mbar\x1b[38;5;209mbaz\x1b[0m'
        bool_0 = True
        int_1 = 2493
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, int_1)
        str_2 = ansi_text_wrapper_0.fill(str_1)
    except BaseException:
        pass