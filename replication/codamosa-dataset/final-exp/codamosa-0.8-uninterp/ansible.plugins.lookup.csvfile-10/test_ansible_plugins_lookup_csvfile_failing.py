# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        bytes_0 = b'\x01\xa5x):\x04J\x05\xef{\xb76]v\xbb\xda\x06'
        c_s_v_recoder_0 = module_0.CSVRecoder(bytes_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        str_1 = ','
        dict_0 = {str_0: str_0, str_1: str_1}
        c_s_v_reader_0 = module_0.CSVReader(dict_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Tv'
        c_s_v_reader_0 = module_0.CSVReader(str_0)
        var_0 = c_s_v_reader_0.__iter__()
        lookup_module_0 = module_0.LookupModule()
        var_1 = lookup_module_0.run(c_s_v_reader_0)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'test'
        var_0 = lookup_module_0.read_csv(str_0, str_0, str_0)
    except BaseException:
        pass