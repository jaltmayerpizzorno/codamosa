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
    str_0 = 'def func():\n  a = yield from [1, 2, 3]\n  b = yield from (i for i in range(10))\n  c = yield from [1, 2, 3]\n  d = yield from (i for i in range(10))\n  e = yield from [1, 2, 3]\n  f = yield from (i for i in range(10))'
    var_0 = module_2.parse(str_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(var_0)
    a_s_t_0 = yield_from_transformer_0.visit(var_0)