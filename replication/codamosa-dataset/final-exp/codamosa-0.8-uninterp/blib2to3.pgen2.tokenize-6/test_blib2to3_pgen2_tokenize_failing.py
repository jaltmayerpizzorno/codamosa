# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        bytes_0 = b'='
        token_error_0 = module_0.TokenError()
        set_0 = None
        str_0 = 'dkDSH|^d)XQ'
        str_1 = 'G"Y.8&rA-Z}tv[.'
        var_0 = module_0.printtoken(bytes_0, token_error_0, set_0, str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 't'
        set_0 = {str_0}
        tuple_0 = None
        str_1 = '{nt^y!!H['
        dict_0 = {str_0: tuple_0, str_1: str_1}
        bytes_0 = b'y\x8a\x80j\xab\t>\x92'
        list_0 = [bytes_0]
        tuple_1 = (str_0, list_0)
        list_1 = [str_1, bytes_0]
        var_0 = module_0.printtoken(set_0, dict_0, tuple_1, list_1, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'V'
        module_0.tokenize(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ':k@TPRsk\r4Z$`;ut'
        str_1 = module_0.untokenize(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 55
        untokenizer_0 = module_0.Untokenizer()
        str_0 = '`}'
        tuple_0 = (int_0, str_0)
        float_0 = 634.34241
        untokenizer_1 = module_0.Untokenizer()
        untokenizer_1.compat(tuple_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        tuple_0 = module_0.detect_encoding(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\x84'
        int_0 = 678
        str_0 = '\rfox 1WX)nSwe+ktfF'
        tuple_0 = (int_0, str_0)
        float_0 = -635.0
        dict_0 = {float_0: tuple_0, tuple_0: tuple_0, int_0: bytes_0, int_0: tuple_0}
        dict_1 = {bytes_0: int_0, bytes_0: str_0, tuple_0: dict_0}
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.compat(tuple_0, dict_1)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 2
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        str_0 = module_0.untokenize(list_0)
        token_error_0 = module_0.TokenError()
        list_1 = [token_error_0, str_0, list_0, str_0]
        tuple_0 = module_0.detect_encoding(list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -355
        untokenizer_0 = module_0.Untokenizer()
        int_1 = 44
        int_2 = 3193
        str_0 = 'ZJa?DN2uG[SLS\t*'
        tuple_0 = (int_2, str_0)
        list_0 = []
        untokenizer_0.compat(tuple_0, list_0)
        list_1 = [int_1, int_1, int_0]
        stop_tokenizing_0 = module_0.StopTokenizing(*list_1)
        callable_0 = None
        module_0.tokenize(callable_0)
    except BaseException:
        pass

def test_case_10():
    try:
        callable_0 = None
        stop_tokenizing_0 = module_0.StopTokenizing()
        grammar_0 = module_1.Grammar()
        iterator_0 = module_0.generate_tokens(callable_0, grammar_0)
        str_0 = module_0.untokenize(iterator_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -355
        int_1 = 548
        tuple_0 = (int_0, int_1)
        str_0 = "#B\rxc'|79_>9f).H?d`"
        tuple_1 = (int_0, str_0)
        set_0 = {tuple_0, tuple_1, tuple_0, str_0}
        untokenizer_0 = module_0.Untokenizer()
        str_1 = untokenizer_0.untokenize(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = module_0.any()
        int_0 = -1406
        str_0 = '0=noN'
        dict_0 = {str_0: int_0}
        untokenizer_0 = module_0.Untokenizer()
        stop_tokenizing_0 = module_0.StopTokenizing()
        str_1 = untokenizer_0.untokenize(dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'x=1 + 2'
        str_1 = [str_0]
        var_0 = iter(str_1)
        var_1 = var_0.__next__
        var_2 = module_0.tokenize_loop(var_1, str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        var_0 = []
        str_0 = 'x=1 + 2'
        str_1 = [str_0]
        var_1 = iter(var_0)
        var_2 = var_1.__next__
        var_3 = module_0.tokenize_loop(var_2, str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        var_0 = []
        var_1 = var_0.append
        str_0 = '(tR68!-PP'
        var_2 = iter(str_0)
        var_3 = var_2.__next__
        var_4 = module_0.tokenize_loop(var_3, var_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = ' Test for tokenize_loop() '
        var_0 = []
        var_1 = var_0.append
        str_1 = [str_0]
        var_2 = iter(str_1)
        var_3 = var_2.__next__
        var_4 = module_0.tokenize_loop(var_3, var_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = ' Test for tokenize_loop() '
        var_0 = []
        var_1 = iter(str_0)
        var_2 = var_1.__next__
        var_3 = module_0.tokenize_loop(var_2, var_0)
    except BaseException:
        pass