# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

def test_case_0():
    try:
        module_x_var_0 = module_0.Module()
        a_s_t_0 = module_0.AST()
        metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
        module_x_var_1 = metaclass_transformer_0.visit_Module(module_x_var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        class_def_0 = module_0.ClassDef()
        list_0 = []
        str_0 = '\r;j.SmAE'
        dict_0 = {str_0: str_0}
        a_s_t_0 = module_0.AST(*list_0, **dict_0)
        metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
        class_def_1 = metaclass_transformer_0.visit_ClassDef(class_def_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        a_s_t_0 = None
        metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
        a_s_t_1 = module_0.AST(**dict_0)
        metaclass_transformer_1 = module_1.MetaclassTransformer(a_s_t_1)
        list_0 = [a_s_t_0, dict_0, a_s_t_1]
        class_def_0 = module_0.ClassDef(*list_0)
        class_def_1 = metaclass_transformer_0.visit_ClassDef(class_def_0)
    except BaseException:
        pass