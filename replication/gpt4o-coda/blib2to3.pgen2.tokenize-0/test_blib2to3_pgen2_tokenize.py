# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = -3936
    tuple_0 = (int_0, int_0)
    untokenizer_0.add_whitespace(tuple_0)

def test_case_2():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = -32
    str_0 = ">2c#W6-:a'0@T+'"
    tuple_0 = (int_0, str_0)
    tuple_1 = (int_0, int_0)
    untokenizer_1 = module_0.Untokenizer()
    untokenizer_2 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_1)
    list_0 = [tuple_0]
    str_1 = untokenizer_0.untokenize(list_0)