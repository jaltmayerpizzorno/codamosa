# Automatically generated by Pynguin.
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    try:
        int_0 = 1
        var_0 = module_0.type_repr(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 916
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        node_0.update_sibling_maps()
    except BaseException:
        pass

def test_case_2():
    try:
        base_0 = module_0.Base()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 3943
        list_0 = []
        list_1 = None
        node_0 = module_0.Node(int_0, list_0, list_1)
        list_2 = [node_0, node_0, node_0, node_0]
        node_1 = module_0.Node(int_0, list_2)
    except BaseException:
        pass

def test_case_4():
    try:
        node_pattern_0 = module_0.NodePattern()
    except BaseException:
        pass

def test_case_5():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        str_0 = leaf_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 2086
        node_pattern_0 = module_0.NodePattern(int_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        wildcard_pattern_0 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_8():
    try:
        negated_pattern_0 = module_0.NegatedPattern()
        iterator_0 = negated_pattern_0.generate_matches(negated_pattern_0)
        var_0 = list(iterator_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 1
        str_0 = 'AP@yvj`/wDIH'
        leaf_0 = module_0.Leaf(int_0, str_0)
        grammar_0 = module_1.Grammar()
        tuple_0 = None
        tuple_1 = (str_0, tuple_0)
        list_0 = [leaf_0, leaf_0]
        tuple_2 = (int_0, str_0, tuple_1, list_0)
        var_0 = module_0.convert(grammar_0, tuple_2)
    except BaseException:
        pass

def test_case_10():
    try:
        leaf_pattern_0 = module_0.LeafPattern()
        int_0 = 602
        str_0 = 'O'
        leaf_0 = module_0.Leaf(int_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'f+o'
        grammar_0 = module_1.Grammar()
        int_0 = -705
        optional_0 = None
        tuple_0 = (int_0, str_0, int_0, optional_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 1
        str_0 = 'APvj`/wDIH'
        leaf_0 = module_0.Leaf(int_0, str_0)
        optional_0 = leaf_0.remove()
        dict_0 = {}
        base_pattern_0 = module_0.BasePattern(**dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 2621
        list_0 = []
        str_0 = 'p'
        list_1 = [list_0, list_0, str_0, int_0, str_0, list_0]
        node_0 = module_0.Node(int_0, list_0, str_0, list_1)
        node_1 = node_0.clone()
        str_1 = 't\t$%\'O}\'Doe\n3}"S&KD9'
        int_1 = -1327
        wildcard_pattern_0 = module_0.WildcardPattern(str_1, int_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '3^*R('
        int_0 = 521
        list_0 = []
        node_0 = module_0.Node(int_0, list_0, str_0)
        node_1 = node_0.clone()
        node_2 = node_1.clone()
        node_3 = node_2.clone()
        str_1 = node_3.__str__()
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        bool_0 = wildcard_pattern_0.match(wildcard_pattern_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Pvj`/wDX?H'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        bool_0 = wildcard_pattern_0.match(wildcard_pattern_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 1
        str_0 = 'APvj`/wDIH'
        leaf_0 = module_0.Leaf(int_0, str_0)
        leaf_1 = leaf_0.clone()
        str_1 = leaf_0.__repr__()
        str_2 = leaf_0.__str__()
        leaf_pattern_0 = module_0.LeafPattern(str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 1
        leaf_pattern_0 = module_0.LeafPattern(int_0)
        leaf_0 = None
        var_0 = leaf_pattern_0.match(leaf_0)
        wildcard_pattern_0 = module_0.WildcardPattern()
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'vB'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        negated_pattern_0 = module_0.NegatedPattern(any_0)
        bool_0 = wildcard_pattern_0.match(negated_pattern_0, negated_pattern_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 83
        str_0 = 'Pvj`/wDI?H'
        leaf_0 = module_0.Leaf(int_0, str_0)
        leaf_pattern_0 = module_0.LeafPattern(int_0)
        var_0 = leaf_pattern_0.match(leaf_0)
        leaf_1 = leaf_0.clone()
        leaf_pattern_1 = module_0.LeafPattern()
        list_0 = [leaf_0]
        base_0 = module_0.Base(*list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = ''
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        grammar_0 = module_1.Grammar()
        int_0 = -798
        str_0 = None
        list_0 = None
        tuple_0 = (int_0, str_0, int_0, list_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = -1685
        int_1 = 2621
        list_0 = []
        node_0 = module_0.Node(int_1, list_0)
        int_2 = 1363
        node_1 = module_0.Node(int_2, list_0)
        node_0.append_child(node_1)
        leaf_pattern_0 = module_0.LeafPattern(int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = 2621
        list_0 = []
        str_0 = '6p'
        list_1 = [list_0, str_0, int_0, str_0]
        node_0 = module_0.Node(int_0, list_0, str_0, list_1)
        wildcard_pattern_0 = module_0.WildcardPattern(int_0)
    except BaseException:
        pass

def test_case_24():
    try:
        int_0 = 3462
        str_0 = 'n'
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    except BaseException:
        pass

def test_case_25():
    try:
        grammar_0 = module_1.Grammar()
        negated_pattern_0 = module_0.NegatedPattern(grammar_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '{@Tr<o\rn'
        int_0 = 2065
        node_pattern_0 = module_0.NodePattern(int_0, str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        int_0 = 1
        str_0 = 'ivu=pc'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0, str_0)
        any_0 = wildcard_pattern_0.optimize()
        node_pattern_0 = module_0.NodePattern(int_0, str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        int_0 = 83
        str_0 = 'Pvj`/wD?H'
        leaf_0 = module_0.Leaf(int_0, str_0)
        int_1 = None
        leaf_pattern_0 = module_0.LeafPattern(int_1, str_0, str_0)
        var_0 = leaf_pattern_0.match(leaf_0)
        leaf_1 = leaf_0.clone()
        leaf_pattern_1 = module_0.LeafPattern()
        list_0 = [leaf_0]
        base_0 = module_0.Base(*list_0)
    except BaseException:
        pass

def test_case_29():
    try:
        int_0 = 3494
        list_0 = []
        list_1 = [list_0, list_0, list_0, list_0]
        node_0 = module_0.Node(int_0, list_0, list_1)
        node_1 = node_0.clone()
        iterator_0 = node_0.post_order()
        int_1 = None
        node_1.set_child(int_1, node_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = '@twz@Mv'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        grammar_0 = module_1.Grammar()
        int_0 = 115
        optional_0 = None
        leaf_pattern_0 = module_0.LeafPattern(int_0, str_0, str_0)
        tuple_0 = (int_0, str_0, optional_0, leaf_pattern_0)
        var_0 = module_0.convert(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_31():
    try:
        int_0 = 418
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        node_0.append_child(node_0)
    except BaseException:
        pass

def test_case_32():
    try:
        int_0 = 1
        str_0 = 'AP@)vj`/DIH'
        leaf_0 = module_0.Leaf(int_0, str_0)
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        int_1 = 1838
        wildcard_pattern_1 = module_0.WildcardPattern(str_0, int_1, int_0)
    except BaseException:
        pass

def test_case_33():
    try:
        int_0 = 1
        str_0 = 'ivu=pc'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0, str_0)
        bool_0 = wildcard_pattern_0.match_seq(str_0)
    except BaseException:
        pass

def test_case_34():
    try:
        negated_pattern_0 = module_0.NegatedPattern()
        var_0 = [negated_pattern_0, negated_pattern_0, negated_pattern_0]
        iterator_0 = negated_pattern_0.generate_matches(var_0)
        var_1 = list(iterator_0)
        int_0 = 1172
        iterator_1 = negated_pattern_0.generate_matches(int_0)
        str_0 = 'YEdM%\tWHdrQdpQ'
        leaf_pattern_0 = module_0.LeafPattern(str_0)
    except BaseException:
        pass

def test_case_35():
    try:
        int_0 = 1
        leaf_pattern_0 = module_0.LeafPattern(int_0)
        str_0 = leaf_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'Pvj`/wDXdd?H'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        dict_0 = {}
        list_0 = [wildcard_pattern_0, dict_0, wildcard_pattern_0, wildcard_pattern_0]
        bool_0 = wildcard_pattern_0.match_seq(dict_0, list_0)
    except BaseException:
        pass

def test_case_37():
    try:
        int_0 = 0
        str_0 = 'APvj`/wDIH'
        leaf_0 = module_0.Leaf(int_0, str_0)
        list_0 = None
        leaf_0.replace(list_0)
    except BaseException:
        pass

def test_case_38():
    try:
        int_0 = 1
        str_0 = ''
        leaf_0 = module_0.Leaf(int_0, str_0)
        int_1 = leaf_0.depth()
        wildcard_pattern_0 = module_0.WildcardPattern(int_0)
    except BaseException:
        pass

def test_case_39():
    try:
        int_0 = 1
        iterable_0 = None
        list_0 = [int_0, iterable_0]
        node_pattern_0 = module_0.NodePattern(iterable_0, list_0)
    except BaseException:
        pass