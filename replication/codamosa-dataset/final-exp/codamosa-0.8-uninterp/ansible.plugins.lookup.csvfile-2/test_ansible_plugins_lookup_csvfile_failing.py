# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        str_0 = '4'
        c_s_v_reader_0 = module_0.CSVReader(str_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        c_s_v_recoder_0 = None
        list_0 = [c_s_v_recoder_0]
        int_0 = 169
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.read_csv(c_s_v_recoder_0, list_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ' ?(:|：) ?'
        str_1 = ';g,luNl'
        str_2 = 'W{;`dmz:,'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_2}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        bool_0 = False
        var_0 = lookup_module_0.run(dict_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        dict_0 = {int_0: int_0, int_0: int_0}
        list_0 = [int_0, dict_0, int_0, dict_0]
        c_s_v_recoder_0 = module_0.CSVRecoder(list_0)
        tuple_0 = ()
        c_s_v_recoder_1 = module_0.CSVRecoder(tuple_0)
        str_0 = 'wmkuA(4Ay'
        c_s_v_recoder_2 = module_0.CSVRecoder(str_0)
        var_0 = c_s_v_recoder_2.__next__()
    except BaseException:
        pass