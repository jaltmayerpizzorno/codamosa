# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0

def test_case_0():
    module_0.test()

def test_case_1():
    str_0 = "'\\x00\\n\\t'"
    str_1 = module_0.evalString(str_0)
    str_2 = '"\\377\\n\\t"'
    str_3 = module_0.evalString(str_2)