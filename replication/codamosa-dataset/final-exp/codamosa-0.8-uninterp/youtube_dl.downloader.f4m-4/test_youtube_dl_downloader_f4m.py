# Automatically generated by Pynguin.
import youtube_dl.downloader.f4m as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    flv_reader_0 = module_0.FlvReader(*list_0)
    var_0 = module_0.write_flv_header(flv_reader_0)

def test_case_2():
    str_0 = 'live'
    str_1 = 'segments'
    str_2 = 'fragments'
    bool_0 = True
    str_3 = 'segment_run'
    int_0 = 1
    var_0 = (bool_0, int_0)
    int_1 = (int_0, int_0)
    var_1 = [var_0, int_1]
    var_2 = {str_3: var_1}
    var_3 = [var_2]
    str_4 = 'first'
    int_2 = {str_4: int_0, str_4: int_0}
    int_3 = 5
    int_4 = {str_4: int_3, str_1: int_0}
    int_5 = {str_4: int_3, str_4: int_2}
    int_6 = [int_2, int_4, int_5]
    int_7 = {str_2: int_6}
    int_8 = [int_7]
    var_4 = {str_0: bool_0, str_1: var_3, str_2: int_8}
    var_5 = module_0.build_fragments_list(var_4)

def test_case_3():
    str_0 = 'live'
    str_1 = 'segments'
    str_2 = 'fragments'
    bool_0 = False
    str_3 = 'segment_run'
    int_0 = 1
    var_0 = (bool_0, int_0)
    int_1 = 4
    int_2 = (int_0, int_1)
    var_1 = [var_0, int_2]
    var_2 = {str_3: var_1}
    var_3 = [var_2]
    str_4 = 'first'
    int_3 = {str_4: int_0, str_4: int_0}
    int_4 = 5
    int_5 = {str_4: int_4, str_1: int_0}
    int_6 = {str_4: int_4, str_4: int_1}
    int_7 = [int_3, int_5, int_6]
    int_8 = {str_2: int_7}
    int_9 = [int_8]
    var_4 = {str_0: bool_0, str_1: var_3, str_2: int_9}
    var_5 = module_0.build_fragments_list(var_4)