# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        bool_0 = False
        untokenizer_0 = module_0.Untokenizer()
        set_0 = {untokenizer_0, bool_0, untokenizer_0}
        int_0 = 3459
        tuple_0 = (int_0,)
        var_0 = module_0.printtoken(bool_0, untokenizer_0, set_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1
        module_0.tokenize(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'utf-8'
        str_1 = module_0.untokenize(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 109
        str_0 = 'P'
        tuple_0 = (int_0, str_0)
        bool_0 = False
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.compat(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 680
        var_0 = module_0.maybe()
        untokenizer_0 = module_0.Untokenizer()
        str_0 = '%!~Wi|Ow+llW(rSb\t'
        tuple_0 = (int_0, str_0)
        list_0 = [int_0, int_0]
        untokenizer_1 = module_0.Untokenizer()
        untokenizer_1.compat(tuple_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = None
        tuple_1 = module_0.detect_encoding(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        untokenizer_0 = module_0.Untokenizer()
        int_0 = 2925
        int_1 = -886
        tuple_0 = (int_0, int_1)
        untokenizer_0.add_whitespace(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = module_0.group()
        int_0 = -284
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
        var_1 = module_0.any()
        var_2 = module_0.maybe()
        str_0 = ''
        str_1 = module_0.untokenize(str_0)
        callable_0 = None
        str_2 = 'x!@'
        tuple_1 = (int_0, str_2)
        list_0 = [var_0, tuple_1]
        untokenizer_0.compat(tuple_1, list_0)
        module_0.tokenize(callable_0)
    except BaseException:
        pass

def test_case_9():
    try:
        untokenizer_0 = module_0.Untokenizer()
        int_0 = True
        str_0 = ''
        tuple_0 = (int_0, str_0)
        iterable_0 = None
        untokenizer_0.compat(tuple_0, iterable_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -359
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
        var_0 = module_0.maybe()
        str_0 = ''
        str_1 = module_0.untokenize(str_0)
        untokenizer_1 = module_0.Untokenizer()
        int_1 = -728
        callable_0 = None
        grammar_0 = module_1.Grammar()
        tuple_1 = (int_1, int_1)
        str_2 = '\x0c\nLs(Hw'
        tuple_2 = (int_1, str_2)
        list_0 = []
        untokenizer_1.compat(tuple_2, list_0)
        untokenizer_1.add_whitespace(tuple_1)
        token_error_0 = module_0.TokenError()
        iterator_0 = module_0.generate_tokens(callable_0, grammar_0)
        bool_0 = False
        str_3 = 'I'
        var_1 = module_0.printtoken(token_error_0, token_error_0, iterator_0, bool_0, str_3)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 0
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
        int_1 = -1543
        tuple_1 = (int_0, int_1)
        untokenizer_1 = module_0.Untokenizer()
        untokenizer_1.add_whitespace(tuple_1)
        untokenizer_1.add_whitespace(tuple_1)
        var_0 = module_0.maybe()
        untokenizer_1.add_whitespace(tuple_1)
        int_2 = 2
        list_0 = []
        stop_tokenizing_0 = module_0.StopTokenizing(*list_0)
        tuple_2 = module_0.detect_encoding(int_2)
    except BaseException:
        pass