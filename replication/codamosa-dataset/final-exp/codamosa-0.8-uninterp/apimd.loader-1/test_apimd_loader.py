# Automatically generated by Pynguin.
import apimd.loader as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'A'
    dict_0 = {str_0: str_0}
    sequence_0 = module_0.gen_api(dict_0)

def test_case_2():
    str_0 = '\t'
    dict_0 = {str_0: str_0, str_0: str_0}
    sequence_0 = module_0.gen_api(dict_0, prefix=str_0)

def test_case_3():
    str_0 = 'docs'
    str_1 = 'BkLRXD07JHoLwVo'
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
    str_2 = '$Gl\x0c(.PST'
    bool_0 = True
    sequence_0 = module_0.gen_api(dict_0, prefix=str_2, toc=bool_0, dry=bool_0)

def test_case_4():
    str_0 = 'c'
    dict_0 = {str_0: str_0}
    sequence_0 = module_0.gen_api(dict_0, str_0, prefix=str_0)

def test_case_5():
    str_0 = 'c'
    dict_0 = {str_0: str_0}
    sequence_0 = module_0.gen_api(dict_0, prefix=str_0)