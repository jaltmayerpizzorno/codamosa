# Automatically generated by Pynguin.
import ansible.modules.lineinfile as module_0
import tempfile as module_1

def test_case_0():
    try:
        bool_0 = True
        int_0 = -409
        var_0 = module_0.write_changes(bool_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'W\x13\xcaD%\xe9\xb6\x92a\xbaP\x0b'
        tuple_0 = None
        int_0 = 1050
        float_0 = None
        var_0 = module_0.check_file_attrs(bytes_0, tuple_0, int_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -4857
        float_0 = 0.5
        bytes_0 = b'\xbe\xf9F\x14\x18'
        str_0 = 'e#[dUcS+~;t\\.'
        list_0 = [bytes_0, float_0]
        var_0 = module_0.present(int_0, float_0, bytes_0, str_0, bytes_0, str_0, bytes_0, float_0, bytes_0, list_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        bool_0 = False
        tuple_0 = ()
        set_0 = {dict_0, tuple_0, tuple_0, dict_0}
        str_0 = 'M/]A}!3x\nqu6'
        bool_1 = True
        int_0 = -1028
        bytes_0 = b''
        var_0 = module_0.present(dict_0, bool_0, tuple_0, set_0, dict_0, str_0, bool_1, dict_0, int_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -4686
        bytes_0 = b'\xa6o\xf5\xc65\x86\xc7\xebW'
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: bytes_0}
        bool_0 = False
        var_0 = module_0.absent(int_0, dict_0, dict_0, dict_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        str_0 = 'fz| D_\rgseQxzZs'
        str_1 = './5BDy^X\n:W[He\n\r&^@'
        dict_0 = {str_0: str_0, str_0: bool_0, str_0: str_1}
        tuple_0 = (dict_0,)
        list_0 = []
        set_0 = None
        bytes_0 = b'.\x8b\xac\xcc'
        bytes_1 = b'\x8b\x0c\xa4)K7\xd8\xf97'
        str_2 = '8@'
        dict_1 = {str_2: bytes_0}
        list_1 = [dict_1, dict_0]
        str_3 = " ]'PU#_"
        var_0 = module_0.present(tuple_0, tuple_0, list_0, list_0, set_0, bytes_0, bytes_1, dict_1, list_1, bool_0, str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = module_1.NamedTemporaryFile()
        var_1 = var_0.name
        var_2 = None
        str_0 = 'ba[rz]'
        str_1 = 'bar'
        bool_0 = False
        var_3 = module_0.absent(var_2, var_1, str_0, var_2, str_1, bool_0)
    except BaseException:
        pass