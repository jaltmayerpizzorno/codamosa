# Automatically generated by Pynguin.
import thonny.jedi_utils as module_0

def test_case_0():
    try:
        float_0 = -1451.0
        list_0 = [float_0]
        var_0 = module_0.get_statement_of_position(float_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'view.full_screen'
        int_0 = -435
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        str_0 = '2Y7:Q:o'
        var_0 = module_0.get_interpreter_completions(str_0, list_0)
        str_1 = '(EhAE'
        var_1 = module_0.parse_source(str_1)
        int_0 = None
        str_2 = 'eJ!!cN$'
        str_3 = None
        str_4 = "'N"
        var_2 = module_0.get_script_completions(str_2, int_0, int_0, str_3, str_4)
        int_1 = -2230
        str_5 = 'Used when dict.values is referenced in a non-iterating context (returns an iterator in Python 3)'
        var_3 = module_0.get_definitions(str_1, int_1, int_1, str_5)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ' -?Ekg/wx]E57S%1#H+'
        int_0 = 4051
        var_0 = module_0.get_definitions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xf2\x0b\xadm\xc3\x99\xd4L\xd5\xef\xbb\x06@\xf5\xa1\xf3\xda\xf8y'
        str_0 = 'contains_docstring'
        int_0 = 123
        dict_0 = {int_0: int_0, int_0: str_0}
        float_0 = -2769.237
        str_1 = 's0\\h\\8cQI9\x0c`R~|#D_)'
        tuple_0 = (float_0, str_1)
        bool_0 = True
        thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_0, int_0, dict_0, tuple_0, bool_0)
        var_0 = thonny_completion_0.__getitem__(bytes_0)
    except BaseException:
        pass