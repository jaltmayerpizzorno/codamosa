# Automatically generated by Pynguin.
import thonny.jedi_utils as module_0

def test_case_0():
    try:
        list_0 = []
        bool_0 = True
        var_0 = module_0.get_statement_of_position(list_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -479
        set_0 = {int_0}
        var_0 = module_0.parse_source(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '}+rZ_[='
        int_0 = -2605
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '=e'
        list_0 = None
        var_0 = module_0.get_interpreter_completions(str_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '"I4dvdc'
        int_0 = -860
        var_0 = module_0.get_definitions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'p_0pU'
        str_1 = ";#fcy,<+l''9Y$ kye,"
        complex_0 = None
        bytes_0 = None
        str_2 = None
        bytes_1 = b'\x96\xef\xa2\\\x96\x08\xf8W\x03\xf4\xe2AH1\xa3\x94'
        list_0 = [str_2, str_2, bytes_1, str_2]
        float_0 = -794.36656
        thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_1, complex_0, bytes_0, list_0, float_0)
        str_3 = 'Help'
        str_4 = '\\Nh:(X\t!!'
        int_0 = 1455
        str_5 = 'G?+V@s'
        dict_0 = {}
        str_6 = 'Change cursor width\n\n        NB! Need to be careful with setting text["insertwidth"]!\n        My first straightforward solution caused unexplainable\n        infinite loop of insertions and deletions in the text\n        (Repro: insert a line and a word, select that word and then do Ctrl-Z).\n\n        This solution seems safe but be careful!\n        '
        thonny_completion_1 = module_0.ThonnyCompletion(str_3, str_4, int_0, str_5, dict_0, str_6)
        var_0 = thonny_completion_1.__getitem__(thonny_completion_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -479
        str_0 = 'r'
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0, int_0)
    except BaseException:
        pass