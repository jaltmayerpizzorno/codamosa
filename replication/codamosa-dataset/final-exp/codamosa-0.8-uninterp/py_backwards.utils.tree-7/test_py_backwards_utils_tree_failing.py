# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.tree as module_1
import typed_ast.ast3 as module_2
import weakref as module_3

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1684
        a_s_t_0 = module_0.AST()
        module_1.insert_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1059
        a_s_t_0 = None
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
        str_0 = 'def fn(x):\n    while True:\n        yield x'
        str_1 = '<test file>'
        str_2 = 'exec'
        var_0 = module_2.parse(str_0, str_1, str_2)
        int_0 = 0
        var_1 = var_0.body[int_0]
        var_2 = var_1.body[int_0]
        a_s_t_0 = module_1.get_parent(var_0, var_2)
        var_3 = var_0.body[int_0]
        var_4 = var_3.body[int_0]
        var_5 = var_4.body
        str_3 = 'EBze"k\ta{8xUN}(.LPH'
        str_4 = 'HTTPHandler'
        dict_0 = {str_3: str_1, str_3: int_0, str_4: str_0}
        var_6 = module_1.get_closest_parent_of(a_s_t_0, a_s_t_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Parent for {} not found'
        dict_0 = {str_0: str_0}
        a_s_t_0 = module_0.AST(**dict_0)
        list_0 = [str_0]
        iterable_0 = module_1.find(a_s_t_0, list_0)
        weak_key_dictionary_0 = module_3.WeakKeyDictionary(iterable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'def fn(x):\n    while True:\n        yield x'
        str_1 = '<test file>'
        str_2 = 'exec'
        var_0 = module_2.parse(str_0, str_1, str_2)
        int_0 = 0
        var_1 = var_0.body[int_0]
        var_2 = var_1.body[int_0]
        a_s_t_0 = module_1.get_parent(var_0, var_2)
        bool_0 = True
        a_s_t_1 = module_1.get_parent(a_s_t_0, a_s_t_0, bool_0)
        var_3 = var_0.body[int_0]
        var_4 = var_3.body[int_0]
        var_5 = var_4.body
        str_3 = 'EBze"k\ta{8xUN}(.LPH'
        str_4 = 'HTTPHandler'
        dict_0 = {str_3: str_1, str_3: int_0, str_4: str_0}
        var_6 = module_1.get_closest_parent_of(a_s_t_0, a_s_t_0, dict_0)
    except BaseException:
        pass