# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast._ast3 as module_2

def test_case_0():
    try:
        str_0 = '\nsuper()\n        '
        var_0 = module_0.parse(str_0)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
        var_1 = super_without_arguments_transformer_0.visit(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'supaer()'
        var_0 = module_0.parse(str_0)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
        var_1 = super_without_arguments_transformer_0.visit(var_0)
        list_0 = [super_without_arguments_transformer_0, var_0, str_0]
        str_1 = 'Z'
        dict_0 = {str_1: var_0}
        a_s_t_0 = module_2.AST(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'super(NM)'
        var_0 = module_0.parse(str_0)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
        list_0 = [var_0, super_without_arguments_transformer_0, super_without_arguments_transformer_0]
        call_0 = module_2.Call(*list_0)
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
        call_2 = super_without_arguments_transformer_0.visit_Call(call_1)
        var_1 = super_without_arguments_transformer_0.visit(var_0)
        a_s_t_0 = module_2.AST()
        super_without_arguments_transformer_1 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
        int_0 = 0
        var_2 = var_0.body[int_0]
        var_3 = var_2.body[int_0]
    except BaseException:
        pass