# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        str_0 = '2fN\\PK \\GU|b{mRx'
        bool_0 = False
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        sequence_0 = None
        int_0 = module_0.len_without_ansi(sequence_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'KJQ.w-tmcI'
        str_1 = 'bsn5e6p\tPZ1O+v&]Kbc'
        bool_0 = True
        bool_1 = False
        bool_2 = False
        int_0 = -1104
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_1, bool_0, bool_2, bool_2, max_lines=int_0, placeholder=str_0)
        list_0 = ansi_text_wrapper_0.wrap(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        str_0 = '\n\n'
        int_0 = 5
        str_1 = 'hom'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
        str_2 = '__additional_attrs__ must be a dict in %r'
        list_0 = ansi_text_wrapper_0.wrap(str_2)
        str_3 = 'f@EQv PQ&hHybQ\r}h}l'
        list_1 = ansi_text_wrapper_0.wrap(str_3)
        str_4 = ansi_text_wrapper_0.fill(str_0)
        str_5 = 'hw_O-WZk'
        str_6 = 'W'
        list_2 = ansi_text_wrapper_0.wrap(str_0)
        int_1 = module_0.len_without_ansi(str_6)
        list_3 = ansi_text_wrapper_0.wrap(str_5)
        list_4 = ansi_text_wrapper_0.wrap(str_4)
        int_2 = 2522
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_1, max_lines=int_2)
        str_7 = ansi_text_wrapper_1.fill(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n\n'
        int_0 = 6
        str_1 = 'hom'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
        str_2 = '__additional_attrs__ must be a dict in %r'
        list_0 = ansi_text_wrapper_0.wrap(str_2)
        list_1 = ansi_text_wrapper_0.wrap(str_1)
        str_3 = ansi_text_wrapper_0.fill(str_0)
        bool_0 = True
        str_4 = 'hw_O-WZk'
        str_5 = 'W'
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_0, int_0, placeholder=str_5)
        list_2 = ansi_text_wrapper_0.wrap(str_0)
        int_1 = module_0.len_without_ansi(str_5)
        list_3 = ansi_text_wrapper_0.wrap(str_4)
        list_4 = [list_3]
        int_2 = module_0.len_without_ansi(list_4)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\n\n'
        int_0 = 5
        str_1 = 'Eo'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
        str_2 = '.u\ti./l *U?Bg~(-voWL'
        str_3 = ansi_text_wrapper_0.fill(str_2)
        str_4 = '__additional_atrs_ must be a dict in %r'
        list_0 = ansi_text_wrapper_0.wrap(str_4)
        str_5 = ansi_text_wrapper_0.fill(str_0)
        bool_0 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_0, int_0, placeholder=str_4)
        list_1 = ansi_text_wrapper_0.wrap(str_0)
        int_1 = module_0.len_without_ansi(str_2)
        str_6 = ansi_text_wrapper_1.fill(str_2)
    except BaseException:
        pass