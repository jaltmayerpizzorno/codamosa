# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    pass

def test_case_1():
    grammar_0 = module_0.Grammar()
    int_0 = 763
    none_type_0 = None
    bool_0 = None
    list_0 = []
    tuple_0 = (int_0, none_type_0, bool_0, list_0)
    var_0 = module_1.lam_sub(grammar_0, tuple_0)

def test_case_2():
    grammar_0 = module_0.Grammar()
    parser_0 = module_1.Parser(grammar_0)