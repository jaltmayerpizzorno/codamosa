# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        complex_0 = None
        float_0 = -143.137247
        set_0 = {complex_0, complex_0, float_0, float_0}
        list_0 = [set_0, set_0]
        bool_0 = None
        var_0 = module_0.printtoken(complex_0, float_0, set_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callable_0 = None
        module_0.tokenize(callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callable_0 = None
        tuple_0 = module_0.detect_encoding(callable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        token_error_0 = None
        dict_0 = {token_error_0: token_error_0, token_error_0: token_error_0, token_error_0: token_error_0, token_error_0: token_error_0}
        dict_1 = {}
        token_error_1 = module_0.TokenError(**dict_1)
        str_0 = module_0.untokenize(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        untokenizer_0 = module_0.Untokenizer()
        int_0 = 4117
        tuple_0 = (int_0, int_0)
        untokenizer_0.add_whitespace(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = module_0.group()
        untokenizer_0 = module_0.Untokenizer()
        set_0 = {var_0}
        str_0 = untokenizer_0.untokenize(set_0)
        dict_0 = {str_0: str_0}
        str_1 = untokenizer_0.untokenize(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = module_0.group()
        dict_0 = {}
        untokenizer_0 = module_0.Untokenizer()
        str_0 = untokenizer_0.untokenize(dict_0)
        untokenizer_1 = module_0.Untokenizer()
        module_0.tokenize(untokenizer_1)
    except BaseException:
        pass

def test_case_7():
    try:
        untokenizer_0 = module_0.Untokenizer()
        int_0 = 1
        int_1 = 0
        int_2 = (int_0, int_1)
        untokenizer_0.add_whitespace(int_2)
        untokenizer_1 = module_0.Untokenizer()
        int_3 = 2
        int_4 = (int_3, int_1)
        untokenizer_1.add_whitespace(int_4)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = True
        str_0 = 'N'
        tuple_0 = (int_0, str_0)
        iterable_0 = None
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.compat(tuple_0, iterable_0)
    except BaseException:
        pass

def test_case_9():
    try:
        callable_0 = None
        var_0 = module_0.any()
        grammar_0 = module_1.Grammar()
        iterator_0 = module_0.generate_tokens(callable_0, grammar_0)
        untokenizer_0 = module_0.Untokenizer()
        str_0 = untokenizer_0.untokenize(iterator_0)
    except BaseException:
        pass

def test_case_10():
    try:
        untokenizer_0 = module_0.Untokenizer()
        var_0 = module_0.maybe()
        str_0 = 'kSY*w'
        bytes_0 = b'\xeb\x11\xcc'
        list_0 = [bytes_0]
        tuple_0 = (str_0, list_0)
        str_1 = untokenizer_0.untokenize(tuple_0)
    except BaseException:
        pass