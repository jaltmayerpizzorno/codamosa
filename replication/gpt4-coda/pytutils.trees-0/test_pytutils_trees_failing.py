# Automatically generated by Pynguin.
import pytutils.trees as module_0

def test_case_0():
    try:
        tree_0 = module_0.Tree()
        str_0 = 'U$/8Oq/mk)NsFd-8lCG~'
        var_0 = tree_0.__getitem__(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tree_0 = module_0.Tree()
        var_0 = tree_0.__getitem__(tree_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tree_0 = module_0.Tree()
        bytes_0 = b'\xa0\xf6\x10c'
        var_0 = tree_0.__setitem__(tree_0, bytes_0, tree_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        tree_0 = module_0.Tree(str_0)
        var_0 = tree_0.__getitem__(tree_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'n.\x06\x15\x0fi}\x81\xea\x05\xab'
        str_0 = ''
        tree_0 = module_0.Tree(str_0)
        var_0 = tree_0.__getitem__(bytes_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = None
        float_0 = -4.53
        dict_0 = {float_0: float_0}
        bool_1 = True
        tuple_0 = (float_0, dict_0, dict_0, bool_1)
        str_0 = ''
        str_1 = 'XbFsfxK\nd0gDHvu~ASB3'
        tuple_1 = (bool_0, tuple_0, str_0, str_1)
        str_2 = '2<9uaP^\tvk)nnCI;8x\t7'
        float_1 = -1047.91237
        tree_0 = module_0.Tree(tuple_1, str_2, float_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b''
        str_0 = '?O[nZ8\x0cA2 6{a'
        tree_0 = module_0.Tree()
        var_0 = tree_0.__setitem__(bytes_0, str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'n.\x06\x15\x0fi}\x81\xea\x05\xab'
        str_0 = ''
        float_0 = -836.0
        str_1 = 'qV|!\t;?clpuc'
        var_0 = module_0.get_tree_node(bytes_0, str_0, float_0, str_1)
    except BaseException:
        pass