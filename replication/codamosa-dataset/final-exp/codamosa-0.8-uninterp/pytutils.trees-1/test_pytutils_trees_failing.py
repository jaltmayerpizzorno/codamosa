# Automatically generated by Pynguin.
import collections as module_0
import pytutils.trees as module_1

def test_case_0():
    try:
        defaultdict_0 = module_0.defaultdict()
        str_0 = 'arr:0'
        var_0 = module_1.get_tree_node(defaultdict_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'SkTAQv'
        set_0 = {str_0}
        var_0 = module_1.get_tree_node(str_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '.H0-'
        bytes_0 = None
        set_0 = {str_0, bytes_0, str_0, bytes_0}
        var_0 = module_1.set_tree_node(str_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        bytes_0 = b'D\x85\x98'
        int_0 = 478
        str_0 = '_member'
        tree_0 = module_1.Tree(dict_0)
        var_0 = tree_0.__setitem__(bytes_0, int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2431
        float_0 = None
        bytes_0 = b'e\xe2\xf8\xa8\xb73\xcf.Tp\xd0\xea\xdf4\x8a<\xb98KJ'
        registry_tree_0 = module_1.RegistryTree(int_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '_K>'
        registry_tree_0 = module_1.RegistryTree(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        tree_0 = module_1.Tree()
        var_0 = tree_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'x;XH/'
        set_0 = set()
        tree_0 = module_1.Tree()
        var_0 = tree_0.__setitem__(str_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = module_1.tree()
        dict_0 = {}
        list_0 = [dict_0, dict_0, var_0]
        str_0 = '_CaEO9$aj@-ck'
        int_0 = 63
        var_1 = module_1.get_tree_node(list_0, str_0, int_0, list_0)
    except BaseException:
        pass