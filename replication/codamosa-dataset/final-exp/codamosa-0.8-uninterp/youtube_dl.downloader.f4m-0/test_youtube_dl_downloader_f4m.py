# Automatically generated by Pynguin.
import youtube_dl.compat as module_0
import youtube_dl.downloader.f4m as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '<manifest xmlns="http://ns.adobe.com/f4m/1.0"/>'
    var_0 = module_0.compat_etree_fromstring(str_0)
    var_1 = module_1.get_base_url(var_0)

def test_case_2():
    str_0 = '<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>{0}</baseURL></manifest>'
    var_0 = module_0.compat_etree_fromstring(str_0)
    var_1 = module_1.get_base_url(var_0)

def test_case_3():
    str_0 = 'segments'
    str_1 = 'fragments'
    str_2 = 'live'
    str_3 = 'segment_run'
    int_0 = 4
    int_1 = (int_0, int_0)
    int_2 = [int_1]
    int_3 = {str_3: int_2}
    int_4 = [int_3]
    str_4 = 'first'
    int_5 = 1
    int_6 = {str_4: int_5}
    int_7 = [int_6]
    int_8 = {str_1: int_7}
    int_9 = [int_8]
    bool_0 = False
    var_0 = {str_0: int_4, str_1: int_9, str_2: bool_0}
    var_1 = module_1.build_fragments_list(var_0)

def test_case_4():
    str_0 = 'segments'
    str_1 = 'fragments'
    dict_0 = {}
    f4m_f_d_0 = module_1.F4mFD(dict_0, dict_0)
    str_2 = 'live'
    str_3 = 'segment_run'
    int_0 = 1
    int_1 = 2
    int_2 = (int_0, int_1)
    int_3 = [int_2]
    int_4 = {str_3: int_3}
    int_5 = [int_4]
    str_4 = 'first'
    str_5 = 'ts'
    str_6 = 'duration'
    int_6 = 100
    var_0 = None
    var_1 = {str_4: int_0, str_5: int_6, str_6: int_0, str_2: var_0}
    var_2 = [var_1]
    var_3 = {str_1: var_2}
    var_4 = [var_3]
    bool_0 = True
    var_5 = {str_0: int_5, str_1: var_4, str_2: bool_0}
    var_6 = module_1.build_fragments_list(var_5)