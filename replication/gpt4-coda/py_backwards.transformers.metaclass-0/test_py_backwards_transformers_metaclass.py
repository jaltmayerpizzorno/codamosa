# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

def test_case_0():
    str_0 = 'tkinter.tix'
    list_0 = []
    module_x_var_0 = module_0.Module(*list_0)
    dict_0 = {str_0: module_x_var_0}
    str_1 = 'Bzh|\x0bBS='
    list_1 = [dict_0, str_1, list_0, list_0]
    class_def_0 = module_0.ClassDef(*list_1)
    a_s_t_0 = module_0.AST()
    metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
    class_def_1 = metaclass_transformer_0.visit_ClassDef(class_def_0)
    a_s_t_1 = module_0.AST()
    metaclass_transformer_1 = module_1.MetaclassTransformer(a_s_t_1)
    class_def_2 = metaclass_transformer_1.visit_ClassDef(class_def_1)