# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1

def test_case_0():
    try:
        str_0 = 'gbo[8m%^8A/\x0b;JhkBjf'
        str_1 = '){s\r-\rY'
        dict_0 = {str_0: str_0, str_1: str_1}
        import_0 = module_0.Import(**dict_0)
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_Import(import_0)
    except BaseException:
        pass

def test_case_1():
    try:
        import_0 = module_0.Import()
        str_0 = None
        list_0 = []
        list_1 = [str_0, list_0, import_0]
        import_from_0 = module_0.ImportFrom(*list_1)
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass