# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.python2_future as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = ''
    var_0 = module_0.parse(str_0)
    var_1 = ()
    python2_future_transformer_0 = module_1.Python2FutureTransformer(var_1)
    module_x_var_0 = python2_future_transformer_0.visit_Module(var_0)