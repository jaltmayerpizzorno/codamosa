# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

def test_case_0():
    try:
        dict_0 = {}
        module_x_var_0 = module_0.Module(**dict_0)
        list_0 = []
        a_s_t_0 = module_0.AST(*list_0)
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        module_x_var_1 = dict_unpacking_transformer_0.visit_Module(module_x_var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
    except BaseException:
        pass