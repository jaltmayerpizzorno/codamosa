# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0

def test_case_0():
    pass

def test_case_1():
    grammar_0 = module_0.Grammar()

def test_case_2():
    str_0 = ';q""SXYah:;'
    grammar_0 = module_0.Grammar()
    grammar_0.dump(str_0)

def test_case_3():
    grammar_0 = module_0.Grammar()
    grammar_0.report()

def test_case_4():
    grammar_0 = module_0.Grammar()
    var_0 = grammar_0.copy()
    grammar_1 = module_0.Grammar()
    str_0 = '^[4y=A<\\ST!\tX$(z;c!'
    grammar_0.load(str_0)
    grammar_2 = module_0.Grammar()
    var_1 = grammar_2.copy()
    grammar_3 = module_0.Grammar()
    grammar_3.dump(str_0)
    grammar_0.report()
    grammar_1.report()
    grammar_4 = module_0.Grammar()
    grammar_4.load(str_0)