# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        int_0 = -1389
        var_0 = module_0.human_to_bytes(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '7Wx<vz0'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '8KA6`ER,i8t>b\t{JP'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        float_0 = 2053.726019
        var_0 = module_0.bytes_to_human(tuple_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2459
        var_0 = module_0.bytes_to_human(int_0)
        str_0 = ''
        float_0 = -1843.3865
        tuple_0 = (str_0, float_0)
        list_0 = [tuple_0]
        float_1 = -847.287282
        var_1 = module_0.bytes_to_human(list_0, float_1)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 2.0
        bytes_0 = b'\x99h\xdf\xa5s\xabT'
        int_0 = 1120
        tuple_0 = (bytes_0, int_0)
        bool_0 = False
        var_0 = module_0.bytes_to_human(float_0, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1B'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '2T'
        var_1 = module_0.human_to_bytes(str_1)
        var_2 = module_0.human_to_bytes(str_1)
        str_2 = '1bb'
        var_3 = module_0.human_to_bytes(str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1B'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '1GB'
        var_1 = module_0.human_to_bytes(str_1)
        str_2 = '2T'
        var_2 = module_0.human_to_bytes(str_2)
        var_3 = module_0.human_to_bytes(str_0)
        var_4 = module_0.human_to_bytes(str_0)
        str_3 = '1bb'
        var_5 = module_0.human_to_bytes(str_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '1GB'
        var_0 = module_0.human_to_bytes(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '1b'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '1byte'
        var_1 = module_0.human_to_bytes(str_1)
        str_2 = '1bytes'
        var_2 = module_0.human_to_bytes(str_2)
        str_3 = '1 B'
        var_3 = module_0.human_to_bytes(str_3)
        str_4 = '1Byte'
        var_4 = module_0.human_to_bytes(str_4)
        str_5 = '1Bytes'
        var_5 = module_0.human_to_bytes(str_5)
        var_6 = module_0.human_to_bytes(str_1)
        var_7 = module_0.human_to_bytes(str_2)
        str_6 = '1k'
        var_8 = module_0.human_to_bytes(str_6)
        str_7 = '1K'
        var_9 = module_0.human_to_bytes(str_7)
        str_8 = '1Ki'
        var_10 = module_0.human_to_bytes(str_8)
    except BaseException:
        pass