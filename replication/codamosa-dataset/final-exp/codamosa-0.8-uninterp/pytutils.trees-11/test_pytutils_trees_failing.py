# Automatically generated by Pynguin.
import pytutils.trees as module_0

def test_case_0():
    try:
        tree_0 = module_0.Tree()
        str_0 = '^qP>dwZ.t-j"C?/C'
        var_0 = tree_0.__getitem__(str_0)
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
        bool_0 = True
        var_0 = tree_0.__setitem__(tree_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 600
        registry_tree_0 = module_0.RegistryTree(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tree_0 = module_0.Tree()
        float_0 = -1124.19325
        set_0 = set()
        bool_0 = True
        var_0 = tree_0.__setitem__(float_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tree_0 = module_0.Tree()
        registry_tree_0 = module_0.RegistryTree()
        str_0 = '; Q*]eRGT2@lIwv'
        str_1 = ' '
        str_2 = 'J@T{9SZ&O\\W&{z?#"'
        var_0 = tree_0.__getitem__(str_0, str_1, str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        set_0 = None
        bytes_0 = b'\xaa\xfet\x19\x96\x95\x17\xc6]'
        tree_0 = module_0.Tree(bool_0, set_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = None
        str_0 = 'D2)(7FIoyk'
        registry_tree_0 = module_0.RegistryTree(int_0, str_0)
        tree_0 = module_0.Tree(registry_tree_0)
        bool_0 = True
        str_1 = '!?B+\x0b\n:'
        str_2 = 'JyTxmo^'
        var_0 = module_0.get_tree_node(bool_0, str_0, str_1, str_2)
    except BaseException:
        pass