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