# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        str_0 = 'L|9]8ID1ZYxM\r~~C|!C'
        bool_0 = True
        int_0 = 309
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, int_0, max_lines=int_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 't\r/s41nGY2|%\\+EtC^@'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(str_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 15
        str_0 = '6N~!^UOWx^[=['
        bool_0 = False
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, int_0, max_lines=int_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '`^j%i9R/Ot0jy-/'
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_0)
        bool_1 = True
        int_0 = -611
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, max_lines=int_0)
        list_0 = ansi_text_wrapper_1.wrap(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '@a'
        bool_0 = True
        str_1 = '<aXJKCcez,:\\ '
        int_0 = 1317
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        str_2 = ansi_text_wrapper_0.fill(str_1)
        int_1 = -1218
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, int_1, max_lines=int_1)
        list_0 = ansi_text_wrapper_1.wrap(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '_a'
        bool_0 = True
        str_1 = '|g; i"'
        int_0 = 568
        str_2 = '7T]KaR-)N\\BU'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_1, str_2, bool_0, bool_0, int_0, max_lines=int_0)
        str_3 = 'edVq-+5KQ"='
        str_4 = ansi_text_wrapper_0.fill(str_3)
        int_1 = 188
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(placeholder=str_2)
        str_5 = ansi_text_wrapper_0.fill(str_0)
        int_2 = -1260
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_2, str_1, int_2, max_lines=int_1)
        str_6 = '\x0c'
        str_7 = ansi_text_wrapper_0.fill(str_6)
        str_8 = ansi_text_wrapper_2.fill(str_6)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_0 = module_0.len_without_ansi(str_0)
        str_1 = 'sgRD}\n\x0c:c'
        bool_0 = False
        int_1 = 477
        str_2 = 'gy4qgDmz*=kLi7'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(str_1, str_0, bool_0, bool_0, int_1, placeholder=str_2)
        str_3 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass