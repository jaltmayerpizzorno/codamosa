# Automatically generated by Pynguin.
import blib2to3.pgen2.parse as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        grammar_0 = None
        int_0 = 17
        float_0 = None
        str_0 = '8pZ8@pHn[gG\x0bAP,.Hf8d'
        int_1 = -1077
        int_2 = 1995
        tuple_0 = (int_1, int_2)
        tuple_1 = (str_0, tuple_0)
        var_0 = None
        str_1 = ''
        list_0 = [var_0, str_1]
        tuple_2 = (int_0, float_0, tuple_1, list_0)
        var_1 = module_0.lam_sub(grammar_0, tuple_2)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        list_0 = [int_0]
        tuple_0 = None
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        bool_0 = parser_0.addtoken(int_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        parser_0.setup()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 611
        parser_0 = None
        str_0 = ',z[)@8k'
        int_1 = 2283
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_1.Grammar()
        parser_1 = module_0.Parser(grammar_0)
        parser_1.shift(int_0, parser_0, int_0, tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 170
        list_0 = None
        dict_0 = None
        tuple_0 = (list_0, dict_0)
        tuple_1 = None
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        parser_0.push(int_0, tuple_0, int_0, tuple_1)
    except BaseException:
        pass

def test_case_5():
    try:
        grammar_0 = module_1.Grammar()
        var_0 = grammar_0.copy()
        bool_0 = True
        parser_0 = module_0.Parser(grammar_0, bool_0)
        parser_0.pop()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1
        grammar_0 = module_1.Grammar()
        str_0 = 'GM\nF'
        parser_0 = module_0.Parser(grammar_0, str_0)
        str_1 = 'SQL0>[~W}}nx|'
        tuple_0 = None
        tuple_1 = (str_1, tuple_0)
        int_1 = parser_0.classify(int_0, str_1, tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -970
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        parser_0.setup(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 1628
        str_0 = 'Parse the .h file written by pgen.  (Internal)\n\n        This file is a sequence of #define statements defining the\n        nonterminals of the grammar as numbers.  We build two tables\n        mapping the numbers to names and back.\n\n        '
        grammar_0 = module_1.Grammar()
        optional_0 = None
        path_like_0 = None
        tuple_0 = (int_0, str_0, optional_0, path_like_0)
        var_0 = module_0.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 1
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        str_0 = 'EH'
        int_1 = parser_0.classify(int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 1
        grammar_0 = module_1.Grammar()
        parser_0 = module_0.Parser(grammar_0)
        str_0 = None
        tuple_0 = (int_0, int_0)
        tuple_1 = (str_0, tuple_0)
        int_1 = parser_0.classify(int_0, str_0, tuple_1)
    except BaseException:
        pass