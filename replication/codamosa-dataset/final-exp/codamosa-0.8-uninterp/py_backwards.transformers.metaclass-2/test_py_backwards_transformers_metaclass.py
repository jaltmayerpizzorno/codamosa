# Automatically generated by Pynguin.
import py_backwards.transformers.metaclass as module_0
import typed_ast.ast3 as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    metaclass_transformer_0 = module_0.MetaclassTransformer(var_0)
    str_0 = 'class A(object, metaclass=B): pass'
    var_1 = module_1.parse(str_0)
    var_2 = metaclass_transformer_0.visit(var_1)
    str_1 = 'from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)): pass'
    var_3 = module_1.parse(str_1)