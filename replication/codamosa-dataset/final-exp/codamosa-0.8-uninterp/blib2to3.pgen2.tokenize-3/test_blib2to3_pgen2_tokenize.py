# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = -382
    tuple_0 = (int_0, int_0)
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    str_0 = '.qg[5f%\n'
    var_0 = module_0.group()
    dict_0 = {var_0: str_0}
    str_1 = module_0.untokenize(dict_0)

def test_case_4():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = 1
    str_0 = ''
    var_0 = (int_0, str_0)
    var_1 = (int_0, str_0)
    int_1 = 3
    var_2 = (int_1, str_0)
    var_3 = [var_1, var_2]
    untokenizer_0.compat(var_0, var_3)

def test_case_5():
    bytes_0 = b"# coding: ISO-8859-1\n# stuff\n# more stuff\n#!/usr/bin/env python\n'''hello world'''\n"
    var_0 = bytes(bytes_0)
    var_1 = [var_0]
    var_2 = iter(var_1)
    var_3 = var_2.__next__
    tuple_0 = module_0.detect_encoding(var_3)
    var_4 = [var_0]
    var_5 = iter(var_4)

def test_case_6():
    str_0 = '#tW{;{RVmMdI3@c_@O'
    str_1 = [str_0]
    int_0 = -27
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)
    var_0 = iter(str_1)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    untokenizer_1 = module_0.Untokenizer()
    str_2 = untokenizer_1.untokenize(iterator_0)