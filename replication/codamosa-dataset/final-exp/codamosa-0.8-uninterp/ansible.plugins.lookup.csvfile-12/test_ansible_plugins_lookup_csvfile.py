# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    c_s_v_recoder_0 = module_0.CSVRecoder(bool_0)
    str_0 = '-Y1aR'
    str_1 = 'm>[f'
    str_2 = '*s~`N'
    dict_0 = {str_0: c_s_v_recoder_0, str_1: c_s_v_recoder_0, str_2: str_0}
    lookup_module_0 = module_0.LookupModule(c_s_v_recoder_0, **dict_0)

def test_case_2():
    float_0 = -1322.3
    c_s_v_reader_0 = module_0.CSVReader(float_0)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '/dev/null'
    str_1 = 'ascii'
    str_2 = ','
    var_0 = lookup_module_0.read_csv(str_0, str_0, str_2, str_1, str_1)