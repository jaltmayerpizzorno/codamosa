# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0
import os as module_1

def test_case_0():
    try:
        str_0 = '\rwKgz+*5o]'
        str_1 = 'ahpiCj ]]`YZx'
        parser_generator_0 = module_0.ParserGenerator(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'g.xW6R\\'
        parser_generator_0 = module_0.ParserGenerator(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        n_f_a_state_0 = None
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    except BaseException:
        pass

def test_case_3():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        path_like_0 = module_1.PathLike()
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
        str_0 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'symbol2lab~l'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = None
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1.addarc(d_f_a_state_0, str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        n_f_a_state_0 = module_0.NFAState()
        str_0 = '\n    A wildcard pattern can match zero or more nodes.\n\n    This has all the flexibility needed to implement patterns like:\n\n    .*      .+      .?      .{m,n}\n    (a b c | d e | f)\n    (...)*  (...)+  (...)?  (...){m,n}\n\n    except it always uses non-greedy matching.\n    '
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_1, str_0)
        pgen_grammar_0 = module_0.generate_grammar()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ']NV_vU\r)uX^W!\nY$7K'
        list_0 = [str_0, str_0]
        d_f_a_state_0 = None
        str_1 = "7@\x0cv'"
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0, n_f_a_state_0: list_0, n_f_a_state_0: list_0}
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_1.addarc(d_f_a_state_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'symbol2lab~l'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        bool_1 = d_f_a_state_0.__eq__(n_f_a_state_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'symbo2lab~'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = '"%YYNd=R\t'
        d_f_a_state_0.addarc(d_f_a_state_1, str_2)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_1 = None
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_1, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        pgen_grammar_0 = None
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_1 = None
        dict_0 = {n_f_a_state_0: pgen_grammar_0, n_f_a_state_1: n_f_a_state_0, n_f_a_state_0: n_f_a_state_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        dict_1 = {n_f_a_state_0: pgen_grammar_0}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'symbol2lab~l'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_1)
        n_f_a_state_0.addarc(n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        str_2 = ')]}'
        parser_generator_0 = module_0.ParserGenerator(str_2, n_f_a_state_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'symbo2lab~'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = '"%YYNd=R\t'
        d_f_a_state_0.addarc(d_f_a_state_1, str_2)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_3 = 'E&^V9lLk=1CF![cq'
        d_f_a_state_3 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_4 = '\x0cnkt5hp~\x0b<@8Z'
        pgen_grammar_0 = module_0.PgenGrammar()
        d_f_a_state_3.addarc(d_f_a_state_1, str_4)
        float_0 = -468.262
        parser_generator_0 = module_0.ParserGenerator(str_3, float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'symbol2>lab~l'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_1)
        n_f_a_state_0.addarc(n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = ')]}'
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_1)
        d_f_a_state_0.addarc(d_f_a_state_1, str_2)
        parser_generator_0 = module_0.ParserGenerator(str_2, n_f_a_state_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '_\x0bo5d\x0c$'
        str_1 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = '"%YYNd=R\t'
        d_f_a_state_0.addarc(d_f_a_state_1, str_2)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        pgen_grammar_0 = module_0.generate_grammar()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '^'
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1.unifystate(d_f_a_state_0, d_f_a_state_1)
        n_f_a_state_1 = module_0.NFAState()
        d_f_a_state_2 = module_0.DFAState(dict_0, n_f_a_state_1)
        str_1 = 'EIOLx7sgs6'
        d_f_a_state_0.addarc(d_f_a_state_2, str_1)
        n_f_a_state_1.addarc(n_f_a_state_1)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_2)
        str_2 = ')]}'
        parser_generator_0 = module_0.ParserGenerator(str_2)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'symbol2lab~l'
        str_1 = ''
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: str_0, n_f_a_state_0: str_1}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0, str_0)
        d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_2 = '"%YYNd=R\t'
        d_f_a_state_0.addarc(d_f_a_state_1, str_2)
        n_f_a_state_0.addarc(n_f_a_state_0)
        d_f_a_state_1.addarc(d_f_a_state_1, str_1)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)
        dict_1 = None
        d_f_a_state_2 = module_0.DFAState(dict_1, n_f_a_state_0)
    except BaseException:
        pass

def test_case_19():
    try:
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        float_0 = -2797.31
        n_f_a_state_0.addarc(n_f_a_state_0, float_0)
    except BaseException:
        pass