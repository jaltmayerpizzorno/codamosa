# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'G(!`<7%to\r&w]Qe^l\\'
    var_0 = module_0.container_to_bytes(str_0)

def test_case_2():
    str_0 = 'simplerepr'
    var_0 = module_0.to_text(str_0, str_0, str_0, str_0)
    str_1 = 'passthru'
    int_0 = 12
    var_1 = module_0.to_text(int_0, str_0, var_0, str_0)
    var_2 = module_0.to_text(int_0, str_1, var_1, str_1)

def test_case_3():
    bytes_0 = b''
    var_0 = module_0.container_to_text(bytes_0)

def test_case_4():
    list_0 = None
    var_0 = module_0.to_text(list_0)

def test_case_5():
    int_0 = 641
    set_0 = {int_0, int_0}
    var_0 = module_0.jsonify(set_0)

def test_case_6():
    str_0 = "a'B0-;"
    var_0 = module_0.jsonify(str_0)

def test_case_7():
    bytes_0 = b'@\xd1'
    dict_0 = None
    tuple_0 = (dict_0,)
    var_0 = module_0.container_to_bytes(bytes_0, tuple_0)

def test_case_8():
    var_0 = {}
    var_1 = module_0.jsonify(var_0)

def test_case_9():
    list_0 = []
    var_0 = module_0.jsonify(list_0)

def test_case_10():
    tuple_0 = ()
    var_0 = module_0.jsonify(tuple_0)

def test_case_11():
    str_0 = '7=$&\x0bO'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = None
    var_0 = module_0.to_text(list_0)
    var_1 = module_0.container_to_text(dict_0)