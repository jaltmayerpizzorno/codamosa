# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        c_s_v_recoder_0 = module_0.CSVRecoder(lookup_module_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -317
        set_0 = {int_0, int_0, int_0, int_0}
        list_0 = [set_0, set_0, int_0]
        c_s_v_reader_0 = module_0.CSVReader(set_0, list_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '/tmp/test.csv'
        var_0 = lookup_module_0.read_csv(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'k(eDG\x0c0F@oB*}+Gvv5\x0b'
        c_s_v_recoder_0 = module_0.CSVRecoder(str_0)
        str_1 = '2('
        str_2 = 'UNKNOWN'
        str_3 = '3WZrFKY\\\\v'
        dict_0 = {str_1: str_0, str_2: str_2, str_3: str_3}
        list_0 = [str_3, str_0, str_1, str_3]
        int_0 = -1567
        tuple_0 = (c_s_v_recoder_0, dict_0, list_0, int_0)
        dict_1 = {}
        lookup_module_0 = module_0.LookupModule(dict_1, **dict_1)
        var_0 = lookup_module_0.run(c_s_v_recoder_0, tuple_0, **dict_0)
    except BaseException:
        pass