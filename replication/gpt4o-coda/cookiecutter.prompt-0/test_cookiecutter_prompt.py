# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1991
    list_0 = []
    set_0 = set()
    var_0 = module_0.render_variable(int_0, list_0, set_0)

def test_case_2():
    dict_0 = {}
    bytes_0 = b''
    float_0 = 1675.1324
    var_0 = module_0.render_variable(bytes_0, dict_0, float_0)

def test_case_3():
    str_0 = '{"key": "value"}'
    var_0 = module_0.process_json(str_0)