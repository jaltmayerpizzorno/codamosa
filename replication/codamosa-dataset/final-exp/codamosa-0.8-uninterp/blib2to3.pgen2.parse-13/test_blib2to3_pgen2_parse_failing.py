# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = 663
        str_0 = 'q?rG(d]eKr(I\x0c?x,J#O#'
        float_0 = -345.3
        grammar_1 = module_0.Grammar()
        list_0 = [grammar_1]
        tuple_0 = (int_0, str_0, float_0, list_0)
        var_0 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.setup()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 12
        str_0 = 'latin-1'
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -398
        dict_0 = {}
        int_1 = 39
        str_0 = "[^'\\\\]*(?:\\\\.[^'\\\\]*)*'"
        int_2 = None
        tuple_0 = (int_0, int_2)
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.shift(int_0, dict_0, int_1, tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 30
        tuple_0 = None
        str_0 = "\n        Equivalent to 'node.children.append(child)'. This method also sets the\n        child's parent attribute appropriately.\n        "
        int_1 = -2302
        tuple_1 = (int_1, int_0)
        tuple_2 = (str_0, tuple_1)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.push(int_0, tuple_0, int_0, tuple_2)
    except BaseException:
        pass

def test_case_5():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.pop()
    except BaseException:
        pass

def test_case_6():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = -5566
        str_0 = ' \t'
        str_1 = None
        tuple_0 = (int_0, int_0)
        tuple_1 = (str_1, tuple_0)
        tuple_2 = None
        tuple_3 = (int_0, str_0, tuple_1, tuple_2)
        var_0 = module_1.lam_sub(grammar_0, tuple_3)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -4
        str_0 = 'latin-1'
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0, str_0)
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        grammar_0 = module_0.Grammar()
        dict_0 = {grammar_0: grammar_0, grammar_0: grammar_0, grammar_0: grammar_0, grammar_0: grammar_0}
        parser_0 = module_1.Parser(grammar_0, dict_0)
        int_0 = -2627
        parser_0.setup(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 1
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        str_0 = '%$d'
        parser_0 = module_1.Parser(grammar_0, str_0)
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -6
        int_1 = 1
        optional_0 = None
        str_0 = 'z'
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_2 = parser_0.classify(int_1, optional_0, tuple_1)
    except BaseException:
        pass