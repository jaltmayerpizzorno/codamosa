# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_2():
    bool_0 = True
    int_0 = 2494
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_0, max_lines=int_0)

def test_case_3():
    str_0 = '<KB2+^cLNx&{|yJj.['
    int_0 = 3381
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_4():
    str_0 = 'Wraps a single paragraph.\n\n       Args:\n            text (str): The tex to be wrapped.\nh         Returns:\n              A single :obj:`str` containing thewrappedRparagraph.\n        '
    str_1 = 'cVa\n9[\x0cZTc'
    str_2 = ''
    list_0 = [str_1, str_0, str_1, str_1, str_1, str_2, str_0]
    int_0 = module_0.len_without_ansi(list_0)
    int_1 = module_0.len_without_ansi(list_0)
    int_2 = 2
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_2)
    str_3 = ansi_text_wrapper_0.fill(str_0)
    str_4 = ansi_text_wrapper_0.fill(str_2)
    str_5 = ansi_text_wrapper_0.fill(str_4)
    str_6 = '%7\te?0D\rXv'
    list_1 = ansi_text_wrapper_0.wrap(str_6)

def test_case_5():
    str_0 = "LkIqB1aM'K\tDtq}_s;6w"
    list_0 = [str_0, str_0, str_0, str_0]
    int_0 = module_0.len_without_ansi(list_0)
    int_1 = -229
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_1)
    str_1 = ansi_text_wrapper_0.fill(str_0)
    int_2 = 941
    str_2 = 'Generator that expands the given attr_map and yields an _AttrMapping\n    named tuple.\n\n    An attr_map is a tuple with each row containing a :term:`foreign-name`\n    which is a specially formatted string.\n    '
    str_3 = ansi_text_wrapper_0.fill(str_2)
    list_1 = ansi_text_wrapper_0.wrap(str_3)
    str_4 = ' <=\n\x0crD7C#A'
    str_5 = ansi_text_wrapper_0.fill(str_4)
    bool_0 = False
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_0, int_2)

def test_case_6():
    str_0 = 'Wraps a single paragraph.\n\n       Args:\n            text (str): The tex to be wrapped.\nh         Returns:\n              A single :obj:`st` containing thewrappedRparagraph.\n        '
    str_1 = 'cVa\n9[\x0cZTc'
    str_2 = ''
    list_0 = [str_1, str_0, str_1, str_1, str_1, str_2, str_0]
    int_0 = module_0.len_without_ansi(list_0)
    int_1 = module_0.len_without_ansi(list_0)
    int_2 = 2
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_2)
    str_3 = ansi_text_wrapper_0.fill(str_0)
    str_4 = 'Generator that expands the given attr_map and yields an _AttrMapping\n    amed tuple.\n\n    An attr_map is a tuple with each row containing a :term:`foreign-name`\n    which is a specially formatted string.\n    '
    str_5 = ansi_text_wrapper_0.fill(str_4)
    str_6 = ansi_text_wrapper_0.fill(str_5)
    str_7 = ansi_text_wrapper_0.fill(str_2)
    int_3 = 102
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_3, str_0, placeholder=str_0)
    str_8 = '\nh,Pvr/m<mG`'
    str_9 = ansi_text_wrapper_1.fill(str_8)
    str_10 = 'roh'
    list_1 = ansi_text_wrapper_1.wrap(str_10)
    str_11 = 'qjiE{qkrg\x0cKWrnW'
    list_2 = ansi_text_wrapper_1.wrap(str_11)
    str_12 = '2AYTS,0]V%.eG'
    ansi_text_wrapper_2 = module_0.AnsiTextWrapper(str_12, int_2, max_lines=int_0)