# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        bool_0 = True
        bytes_0 = None
        var_0 = module_0.bytes_to_human(bool_0, bytes_0)
        bytes_1 = b'\xa5\x1f\xa6'
        var_1 = module_0.lenient_lowercase(bytes_1)
        str_0 = '1gv0x'
        var_2 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        var_0 = module_0.human_to_bytes(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 16
        var_0 = module_0.bytes_to_human(int_0)
        str_0 = 'P'
        var_1 = module_0.human_to_bytes(int_0, str_0)
        str_1 = '16L_;'
        var_2 = module_0.human_to_bytes(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 817.4836
        var_0 = module_0.human_to_bytes(float_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '16L_T;'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b';\xe3O\xcf'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        var_0 = module_0.bytes_to_human(bytes_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'c\xce,'
        var_0 = module_0.lenient_lowercase(bytes_0)
        int_0 = -698
        var_1 = module_0.bytes_to_human(int_0)
        str_0 = '@'
        float_0 = -3734.9688
        str_1 = 'k8$\nJ4uE|aT)y:>LE~'
        var_2 = module_0.bytes_to_human(str_0, float_0, str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\xf4d\xf7\x9cB\x96\xf0]\x04\xc5\xdd"\xa3f\x8a\r\r\x94w"'
        var_0 = module_0.lenient_lowercase(bytes_0)
        int_0 = 16
        var_1 = module_0.bytes_to_human(int_0)
        str_0 = '7 >`C\x0ci0]q8bnThi]'
        str_1 = 'T'
        var_2 = module_0.bytes_to_human(str_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '10b'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '10byte'
        var_1 = module_0.human_to_bytes(str_1)
        str_2 = '10bytes'
        var_2 = module_0.human_to_bytes(str_2)
        str_3 = '1kb'
        var_3 = module_0.human_to_bytes(str_3)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '1.5KB'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '1KB'
        var_1 = module_0.human_to_bytes(str_1)
        var_2 = module_0.human_to_bytes(str_0)
        str_2 = '1'
        var_3 = module_0.human_to_bytes(str_2)
        str_3 = 'B'
        var_4 = module_0.human_to_bytes(str_1, str_3)
        bool_0 = True
        var_5 = module_0.human_to_bytes(str_1, str_3, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '10MB'
        var_0 = module_0.human_to_bytes(str_0)
        int_0 = 10
        var_1 = module_0.human_to_bytes(int_0)
        str_1 = 'MB'
        var_2 = module_0.human_to_bytes(int_0, str_1)
        str_2 = 'kb'
        var_3 = module_0.human_to_bytes(int_0, str_2)
    except BaseException:
        pass