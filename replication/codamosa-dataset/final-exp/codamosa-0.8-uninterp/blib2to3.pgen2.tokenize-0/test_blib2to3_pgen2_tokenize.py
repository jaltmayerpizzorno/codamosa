# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = -290
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    dict_0 = {}
    str_0 = module_0.untokenize(dict_0)
    var_0 = module_0.any()

def test_case_4():
    bytes_0 = b' \t\x0c\n\r'
    var_0 = iter(bytes_0)
    var_1 = var_0.__next__
    bytes_1 = [bytes_0, bytes_0]
    var_2 = iter(bytes_1)
    var_3 = var_2.__next__
    tuple_0 = module_0.detect_encoding(var_3)
    bytes_2 = b' \t\x0c\n\r#'
    bytes_3 = [bytes_2]
    stop_tokenizing_0 = module_0.StopTokenizing()
    var_4 = iter(bytes_3)

def test_case_5():
    bytes_0 = b'\xff\xd4\x03\x1d\xbf\xf8\xfe\x8b\x81\xb5\xb2a\xb1'
    bytes_1 = [bytes_0]
    var_0 = iter(bytes_1)
    var_1 = var_0.__next__
    tuple_0 = module_0.detect_encoding(var_1)
    bytes_2 = [bytes_0, bytes_0]
    var_2 = iter(bytes_2)
    var_3 = var_2.__next__
    tuple_1 = module_0.detect_encoding(var_3)
    stop_tokenizing_0 = module_0.StopTokenizing()

def test_case_6():
    str_0 = 'if 1: #comment\n'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [x for x in iterator_0]

def test_case_7():
    str_0 = 'prin1'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [x for x in iterator_0]

def test_case_8():
    bytes_0 = b'# -*- coding: latin-1 -*-\n'
    bytes_1 = [bytes_0]
    var_0 = iter(bytes_1)
    var_1 = var_0.__next__
    tuple_0 = module_0.detect_encoding(var_1)
    int_0 = 5
    var_2 = bytes_0[:int_0]
    var_3 = bytes_0[int_0:]
    var_4 = [var_2, var_3]
    var_5 = iter(var_4)
    var_6 = var_5.__next__

def test_case_9():
    str_0 = 'if 1: #comment\n'
    str_1 = '  print(1)\n'
    str_2 = [str_0, str_1]
    var_0 = iter(str_2)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = [x for x in iterator_0]