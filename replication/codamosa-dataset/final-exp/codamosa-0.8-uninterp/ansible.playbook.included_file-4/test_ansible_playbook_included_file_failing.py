# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0
import ansible.playbook.role_include as module_1

def test_case_0():
    try:
        float_0 = 238.596
        int_0 = -57
        float_1 = 2656.0
        set_0 = set()
        included_file_0 = module_0.IncludedFile(int_0, float_1, float_1, set_0)
        var_0 = included_file_0.__eq__(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '14 |'
        int_0 = -811
        list_0 = []
        int_1 = 574
        int_2 = -6156
        float_0 = 1.5
        included_file_0 = module_0.IncludedFile(int_1, int_2, float_0, int_2)
        var_0 = included_file_0.process_include_results(str_0, int_0, list_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ']vyxC5/ynd|c\tDpQe7f,'
        int_0 = 95
        float_0 = -507.0
        bytes_0 = b'\xc9\xab\x88\xf7'
        set_0 = set()
        included_file_0 = None
        included_file_1 = module_0.IncludedFile(bytes_0, int_0, set_0, included_file_0)
        list_0 = []
        included_file_2 = module_0.IncludedFile(float_0, bytes_0, included_file_1, list_0)
        dict_0 = {str_0: str_0, str_0: bytes_0}
        var_0 = included_file_1.__eq__(included_file_2)
        tuple_0 = (int_0, str_0, dict_0)
        bytes_1 = b'\xdf\xd6\xec\xdfN\x8c'
        var_1 = included_file_2.__repr__()
        included_file_3 = module_0.IncludedFile(list_0, float_0, float_0, bytes_1)
        set_1 = {int_0, int_0}
        var_2 = included_file_1.add_host(included_file_1)
        var_3 = included_file_3.process_include_results(set_0, int_0, float_0, included_file_2)
        included_file_4 = module_0.IncludedFile(bytes_0, dict_0, list_0, set_1)
        included_file_5 = module_0.IncludedFile(tuple_0, set_1, bytes_1, included_file_3, dict_0)
        var_4 = included_file_1.process_include_results(str_0, dict_0, included_file_1, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'filename'
        str_1 = 'filename'
        str_2 = 'vars'
        str_3 = 'task'
        included_file_0 = module_0.IncludedFile(str_0, str_1, str_2, str_3)
        included_file_1 = module_0.IncludedFile(str_0, str_1, str_2, str_3)
        dict_0 = {}
        bytes_0 = b'8#\xf8\xb7~9\x8fZ\x00\x19\x06}'
        include_role_0 = module_1.IncludeRole()
        list_0 = []
        var_0 = included_file_0.process_include_results(dict_0, bytes_0, include_role_0, list_0)
        str_4 = 'task2'
        included_file_2 = module_0.IncludedFile(str_0, str_1, str_2, str_4)
        var_1 = print(var_0)
        var_2 = included_file_0 == included_file_2
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'aIAW%:'
        set_0 = {str_0, str_0}
        bool_0 = True
        complex_0 = None
        bytes_0 = b'u\x06v\xcak\xde\x15?#\x12\x02\xb7N;\x01a9bF'
        dict_0 = {bytes_0: bool_0}
        float_0 = 2480.2395
        int_0 = 803
        set_1 = {bool_0}
        list_0 = [set_1, set_1]
        included_file_0 = module_0.IncludedFile(bytes_0, dict_0, float_0, int_0, list_0)
        var_0 = included_file_0.add_host(complex_0)
        bytes_1 = b'\xdfv\x80E\x9aN=\nm\xdeUF\xca\xc9O\xea\\M\x08'
        included_file_1 = module_0.IncludedFile(set_0, bytes_1, bool_0, bytes_1)
        var_1 = included_file_1.__repr__()
        str_1 = '{/tobBk7S-\\%d0$V'
        float_1 = None
        int_1 = 870
        included_file_2 = module_0.IncludedFile(included_file_1, float_1, int_1, str_1)
        var_2 = included_file_0.__repr__()
        var_3 = included_file_0.add_host(float_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'filename'
        str_1 = 'args'
        included_file_0 = module_0.IncludedFile(str_0, str_1, str_1, str_0)
        var_0 = included_file_0 == included_file_0
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ']vyxC5/ynd|c\tDpQe7f,'
        int_0 = 73
        float_0 = 1.0
        bytes_0 = b'\xe1x\xa9G\xb5\xb7'
        set_0 = set()
        included_file_0 = None
        included_file_1 = module_0.IncludedFile(bytes_0, int_0, set_0, included_file_0)
        list_0 = []
        included_file_2 = module_0.IncludedFile(float_0, bytes_0, included_file_1, list_0)
        bool_0 = True
        bytes_1 = b'\x1c\x84~z\xf1\xc0'
        dict_0 = {str_0: str_0, bytes_1: bool_0, str_0: bytes_1, int_0: str_0}
        tuple_0 = (bytes_1, dict_0, dict_0)
        included_file_3 = module_0.IncludedFile(bool_0, tuple_0, set_0, dict_0)
        var_0 = included_file_3.__eq__(included_file_2)
        dict_1 = {int_0: str_0, str_0: str_0, int_0: str_0, int_0: int_0}
        bytes_2 = b'\xf4\xb3]\x90\x97\xf6'
        list_1 = [dict_1, bytes_2, int_0, str_0]
        float_1 = 0.001
        set_1 = {int_0, float_1}
        bytes_3 = b'\xa8\x04\r\xeb\x9e\x1c\x97o\x94\x99C\xbf\x9b'
        included_file_4 = module_0.IncludedFile(list_1, float_1, float_1, bytes_2)
        list_2 = []
        var_1 = included_file_1.add_host(included_file_1)
        var_2 = included_file_4.process_include_results(set_0, int_0, float_0, included_file_2)
        included_file_5 = module_0.IncludedFile(bytes_3, dict_1, list_2, set_0)
        var_3 = included_file_5.process_include_results(bytes_2, list_1, float_1, set_1)
    except BaseException:
        pass