# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast._ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'supeG()'
    var_0 = module_0.parse(str_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_1 = super_without_arguments_transformer_0.visit(var_0)
    var_2 = module_0.fix_missing_locations(var_0)

def test_case_2():
    dict_0 = None
    list_0 = [dict_0, dict_0, dict_0]
    call_0 = module_2.Call(*list_0)
    a_s_t_0 = module_2.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)