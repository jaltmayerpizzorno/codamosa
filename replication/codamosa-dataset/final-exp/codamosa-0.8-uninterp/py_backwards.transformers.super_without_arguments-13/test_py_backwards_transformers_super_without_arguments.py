# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    list_0 = [super_without_arguments_transformer_0, super_without_arguments_transformer_0]
    call_0 = module_0.Call(*list_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

def test_case_2():
    str_0 = 'super(U)'
    var_0 = module_2.parse(str_0, str_0)
    list_0 = [str_0, var_0, var_0]
    call_0 = module_0.Call(*list_0)
    a_s_t_0 = module_0.AST()
    str_1 = 'T\t./(IooN,f9sAHuC\\&`'
    dict_0 = {str_1: a_s_t_0}
    a_s_t_1 = module_0.AST(**dict_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_1)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)