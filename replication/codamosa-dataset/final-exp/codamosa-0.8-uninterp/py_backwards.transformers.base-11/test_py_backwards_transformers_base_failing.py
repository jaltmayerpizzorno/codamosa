# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        list_0 = [base_import_rewrite_0, base_import_rewrite_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_s_t_0 = None
        import_0 = module_0.Import()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        base_import_rewrite_1 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_1.visit_Import(import_0)
    except BaseException:
        pass

def test_case_2():
    try:
        import_from_0 = module_0.ImportFrom()
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_3():
    try:
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = None
        list_0 = [base_import_rewrite_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        base_import_rewrite_1 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_1.visit_ImportFrom(import_from_0)
    except BaseException:
        pass