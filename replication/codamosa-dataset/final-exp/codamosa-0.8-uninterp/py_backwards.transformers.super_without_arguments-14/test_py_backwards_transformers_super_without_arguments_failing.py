# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1

def test_case_0():
    try:
        str_0 = 'a = super()'
        var_0 = module_0.parse(str_0)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
        var_1 = super_without_arguments_transformer_0.visit(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'a = super(On)'
        var_0 = module_0.parse(str_0)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
        var_1 = super_without_arguments_transformer_0.visit(var_0)
        call_0 = None
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
    except BaseException:
        pass