# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'rgb123'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'gray0'
    var_1 = module_0.parsecolor(str_1)

def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.stringc(bool_0, list_0)

def test_case_3():
    str_0 = '{.699rJojFq~t)j/i'
    bytes_0 = b'\xc8D\x0f\xe0\xcf\xf0^'
    var_0 = module_0.colorize(str_0, str_0, bytes_0)

def test_case_4():
    int_0 = 90
    bytes_0 = b'$\xa6\xe1\x15e\x00r<-\xff\x1f{'
    var_0 = module_0.hostcolor(int_0, bytes_0)

def test_case_5():
    str_0 = 'color255'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'rgb123'
    var_1 = module_0.parsecolor(str_1)
    str_2 = 'rgb321'
    var_2 = module_0.parsecolor(str_2)
    str_3 = 'gray0'
    var_3 = module_0.parsecolor(str_3)