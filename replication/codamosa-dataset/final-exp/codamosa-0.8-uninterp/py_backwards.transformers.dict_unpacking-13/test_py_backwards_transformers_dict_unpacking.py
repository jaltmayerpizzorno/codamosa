# Automatically generated by Pynguin.
import py_backwards.transformers.dict_unpacking as module_0
import typed_ast.ast3 as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    dict_unpacking_transformer_0 = module_0.DictUnpackingTransformer(var_0)
    str_0 = '\n{None: None, **{1: 1}}\n'
    var_1 = module_1.parse(str_0)
    var_2 = dict_unpacking_transformer_0.visit(var_1)