# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.yield_from as module_1

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
    a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)

def test_case_2():
    str_0 = 'body'
    float_0 = 607.7337529274758
    dict_0 = {str_0: float_0, str_0: str_0, str_0: str_0, str_0: float_0, str_0: float_0}
    a_s_t_0 = module_0.AST(**dict_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
    a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)

def test_case_3():
    str_0 = 'body'
    list_0 = []
    str_1 = 'ox[bt"]7;jVc`'
    dict_0 = {str_1: str_1, str_0: list_0, str_1: str_0, str_1: str_0}
    a_s_t_0 = module_0.AST(*list_0, **dict_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
    a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)

def test_case_4():
    set_0 = set()
    list_0 = [set_0, set_0]
    str_0 = 'body'
    dict_0 = {str_0: list_0}
    a_s_t_0 = module_0.AST(**dict_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
    yield_from_transformer_1 = module_1.YieldFromTransformer(a_s_t_0)
    a_s_t_1 = yield_from_transformer_1.visit(a_s_t_0)