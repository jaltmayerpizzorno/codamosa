# Automatically generated by Pynguin.
import py_backwards.utils.tree as module_0
import typed_ast.ast3 as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = 1939
    a_s_t_0 = None
    list_0 = []
    module_0.insert_at(int_0, a_s_t_0, list_0)
    int_1 = 0
    str_0 = 'a + b'
    var_0 = module_1.parse(str_0)
    var_1 = var_0.body[int_1]
    var_2 = var_1.value

def test_case_2():
    str_0 = 'def a(b):\n    return b + 2\na(2)'
    var_0 = module_1.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    tuple_0 = module_0.get_non_exp_parent_and_index(var_0, var_1)

def test_case_3():
    str_0 = 'def a(b):\n    return b + 2\na(2)'
    var_0 = module_1.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    tuple_0 = module_0.get_non_exp_parent_and_index(var_0, var_1)
    tuple_1 = module_0.get_non_exp_parent_and_index(var_0, var_1)