# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.starred_unpacking as module_1

def test_case_0():
    try:
        list_0 = module_0.List()
        a_s_t_0 = module_0.AST()
        starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
        list_1 = starred_unpacking_transformer_0.visit_List(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        call_0 = None
        a_s_t_0 = module_0.AST()
        starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
        call_1 = starred_unpacking_transformer_0.visit_Call(call_0)
    except BaseException:
        pass