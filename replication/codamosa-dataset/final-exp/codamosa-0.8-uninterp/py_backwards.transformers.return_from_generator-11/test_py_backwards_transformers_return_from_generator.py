# Automatically generated by Pynguin.
import py_backwards.transformers.return_from_generator as module_0
import typed_ast._ast3 as module_1

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = None
    str_0 = 'c)0{Z:k ,RXNX\r($'
    list_0 = [str_0, str_0, str_0, a_s_t_0]
    return_from_generator_transformer_0 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
    function_def_0 = module_1.FunctionDef(*list_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

def test_case_2():
    a_s_t_0 = None
    str_0 = ''
    list_0 = [str_0, str_0, str_0, a_s_t_0]
    return_from_generator_transformer_0 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
    function_def_0 = module_1.FunctionDef(*list_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)