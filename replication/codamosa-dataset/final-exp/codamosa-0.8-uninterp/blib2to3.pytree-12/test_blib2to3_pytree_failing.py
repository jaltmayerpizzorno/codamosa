# Automatically generated by Pynguin.
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        int_0 = 0
        var_0 = module_0.type_repr(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_0 = module_0.Base()
    except BaseException:
        pass

def test_case_2():
    try:
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "aWxJs'H\r\r<`"
        node_pattern_0 = module_0.NodePattern(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        wildcard_pattern_0 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_5():
    try:
        negated_pattern_0 = module_0.NegatedPattern()
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'R+\\#ns'
        negated_pattern_0 = module_0.NegatedPattern()
        iterator_0 = negated_pattern_0.generate_matches(str_0)
        int_0 = -3818
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 2685
        str_0 = '\n    Abstract base class for Node and Leaf.\n\n    This provides some default functionality and boilerplate using the\n    template pattern.\n\n    A node may be a subnode of at most one parent.\n    '
        bool_0 = None
        list_0 = [int_0, int_0]
        leaf_0 = module_0.Leaf(int_0, str_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -2245
        str_0 = 'YG*.?{ujC"'
        leaf_0 = module_0.Leaf(int_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        base_pattern_0 = module_0.BasePattern(*list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 4390
        leaf_pattern_0 = module_0.LeafPattern()
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = -738
        any_0 = wildcard_pattern_0.optimize()
        wildcard_pattern_1 = module_0.WildcardPattern(int_1, int_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '8-O*=i+'
        int_0 = -434
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        negated_pattern_0 = module_0.NegatedPattern()
        str_0 = "\n        Equivalent to 'node.children.insert(i, child)'. This method also sets\n        the child's parent attribute appropriately.\n        "
        bool_0 = negated_pattern_0.match(str_0)
        int_0 = None
        wildcard_pattern_0 = module_0.WildcardPattern(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 2162
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        grammar_0 = None
        negated_pattern_0 = module_0.NegatedPattern()
        bool_0 = negated_pattern_0.match_seq(grammar_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 2221
        none_type_0 = None
        leaf_pattern_0 = module_0.LeafPattern(int_0, none_type_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        str_1 = 'PF\x0cc0G] '
        int_0 = 33
        list_0 = []
        leaf_pattern_0 = module_0.LeafPattern(int_0)
        list_1 = [leaf_pattern_0, str_0]
        node_0 = module_0.Node(int_0, list_0, str_1, list_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'KEm#'
        int_0 = 2104
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 113
        int_2 = -738
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_0 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        leaf_1 = leaf_0.clone()
        str_1 = leaf_0.__repr__()
        leaf_pattern_0 = module_0.LeafPattern()
        negated_pattern_0 = module_0.NegatedPattern()
        iterator_0 = negated_pattern_0.generate_matches(leaf_pattern_0)
        str_2 = leaf_0.__repr__()
        int_3 = 2113
        list_0 = []
        node_0 = module_0.Node(int_3, list_0)
        iterator_1 = negated_pattern_0.generate_matches(wildcard_pattern_0)
        iterator_2 = leaf_0.post_order()
        iterable_0 = None
        node_pattern_0 = module_0.NodePattern(int_2, iterable_0, str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = "'qo-vJ 7%R"
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        leaf_pattern_0 = module_0.LeafPattern()
        bool_0 = wildcard_pattern_0.match(leaf_pattern_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 2154
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        any_0 = wildcard_pattern_0.optimize()
        any_1 = wildcard_pattern_0.optimize()
        wildcard_pattern_1 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 187
        int_1 = -738
        tuple_0 = (int_1, int_1)
        tuple_1 = (str_0, tuple_0)
        leaf_0 = module_0.Leaf(int_0, str_0, tuple_1, str_0)
        leaf_1 = leaf_0.clone()
        str_1 = leaf_0.__str__()
        str_2 = leaf_0.__repr__()
        leaf_2 = leaf_0.clone()
        leaf_pattern_0 = module_0.LeafPattern()
        leaf_3 = leaf_0.clone()
        str_3 = '\\s+{(\\d+), labels},$'
        leaf_4 = module_0.Leaf(int_1, str_3)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 280
        list_0 = []
        str_0 = "l.'n\x0c:l8~A6^"
        node_0 = module_0.Node(int_0, list_0, str_0, str_0)
        node_1 = node_0.clone()
        base_0 = module_0.Base()
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 1928
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        node_0.update_sibling_maps()
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 2119
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        bool_0 = False
        bool_1 = wildcard_pattern_0.match(bool_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 2101
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        grammar_0 = module_1.Grammar()
        int_1 = -2496
        tuple_0 = (int_0, str_0, int_1, str_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_24():
    try:
        grammar_0 = module_1.Grammar()
        int_0 = -2561
        str_0 = "A'B{%B{"
        list_0 = None
        none_type_0 = None
        tuple_0 = (int_0, str_0, list_0, none_type_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_25():
    try:
        grammar_0 = module_1.Grammar()
        int_0 = -2409
        optional_0 = None
        tuple_0 = (int_0, int_0, optional_0, int_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'e'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        iterator_0 = wildcard_pattern_0.generate_matches(negated_pattern_0)
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_27():
    try:
        grammar_0 = module_1.Grammar()
        var_0 = grammar_0.copy()
        negated_pattern_0 = module_0.NegatedPattern(var_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        int_0 = 2162
        int_1 = 50
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        any_0 = wildcard_pattern_0.optimize()
        int_2 = 715
        list_0 = []
        list_1 = [int_1, int_0]
        node_0 = module_0.Node(int_2, list_0, str_0, list_1)
        list_2 = [node_0, node_0, node_0]
        node_1 = module_0.Node(int_0, list_2)
    except BaseException:
        pass

def test_case_29():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        int_0 = 2160
        int_1 = -724
        grammar_0 = module_1.Grammar()
        str_0 = None
        node_pattern_0 = module_0.NodePattern(int_0, int_1, str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = "'qo-vJ 7%R"
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        leaf_pattern_0 = module_0.LeafPattern()
        int_0 = 900
        list_0 = []
        node_0 = module_0.Node(int_0, list_0, str_0)
        str_1 = node_0.__repr__()
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'B'
        int_0 = 2061
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 114
        int_2 = -738
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_0 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        str_1 = leaf_0.__repr__()
        negated_pattern_0 = module_0.NegatedPattern()
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_0, list_0, any_0)
        node_1 = node_0.clone()
        leaf_pattern_0 = module_0.LeafPattern()
        var_0 = leaf_pattern_0.match(node_0)
        node_1.append_child(leaf_0)
        str_2 = leaf_0.__repr__()
        str_3 = node_1.__str__()
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
        set_0 = {str_0}
        bool_0 = wildcard_pattern_1.match(set_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        negated_pattern_0 = module_0.NegatedPattern()
        int_0 = 156
        leaf_0 = module_0.Leaf(int_0, str_0)
        leaf_pattern_0 = module_0.LeafPattern()
        var_0 = leaf_pattern_0.match(leaf_0)
        wildcard_pattern_0 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'KEm#'
        int_0 = 2939
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 113
        int_2 = -738
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_0 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        leaf_1 = leaf_0.clone()
        str_1 = leaf_0.__repr__()
        leaf_pattern_0 = module_0.LeafPattern()
        negated_pattern_0 = module_0.NegatedPattern()
        iterator_0 = negated_pattern_0.generate_matches(leaf_pattern_0)
        int_3 = 2113
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_3, list_0)
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
        bool_0 = True
        iterator_1 = negated_pattern_0.generate_matches(bool_0)
        wildcard_pattern_2 = module_0.WildcardPattern(str_0, int_0, int_2)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        negated_pattern_0 = module_0.NegatedPattern()
        int_0 = 2154
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 156
        int_2 = 693
        any_0 = wildcard_pattern_0.optimize()
        any_1 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0)
        int_3 = 1921
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_3, list_0)
        node_0.insert_child(int_2, leaf_0)
        leaf_pattern_0 = module_0.LeafPattern()
        var_0 = leaf_pattern_0.match(leaf_0)
        wildcard_pattern_1 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = 'WEw#v'
        int_0 = 109
        int_1 = -738
        tuple_0 = (int_1, int_0)
        tuple_1 = (str_0, tuple_0)
        leaf_0 = module_0.Leaf(int_0, str_0, tuple_1, str_0)
        leaf_1 = leaf_0.clone()
        str_1 = leaf_0.__repr__()
        leaf_pattern_0 = module_0.LeafPattern()
        negated_pattern_0 = module_0.NegatedPattern()
        leaf_2 = None
        var_0 = leaf_pattern_0.match(leaf_2, leaf_0)
        iterator_0 = negated_pattern_0.generate_matches(leaf_pattern_0)
        wildcard_pattern_0 = module_0.WildcardPattern(str_1)
        list_0 = [leaf_0, leaf_1, leaf_0, leaf_0]
        node_0 = module_0.Node(int_0, list_0, str_1)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = "]cKfH<!\\6'kYD7I"
        grammar_0 = module_1.Grammar()
        int_0 = -2496
        tuple_0 = (int_0, str_0, int_0, str_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_37():
    try:
        optional_0 = None
        str_0 = '4H9^gb\x0bf&gs\rE2'
        node_pattern_0 = module_0.NodePattern(optional_0, str_0)
    except BaseException:
        pass

def test_case_38():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        str_0 = '""'
        int_0 = 2160
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        grammar_0 = module_1.Grammar()
        any_0 = wildcard_pattern_0.optimize()
        bool_0 = False
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        bool_1 = False
        iterator_0 = negated_pattern_0.generate_matches(bool_1)
        iterator_1 = wildcard_pattern_0.generate_matches(bool_0)
        dict_0 = {}
        bool_2 = wildcard_pattern_0.match_seq(dict_0)
        int_1 = 105
        leaf_0 = module_0.Leaf(int_1, str_0)
        leaf_1 = leaf_0.clone()
        leaf_2 = leaf_1.clone()
        str_1 = leaf_2.__str__()
        list_0 = [leaf_2, leaf_1, leaf_0]
        list_1 = [int_1]
        node_0 = module_0.Node(int_0, list_0, any_0, list_1)
        node_1 = node_0.clone()
        int_2 = 196
        set_0 = set()
        tuple_0 = (int_2, str_0, set_0, list_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = "(M%qZ'wH[+pxIbA4X"
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        str_1 = ''
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = ']1UB8PWj'
        int_0 = 2177
        int_1 = 1839
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        dict_0 = {}
        bool_0 = wildcard_pattern_0.match_seq(dict_0)
        list_0 = []
        list_1 = [int_1]
        node_0 = module_0.Node(int_0, list_0, any_0, list_1)
        node_1 = module_0.Node(int_0, list_0, str_0, list_1)
        grammar_0 = module_1.Grammar()
        list_2 = []
        float_0 = 1419.9794
        bool_1 = negated_pattern_0.match(list_2, float_0)
        leaf_pattern_0 = module_0.LeafPattern()
        var_0 = leaf_pattern_0.match(node_1, list_2)
        str_1 = None
        int_2 = -1523
        optional_0 = None
        tuple_0 = (int_2, str_1, optional_0, list_0)
        var_1 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'KE'
        int_0 = 2071
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 113
        int_2 = -738
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_0 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        str_1 = leaf_0.__repr__()
        negated_pattern_0 = module_0.NegatedPattern()
        leaf_1 = leaf_0.clone()
        leaf_2 = leaf_0.clone()
        str_2 = leaf_0.__repr__()
        list_0 = [leaf_0]
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
        grammar_0 = None
        tuple_2 = (int_2, str_0, tuple_1, list_0)
        var_0 = module_0.convert(grammar_0, tuple_2)
        int_3 = 343
        int_4 = 3113
        node_0 = module_0.Node(int_4, list_0)
        node_1 = node_0.clone()
        node_2 = node_1.clone()
        node_3 = node_2.clone()
        node_3.set_child(int_3, leaf_1)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'KE'
        int_0 = 2071
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 113
        int_2 = -738
        any_0 = wildcard_pattern_0.optimize()
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_1 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        str_1 = leaf_0.__repr__()
        negated_pattern_0 = module_0.NegatedPattern()
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_0, list_0, any_1)
        node_1 = node_0.clone()
        leaf_1 = leaf_0.clone()
        node_1.update_sibling_maps()
        str_2 = leaf_0.__repr__()
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
        grammar_0 = None
        tuple_2 = (int_2, str_0, tuple_1, list_0)
        var_0 = module_0.convert(grammar_0, tuple_2)
        complex_0 = None
        bool_0 = wildcard_pattern_1.match(complex_0)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'KE'
        int_0 = 2071
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        int_1 = 113
        int_2 = 3165
        tuple_0 = (int_2, int_0)
        tuple_1 = (str_0, tuple_0)
        any_0 = wildcard_pattern_0.optimize()
        leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
        str_1 = leaf_0.__repr__()
        negated_pattern_0 = module_0.NegatedPattern()
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_0, list_0, any_0)
        node_1 = node_0.clone()
        leaf_1 = leaf_0.clone()
        node_1.append_child(leaf_0)
        node_1.insert_child(int_0, leaf_0)
        str_2 = leaf_0.__repr__()
        wildcard_pattern_1 = module_0.WildcardPattern(str_1)
        grammar_0 = None
        tuple_2 = (int_2, str_0, tuple_1, list_0)
        var_0 = module_0.convert(grammar_0, tuple_2)
        bool_0 = wildcard_pattern_1.match(int_0)
    except BaseException:
        pass

def test_case_44():
    try:
        var_0 = []
        iterator_0 = module_0.generate_matches(var_0, var_0)
        var_1 = list(iterator_0)
        var_2 = list(iterator_0)
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'O'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        iterator_0 = wildcard_pattern_0.generate_matches(negated_pattern_0)
        dict_0 = {}
        bool_0 = wildcard_pattern_0.match_seq(dict_0, iterator_0)
    except BaseException:
        pass

def test_case_46():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        str_0 = '""'
        int_0 = 2160
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        grammar_0 = module_1.Grammar()
        any_0 = wildcard_pattern_0.optimize()
        bool_0 = True
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        bool_1 = False
        iterator_0 = negated_pattern_0.generate_matches(bool_1)
        iterator_1 = wildcard_pattern_0.generate_matches(bool_0)
        dict_0 = {}
        bool_2 = wildcard_pattern_0.match_seq(dict_0)
        int_1 = 105
        leaf_0 = module_0.Leaf(int_1, str_0)
        leaf_1 = leaf_0.clone()
        leaf_2 = leaf_1.clone()
        str_1 = leaf_2.__str__()
        var_0 = leaf_pattern_0.match(leaf_1, iterator_1)
        list_0 = []
        leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)
        list_1 = [int_1]
        var_1 = leaf_pattern_1.match(leaf_2)
        node_0 = module_0.Node(int_0, list_0, any_0, list_1)
        leaf_pattern_2 = module_0.LeafPattern()
        node_1 = module_0.Node(int_0, list_0, any_0, str_1, list_1)
        int_2 = 196
        str_2 = leaf_2.__repr__()
        set_0 = set()
        tuple_0 = (int_2, str_0, set_0, list_0)
        var_2 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_47():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        str_0 = '""'
        int_0 = 2160
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        grammar_0 = module_1.Grammar()
        any_0 = wildcard_pattern_0.optimize()
        bool_0 = False
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        bool_1 = False
        iterator_0 = negated_pattern_0.generate_matches(bool_1)
        iterator_1 = wildcard_pattern_0.generate_matches(bool_0)
        dict_0 = {}
        bool_2 = wildcard_pattern_0.match_seq(dict_0)
        int_1 = 105
        str_1 = None
        leaf_0 = module_0.Leaf(int_1, str_1)
        leaf_1 = leaf_0.clone()
        leaf_2 = leaf_1.clone()
        str_2 = leaf_2.__str__()
        var_0 = leaf_pattern_0.match(leaf_1, iterator_1)
        list_0 = []
        leaf_pattern_1 = module_0.LeafPattern(int_1, str_0)
        list_1 = [int_1]
        var_1 = leaf_pattern_1.match(leaf_2)
        node_0 = module_0.Node(int_0, list_0, any_0, list_1)
        leaf_pattern_2 = module_0.LeafPattern()
        node_1 = node_0.clone()
        int_2 = 196
        str_3 = leaf_2.__repr__()
        set_0 = set()
        tuple_0 = (int_2, str_0, set_0, list_0)
        var_2 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass