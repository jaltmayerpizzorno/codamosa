# Automatically generated by Pynguin.
import thonny.jedi_utils as module_0

def test_case_0():
    try:
        str_0 = 'Xz?*lp`'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, dict_0, dict_0]
        var_0 = module_0.get_interpreter_completions(str_0, list_0)
        bytes_0 = b'\xf9Qz\x8c?\x92\xc7@'
        list_1 = [list_0, str_0]
        var_1 = module_0.get_statement_of_position(bytes_0, list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        var_0 = module_0.parse_source(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -4619
        str_0 = 'KqTO{R3 H'
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '{*):M\\^of\tl*AD49'
        int_0 = 379
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        str_0 = 'shelve'
        str_1 = 'N\x0c&il\r'
        tuple_0 = (bool_0, str_0, str_1)
        str_2 = 'U\x0b sn'
        str_3 = 'FO2>'
        set_0 = {str_2, str_3, str_3, str_3}
        int_0 = -4413
        dict_0 = {str_3: int_0}
        float_0 = 1.1
        thonny_completion_0 = module_0.ThonnyCompletion(str_2, str_3, set_0, int_0, dict_0, float_0)
        var_0 = thonny_completion_0.__getitem__(tuple_0)
    except BaseException:
        pass