# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        call_0 = None
        a_s_t_0 = module_0.AST()
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'super()'
        var_0 = module_2.parse(str_0, str_0)
        list_0 = [str_0, var_0, var_0]
        call_0 = module_0.Call(*list_0)
        a_s_t_0 = module_0.AST()
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'su|per()'
        str_1 = '[d:\x0cF!f\r|(yZ'
        var_0 = module_2.parse(str_0, str_1)
        var_1 = var_0.body
        var_2 = module_2.parse(str_0, str_1)
        list_0 = [var_1]
        call_0 = module_0.Call(*list_0)
        list_1 = []
        str_2 = '&L(nx1|]h9%z@p\x0c1'
        dict_0 = {str_0: str_1, str_2: list_0}
        a_s_t_0 = module_0.AST(*list_1)
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
        call_2 = super_without_arguments_transformer_0.visit_Call(call_0)
        var_3 = module_2.parse(dict_0, super_without_arguments_transformer_0)
    except BaseException:
        pass