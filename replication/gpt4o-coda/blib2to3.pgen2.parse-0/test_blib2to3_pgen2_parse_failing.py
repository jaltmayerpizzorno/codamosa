# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = 57
        str_0 = 'Kq+hy-C'
        str_1 = 'qp:kHQte}"$aoL3qfO?'
        str_2 = '"i['
        str_3 = 'mT``k\r<5(o@A3'
        dict_0 = {str_0: grammar_0, str_1: grammar_0, str_2: grammar_0, str_3: int_0}
        tuple_0 = (str_0,)
        dict_1 = {}
        tuple_1 = (int_0, dict_0, tuple_0, dict_1)
        var_0 = module_1.lam_sub(grammar_0, tuple_1)
    except BaseException:
        pass

def test_case_1():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = 1322
        optional_0 = None
        none_type_0 = None
        tuple_0 = (int_0, optional_0, grammar_0, none_type_0)
        var_0 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = -1079
        tuple_0 = None
        parser_0 = module_1.Parser(grammar_0)
        bool_0 = parser_0.addtoken(int_0, grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1686.0
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.setup(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -2819
        str_0 = '\n        Compare two nodes for equality.\n\n        This calls the method _eq().\n        '
        int_1 = 347
        str_1 = 'r:\r[\x0cT;Q\x0ci=\x0bB:._GsDd'
        int_2 = -3356
        int_3 = 1814
        tuple_0 = (int_2, int_3)
        tuple_1 = (str_0, tuple_0)
        parse_error_0 = module_1.ParseError(str_1, int_0, str_0, tuple_1)
        int_4 = 39
        tuple_2 = (int_4, int_4)
        tuple_3 = (str_0, tuple_2)
        parse_error_1 = module_1.ParseError(str_0, int_1, str_0, tuple_3)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.setup()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = None
        str_0 = 'symbol2label'
        int_1 = -52
        int_2 = -2367
        int_3 = 809
        tuple_0 = (int_2, int_3)
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.shift(int_0, str_0, int_1, tuple_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 248
        list_0 = []
        int_1 = None
        int_2 = -333
        dict_0 = {int_1: int_2}
        tuple_0 = (list_0, dict_0)
        str_0 = 'i\tN^'
        int_3 = 2624
        int_4 = -354
        tuple_1 = (int_3, int_4)
        tuple_2 = (str_0, tuple_1)
        grammar_0 = module_0.Grammar()
        dict_1 = {}
        parser_0 = module_1.Parser(grammar_0, dict_1)
        parser_0.push(int_0, tuple_0, int_2, tuple_2)
    except BaseException:
        pass

def test_case_7():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.pop()
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = None
        int_0 = True
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0, grammar_0)
        bool_0 = parser_0.addtoken(int_0, parser_0, tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        grammar_0 = module_0.Grammar()
        tuple_0 = None
        str_0 = '0S2OvO)g4m?'
        str_1 = None
        dict_0 = {grammar_0: str_0, str_0: str_1, grammar_0: tuple_0, grammar_0: str_1}
        parser_0 = module_1.Parser(grammar_0, dict_0)
        int_0 = True
        bool_0 = parser_0.addtoken(int_0, str_1, tuple_0)
    except BaseException:
        pass