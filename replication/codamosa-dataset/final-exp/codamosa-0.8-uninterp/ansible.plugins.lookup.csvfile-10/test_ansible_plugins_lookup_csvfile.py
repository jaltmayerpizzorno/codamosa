# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0
import codecs as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = 835.27
    c_s_v_recoder_0 = module_0.CSVRecoder(float_0)

def test_case_2():
    float_0 = 835.27
    c_s_v_recoder_0 = module_0.CSVRecoder(float_0)
    var_0 = c_s_v_recoder_0.__iter__()

def test_case_3():
    str_0 = 'modified files in the working repository will be discarded'
    c_s_v_reader_0 = module_0.CSVReader(str_0)

def test_case_4():
    str_0 = '/etc/hosts'
    str_1 = 'rb'
    var_0 = module_1.open(str_0, str_1)
    c_s_v_reader_0 = module_0.CSVReader(var_0)
    var_1 = next(c_s_v_reader_0)
    var_2 = next(c_s_v_reader_0)
    var_3 = next(c_s_v_reader_0)
    var_4 = module_1.open(str_0, str_1)
    str_2 = '\t'
    c_s_v_reader_1 = module_0.CSVReader(var_4)

def test_case_5():
    lookup_module_0 = module_0.LookupModule()
    str_0 = 'test.csv'
    str_1 = 'w'
    var_0 = module_1.open(str_0, str_1)
    str_2 = 'Test3'
    str_3 = ','
    var_1 = lookup_module_0.read_csv(str_0, str_2, str_3)