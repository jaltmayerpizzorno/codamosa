# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.utils.tree as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'a = 1\nb = 2\nc = 3'
    var_0 = module_0.parse(str_0)
    int_0 = 1
    var_1 = var_0.body[int_0]
    int_1 = 2
    var_2 = var_0.body[int_1]
    var_3 = var_0.body[int_1]
    var_4 = var_3.value
    var_5 = var_0.body[int_1]
    module_1.replace_at(int_0, var_0, var_1)

def test_case_2():
    str_0 = 'exec'
    var_0 = module_0.parse(str_0, str_0, str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    tuple_0 = module_1.get_non_exp_parent_and_index(var_0, var_1)