# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'device_links'
    c_s_v_recoder_0 = module_0.CSVRecoder(str_0)

def test_case_2():
    int_0 = 1596
    c_s_v_reader_0 = module_0.CSVReader(int_0)

def test_case_3():
    int_0 = 1596
    c_s_v_reader_0 = module_0.CSVReader(int_0)
    var_0 = c_s_v_reader_0.__iter__()

def test_case_4():
    lookup_module_0 = module_0.LookupModule()
    str_0 = './test_LookupModule_read_csv.csv'
    str_1 = '_'
    var_0 = lookup_module_0.read_csv(str_0, str_1, str_1)