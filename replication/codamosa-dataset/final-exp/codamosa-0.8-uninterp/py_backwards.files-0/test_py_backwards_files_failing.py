# Automatically generated by Pynguin.
import py_backwards.files as module_0

def test_case_0():
    try:
        str_0 = 'lD'
        str_1 = 'b.py'
        var_0 = None
        iterable_0 = module_0.get_input_output_paths(str_0, str_1, var_0)
        var_1 = tuple(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'b.py'
        var_0 = None
        iterable_0 = module_0.get_input_output_paths(str_0, str_0, var_0)
        str_1 = 'c/d/b.py'
        iterable_1 = module_0.get_input_output_paths(str_1, str_1, var_0)
        var_1 = tuple(iterable_1)
    except BaseException:
        pass