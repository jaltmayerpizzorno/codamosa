# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = 2736
    str_0 = '>6=*| '
    tuple_0 = (int_0, str_0)
    dict_0 = {str_0: str_0, str_0: int_0, str_0: tuple_0}
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.compat(tuple_0, dict_0)

def test_case_3():
    int_0 = False
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    var_0 = module_0.group()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_4():
    token_error_0 = module_0.TokenError()
    int_0 = -6066
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_1 = module_0.Untokenizer()
    untokenizer_1.add_whitespace(tuple_0)

def test_case_5():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = 1
    str_0 = '1'
    var_0 = (int_0, str_0)
    var_1 = [var_0]
    untokenizer_0.compat(var_0, var_1)

def test_case_6():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = 5
    str_0 = 'if'
    var_0 = (int_0, str_0)
    var_1 = (int_0, str_0)
    int_1 = 1
    var_2 = (int_1, str_0)
    var_3 = (int_0, str_0)
    str_1 = 'pass'
    var_4 = (int_0, str_1)
    var_5 = [var_1, var_2, var_3, str_1, var_4]
    untokenizer_0.compat(var_0, var_5)

def test_case_7():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = 5
    str_0 = 'if'
    var_0 = (int_0, str_0)
    var_1 = (int_0, str_0)
    int_1 = 1
    str_1 = ' '
    var_2 = (int_1, str_1)
    int_2 = 4
    var_3 = (int_2, str_1)
    var_4 = (int_2, str_1)
    str_2 = 'pass'
    var_5 = (int_2, str_2)
    var_6 = [var_1, var_2, var_3, var_4, var_5]
    untokenizer_0.compat(var_0, var_6)

def test_case_8():
    str_0 = '\n'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_9():
    str_0 = '|'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_10():
    str_0 = 'N\n'
    str_1 = [str_0]
    var_0 = iter(str_1)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_11():
    str_0 = "r'*E7cb-' V}/,%B"
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_12():
    str_0 = 'e@\x0c\rQ#\t'
    str_1 = [str_0, str_0, str_0, str_0]
    var_0 = iter(str_1)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_13():
    str_0 = 'e@\x0c\rQ#\t'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_14():
    str_0 = '\t'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)