# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = 1232
        list_0 = [int_0]
        bool_0 = False
        node_0 = None
        list_1 = [bool_0, node_0]
        tuple_0 = (int_0, int_0, list_0, list_1)
        var_0 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -459
        str_0 = '/z$NP,WZUM\x0cs P\\Ei@'
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.pop()
    except BaseException:
        pass

def test_case_3():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.setup()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        str_0 = 'H%\x0c4H@0G]IuI0-? \r'
        int_1 = 2155
        tuple_0 = None
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        bool_0 = False
        parser_0 = module_1.Parser(grammar_0, bool_0)
        parser_0.shift(int_0, str_0, int_1, tuple_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -409
        int_1 = 2584
        tuple_0 = (int_0, int_1)
        list_0 = [tuple_0]
        list_1 = [list_0]
        dict_0 = {}
        tuple_1 = (list_1, dict_0)
        str_0 = '!U'
        tuple_2 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.push(int_0, tuple_1, int_0, tuple_2)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1
        str_0 = 'n9,K'
        tuple_0 = None
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        list_0 = [grammar_0, grammar_0, grammar_0, grammar_0]
        parser_0 = module_1.Parser(grammar_0, list_0)
        int_1 = parser_0.classify(int_0, str_0, tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -2856
        grammar_0 = module_0.Grammar()
        var_0 = grammar_0.copy()
        parser_0 = module_1.Parser(grammar_0, grammar_0)
        parser_0.setup(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 1
        str_0 = '\r\x0cJTZ,Waj'
        tuple_0 = None
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_1 = parser_0.classify(int_0, str_0, tuple_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = None
        str_0 = 'H%\x0c4H@0G]IuI0-? \r'
        grammar_0 = module_0.Grammar()
        optional_0 = None
        optional_1 = None
        tuple_0 = (int_0, str_0, optional_0, optional_1)
        var_0 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 1
        str_0 = 'd=D{d9|E&8a$ta'
        str_1 = '[^"\\\\]*(?:(?:\\\\.|"(?!""))[^"\\\\]*)*"""'
        tuple_0 = (int_0, int_0)
        tuple_1 = (str_1, tuple_0)
        parse_error_0 = module_1.ParseError(str_0, int_0, str_0, tuple_1)
        str_2 = 'n9,K'
        tuple_2 = (str_2, tuple_0)
        grammar_0 = module_0.Grammar()
        list_0 = [grammar_0, grammar_0, grammar_0, grammar_0]
        parser_0 = module_1.Parser(grammar_0, list_0)
        str_3 = None
        int_1 = parser_0.classify(int_0, str_3, tuple_2)
    except BaseException:
        pass