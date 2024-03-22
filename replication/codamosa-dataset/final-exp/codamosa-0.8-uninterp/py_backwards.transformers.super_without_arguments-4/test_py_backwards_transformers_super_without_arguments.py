# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'class Foo(Super):\n    def foo(self):\n        super()'
    var_0 = module_0.parse(str_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_1 = super_without_arguments_transformer_0.visit(var_0)

def test_case_2():
    str_0 = 'def some_Uethod(self):  uper()'
    var_0 = module_0.parse(str_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_1 = super_without_arguments_transformer_0.visit(var_0)
    int_0 = 0
    var_2 = var_1.body[int_0]
    var_3 = var_2.body[int_0]

def test_case_3():
    str_0 = 'class Foo(Super):\n    def foo(self):\n        super()'
    var_0 = module_0.parse(str_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_0)
    var_1 = super_without_arguments_transformer_0.visit(var_0)
    var_2 = super_without_arguments_transformer_0.visit(var_1)