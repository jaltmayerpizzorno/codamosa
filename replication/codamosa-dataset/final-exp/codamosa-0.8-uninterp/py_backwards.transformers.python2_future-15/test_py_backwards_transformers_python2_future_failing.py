# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.python2_future as module_1

def test_case_0():
    try:
        list_0 = []
        module_x_var_0 = module_0.Module(*list_0)
        a_s_t_0 = module_0.AST()
        python2_future_transformer_0 = module_1.Python2FutureTransformer(a_s_t_0)
        module_x_var_1 = python2_future_transformer_0.visit_Module(module_x_var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'str'
        dict_0 = {str_0: str_0, str_0: str_0}
        a_s_t_0 = module_0.AST(**dict_0)
        a_s_t_1 = module_0.AST()
        list_0 = [str_0, a_s_t_1, a_s_t_0, a_s_t_1]
        int_0 = -1666
        list_1 = [list_0, int_0]
        module_x_var_0 = module_0.Module(*list_1, **dict_0)
        python2_future_transformer_0 = module_1.Python2FutureTransformer(a_s_t_0)
        module_x_var_1 = python2_future_transformer_0.visit_Module(module_x_var_0)
        python2_future_transformer_1 = module_1.Python2FutureTransformer(a_s_t_1)
        python2_future_transformer_2 = module_1.Python2FutureTransformer(a_s_t_1)
        module_x_var_2 = module_0.Module()
        module_x_var_3 = python2_future_transformer_1.visit_Module(module_x_var_2)
    except BaseException:
        pass