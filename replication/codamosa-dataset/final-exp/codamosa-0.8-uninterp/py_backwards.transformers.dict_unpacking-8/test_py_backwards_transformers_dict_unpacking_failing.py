# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

def test_case_0():
    try:
        dict_0 = {}
        module_x_var_0 = module_0.Module()
        list_0 = [dict_0, module_x_var_0]
        dict_1 = module_0.Dict(*list_0, **dict_0)
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        var_0 = dict_unpacking_transformer_0.visit_Dict(dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = module_0.Dict()
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        list_1 = [list_0]
        module_x_var_0 = module_0.Module(*list_1)
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        module_x_var_1 = dict_unpacking_transformer_0.visit_Module(module_x_var_0)
        module_x_var_2 = module_0.Module()
        list_2 = [dict_0, module_x_var_2]
        dict_1 = module_0.Dict(*list_2, **dict_0)
        a_s_t_1 = module_0.AST()
        dict_unpacking_transformer_1 = module_1.DictUnpackingTransformer(a_s_t_1)
        var_0 = dict_unpacking_transformer_1.visit_Dict(dict_1)
    except BaseException:
        pass