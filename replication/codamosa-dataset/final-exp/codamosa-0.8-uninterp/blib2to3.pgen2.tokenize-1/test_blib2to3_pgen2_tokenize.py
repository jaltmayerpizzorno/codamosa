# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = -2264
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    var_0 = module_0.group()
    untokenizer_0 = module_0.Untokenizer()
    set_0 = {var_0}
    str_0 = untokenizer_0.untokenize(set_0)