# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0
import typesystem.base as module_1

def test_case_0():
    try:
        str_0 = 'Pfb>tf4J3!u^!}'
        int_0 = -2182
        token_0 = module_0.Token(str_0, int_0, int_0)
        str_1 = token_0.__repr__()
        list_0 = [str_1, str_1, str_0, str_0]
        token_1 = token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'w\x0cQ{hvVI?n{\rH'
        list_0 = [str_0]
        str_1 = '"p,O+'
        int_0 = -1343
        int_1 = 6
        list_token_0 = module_0.ListToken(str_1, int_0, int_1)
        list_1 = [list_token_0, list_token_0, list_token_0, list_token_0]
        scalar_token_0 = module_0.ScalarToken(list_1, int_1, int_0, str_1)
        int_2 = 4
        token_0 = module_0.Token(scalar_token_0, int_2, int_0)
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '3E-v'
        list_0 = []
        int_0 = 1123
        token_0 = module_0.Token(str_0, int_0, int_0)
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -5
        token_0 = module_0.Token(int_0, int_0, int_0)
        bool_0 = token_0.__eq__(int_0)
        bool_1 = token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        list_1 = [dict_0, dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_1)
        int_0 = 3
        list_token_0 = module_0.ListToken(list_0, int_0, int_0)
        token_0 = dict_token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        list_1 = [dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_1)
        list_2 = []
        token_0 = dict_token_0.lookup(list_2)
        bool_0 = token_0.__eq__(list_1)
        bool_1 = token_0.__eq__(dict_token_0)
        int_0 = 3
        int_1 = 35
        list_token_0 = module_0.ListToken(list_2, int_0, int_1)
        bool_2 = token_0.__eq__(list_1)
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -710
        int_1 = None
        position_0 = module_1.Position(int_0, int_0, int_1)
        float_0 = 1852.230955
        int_2 = -923
        str_0 = 'cUdZ5Wdk'
        scalar_token_0 = module_0.ScalarToken(float_0, int_2, int_2, str_0)
        dict_0 = {scalar_token_0: scalar_token_0}
        list_0 = [dict_0, scalar_token_0, int_2]
        dict_token_0 = module_0.DictToken(*list_0)
        dict_token_1 = module_0.DictToken()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0]
        int_0 = 169
        str_0 = None
        scalar_token_0 = module_0.ScalarToken(list_0, int_0, int_0, str_0)
        dict_0 = {}
        list_1 = [dict_0, dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_1)
        list_2 = []
        token_0 = dict_token_0.lookup(list_2)
        bool_1 = token_0.__eq__(scalar_token_0)
        token_1 = dict_token_0.lookup(list_2)
        token_2 = dict_token_0.lookup(list_2)
        str_1 = token_2.__repr__()
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_0)
        list_1 = []
        token_0 = dict_token_0.lookup(list_1)
        token_1 = token_0.lookup(list_1)
        bool_0 = token_0.__eq__(list_0)
        int_0 = -2028
        token_2 = module_0.Token(dict_0, int_0, int_0)
        bool_1 = token_0.__eq__(dict_token_0)
        int_1 = 51
        str_0 = "')\tr\tJB=Pf-OBU55HJ"
        list_token_0 = module_0.ListToken(list_1, int_1, int_1, str_0)
        bool_2 = token_0.__eq__(list_token_0)
        token_3 = dict_token_0.lookup(list_1)
        str_1 = token_3.__repr__()
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        list_1 = [dict_0, dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_1)
        list_2 = []
        token_0 = dict_token_0.lookup(list_2)
        token_1 = token_0.lookup(list_2)
        int_0 = -2028
        token_2 = module_0.Token(dict_0, int_0, int_0)
        bool_0 = token_0.__eq__(dict_token_0)
        int_1 = 3
        int_2 = None
        str_0 = "')\tr\tJB=Pf-OBU55HJ"
        list_token_0 = module_0.ListToken(list_0, int_2, int_1, str_0)
        bool_1 = token_0.__eq__(list_token_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '4XS_*-q!1L"3oH'
        list_0 = None
        list_1 = [str_0, list_0]
        int_0 = 482
        int_1 = -2122
        list_token_0 = module_0.ListToken(list_1, int_0, int_1)
        token_0 = list_token_0.lookup_key(list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'c'
        int_0 = 1
        scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0, str_0)
        var_0 = scalar_token_0.start.line
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'c'
        int_0 = -3
        int_1 = 1
        scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_1, str_0)
        var_0 = scalar_token_0.start.line
    except BaseException:
        pass