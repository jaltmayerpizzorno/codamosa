# Automatically generated by Pynguin.
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        int_0 = None
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
        grammar_0 = module_1.Grammar()
        int_0 = 556
        str_0 = '6V".J0'
        optional_0 = None
        list_0 = None
        tuple_0 = (int_0, str_0, optional_0, list_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_4():
    try:
        wildcard_pattern_0 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Q9)wZ`FVV\\&cz'
        str_1 = 'F*>B[^1:19'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
        negated_pattern_0 = module_0.NegatedPattern()
        bool_0 = negated_pattern_0.match(dict_0)
        int_0 = 1890
        str_2 = 'V0NW>6s'
        leaf_0 = module_0.Leaf(int_0, str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '0[bB]_?[01]+(?:_[01]+)*'
        int_0 = 5
        list_0 = []
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        node_0 = module_0.Node(int_0, list_0, list_0, wildcard_pattern_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -2508
        str_0 = '\\KKpRj?$379D'
        list_0 = [str_0, str_0, int_0]
        leaf_0 = module_0.Leaf(int_0, str_0, str_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        base_pattern_0 = module_0.BasePattern()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 553
        leaf_0 = None
        list_0 = [leaf_0, leaf_0, leaf_0]
        node_0 = module_0.Node(int_0, list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 875
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        node_1 = node_0.clone()
        node_1.update_sibling_maps()
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -1098
        wildcard_pattern_0 = module_0.WildcardPattern(int_0, int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ''
        leaf_pattern_0 = module_0.LeafPattern()
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '9&'
        int_0 = 769
        bytes_0 = b'\x8e\x0f'
        negated_pattern_0 = module_0.NegatedPattern()
        bool_0 = negated_pattern_0.match_seq(bytes_0)
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
        negated_pattern_1 = module_0.NegatedPattern()
        grammar_0 = module_1.Grammar()
        str_1 = '\r/MJjK[+'
        bool_1 = wildcard_pattern_0.match(str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '3nE9&'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'pkX{'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        leaf_pattern_0 = module_0.LeafPattern()
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        list_0 = [leaf_pattern_0, dict_0, str_0, leaf_pattern_0]
        negated_pattern_0 = module_0.NegatedPattern(list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '3yEWP'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        bool_0 = wildcard_pattern_0.match(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '&'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        dict_0 = {}
        bool_0 = wildcard_pattern_0.match_seq(dict_0)
        any_0 = wildcard_pattern_0.optimize()
        int_0 = -350
        leaf_pattern_0 = module_0.LeafPattern(int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        grammar_0 = module_1.Grammar()
        str_0 = ''
        int_0 = -3383
        int_1 = -1966
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_0, tuple_0)
        leaf_0 = None
        list_0 = [leaf_0, leaf_0, leaf_0]
        tuple_2 = (int_1, int_1, tuple_1, list_0)
        var_0 = module_0.convert(grammar_0, tuple_2)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 27
        str_0 = 'E\x0cb*fc<Ya|"&V|T'
        leaf_0 = module_0.Leaf(int_0, str_0)
        int_1 = 1301
        list_0 = []
        grammar_0 = module_1.Grammar()
        node_0 = module_0.Node(int_1, list_0, grammar_0)
        int_2 = 2551
        node_0.insert_child(int_2, node_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '\nGU{=?0N<_Ki'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        int_0 = 1108
        list_0 = []
        node_0 = module_0.Node(int_0, list_0, int_0, str_0)
        list_1 = [node_0, node_0]
        node_1 = module_0.Node(int_0, list_1, str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 317
        list_0 = []
        list_1 = [int_0, list_0, int_0]
        node_0 = module_0.Node(int_0, list_0, list_1)
        grammar_0 = module_1.Grammar()
        optional_0 = None
        tuple_0 = (int_0, optional_0, int_0, list_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '&'
        int_0 = 1284
        node_pattern_0 = module_0.NodePattern(int_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = 377
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        str_0 = node_0.__repr__()
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '9&'
        int_0 = 2
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
        bool_0 = wildcard_pattern_0.match(int_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '9&'
        int_0 = 768
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
        any_0 = wildcard_pattern_0.optimize()
        any_1 = wildcard_pattern_0.optimize()
        leaf_pattern_0 = module_0.LeafPattern(int_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '9 '
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        int_0 = 2147483647
        list_0 = []
        str_1 = 'M'
        list_1 = [str_1, str_0, str_0]
        node_0 = module_0.Node(int_0, list_0, str_0, list_1)
        iterator_0 = node_0.post_order()
        leaf_0 = None
        node_0.set_child(int_0, leaf_0)
    except BaseException:
        pass

def test_case_27():
    try:
        int_0 = 363
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        node_1 = node_0.clone()
        node_2 = node_1.clone()
        node_3 = node_2.clone()
        str_0 = node_3.__str__()
        str_1 = '\\I[f({Jy@tqnC7+z'
        wildcard_pattern_0 = module_0.WildcardPattern(str_1)
        bool_0 = wildcard_pattern_0.match(wildcard_pattern_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '&'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        dict_0 = {}
        bool_0 = wildcard_pattern_0.match_seq(dict_0)
        int_0 = 38
        grammar_0 = module_1.Grammar()
        none_type_0 = None
        node_pattern_0 = module_0.NodePattern(int_0, none_type_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = '3yEWP'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        optional_0 = None
        leaf_pattern_0 = module_0.LeafPattern(optional_0, str_0)
        leaf_pattern_1 = module_0.LeafPattern(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        int_0 = 21
        str_0 = 'c'
        leaf_0 = module_0.Leaf(int_0, str_0)
        str_1 = leaf_0.__str__()
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
        dict_0 = {}
        var_0 = leaf_pattern_0.match(leaf_0, dict_0)
        str_2 = '!mG9,^\ny@('
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        bool_0 = wildcard_pattern_0.match(str_2)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'C'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        leaf_0 = None
        any_0 = wildcard_pattern_0.optimize()
        int_0 = None
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0, str_0)
        int_1 = 1510
        list_0 = []
        list_1 = []
        node_0 = module_0.Node(int_1, list_0, list_1)
        node_1 = node_0.clone()
        node_2 = node_1.clone()
        node_2.append_child(leaf_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = '\\I[f({Jy@tqnC7+z'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        none_type_0 = None
        node_pattern_0 = module_0.NodePattern(none_type_0, wildcard_pattern_0)
    except BaseException:
        pass

def test_case_33():
    try:
        int_0 = 1297
        iterator_0 = None
        list_0 = [iterator_0, iterator_0]
        node_pattern_0 = module_0.NodePattern(int_0, list_0)
    except BaseException:
        pass

def test_case_34():
    try:
        negated_pattern_0 = module_0.NegatedPattern()
        iterator_0 = negated_pattern_0.generate_matches(negated_pattern_0)
        var_0 = sorted(iterator_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = '.'
        int_0 = 1
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
        any_0 = wildcard_pattern_0.optimize()
    except BaseException:
        pass

def test_case_36():
    try:
        int_0 = 2543
        int_1 = 25
        float_0 = -751.484603
        wildcard_pattern_0 = module_0.WildcardPattern(int_0, int_1, float_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = '.'
        int_0 = 1
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0)
        any_0 = wildcard_pattern_0.optimize()
        bool_0 = wildcard_pattern_0.match(str_0)
    except BaseException:
        pass

def test_case_38():
    try:
        optional_0 = None
        grammar_0 = module_1.Grammar()
        str_0 = ',.@Y %Z\x0bKZO.50-q'
        grammar_0.dump(str_0)
        leaf_pattern_0 = module_0.LeafPattern(optional_0, grammar_0)
    except BaseException:
        pass

def test_case_39():
    try:
        int_0 = 349
        list_0 = []
        list_1 = [int_0]
        node_0 = module_0.Node(int_0, list_0, list_1)
        any_0 = None
        str_0 = ''
        node_1 = module_0.Node(int_0, list_0, any_0, str_0, list_1)
        str_1 = node_1.__repr__()
    except BaseException:
        pass

def test_case_40():
    try:
        int_0 = 317
        list_0 = []
        list_1 = [int_0, list_0, int_0]
        node_0 = module_0.Node(int_0, list_0, list_1)
        int_1 = node_0.depth()
        node_0.set_child(int_0, node_0)
    except BaseException:
        pass

def test_case_41():
    try:
        int_0 = 21
        str_0 = 'e.'
        leaf_0 = module_0.Leaf(int_0, str_0)
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
        bool_0 = True
        var_0 = leaf_pattern_0.match(leaf_0, bool_0)
        grammar_0 = None
        int_1 = 882
        list_0 = [leaf_0]
        node_0 = module_0.Node(int_1, list_0)
        node_1 = node_0.clone()
        node_0.insert_child(int_0, node_1)
        iterator_0 = node_1.post_order()
        iterator_1 = leaf_0.post_order()
        tuple_0 = (int_1, str_0, iterator_0, list_0)
        var_1 = module_0.convert(grammar_0, tuple_0)
        int_2 = node_1.depth()
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        bool_1 = wildcard_pattern_0.match(bool_0)
    except BaseException:
        pass