# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    try:
        str_0 = '&%'
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        pgen_grammar_0 = module_0.generate_grammar()
    except BaseException:
        pass

def test_case_2():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = 'D)#&SD|oosOV\rn@sv]I'
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        bool_0 = True
        parser_generator_0 = module_0.ParserGenerator(str_0, bool_0)
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
        n_f_a_state_0 = None
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    except BaseException:
        pass

def test_case_6():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = 'D)#&SD|oosOV\rn@sv]I'
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = None
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_1)
    except BaseException:
        pass

def test_case_7():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        tuple_0 = (n_f_a_state_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '&%'
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '&%'
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = None
        n_f_a_state_0.addarc(n_f_a_state_1)
    except BaseException:
        pass

def test_case_10():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = None
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '&%'
        d_f_a_state_1 = None
        d_f_a_state_0.addarc(d_f_a_state_1, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_0 = '&%'
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        str_1 = ''
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1.addarc(d_f_a_state_1, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_1, d_f_a_state_1)
        bool_1 = d_f_a_state_0.__eq__(str_1)
    except BaseException:
        pass