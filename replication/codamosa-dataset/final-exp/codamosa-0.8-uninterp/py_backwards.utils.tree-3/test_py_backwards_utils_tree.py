# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.utils.tree as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'a = 3'
    var_0 = module_0.parse(str_0)
    int_0 = 0
    str_1 = 'b = 4'
    var_1 = module_0.parse(str_1)
    var_2 = var_1.body
    module_1.replace_at(int_0, var_0, var_2)
    var_3 = module_0.dump(var_0)

def test_case_2():
    str_0 = 'simple_string'
    var_0 = module_0.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    a_s_t_0 = module_1.get_parent(var_0, var_2)

def test_case_3():
    str_0 = 'simple_string'
    var_0 = module_0.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    a_s_t_0 = module_1.get_parent(var_0, var_2)
    a_s_t_1 = module_1.get_parent(a_s_t_0, a_s_t_0)

def test_case_4():
    str_0 = 'test = []'
    var_0 = module_0.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    str_1 = 'test = get_parent(tree.body[0].value)'
    var_3 = module_0.parse(str_1)
    var_4 = var_3.body[int_0]
    var_5 = var_4.value.args[int_0]
    a_s_t_0 = module_1.get_parent(var_3, var_5)
    var_6 = var_3.body[int_0]
    var_7 = var_6.value.args[int_0]
    var_8 = var_7.value
    tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    a_s_t_1 = module_1.get_parent(var_3, var_8)