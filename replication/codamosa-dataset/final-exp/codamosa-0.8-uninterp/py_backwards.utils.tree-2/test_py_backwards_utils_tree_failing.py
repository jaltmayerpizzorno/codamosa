# Automatically generated by Pynguin.
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        a_s_t_0 = None
        a_s_t_1 = module_0.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_s_t_0 = module_1.AST()
        a_s_t_1 = module_0.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_s_t_0 = module_1.AST()
        tuple_0 = module_0.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_3():
    try:
        a_s_t_0 = module_1.AST()
        int_0 = 903
        module_0.insert_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2
        a_s_t_0 = module_1.AST()
        module_0.replace_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_5():
    try:
        a_s_t_0 = module_1.AST()
        tuple_0 = None
        var_0 = module_0.get_closest_parent_of(a_s_t_0, a_s_t_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        a_s_t_0 = module_1.AST()
        int_0 = 903
        list_0 = [a_s_t_0, a_s_t_0]
        module_0.insert_at(int_0, a_s_t_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '(1 + 2) * 3'
        var_0 = module_2.parse(str_0)
        tuple_0 = module_0.get_non_exp_parent_and_index(var_0, var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '3 + 2'
        var_0 = module_2.parse(str_0)
        int_0 = 0
        var_1 = var_0.body[int_0]
        str_1 = '4'
        var_2 = var_0.body[int_0]
        a_s_t_0 = module_0.get_parent(var_0, var_2)
        var_3 = a_s_t_0.body
        var_4 = len(var_3)
        str_2 = [str_1, str_1]
        module_0.replace_at(int_0, a_s_t_0, str_2)
        var_5 = var_0.body[int_0]
        a_s_t_1 = module_0.get_parent(var_0, var_5)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'a(1) + b(2)'
        var_0 = module_2.parse(str_0)
        int_0 = 0
        var_1 = var_0.body[int_0]
        a_s_t_0 = None
        list_0 = []
        module_0.insert_at(int_0, a_s_t_0, list_0)
        a_s_t_1 = module_0.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass