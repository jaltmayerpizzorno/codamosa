# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    try:
        bytes_0 = b'GS\xa3\xd9'
        bool_0 = True
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        none_type_0 = None
        bool_0 = True
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(none_type_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '2rRSu\t='
        str_1 = ''
        dict_0 = {str_0: str_0, str_1: str_1}
        int_0 = None
        bool_0 = True
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(dict_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        choice_0 = module_0.Choice()
        list_0 = []
        int_0 = 1011
        var_0 = choice_0.__call__(list_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        str_0 = 'xVwF&q"t#bdLI0qv'
        int_0 = 1130
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(str_0, int_0)
        choice_1 = module_0.Choice(*list_0)
        choice_2 = module_0.Choice()
        dict_0 = {}
        choice_3 = module_0.Choice(**dict_0)
        sequence_0 = None
        list_1 = []
        choice_4 = module_0.Choice(*list_1)
        var_1 = choice_3.__call__(sequence_0)
    except BaseException:
        pass

def test_case_5():
    try:
        choice_0 = module_0.Choice()
        choice_1 = module_0.Choice()
        bool_0 = True
        str_0 = 'iN;\nJ>y'
        var_0 = choice_1.__call__(str_0, bool_0)
        bool_1 = True
        var_1 = choice_1.__call__(str_0, bool_1)
        var_2 = choice_0.__call__(str_0)
        str_1 = '!~C6sIK)6Ya_'
        list_0 = [var_1, str_0, bool_1, str_1]
        var_3 = choice_1.__call__(list_0, bool_0)
        int_0 = 1411
        bool_2 = True
        var_4 = choice_0.__call__(str_1, int_0, bool_2)
    except BaseException:
        pass

def test_case_6():
    try:
        choice_0 = module_0.Choice()
        str_0 = 's#U,!$WzG`q_1LZ]}\x0c3'
        set_0 = set()
        list_0 = [set_0, str_0]
        int_0 = -1119
        var_0 = choice_0.__call__(list_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        choice_0 = module_0.Choice()
        list_0 = [choice_0]
        list_1 = [choice_0, choice_0, choice_0, list_0]
        tuple_0 = (list_1,)
        bool_0 = True
        var_0 = choice_0.__call__(tuple_0, bool_0)
        str_0 = 'su|o>\t,v[]^}jv{St\x0bs'
        dict_0 = {str_0: str_0}
        choice_1 = module_0.Choice(**dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        choice_0 = module_0.Choice()
        str_0 = '!~C6sIK)6_'
        int_0 = 1442
        bool_0 = True
        var_0 = choice_0.__call__(str_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        choice_0 = module_0.Choice()
        choice_1 = module_0.Choice()
        str_0 = 'vn3|aCy2B'
        int_0 = 4434
        bool_0 = False
        var_0 = choice_0.__call__(str_0, int_0, bool_0)
        bool_1 = True
        str_1 = 'iN;"J>y'
        var_1 = choice_1.__call__(str_1, bool_1)
        list_0 = [var_1, str_1]
        list_1 = [choice_0, list_0]
        var_2 = choice_0.__call__(list_1)
        list_2 = [list_0, var_2]
        var_3 = choice_1.__call__(list_2, bool_1)
        bool_2 = True
        str_2 = "%' >WkGFyC[xOw=pMNU"
        int_1 = 15
        var_4 = choice_1.__call__(str_2, int_1, bool_2)
        str_3 = 'Q\\NUx$Q}7>o<unp#'
        var_5 = choice_1.__call__(str_3)
        list_3 = [str_2]
        var_6 = choice_1.__call__(list_3)
        optional_0 = None
        var_7 = choice_1.__call__(optional_0)
    except BaseException:
        pass