# Automatically generated by Pynguin.
import pytutils.trees as module_0
import collections as module_1

def test_case_0():
    try:
        tree_0 = module_0.Tree()
        str_0 = '-'
        var_0 = tree_0.__getitem__(tree_0, tree_0, str_0)
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
        str_0 = 'rB_UaI,rG}-S0-N'
        int_0 = 1
        var_0 = module_0.set_tree_node(str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x80\xf0;['
        registry_tree_0 = module_0.RegistryTree()
        tree_0 = module_0.Tree()
        var_0 = tree_0.__setitem__(bytes_0, registry_tree_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b's\xa7\x16\xd3\xebW-R?"\x8fB\x98'
        tree_0 = module_0.Tree()
        tuple_0 = (bytes_0,)
        tuple_1 = ()
        list_0 = [tuple_1]
        float_0 = -877.0
        tree_1 = module_0.Tree(tuple_1, list_0, float_0)
        var_0 = tree_1.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'Q\x02\xac\xbf\xc7'
        int_0 = -1569
        tree_0 = module_0.Tree(bytes_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tree_0 = module_0.Tree()
        bool_0 = True
        var_0 = tree_0.__setitem__(tree_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        registry_tree_0 = module_0.RegistryTree()
        tree_0 = module_0.Tree()
        str_0 = 'n(CHg3wj^'
        defaultdict_0 = module_1.defaultdict()
        str_1 = 'LoE)*Fu#x*!'
        var_0 = module_0.get_tree_node(tree_0, str_0, defaultdict_0, str_1)
    except BaseException:
        pass