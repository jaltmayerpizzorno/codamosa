# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.yield_from as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
    a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)

def test_case_2():
    str_0 = 'x = yield from y'
    var_0 = module_2.parse(str_0)
    int_0 = 3
    yield_from_transformer_0 = module_1.YieldFromTransformer(int_0)
    a_s_t_0 = yield_from_transformer_0.visit(var_0)

def test_case_3():
    str_0 = 'x = yield from y'
    var_0 = module_2.parse(str_0)
    int_0 = -40
    a_s_t_0 = module_0.AST()
    str_1 = 'body'
    str_2 = 'Tk\x0c"OG*F'
    list_0 = [str_0, int_0, str_1]
    dict_0 = {str_0: var_0, str_1: str_0, str_1: str_1, str_2: list_0}
    a_s_t_1 = module_0.AST(**dict_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_1)
    a_s_t_2 = yield_from_transformer_0.visit(a_s_t_0)
    yield_from_transformer_1 = module_1.YieldFromTransformer(a_s_t_2)
    a_s_t_3 = yield_from_transformer_0.visit(a_s_t_1)
    a_s_t_4 = yield_from_transformer_0.visit(a_s_t_2)