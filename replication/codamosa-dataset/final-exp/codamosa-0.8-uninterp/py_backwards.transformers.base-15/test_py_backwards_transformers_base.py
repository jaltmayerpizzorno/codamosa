# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    base_node_transformer_0 = module_1.BaseNodeTransformer(a_s_t_0)

def test_case_2():
    str_0 = 'import foo'
    base_import_rewrite_0 = module_1.BaseImportRewrite(str_0)
    var_0 = module_2.parse(str_0)
    var_1 = base_import_rewrite_0.visit(var_0)

def test_case_3():
    var_0 = None
    base_import_rewrite_0 = module_1.BaseImportRewrite(var_0)
    str_0 = 'from t1 import a, b, c'
    var_1 = module_2.parse(str_0, str_0)
    var_2 = base_import_rewrite_0.visit(var_1)

def test_case_4():
    var_0 = None
    base_import_rewrite_0 = module_1.BaseImportRewrite(var_0)
    str_0 = 'from t1 import a, b, c'
    str_1 = 'exec'
    var_1 = module_2.parse(str_0, str_1)
    var_2 = base_import_rewrite_0.visit(var_1)
    str_2 = 'from t1 import a, b, c\n'
    var_3 = module_2.parse(str_2, str_1)
    var_4 = base_import_rewrite_0.visit(var_1)
    str_3 = 'from t1 import a as b, b, c\n'
    var_5 = module_2.parse(str_3, str_1)
    str_4 = 'from t1 import *'
    var_6 = module_2.parse(str_4, str_1)
    var_7 = base_import_rewrite_0.visit(var_6)