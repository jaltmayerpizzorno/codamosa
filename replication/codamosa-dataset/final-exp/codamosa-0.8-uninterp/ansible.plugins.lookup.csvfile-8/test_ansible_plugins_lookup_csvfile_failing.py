# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        bytes_0 = None
        int_0 = -1192
        c_s_v_reader_0 = module_0.CSVReader(int_0)
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        bytes_1 = b'\xb2'
        lookup_module_0 = module_0.LookupModule(bytes_1)
        c_s_v_recoder_0 = module_0.CSVRecoder(dict_0)
        bytes_2 = b'[O\x0bi0\x11\xf1\x173\xed\xd6\x92\xfa\x03\x80k\t'
        c_s_v_reader_1 = module_0.CSVReader(bytes_2)
        var_0 = c_s_v_recoder_0.__iter__()
        var_1 = c_s_v_recoder_0.__iter__()
        float_0 = 0.0001
        c_s_v_recoder_1 = module_0.CSVRecoder(float_0, c_s_v_reader_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'X\r'
        c_s_v_recoder_0 = module_0.CSVRecoder(str_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'compresseddirty'
        c_s_v_reader_0 = module_0.CSVReader(str_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = "tNQ'"
        list_0 = None
        tuple_0 = None
        bool_0 = True
        var_0 = lookup_module_0.read_csv(str_0, list_0, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(lookup_module_0)
    except BaseException:
        pass