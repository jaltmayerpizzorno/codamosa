# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -4151
    var_0 = module_0.to_text(int_0)

def test_case_2():
    int_0 = None
    bytes_0 = b'\xbc\xa8\x17W\'"\xba\xf0\xbd\xee8t\xc7\xa7\xa7O\x85'
    float_0 = -734.4
    var_0 = module_0.to_text(int_0, bytes_0, float_0)
    set_0 = set()
    str_0 = 'OQ73^]X5\\V6o\np<'
    var_1 = module_0.container_to_bytes(str_0)
    list_0 = [set_0, set_0, set_0]
    var_2 = module_0.jsonify(list_0)
    int_1 = 10
    var_3 = module_0.container_to_bytes(int_1)

def test_case_3():
    str_0 = None
    var_0 = module_0.jsonify(str_0)

def test_case_4():
    str_0 = 'Z&2GUQ\\HLgG'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.container_to_bytes(dict_0)

def test_case_5():
    float_0 = 605.11
    str_0 = ":;]0s*vIjL*6q5U'0}pI"
    var_0 = module_0.container_to_bytes(float_0, str_0)
    str_1 = None
    var_1 = module_0.jsonify(str_1)

def test_case_6():
    float_0 = -245.32
    var_0 = module_0.container_to_text(float_0)

def test_case_7():
    dict_0 = {}
    var_0 = module_0.jsonify(dict_0)

def test_case_8():
    list_0 = []
    var_0 = module_0.jsonify(list_0)

def test_case_9():
    int_0 = 92
    str_0 = 'u$_IyJ K|lv\x0cVT'
    var_0 = module_0.jsonify(str_0)
    dict_0 = {int_0: int_0}
    var_1 = module_0.container_to_text(dict_0)

def test_case_10():
    bytes_0 = b'\x05P\x8f<O6\xfcN\x99\xb5\x00\xe9'
    list_0 = [bytes_0, bytes_0]
    dict_0 = None
    var_0 = module_0.to_bytes(dict_0)
    list_1 = [list_0, list_0]
    bool_0 = False
    var_1 = module_0.jsonify(bool_0)
    bool_1 = None
    var_2 = module_0.container_to_bytes(list_1, bool_1)