# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    pass

def test_case_1():
    n_f_a_state_0 = module_0.NFAState()

def test_case_2():
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)

def test_case_3():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_1 = module_0.NFAState()
    n_f_a_state_2 = module_0.NFAState()

def test_case_4():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_1 = module_0.NFAState()
    tuple_0 = None
    dict_1 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_1: tuple_0, n_f_a_state_1: n_f_a_state_0}
    d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_1)
    d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_0)

def test_case_5():
    str_0 = '"y1d\rg'
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_1 = module_0.NFAState()
    n_f_a_state_1.addarc(n_f_a_state_1, str_0)

def test_case_6():
    str_0 = '"y1d\rg'
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0, n_f_a_state_0: str_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_7():
    str_0 = '"y1d\rg'
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_1 = "A'2fqfMR9vK38]Zg7"
    d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    bool_1 = d_f_a_state_1.__eq__(d_f_a_state_1)

def test_case_8():
    str_0 = "IG'S"
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0, n_f_a_state_0: str_0}
    dict_1 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: dict_0}
    dict_2 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0, n_f_a_state_0: str_0, n_f_a_state_0: dict_0, n_f_a_state_0: str_0}
    d_f_a_state_0 = module_0.DFAState(dict_2, n_f_a_state_0)
    str_1 = '5\\WZ+Mz./w#\r\x0cnwJ.9s'
    d_f_a_state_0.addarc(d_f_a_state_0, str_1)
    d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
    bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)

def test_case_9():
    str_0 = 'AG\\)N1ZS*[+CV""'
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    pgen_grammar_0 = module_0.PgenGrammar()
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    str_1 = 'x\\2zR,yGH>Mv7a'
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
    d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    bool_1 = d_f_a_state_0.__eq__(d_f_a_state_1)

def test_case_10():
    str_0 = '"yhdig'
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_1 = module_0.NFAState()
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_1)
    bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)
    d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_1 = '8q'
    d_f_a_state_0.addarc(d_f_a_state_2, str_1)
    bool_1 = d_f_a_state_2.__eq__(d_f_a_state_2)