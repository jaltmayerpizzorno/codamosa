# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Dl6sci'
    list_0 = [str_0, str_0, str_0]
    call_0 = module_0.Call(*list_0)
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

def test_case_2():
    str_0 = 'supler()'
    str_1 = '<ast>'
    str_2 = 'exec'
    var_0 = module_2.parse(str_0, str_1, str_2)
    int_0 = 0
    var_1 = var_0.body[int_0]
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_2 = super_without_arguments_transformer_0.visit(var_1)

def test_case_3():
    str_0 = 'super(g)'
    str_1 = '<ast>'
    str_2 = 'exec'
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    var_0 = module_2.parse(str_0, str_1, str_2)
    int_0 = 0
    list_0 = [str_1, str_0, var_0]
    call_0 = module_0.Call(*list_0)
    a_s_t_1 = module_0.AST()
    super_without_arguments_transformer_1 = module_1.SuperWithoutArgumentsTransformer(a_s_t_1)
    call_1 = super_without_arguments_transformer_1.visit_Call(call_0)
    call_2 = module_0.Call(*list_0)
    call_3 = super_without_arguments_transformer_1.visit_Call(call_2)
    var_1 = var_0.body[int_0]
    a_s_t_2 = module_0.AST()
    super_without_arguments_transformer_2 = module_1.SuperWithoutArgumentsTransformer(a_s_t_2)
    super_without_arguments_transformer_3 = module_1.SuperWithoutArgumentsTransformer(a_s_t_1)
    call_4 = super_without_arguments_transformer_2.visit_Call(call_1)