# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ':'
    c_s_v_recoder_0 = module_0.CSVRecoder(str_0)

def test_case_2():
    int_0 = -733
    c_s_v_reader_0 = module_0.CSVReader(int_0)

def test_case_3():
    float_0 = -511.9798
    list_0 = [float_0, float_0, float_0, float_0]
    c_s_v_reader_0 = module_0.CSVReader(list_0)
    var_0 = c_s_v_reader_0.__iter__()