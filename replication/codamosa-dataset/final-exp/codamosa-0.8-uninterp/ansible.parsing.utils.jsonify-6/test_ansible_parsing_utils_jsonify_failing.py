# Automatically generated by Pynguin.
import ansible.parsing.utils.jsonify as module_0

def test_case_0():
    try:
        bytes_0 = b"\x15'\x1fz\x96\xf4\x1c\xbb\x9d\xfd\xc4]\\v\xe5\xcd"
        var_0 = module_0.jsonify(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'h\xa0e\x85\x85V\xbd\x1a5'
        list_0 = None
        var_0 = module_0.jsonify(list_0)
        str_0 = 'Qe>3Duf}sc'
        list_1 = [bytes_0, bytes_0, str_0]
        var_1 = module_0.jsonify(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xec\xa9O\x99\x19\xa5f\x7f\x17\xfc\xab\xb8\xf2\x8c\xece\xeb\xca'
        var_0 = module_0.jsonify(bytes_0, bytes_0)
    except BaseException:
        pass