# Automatically generated by Pynguin.
import py_backwards.files as module_0

def test_case_0():
    try:
        str_0 = '/home/test/input'
        str_1 = '/home/test/output'
        iterable_0 = module_0.get_input_output_paths(str_0, str_1, str_0)
        var_0 = list(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 0
        str_0 = 'foo.py'
        iterable_0 = module_0.get_input_output_paths(str_0, str_0, int_0)
        var_0 = list(iterable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        str_0 = ''
        str_1 = 'X`u.{X_}x&'
        iterable_0 = module_0.get_input_output_paths(str_1, str_1, str_1)
        str_2 = '8q8n5J7Q_Q\t|j0IO^'
        str_3 = '+cfwPgSZs\nub^??'
        iterable_1 = module_0.get_input_output_paths(str_2, str_3, str_2)
        str_4 = 'zA\x0c^\\d<_72O|K)'
        iterable_2 = module_0.get_input_output_paths(str_0, str_0, str_4)
        str_5 = 'foo.pz'
        str_6 = 'bar.py'
        iterable_3 = module_0.get_input_output_paths(str_5, str_6, var_0)
        var_1 = list(iterable_3)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        str_1 = None
        str_2 = '>\r9zGu&\n\x0bB=zm2W'
        str_3 = 'D`\\b<X1cn\tB\t\n1j'
        iterable_0 = module_0.get_input_output_paths(str_2, str_3, str_3)
        iterable_1 = module_0.get_input_output_paths(str_0, str_0, str_1)
        str_4 = '/home/input.py'
        var_0 = list(iterable_1)
        str_5 = '/home/test/input'
        str_6 = '/home/test/output'
        iterable_2 = module_0.get_input_output_paths(str_5, str_6, str_4)
        var_1 = list(iterable_2)
    except BaseException:
        pass