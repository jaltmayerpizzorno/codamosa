# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.tree as module_1

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -356
        a_s_t_0 = module_0.AST()
        module_1.insert_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 4907
        a_s_t_0 = module_0.AST()
        type_0 = None
        iterable_0 = module_1.find(a_s_t_0, type_0)
        module_1.replace_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_3():
    try:
        a_s_t_0 = module_0.AST()
        var_0 = module_1.get_closest_parent_of(a_s_t_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_4():
    try:
        a_s_t_0 = module_0.AST()
        int_0 = -239
        list_0 = []
        module_1.insert_at(int_0, a_s_t_0, list_0)
        a_s_t_1 = module_1.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass