# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        callable_0 = None
        module_0.tokenize(callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        list_0 = [str_0, str_0]
        token_error_0 = module_0.TokenError(*list_0)
        str_1 = module_0.untokenize(token_error_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '&MTc'
        bytes_0 = b'\x07\xa2\xa9\xce\xecF4\x13'
        bytes_1 = None
        list_0 = [bytes_0, bytes_0, bytes_1, bytes_1]
        tuple_0 = (str_0, list_0)
        list_1 = [tuple_0, str_0]
        str_1 = module_0.untokenize(list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        callable_0 = None
        tuple_0 = module_0.detect_encoding(callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 3421
        tuple_0 = (int_0, int_0)
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.add_whitespace(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = module_0.group()
        str_0 = 'W`3N um-U+DZv1\x0b'
        untokenizer_0 = module_0.Untokenizer()
        int_0 = -3280
        tuple_0 = (int_0, int_0)
        untokenizer_0.add_whitespace(tuple_0)
        var_1 = module_0.group()
        str_1 = untokenizer_0.untokenize(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = module_0.any()
        int_0 = -1473
        list_0 = []
        var_1 = module_0.any()
        str_0 = module_0.untokenize(list_0)
        var_2 = module_0.maybe()
        untokenizer_0 = module_0.Untokenizer()
        tuple_0 = module_0.detect_encoding(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -807
        str_0 = 'u $Luw'
        tuple_0 = (int_0, str_0)
        int_1 = -1473
        list_0 = [tuple_0, tuple_0]
        str_1 = module_0.untokenize(list_0)
        untokenizer_0 = module_0.Untokenizer()
        int_2 = 1988
        tuple_1 = (int_1, int_2)
        str_2 = 'EkCI:'
        str_3 = ''
        str_4 = 'ZY6V>['
        dict_0 = {str_2: list_0, str_3: tuple_1, str_4: untokenizer_0}
        str_5 = untokenizer_0.untokenize(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        token_error_0 = module_0.TokenError()
        str_0 = '\x0cm<s|:S3IM='
        bool_0 = True
        bool_1 = True
        iterator_0 = module_0.generate_tokens(bool_1)
        grammar_0 = module_1.Grammar()
        iterator_1 = module_0.generate_tokens(iterator_0, grammar_0)
        dict_0 = {iterator_0: token_error_0, bool_0: bool_1, grammar_0: iterator_1}
        bool_2 = False
        var_0 = module_0.printtoken(str_0, bool_0, iterator_1, dict_0, bool_2)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -769
        str_0 = 'y$uw'
        tuple_0 = (int_0, str_0)
        list_0 = [tuple_0, tuple_0]
        str_1 = module_0.untokenize(list_0)
        int_1 = 1925
        tuple_1 = (int_0, int_1)
        untokenizer_0 = module_0.Untokenizer()
        tuple_2 = ()
        untokenizer_1 = module_0.Untokenizer()
        untokenizer_1.compat(tuple_0, tuple_2)
        untokenizer_1.add_whitespace(tuple_1)
        int_2 = 54
        tuple_3 = (int_2, str_1)
        untokenizer_0.compat(tuple_3, tuple_2)
        dict_0 = {tuple_3: tuple_0, int_1: int_2}
        untokenizer_1.compat(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -759
        str_0 = 'u $Luw'
        tuple_0 = (int_0, str_0)
        list_0 = [tuple_0, tuple_0]
        str_1 = module_0.untokenize(list_0)
        int_1 = 1952
        tuple_1 = (int_0, int_1)
        untokenizer_0 = module_0.Untokenizer()
        var_0 = module_0.maybe()
        tuple_2 = ()
        untokenizer_0.compat(tuple_0, tuple_2)
        untokenizer_0.add_whitespace(tuple_1)
        int_2 = 1
        tuple_3 = (int_2, str_1)
        untokenizer_0.compat(tuple_3, tuple_2)
        grammar_0 = module_1.Grammar()
        var_1 = grammar_0.copy()
        grammar_1 = module_1.Grammar()
        callable_0 = None
        iterator_0 = None
        module_0.tokenize(iterator_0, callable_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'while 1: #comment\n  pass\n'
        str_1 = [str_0]
        var_0 = iter(str_1)
        var_1 = var_0.__next__
        module_0.tokenize(var_1)
        var_2 = list(none_type_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'SD}{R0!sMi]n'
        str_1 = [str_0]
        var_0 = iter(str_1)
        var_1 = var_0.__next__
        module_0.tokenize(var_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'SD}{R0!sMi]n'
        var_0 = iter(str_0)
        var_1 = var_0.__next__
        module_0.tokenize(var_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\x0c'
        token_error_0 = module_0.TokenError()
        untokenizer_0 = module_0.Untokenizer()
        var_0 = iter(str_0)
        var_1 = var_0.__next__
        module_0.tokenize(var_1)
        var_2 = list(str_0)
        str_1 = '\x0c'
        set_0 = {str_1, str_0}
        str_2 = untokenizer_0.untokenize(set_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'whi= 1: com[n\n  pas\n'
        str_1 = [str_0]
        token_error_0 = module_0.TokenError()
        var_0 = iter(str_1)
        var_1 = var_0.__next__
        module_0.tokenize(var_1)
    except BaseException:
        pass