# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.return_from_generator as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '4u'
    list_0 = [str_0, str_0, str_0, str_0]
    function_def_0 = module_0.FunctionDef(*list_0)
    a_s_t_0 = module_0.AST()
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

def test_case_2():
    str_0 = ''
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    function_def_0 = module_0.FunctionDef(*list_0)
    a_s_t_0 = module_0.AST()
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

def test_case_3():
    str_0 = ''
    int_0 = -3211
    function_def_0 = module_0.FunctionDef()
    tuple_0 = (int_0, function_def_0)
    list_0 = [str_0, str_0, tuple_0]
    function_def_1 = module_0.FunctionDef(*list_0)
    str_1 = "MpH!AHUF #=Ek'"
    list_1 = [str_0, str_0, str_0]
    dict_0 = {str_0: str_1, str_1: list_1, str_0: str_0}
    a_s_t_0 = module_0.AST(**dict_0)
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    str_2 = ' Nt1B%sF@c'
    dict_1 = {str_1: return_from_generator_transformer_0, str_2: str_2, str_1: str_2}
    a_s_t_1 = module_0.AST(**dict_1)
    return_from_generator_transformer_1 = module_1.ReturnFromGeneratorTransformer(a_s_t_1)
    function_def_2 = return_from_generator_transformer_1.visit_FunctionDef(function_def_1)
    list_2 = [str_0, str_0, str_0, str_0, str_0]
    function_def_3 = module_0.FunctionDef(*list_2)
    a_s_t_2 = module_0.AST()
    return_from_generator_transformer_2 = module_1.ReturnFromGeneratorTransformer(a_s_t_2)
    return_from_generator_transformer_3 = module_1.ReturnFromGeneratorTransformer(a_s_t_1)
    function_def_4 = return_from_generator_transformer_2.visit_FunctionDef(function_def_3)
    function_def_5 = return_from_generator_transformer_2.visit_FunctionDef(function_def_4)