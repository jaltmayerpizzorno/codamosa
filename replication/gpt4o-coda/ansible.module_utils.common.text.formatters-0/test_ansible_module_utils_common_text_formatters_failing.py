# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        list_0 = None
        var_0 = module_0.bytes_to_human(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -227
        var_0 = module_0.human_to_bytes(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        dict_0 = {set_0: set_0, set_0: set_0}
        var_0 = module_0.bytes_to_human(set_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        str_0 = '-o&/'
        var_0 = module_0.bytes_to_human(str_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '0\rH'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        var_0 = module_0.bytes_to_human(bool_0)
        str_0 = "83ps%8#!5S.n'/P"
        var_1 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/"/)x\x0cZb8n<:F\x0bf'
        float_0 = 1284.0
        bool_0 = True
        var_0 = module_0.bytes_to_human(bool_0)
        int_0 = None
        tuple_0 = (float_0, int_0)
        var_1 = module_0.lenient_lowercase(tuple_0)
        str_1 = "83ps%8#!5S.n'/P"
        var_2 = module_0.human_to_bytes(var_0)
        var_3 = module_0.bytes_to_human(bool_0)
        str_2 = "67r\\3)8\x0cBV-Xu?'9^"
        set_0 = {str_1, str_0, var_3}
        var_4 = module_0.human_to_bytes(str_2, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 1284.0
        bool_0 = False
        var_0 = module_0.bytes_to_human(bool_0)
        int_0 = None
        tuple_0 = (float_0, int_0)
        var_1 = module_0.lenient_lowercase(tuple_0)
        str_0 = "83ps%8#!5.n'/P"
        var_2 = module_0.human_to_bytes(var_0)
        var_3 = module_0.bytes_to_human(bool_0)
        list_0 = None
        float_1 = 393.8726064674496
        set_0 = {list_0, var_0, var_2}
        var_4 = module_0.human_to_bytes(str_0, float_1, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '/"/)x\x0cZb8n<:F\x0bf'
        float_0 = 1284.0
        var_0 = module_0.bytes_to_human(float_0)
        int_0 = None
        tuple_0 = (float_0, int_0)
        var_1 = module_0.lenient_lowercase(tuple_0)
        var_2 = module_0.human_to_bytes(var_0)
        list_0 = None
        int_1 = 529
        var_3 = module_0.human_to_bytes(int_1)
        set_0 = {list_0, var_0, var_2}
        var_4 = module_0.human_to_bytes(str_0, float_0, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = None
        float_0 = 1284.0
        var_0 = module_0.bytes_to_human(float_0)
        tuple_0 = None
        complex_0 = None
        set_0 = {var_0, str_0, var_0, complex_0}
        str_1 = 'E'
        var_1 = module_0.bytes_to_human(tuple_0, set_0, str_1)
    except BaseException:
        pass