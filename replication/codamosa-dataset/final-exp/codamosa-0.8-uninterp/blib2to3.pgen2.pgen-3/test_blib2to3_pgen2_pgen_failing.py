# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        parser_generator_0 = module_0.ParserGenerator(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Fj\nUrU6X2lw'
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '/Y_\r5+9l<N"t4'
        pgen_grammar_0 = module_0.generate_grammar(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        bool_0 = d_f_a_state_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        n_f_a_state_0 = None
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_1, str_0)
        dict_1 = None
        d_f_a_state_2 = module_0.DFAState(dict_1, n_f_a_state_0)
    except BaseException:
        pass

def test_case_6():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(n_f_a_state_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_0.addarc(n_f_a_state_0)
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_3 = None
        str_0 = '\n    A pattern is a tree matching pattern.\n\n    It looks for a specific node type (token or symbol), and\n    optionally for a specific content.\n\n    This is an abstract base class.  There are three concrete\n    subclasses:\n\n    - LeafPattern matches a single leaf node;\n    - NodePattern matches a single node (usually non-leaf);\n    - WildcardPattern matches a sequence of nodes of variable length.\n    '
        d_f_a_state_0.addarc(d_f_a_state_3, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_0, str_0)
        n_f_a_state_2 = module_0.NFAState()
        dict_0 = {n_f_a_state_2: n_f_a_state_2}
        n_f_a_state_1.addarc(n_f_a_state_1)
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_2)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_2)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)
        str_1 = None
        d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'w\tp\nj&('
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = module_0.NFAState()
        dict_0 = {n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_1)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_1 = '('
        d_f_a_state_1.addarc(d_f_a_state_2, str_1)
        d_f_a_state_1.unifystate(d_f_a_state_1, d_f_a_state_0)
        str_2 = '\n    Generator yielding matches for a sequence of patterns and nodes.\n\n    Args:\n        patterns: a sequence of patterns\n        nodes: a sequence of nodes\n\n    Yields:\n        (count, results) tuples where:\n        count: the entire sequence of patterns matches nodes[:count];\n        results: dict containing named submatches.\n    '
        d_f_a_state_1.addarc(d_f_a_state_1, str_2)
        d_f_a_state_3 = module_0.DFAState(dict_0, n_f_a_state_1)
        bool_0 = d_f_a_state_3.__eq__(str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "\n        The node immediately preceding the invocant in their parent's children\n        list. If the invocant does not have a previous sibling, it is None.\n        "
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_0, str_0)
        n_f_a_state_2 = module_0.NFAState()
        n_f_a_state_3 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_2)
        dict_0 = {n_f_a_state_3: n_f_a_state_3}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_2)
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_2)
        d_f_a_state_0.unifystate(d_f_a_state_2, d_f_a_state_2)
        d_f_a_state_3 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_3.addarc(d_f_a_state_0, str_0)
        n_f_a_state_4 = None
        d_f_a_state_4 = module_0.DFAState(dict_0, n_f_a_state_4)
    except BaseException:
        pass

def test_case_13():
    try:
        n_f_a_state_0 = module_0.NFAState()
        set_0 = {n_f_a_state_0, n_f_a_state_0, n_f_a_state_0, n_f_a_state_0}
        tuple_0 = (set_0,)
        float_0 = 1214.68
        tuple_1 = (tuple_0, float_0)
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_0, tuple_1)
    except BaseException:
        pass

def test_case_14():
    try:
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_1 = None
        n_f_a_state_0.addarc(n_f_a_state_1)
    except BaseException:
        pass