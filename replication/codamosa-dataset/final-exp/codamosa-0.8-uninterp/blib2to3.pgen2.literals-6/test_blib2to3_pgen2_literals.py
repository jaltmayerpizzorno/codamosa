# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0

def test_case_0():
    pass

def test_case_1():
    module_0.test()

def test_case_2():
    str_0 = '"\\0"'
    str_1 = module_0.evalString(str_0)
    module_0.test()

def test_case_3():
    str_0 = "'a string'"
    str_1 = module_0.evalString(str_0)
    str_2 = '"a string"'
    str_3 = module_0.evalString(str_2)
    str_4 = "'''a string'''"
    str_5 = module_0.evalString(str_4)