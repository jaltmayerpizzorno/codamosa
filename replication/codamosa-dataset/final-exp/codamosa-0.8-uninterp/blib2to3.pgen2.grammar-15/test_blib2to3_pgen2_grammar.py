# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0

def test_case_0():
    pass

def test_case_1():
    grammar_0 = module_0.Grammar()
    grammar_0.report()

def test_case_2():
    str_0 = '%+`YpAWB"(b~'
    grammar_0 = module_0.Grammar()
    grammar_0.dump(str_0)

def test_case_3():
    str_0 = '[:;.,`@]'
    grammar_0 = module_0.Grammar()
    grammar_0.load(str_0)
    grammar_0.dump(str_0)

def test_case_4():
    grammar_0 = module_0.Grammar()
    var_0 = grammar_0.copy()