# Automatically generated by Pynguin.
import ansible.modules.lineinfile as module_0

def test_case_0():
    try:
        float_0 = 1000.0
        set_0 = None
        float_1 = -4063.027871
        var_0 = module_0.write_changes(float_0, set_0, float_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\n\xc7\x90/\xb0\x16u[-e\x97\x17\x0f'
        list_0 = []
        set_0 = set()
        tuple_0 = (list_0, set_0)
        str_0 = '#Mv\t'
        var_0 = module_0.check_file_attrs(bytes_0, list_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ansible.modules.lineinfile'
        bytes_0 = b'/\x10]\x82~GJ\x10`\x8c\xe03vY\x96\xf2'
        list_0 = [bytes_0]
        dict_0 = {str_0: bytes_0}
        tuple_0 = None
        int_0 = -64
        var_0 = module_0.present(str_0, list_0, dict_0, dict_0, tuple_0, list_0, tuple_0, list_0, int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ansible.modules.lineinfile'
        bytes_0 = b'/\x10]\x82~GC\x97J\x10`\x8c\xe03\xc0Y\x96\xf2'
        list_0 = []
        dict_0 = {str_0: bytes_0}
        tuple_0 = None
        int_0 = -56
        var_0 = module_0.present(str_0, list_0, dict_0, dict_0, tuple_0, list_0, tuple_0, list_0, int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'ansible.modu%es.lineinfile'
        bytes_0 = b'\x107\x82GJ\x10`\x8c\xe03v\xef\x96\xf2'
        list_0 = [bytes_0]
        dict_0 = {str_0: bytes_0}
        tuple_0 = None
        int_0 = -72
        var_0 = module_0.present(str_0, list_0, dict_0, dict_0, tuple_0, list_0, tuple_0, list_0, int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        int_0 = -1432
        str_0 = '`ye\ni]mi\\R?#L_'
        int_1 = 5986
        list_0 = [int_0, int_1, int_0, int_1]
        var_0 = module_0.absent(tuple_0, int_0, str_0, int_0, int_1, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ansible.modules.lineinfile'
        bool_0 = True
        bytes_0 = b'/\x10]\x82~GJ\x10`\x8c\xe03vY\x96\xf2'
        list_0 = [bytes_0]
        dict_0 = {str_0: bytes_0}
        int_0 = 2505
        tuple_0 = None
        str_1 = 'ansible.modules.lineinfile'
        str_2 = 'z<i'
        bool_1 = False
        var_0 = module_0.present(list_0, bytes_0, str_2, bytes_0, str_1, tuple_0, str_2, bool_0, bool_1, int_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'ansible.modules.lineinfile'
        bytes_0 = b'/\x10]\x82~GJ\x10`\x8c\xe03vY\x96\xf2'
        dict_0 = {str_0: bytes_0}
        tuple_0 = None
        str_1 = '>IRZ]+nw|&}]JI'
        float_0 = -2862.424642
        str_2 = 'qLe{sL.9[":NR!HYg0'
        dict_1 = {str_0: dict_0, str_1: bytes_0, str_0: float_0, str_2: str_0}
        str_3 = '/'
        float_1 = 85.2651
        var_0 = module_0.absent(dict_1, str_3, tuple_0, float_1, dict_0, str_1)
    except BaseException:
        pass