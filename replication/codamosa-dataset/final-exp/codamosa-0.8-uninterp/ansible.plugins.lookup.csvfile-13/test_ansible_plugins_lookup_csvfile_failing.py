# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        str_0 = 's\n0bQ\t?W*{U\r]n\x0b q'
        c_s_v_recoder_0 = module_0.CSVRecoder(str_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xf7\xec\xef\xa0\x90'
        str_0 = 'Candidate'
        set_0 = {bytes_0, bytes_0, str_0}
        tuple_0 = (bytes_0, set_0, set_0)
        c_s_v_recoder_0 = module_0.CSVRecoder(tuple_0)
        var_0 = c_s_v_recoder_0.__iter__()
        int_0 = -817
        list_0 = [str_0]
        dict_0 = {str_0: var_0}
        c_s_v_reader_0 = module_0.CSVReader(int_0, list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'r'
        var_0 = lookup_module_0.read_csv(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        str_0 = 'C'
        str_1 = '|),\td~$l?^tZEI?g(-9'
        str_2 = 'redirect'
        str_3 = '-f)OBO# <_OYiL'
        bytes_0 = b'v\xf0\x0f4\x97y]\x16.\xc2\xd6\x98\xb8$'
        dict_0 = {str_1: str_1, str_2: str_1, str_3: str_2, str_3: bytes_0}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.run(bool_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'test.txt'
        var_0 = lookup_module_0.read_csv(str_0, str_0, str_0, str_0)
    except BaseException:
        pass