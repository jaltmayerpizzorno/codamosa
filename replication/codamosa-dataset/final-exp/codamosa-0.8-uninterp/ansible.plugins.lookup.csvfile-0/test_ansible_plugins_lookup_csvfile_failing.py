# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        list_0 = []
        str_0 = ''
        c_s_v_recoder_0 = module_0.CSVRecoder(list_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -838.7
        str_0 = 'hostport'
        set_0 = {str_0}
        c_s_v_recoder_0 = module_0.CSVRecoder(set_0)
        var_0 = c_s_v_recoder_0.__iter__()
        lookup_module_0 = None
        c_s_v_recoder_1 = module_0.CSVRecoder(lookup_module_0)
        dict_0 = {float_0: float_0}
        lookup_module_1 = module_0.LookupModule()
        var_1 = lookup_module_1.read_csv(float_0, dict_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xc9\xe9\x1a\xae'
        set_0 = set()
        str_0 = '&4GJ'
        float_0 = 4620.0
        tuple_0 = (bytes_0, set_0, str_0, float_0)
        c_s_v_recoder_0 = module_0.CSVRecoder(tuple_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xbe'
        c_s_v_reader_0 = module_0.CSVReader(bytes_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        c_s_v_reader_0 = module_0.CSVReader(dict_0)
        var_0 = c_s_v_reader_0.__iter__()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -838.7
        dict_0 = {float_0: float_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.read_csv(float_0, dict_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -1295
        dict_0 = {}
        c_s_v_recoder_0 = module_0.CSVRecoder(dict_0)
        c_s_v_reader_0 = module_0.CSVReader(int_0)
        dict_1 = {c_s_v_reader_0: c_s_v_reader_0, int_0: int_0, int_0: c_s_v_reader_0}
        str_0 = ',4dw3Wo>N))g,i&'
        dict_2 = {}
        c_s_v_recoder_1 = module_0.CSVRecoder(dict_1)
        lookup_module_0 = module_0.LookupModule(c_s_v_recoder_1)
        var_0 = lookup_module_0.run(str_0, **dict_2)
    except BaseException:
        pass