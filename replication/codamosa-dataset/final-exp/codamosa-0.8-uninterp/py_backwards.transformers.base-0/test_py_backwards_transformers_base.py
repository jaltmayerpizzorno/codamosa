# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)

def test_case_2():
    int_0 = 0
    str_0 = 'from six.moves import abc'
    var_0 = module_2.parse(str_0)
    var_1 = var_0.body[int_0]
    base_import_rewrite_0 = module_1.BaseImportRewrite(str_0)
    var_2 = base_import_rewrite_0.visit_ImportFrom(var_1)

def test_case_3():
    str_0 = '\nimport test\ntest.test_0()\n'
    var_0 = module_2.parse(str_0, str_0)
    base_import_rewrite_0 = module_1.BaseImportRewrite(str_0)
    int_0 = 0
    var_1 = var_0.body[int_0]
    var_2 = base_import_rewrite_0.visit_Import(var_1)