# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    var_0 = module_0.to_bytes(dict_0)

def test_case_2():
    bytes_0 = b'\xe1\x88\xb4'
    var_0 = module_0.to_bytes(bytes_0)
    str_0 = 'á\x88´'
    str_1 = 'ascii'
    var_1 = module_0.to_bytes(str_0, str_1)

def test_case_3():
    bytes_0 = b'\xea'
    var_0 = module_0.container_to_text(bytes_0)

def test_case_4():
    dict_0 = {}
    var_0 = module_0.to_text(dict_0)

def test_case_5():
    str_0 = 'Yw%W+g:>".jj{UE!&+'
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.jsonify(set_0)

def test_case_6():
    str_0 = 'фициональная область'
    var_0 = module_0.jsonify(str_0)

def test_case_7():
    str_0 = '\x0b&ZBX'
    int_0 = 379
    tuple_0 = (int_0, int_0, int_0)
    var_0 = module_0.jsonify(tuple_0)
    dict_0 = {str_0: str_0}
    var_1 = module_0.container_to_bytes(dict_0)

def test_case_8():
    str_0 = 'ሴ'
    var_0 = module_0.to_bytes(str_0)
    var_1 = module_0.to_bytes(str_0)
    bytes_0 = b'\xe1\x88\xb4'
    var_2 = module_0.to_bytes(bytes_0)
    str_1 = 'á\x88´'
    list_0 = [var_0, var_2]
    var_3 = module_0.container_to_bytes(list_0, str_1)
    var_4 = module_0.to_bytes(str_1)
    str_2 = 'ascii'
    var_5 = module_0.to_bytes(str_1, str_2)

def test_case_9():
    dict_0 = {}
    var_0 = module_0.jsonify(dict_0, **dict_0)

def test_case_10():
    list_0 = []
    var_0 = module_0.jsonify(list_0)

def test_case_11():
    int_0 = 379
    tuple_0 = (int_0, int_0, int_0)
    var_0 = module_0.jsonify(tuple_0)

def test_case_12():
    bytes_0 = b'b\x9d\x85\xba\xae'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    str_0 = 'l Ftk*9@w\x0c83n'
    complex_0 = None
    dict_0 = {bytes_0: list_0, complex_0: list_0}
    var_0 = module_0.container_to_text(dict_0)
    var_1 = module_0.to_text(str_0)
    var_2 = module_0.jsonify(list_0)

def test_case_13():
    float_0 = -1419.2
    dict_0 = {}
    list_0 = [float_0, dict_0]
    var_0 = module_0.container_to_text(list_0)
    var_1 = module_0.to_text(float_0)

def test_case_14():
    str_0 = 'á\x88´'
    str_1 = 'ascii'
    var_0 = module_0.to_bytes(str_0, str_1)