# Automatically generated by Pynguin.
import blib2to3.pytree as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1
    str_0 = 'APvj`/wDI?H'
    leaf_0 = module_0.Leaf(int_0, str_0)
    optional_0 = leaf_0.remove()

def test_case_2():
    int_0 = 1
    str_0 = 'APvj`/wDIH'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()

def test_case_3():
    int_0 = 1
    str_0 = 'APv#`JwDIH'
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)

def test_case_4():
    str_0 = '/g~DKPb8cQOR?'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)

def test_case_5():
    leaf_pattern_0 = module_0.LeafPattern()
    dict_0 = None
    negated_pattern_0 = module_0.NegatedPattern()
    bool_0 = negated_pattern_0.match(dict_0)

def test_case_6():
    int_0 = 1
    str_0 = 'APvj`/wDIH'
    leaf_0 = module_0.Leaf(int_0, str_0)
    str_1 = leaf_0.__repr__()

def test_case_7():
    int_0 = 114
    str_0 = 'Pvj`/wDI?H'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_pattern_0 = module_0.LeafPattern()
    var_0 = leaf_pattern_0.match(leaf_0, int_0)
    leaf_1 = leaf_0.clone()
    int_1 = 114
    leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)

def test_case_8():
    int_0 = 114
    str_0 = 'Pvj`/wDI?H'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()
    leaf_pattern_0 = module_0.LeafPattern()
    var_0 = leaf_pattern_0.match(leaf_1)
    leaf_2 = leaf_1.clone()
    int_1 = 114
    leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)

def test_case_9():
    int_0 = 1
    str_0 = 'N'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()
    str_1 = '-8GeU1'
    negated_pattern_0 = module_0.NegatedPattern()
    str_2 = 'Ka6 cH#\nJ^=L'
    bool_0 = negated_pattern_0.match_seq(str_2)
    wildcard_pattern_0 = module_0.WildcardPattern(str_1, int_0, int_0, str_1)
    any_0 = wildcard_pattern_0.optimize()

def test_case_10():
    str_0 = '/g~DKPb8cQOR?'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_11():
    int_0 = 472
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    node_1 = node_0.clone()
    iterator_0 = node_1.pre_order()

def test_case_12():
    str_0 = 'm'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_13():
    int_0 = 1
    str_0 = '/'
    str_1 = 'V`IFS$8B;Md6O\x0b\t4'
    list_0 = None
    list_1 = [list_0, str_0]
    leaf_0 = module_0.Leaf(int_0, str_1, list_0, list_1)
    optional_0 = leaf_0.remove()

def test_case_14():
    int_0 = -1868
    int_1 = 2089
    list_0 = []
    str_0 = '&are+name'
    node_0 = module_0.Node(int_1, list_0, str_0)
    iterator_0 = node_0.pre_order()
    node_1 = node_0.clone()
    node_1.insert_child(int_0, node_0)
    leaf_pattern_0 = module_0.LeafPattern()

def test_case_15():
    int_0 = 114
    str_0 = 'Pvj`/wDI?H'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()
    leaf_pattern_0 = module_0.LeafPattern()
    var_0 = leaf_pattern_0.match(leaf_1, int_0)
    leaf_2 = leaf_1.clone()
    int_1 = 114
    list_0 = [leaf_1, leaf_2, leaf_0]
    leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)
    int_2 = 367
    node_0 = module_0.Node(int_2, list_0)
    node_0.update_sibling_maps()

def test_case_16():
    int_0 = 114
    str_0 = 'Pvj`/wDI?H'
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()
    leaf_pattern_0 = module_0.LeafPattern()
    var_0 = leaf_pattern_0.match(leaf_1, int_0)
    leaf_2 = leaf_1.clone()
    int_1 = 114
    list_0 = [leaf_1, leaf_2, leaf_0]
    leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)
    int_2 = 367
    node_0 = module_0.Node(int_2, list_0)
    node_1 = node_0.clone()
    node_1.update_sibling_maps()

def test_case_17():
    negated_pattern_0 = module_0.NegatedPattern()
    var_0 = []
    iterator_0 = negated_pattern_0.generate_matches(var_0)
    var_1 = list(iterator_0)

def test_case_18():
    str_0 = '-'
    int_0 = 771
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_19():
    int_0 = 1
    str_0 = 'APvj`/wDIH'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_20():
    str_0 = 'Hk%(Zp'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    list_0 = []
    bool_0 = wildcard_pattern_0.match_seq(list_0)

def test_case_21():
    int_0 = 1
    str_0 = 'ivu=pc'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0, str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_22():
    int_0 = 1
    str_0 = '1'
    leaf_0 = module_0.Leaf(int_0, str_0)
    iterator_0 = leaf_0.post_order()
    var_0 = list(iterator_0)

def test_case_23():
    int_0 = 0
    str_0 = 'APvj`/wDIH'
    leaf_0 = module_0.Leaf(int_0, str_0)
    str_1 = leaf_0.get_suffix()

def test_case_24():
    int_0 = 256
    var_0 = []
    node_0 = module_0.Node(int_0, var_0)
    var_1 = []
    var_2 = None
    str_0 = ''
    node_1 = module_0.Node(int_0, var_1, var_2, str_0)
    var_3 = []
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = [int_1, int_2, int_3]
    node_2 = module_0.Node(int_0, var_3, var_2, str_0, int_4)
    var_4 = []
    var_5 = []
    node_3 = module_0.Node(int_0, var_4, var_5)
    var_6 = []
    node_4 = module_0.Node(int_0, var_6, var_2)
    var_7 = []
    var_8 = []
    node_5 = module_0.Node(int_0, var_7, var_2, var_8)
    var_9 = []
    var_10 = []
    node_6 = module_0.Node(int_0, var_9, var_2, str_0, var_10)