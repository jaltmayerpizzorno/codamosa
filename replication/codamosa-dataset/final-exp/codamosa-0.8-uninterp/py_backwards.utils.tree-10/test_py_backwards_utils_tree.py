# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.tree as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    list_0 = []
    int_0 = -1966
    module_1.insert_at(int_0, a_s_t_0, list_0)
    a_s_t_1 = module_0.AST()
    int_1 = -157
    module_1.insert_at(int_1, a_s_t_1, list_0)

def test_case_2():
    str_0 = 'if False: rint(5)'
    var_0 = module_2.parse(str_0)
    int_0 = 0
    var_1 = var_0.body
    var_2 = list(var_1)[int_0]
    a_s_t_0 = module_1.get_parent(var_0, var_2)
    a_s_t_1 = module_1.get_parent(a_s_t_0, var_2)