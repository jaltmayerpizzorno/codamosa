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
    str_0 = 'from a.b import c'
    var_0 = module_2.parse(str_0)
    base_import_rewrite_0 = module_1.BaseImportRewrite(str_0)
    var_1 = base_import_rewrite_0.visit(var_0)

def test_case_3():
    str_0 = 'import x'
    var_0 = module_2.parse(str_0)
    base_import_rewrite_0 = module_1.BaseImportRewrite(var_0)
    var_1 = base_import_rewrite_0.visit(var_0)
    str_1 = 'import xx'
    var_2 = module_2.parse(str_1)
    var_3 = base_import_rewrite_0.visit(var_2)