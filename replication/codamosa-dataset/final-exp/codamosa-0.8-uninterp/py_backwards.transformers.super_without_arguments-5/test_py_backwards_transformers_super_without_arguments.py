# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n        class A:\n            def m1(self):\n                super()\n    '
    list_0 = [str_0, str_0]
    call_0 = module_0.Call(*list_0)
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

def test_case_2():
    str_0 = 'supar()'
    var_0 = module_2.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    var_3 = var_0.body[int_0]
    var_4 = var_3.value
    var_5 = var_4.func
    var_6 = var_4.args
    var_7 = var_4.args
    var_8 = len(var_7)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    call_0 = super_without_arguments_transformer_0.visit_Call(var_4)
    var_9 = var_4.args
    var_10 = len(var_9)

def test_case_3():
    str_0 = 'super(m)'
    var_0 = module_2.parse(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    var_3 = var_0.body[int_0]
    var_4 = var_3.value
    var_5 = var_4.func
    var_6 = var_4.args
    var_7 = var_4.args
    var_8 = len(var_7)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    call_0 = super_without_arguments_transformer_0.visit_Call(var_4)
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_1 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    var_9 = var_4.args
    var_10 = len(var_9)