# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.return_from_generator as module_1

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    dict_0 = {return_from_generator_transformer_0: a_s_t_0, a_s_t_0: return_from_generator_transformer_0}
    list_0 = [dict_0, dict_0, dict_0]
    function_def_0 = module_0.FunctionDef(*list_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

def test_case_2():
    a_s_t_0 = module_0.AST()
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    dict_0 = {}
    list_0 = [return_from_generator_transformer_0, dict_0, dict_0]
    function_def_0 = module_0.FunctionDef(*list_0)
    function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

def test_case_3():
    a_s_t_0 = module_0.AST()
    return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
    dict_0 = {a_s_t_0: a_s_t_0, a_s_t_0: return_from_generator_transformer_0, return_from_generator_transformer_0: return_from_generator_transformer_0, a_s_t_0: return_from_generator_transformer_0, return_from_generator_transformer_0: a_s_t_0, return_from_generator_transformer_0: return_from_generator_transformer_0, return_from_generator_transformer_0: a_s_t_0, a_s_t_0: a_s_t_0, return_from_generator_transformer_0: return_from_generator_transformer_0}
    list_0 = [return_from_generator_transformer_0, return_from_generator_transformer_0, dict_0, dict_0, dict_0]
    function_def_0 = module_0.FunctionDef(*list_0)
    tuple_0 = None
    list_1 = [dict_0, a_s_t_0, tuple_0, a_s_t_0]
    str_0 = 'cPickle'
    tuple_1 = (function_def_0, list_0)
    list_2 = [list_1, str_0, tuple_1, a_s_t_0]
    str_1 = 'W/\x0cZ(ze&:*S-'
    str_2 = '{K^'
    dict_1 = {str_1: function_def_0, str_2: tuple_1}
    function_def_1 = module_0.FunctionDef(*list_2, **dict_1)
    function_def_2 = return_from_generator_transformer_0.visit_FunctionDef(function_def_1)