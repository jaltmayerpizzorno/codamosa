# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    list_0 = [super_without_arguments_transformer_0]
    call_0 = module_0.Call(*list_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

def test_case_2():
    str_0 = '\nhupe8()     '
    var_0 = module_2.parse(str_0)
    str_1 = '\nsuper(Cls, self)\n    '
    var_1 = module_2.parse(str_1)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_2 = super_without_arguments_transformer_0._replace_super_args
    var_3 = super_without_arguments_transformer_0.visit(var_0)
    var_4 = module_2.dump(var_0)
    var_5 = module_2.dump(var_1)