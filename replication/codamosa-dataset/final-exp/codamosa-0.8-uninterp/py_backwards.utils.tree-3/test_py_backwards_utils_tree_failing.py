# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.tree as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2574
        a_s_t_0 = module_0.AST()
        module_1.insert_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_s_t_0 = module_0.AST()
        type_0 = None
        var_0 = module_1.get_closest_parent_of(a_s_t_0, a_s_t_0, type_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        str_0 = 'DJ6o='
        str_1 = 'Tix'
        dict_0 = {str_1: str_1, str_0: str_1, str_1: str_0, str_1: str_1}
        a_s_t_0 = module_0.AST(*list_0, **dict_0)
        int_0 = 1041
        list_1 = [a_s_t_0]
        module_1.insert_at(int_0, a_s_t_0, list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 0
        str_0 = 'a = 100 + 200'
        var_0 = module_2.parse(str_0)
        var_1 = var_0.body[int_0]
        var_2 = var_1.value
        var_3 = var_2.left
        tuple_0 = module_1.get_non_exp_parent_and_index(var_1, var_3)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'test = []'
        var_0 = module_2.parse(str_0)
        int_0 = 0
        var_1 = var_0.body[int_0]
        var_2 = var_1.value
        a_s_t_0 = module_1.get_parent(var_0, var_2)
        str_1 = 'test = get_parent(tree.body[0].value)'
        tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
        var_3 = module_2.parse(str_1)
        var_4 = var_3.body[int_0]
        var_5 = var_4.value.args[int_0]
        a_s_t_1 = module_1.get_parent(var_3, var_5)
        var_6 = var_2.value.args[int_0]
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test = []'
        var_0 = module_2.parse(str_0)
        int_0 = 0
        a_s_t_0 = None
        type_0 = None
        iterable_0 = module_1.find(a_s_t_0, type_0)
        var_1 = var_0.body[int_0]
        var_2 = var_1.value
        a_s_t_1 = module_1.get_parent(var_0, var_2)
        str_1 = 'test = get_parent(tree.body[0].value)'
        var_3 = module_2.parse(str_1)
        var_4 = var_3.body[int_0]
        var_5 = var_4.value.args[int_0]
        a_s_t_2 = module_1.get_parent(var_3, var_5)
        var_6 = var_3.body[int_0]
        var_7 = var_6.value.args[int_0]
        a_s_t_3 = module_1.get_parent(a_s_t_2, a_s_t_1)
        var_8 = module_1.get_closest_parent_of(a_s_t_1, a_s_t_2, type_0)
    except BaseException:
        pass