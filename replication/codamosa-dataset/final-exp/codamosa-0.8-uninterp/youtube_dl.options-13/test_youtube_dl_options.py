# Automatically generated by Pynguin.
import youtube_dl.options as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = []
    var_1 = module_0.parseOpts(var_0)

def test_case_2():
    var_0 = module_0.parseOpts()

def test_case_3():
    str_0 = '--verbose'
    str_1 = '-v'
    str_2 = [str_0, str_1]
    var_0 = module_0.parseOpts(str_2)