# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = -918
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    list_0 = []
    str_0 = module_0.untokenize(list_0)

def test_case_4():
    bytes_0 = b'5\xcfHt'
    untokenizer_0 = module_0.Untokenizer()
    list_0 = [bytes_0]
    str_0 = 'pr'
    str_1 = 'E[KO@!`w^F@%='
    dict_0 = {str_0: str_0, str_0: str_1, str_1: list_0, str_0: str_1}
    str_2 = module_0.untokenize(dict_0)
    int_0 = 0
    tuple_0 = (int_0, int_0)
    untokenizer_0.add_whitespace(tuple_0)
    str_3 = ''
    tuple_1 = (int_0, str_3)
    untokenizer_0.compat(tuple_1, list_0)
    var_0 = module_0.any()
    grammar_0 = module_1.Grammar()

def test_case_5():
    str_0 = 'x == 2'
    str_1 = "    print('hello')"
    str_2 = 'A`xB1o\x0c4=shmIy+5\\)['
    str_3 = [str_2, str_1, str_0, str_1, str_1, str_2, str_1, str_1]
    var_0 = iter(str_3)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [t for t in iterator_0]

def test_case_6():
    str_0 = "pritnt('done')"
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [t for t in iterator_0]

def test_case_7():
    str_0 = 'if True:'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [t for t in iterator_0]

def test_case_8():
    str_0 = 'i =7'
    str_1 = '\r[/WoCvM^RXR}B'
    str_2 = '?IQ_2{MWf7$a)6\nfuy'
    str_3 = "    print('goodbye')"
    str_4 = [str_0, str_0, str_1, str_2, str_3, str_3, str_0]
    var_0 = iter(str_4)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [t for t in iterator_0]

def test_case_9():
    str_0 = 'x == 2'
    str_1 = 'Y.lq"+VZxOHFPS'
    str_2 = "    print('hello')"
    str_3 = 'A`xB1o\x0c4=shmIy+5\\)['
    str_4 = "print('done')"
    str_5 = [str_3, str_4, str_0, str_1, str_2, str_3, str_4, str_4]
    var_0 = iter(str_5)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [t for t in iterator_0]