# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = -4584
    dict_0 = None
    list_0 = [dict_0, int_0, dict_0, dict_0]
    bool_0 = True
    tuple_0 = (int_0, dict_0, list_0, bool_0)
    a_s_t_0 = module_0.AST()
    list_1 = [tuple_0, list_0]
    dict_1 = module_0.Dict(*list_1)
    dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
    var_0 = dict_unpacking_transformer_0.visit_Dict(dict_1)

def test_case_2():
    int_0 = -4562
    dict_0 = None
    list_0 = [dict_0, int_0]
    bool_0 = True
    tuple_0 = (int_0, dict_0, list_0, bool_0)
    a_s_t_0 = module_0.AST()
    list_1 = [tuple_0, list_0]
    dict_1 = module_0.Dict(*list_1)
    dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
    var_0 = dict_unpacking_transformer_0.visit_Dict(dict_1)