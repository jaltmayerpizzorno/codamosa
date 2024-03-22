# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = -3295
        str_0 = '%s(%s, %r)'
        var_0 = grammar_0.copy()
        list_0 = [grammar_0]
        tuple_0 = (int_0, str_0, list_0, grammar_0)
        var_1 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_0 = 6
        bool_0 = parser_0.addtoken(int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 4923
        grammar_0 = module_0.Grammar()
        str_0 = "Prepare for parsing.\n\n        This *must* be called before starting to parse.\n\n        The optional argument is an alternative start symbol; it\n        defaults to the grammar's start symbol.\n\n        You can use a Parser instance to parse any number of programs;\n        each time you call setup() the parser is reset to an initial\n        state determined by the (implicit or explicit) start symbol.\n\n        "
        str_1 = 'd`LF&?]q=`\r.\twI'
        dict_0 = {str_0: str_0, str_1: str_1, str_0: str_0}
        parser_0 = module_1.Parser(grammar_0, dict_0)
        parser_0.setup(int_0)
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
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_0 = 1
        bool_0 = parser_0.addtoken(int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_0 = 60
        float_0 = None
        int_1 = 865
        str_0 = '\n        Initializer.  Takes optional type, content, and name.\n\n        The type, if given must be a token type (< 256).  If not given,\n        this matches any *leaf* node; the content may still be required.\n\n        The content, if given, must be a string.\n\n        If a name is given, the matching node is stored in the results\n        dict under that key.\n        '
        tuple_0 = None
        parse_error_0 = module_1.ParseError(str_0, int_1, str_0, tuple_0)
        tuple_1 = None
        parser_0.shift(int_0, float_0, int_1, tuple_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1735
        tuple_0 = None
        str_0 = "<#-'a"
        int_1 = 295
        tuple_1 = (int_1, int_0)
        tuple_2 = (str_0, tuple_1)
        grammar_0 = module_0.Grammar()
        list_0 = [grammar_0]
        parser_0 = module_1.Parser(grammar_0, list_0)
        parser_0.push(int_0, tuple_0, int_0, tuple_2)
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
        int_0 = 1390
        str_0 = 'iso-8859-1-'
        str_1 = ':*\x0cN2&'
        int_1 = 769
        tuple_0 = (int_1, int_0)
        tuple_1 = (str_1, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_2 = 1630
        list_0 = None
        tuple_2 = (int_2, str_0, tuple_1, list_0)
        var_0 = module_1.lam_sub(grammar_0, tuple_2)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0, grammar_0)
        str_0 = 'qOGj'
        int_0 = 1
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_0 = 1
        str_0 = None
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass