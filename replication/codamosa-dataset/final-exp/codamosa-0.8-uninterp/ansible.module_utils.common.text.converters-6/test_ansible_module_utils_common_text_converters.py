# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'j)^jY^)j\x0b^\nhl`F7K'
    var_0 = module_0.container_to_bytes(str_0)

def test_case_2():
    set_0 = set()
    var_0 = module_0.to_bytes(set_0)

def test_case_3():
    bytes_0 = b'foobar'
    var_0 = module_0.to_text(bytes_0)

def test_case_4():
    int_0 = 1
    var_0 = module_0.to_text(int_0)

def test_case_5():
    bool_0 = False
    var_0 = module_0.jsonify(bool_0)

def test_case_6():
    list_0 = []
    bool_0 = True
    var_0 = module_0.container_to_bytes(bool_0)
    var_1 = module_0.to_bytes(list_0)

def test_case_7():
    float_0 = 21.072
    tuple_0 = (float_0,)
    list_0 = [tuple_0, float_0, float_0, tuple_0]
    list_1 = []
    var_0 = module_0.container_to_bytes(list_0, list_1)

def test_case_8():
    bytes_0 = b'\xd4Q'
    var_0 = module_0.jsonify(bytes_0)

def test_case_9():
    str_0 = 'ascii'
    var_0 = module_0.to_bytes(str_0, str_0)
    dict_0 = {str_0: var_0}
    var_1 = module_0.jsonify(dict_0)

def test_case_10():
    complex_0 = None
    list_0 = [complex_0, complex_0]
    var_0 = module_0.container_to_text(list_0)

def test_case_11():
    str_0 = 'Ł'
    str_1 = 'ascii'
    var_0 = module_0.to_bytes(str_0, str_1)