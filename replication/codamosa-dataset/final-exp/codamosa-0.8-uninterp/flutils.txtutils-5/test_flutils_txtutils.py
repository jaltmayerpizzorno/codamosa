# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    str_0 = '?;y('
    int_0 = module_0.len_without_ansi(str_0)

def test_case_1():
    optional_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=optional_0)

def test_case_2():
    str_0 = '?;y('
    int_0 = module_0.len_without_ansi(str_0)

def test_case_3():
    str_0 = ' is not a proper bas64 character string: '
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_4():
    int_0 = 5
    str_0 = 'hom'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_1)
    str_2 = ansi_text_wrapper_0.fill(str_1)

def test_case_5():
    str_0 = 'Xp](\t,El}J.?Mh'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(placeholder=str_0)
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_6():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_7():
    str_0 = '\n\n'
    int_0 = 5
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_0)
    str_1 = 'convert_escaped_utf8_literal'
    str_2 = ansi_text_wrapper_0.fill(str_1)
    str_3 = ansi_text_wrapper_0.fill(str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_3)
    str_4 = ansi_text_wrapper_0.fill(str_2)
    str_5 = ansi_text_wrapper_0.fill(str_1)
    str_6 = ansi_text_wrapper_0.fill(str_3)

def test_case_8():
    int_0 = 5
    str_0 = 'hom'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_0)
    str_1 = 'convert_esHaped_utf8Zliteral'
    str_2 = ansi_text_wrapper_0.fill(str_1)
    str_3 = ansi_text_wrapper_0.fill(str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_3)
    str_4 = ansi_text_wrapper_0.fill(str_2)

def test_case_9():
    str_0 = '\n\n'
    int_0 = 5
    str_1 = 'so'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
    str_2 = 'u\ti./ *U?Bg~(-EoWLy'
    str_3 = ansi_text_wrapper_0.fill(str_2)
    str_4 = '__additional_attrs__ must be a dict in %r'
    list_0 = ansi_text_wrapper_0.wrap(str_4)
    str_5 = ansi_text_wrapper_0.fill(str_0)
    str_6 = 'I!/6{\\BGW7a7d@<jHf*'
    list_1 = ansi_text_wrapper_0.wrap(str_6)
    str_7 = 'QkMPFv}uuO,gE|MoH\t'
    list_2 = ansi_text_wrapper_0.wrap(str_7)
    str_8 = ansi_text_wrapper_0.fill(str_2)

def test_case_10():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    str_1 = "f'aHv :!%3b`{"
    list_0 = [str_1]
    str_2 = 'EBJJ4nE'
    int_0 = 279
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0)
    list_1 = ansi_text_wrapper_0.wrap(str_0)
    int_1 = 2837
    str_3 = '56Zj\nty'
    bool_0 = True
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_1, str_3, bool_0)
    list_2 = ansi_text_wrapper_1.wrap(str_2)
    dict_0 = {str_0: list_0}
    int_2 = module_0.len_without_ansi(dict_0)

def test_case_11():
    str_0 = '\x1b[38;5;0&foobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_12():
    str_0 = '\n\n'
    int_0 = 5
    str_1 = 'ho'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
    str_2 = 'u\ti./ *U?Bg~(-EoWLy'
    str_3 = ansi_text_wrapper_0.fill(str_2)
    str_4 = '__additional_attrs__ must be a dict in %r'
    list_0 = ansi_text_wrapper_0.wrap(str_4)
    str_5 = ansi_text_wrapper_0.fill(str_0)
    list_1 = []
    int_1 = module_0.len_without_ansi(list_1)
    str_6 = 'o\t4`r"-G^}WUO'
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, max_lines=int_1)
    str_7 = ansi_text_wrapper_1.fill(str_6)