# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    pass

def test_case_1():
    n_f_a_state_0 = module_0.NFAState()

def test_case_2():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_0.addarc(n_f_a_state_0)

def test_case_3():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)

def test_case_4():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = 'l'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)

def test_case_5():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = 'l'
    d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
    n_f_a_state_0.addarc(n_f_a_state_0, str_0)

def test_case_6():
    pgen_grammar_0 = module_0.PgenGrammar()
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    dict_1 = {n_f_a_state_0: pgen_grammar_0}
    n_f_a_state_1 = module_0.NFAState()
    d_f_a_state_0 = module_0.DFAState(dict_1, n_f_a_state_1)
    str_0 = 'l'
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
    d_f_a_state_1.addarc(d_f_a_state_0, str_0)
    d_f_a_state_1.unifystate(d_f_a_state_1, d_f_a_state_1)

def test_case_7():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_0.addarc(n_f_a_state_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_8():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_1 = module_0.NFAState()
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_1)
    n_f_a_state_0.addarc(n_f_a_state_0)
    bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)

def test_case_9():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = 'l'
    n_f_a_state_0.addarc(n_f_a_state_0)
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_10():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = ''
    n_f_a_state_1 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_1, str_0)
    str_1 = 'bTPjy@a=!.Vr8sIvN'
    d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_1)

def test_case_11():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
    d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = ''
    n_f_a_state_1 = module_0.NFAState()
    n_f_a_state_2 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0, str_0)
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    str_1 = 'bM)B3]1%QRL+Xkvwzr'
    d_f_a_state_1.addarc(d_f_a_state_1, str_1)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_1)