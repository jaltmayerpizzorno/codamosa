# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    try:
        str_0 = 'D)SHY\t^F?bo^bMJ/'
        int_0 = True
        parser_generator_0 = module_0.ParserGenerator(str_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        pgen_grammar_0 = module_0.generate_grammar()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        n_f_a_state_0 = module_0.NFAState()
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    except BaseException:
        pass

def test_case_3():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_1 = None
        dict_1 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_1)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = None
        n_f_a_state_0 = module_0.NFAState()
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    except BaseException:
        pass

def test_case_5():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        n_f_a_state_1 = None
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_1)
    except BaseException:
        pass

def test_case_6():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = -1456.0
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        n_f_a_state_0 = module_0.NFAState()
        str_0 = '-X'
        str_1 = None
        dict_0 = {str_0: n_f_a_state_0, str_1: str_0}
        dict_1 = {n_f_a_state_0: dict_0}
        d_f_a_state_0 = module_0.DFAState(dict_1, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(n_f_a_state_0)
    except BaseException:
        pass

def test_case_8():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)
        str_0 = 'dump_nfa_{}'
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        dict_1 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)
        str_0 = 'dump_nfa_{}'
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        str_0 = ''
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_1 = None
        n_f_a_state_1 = module_0.NFAState()
        dict_1 = {n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_1)
        d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = 1805.0
        dict_0 = {n_f_a_state_0: float_0, n_f_a_state_0: float_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        dict_1 = {n_f_a_state_0: d_f_a_state_0}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        str_0 = 'W@P8xt2$nf.{ae`n,v\tI'
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = module_0.NFAState()
        bytes_0 = b"\xf1'\x06\x96\xab\x13\xa5\xaf\x12\x98\xdd\xf8\xff\xfcn"
        dict_2 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: bytes_0, n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_2 = module_0.DFAState(dict_2, n_f_a_state_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_1)
        str_1 = "'+\\ZXm"
        d_f_a_state_1.addarc(d_f_a_state_0, str_1)
        str_2 = 'h(Y\\^koWkh4?O,V#'
        str_3 = 'T>'
        bool_1 = d_f_a_state_0.__eq__(d_f_a_state_1)
        n_f_a_state_1.addarc(n_f_a_state_0, str_2)
        parser_generator_0 = module_0.ParserGenerator(str_3)
    except BaseException:
        pass

def test_case_12():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = 1805.0
        dict_0 = {n_f_a_state_0: float_0, n_f_a_state_0: float_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '|?F3^*HP'
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        str_1 = 'Dump of NFA for'
        str_2 = 'Tx>'
        n_f_a_state_0.addarc(n_f_a_state_1, str_2)
        parser_generator_0 = module_0.ParserGenerator(str_1, n_f_a_state_1)
    except BaseException:
        pass

def test_case_13():
    try:
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_1 = None
        n_f_a_state_0.addarc(n_f_a_state_1)
    except BaseException:
        pass

def test_case_14():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = 1805.0
        dict_0 = {n_f_a_state_0: float_0, n_f_a_state_0: float_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        dict_1 = {n_f_a_state_0: d_f_a_state_0}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        bytes_0 = b"\xf1'\x06\x96\xab\x13\xa5\xaf\x12\x98\xdd\xf8\xff\xfcn"
        dict_2 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: bytes_0, n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_2 = module_0.DFAState(dict_2, n_f_a_state_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_1)
        str_0 = "'+\\ZXm"
        d_f_a_state_1.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_1)
        d_f_a_state_1.unifystate(d_f_a_state_2, d_f_a_state_1)
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = 1805.0
        dict_0 = {n_f_a_state_0: float_0, n_f_a_state_0: float_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        dict_1 = {n_f_a_state_0: d_f_a_state_0}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        str_0 = 'W@P8xt2$nf.{ae`n,v\tI'
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = module_0.NFAState()
        bytes_0 = b"\xf1'\x06\x96\xab\x13\xa5\xaf\x12\x98\xdd\xf8\xff\xfcn"
        dict_2 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: bytes_0, n_f_a_state_1: n_f_a_state_1}
        d_f_a_state_2 = module_0.DFAState(dict_2, n_f_a_state_1)
        str_1 = '\\s+{(\\d+), arcs_(\\d+)_(\\d+)},$'
        d_f_a_state_3 = module_0.DFAState(dict_1, n_f_a_state_0)
        d_f_a_state_3.addarc(d_f_a_state_0, str_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_1)
        d_f_a_state_1.addarc(d_f_a_state_0, str_0)
        d_f_a_state_3.addarc(d_f_a_state_1, str_1)
    except BaseException:
        pass

def test_case_16():
    try:
        n_f_a_state_0 = module_0.NFAState()
        float_0 = 1805.0
        n_f_a_state_0.addarc(n_f_a_state_0)
        dict_0 = {n_f_a_state_0: float_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '|?F3^*HP'
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        str_1 = "'+\\ZXm"
        d_f_a_state_1 = None
        d_f_a_state_0.addarc(d_f_a_state_1, str_1)
    except BaseException:
        pass