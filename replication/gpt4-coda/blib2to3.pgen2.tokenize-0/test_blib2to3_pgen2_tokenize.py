# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = -166
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    str_0 = 'dS\x0b_'
    int_0 = 4341
    str_1 = 'c3M^JL;'
    tuple_0 = (int_0, str_1)
    callable_0 = None
    iterator_0 = module_0.generate_tokens(callable_0)
    dict_0 = {str_1: iterator_0, tuple_0: tuple_0}
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.compat(tuple_0, dict_0)
    list_0 = [str_0, str_0]
    untokenizer_1 = module_0.Untokenizer()
    var_0 = module_0.any(*list_0)

def test_case_4():
    list_0 = []
    var_0 = module_0.any()
    str_0 = module_0.untokenize(list_0)
    int_0 = -2
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    tuple_1 = (int_0, str_0)
    bytes_0 = b'\x05\xb8\x97\x1f\xeb\xf5Y\x1a1\xcc\xa3\x85I\xfa*\xff'
    tuple_2 = (int_0, str_0)
    list_1 = [tuple_0, tuple_1, bytes_0]
    untokenizer_0.compat(tuple_2, list_1)
    var_1 = module_0.maybe()