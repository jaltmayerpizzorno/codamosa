# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        c_s_v_recoder_0 = module_0.CSVRecoder(lookup_module_0)
        list_0 = [c_s_v_recoder_0]
        c_s_v_recoder_1 = module_0.CSVRecoder(list_0)
        var_0 = c_s_v_recoder_1.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'XK2|Oy'
        c_s_v_reader_0 = module_0.CSVReader(str_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'^\xd0\x1d\x02Q\xc4\x83'
        lookup_module_0 = module_0.LookupModule(bytes_0)
        float_0 = 2415.861
        tuple_0 = (float_0,)
        var_0 = lookup_module_0.read_csv(lookup_module_0, bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        dict_1 = None
        c_s_v_reader_0 = module_0.CSVReader(dict_1)
        float_0 = 0.1
        lookup_module_0 = module_0.LookupModule(float_0, **dict_0)
        var_0 = lookup_module_0.run(c_s_v_reader_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        c_s_v_reader_0 = module_0.CSVReader(bool_0)
        float_0 = 410.0
        list_0 = [bool_0, bool_0, bool_0]
        c_s_v_reader_1 = module_0.CSVReader(list_0)
        var_0 = c_s_v_reader_0.__iter__()
        list_1 = [c_s_v_reader_0, c_s_v_reader_0, bool_0, c_s_v_reader_1]
        str_0 = '--force-handlers'
        str_1 = 'lZD-&'
        dict_0 = {str_0: bool_0, str_1: list_0}
        lookup_module_0 = module_0.LookupModule(list_1, **dict_0)
        var_1 = lookup_module_0.read_csv(c_s_v_reader_0, c_s_v_reader_0, float_0)
    except BaseException:
        pass