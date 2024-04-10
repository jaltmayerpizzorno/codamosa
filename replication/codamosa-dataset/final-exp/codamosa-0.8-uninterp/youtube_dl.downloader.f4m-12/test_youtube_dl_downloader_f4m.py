# Automatically generated by Pynguin.
import youtube_dl.compat as module_0
import youtube_dl.downloader.f4m as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '<manifest><baseURL2>a</baseURL2></manifest>'
    var_0 = module_0.compat_etree_fromstring(str_0)
    var_1 = module_1.get_base_url(var_0)

def test_case_2():
    str_0 = 'segments'
    str_1 = 'fragments'
    str_2 = 'live'
    str_3 = 'segment_run'
    int_0 = 5
    int_1 = (int_0, int_0)
    int_2 = 10
    int_3 = [int_1, int_1]
    int_4 = {str_3: int_3}
    int_5 = [int_4]
    str_4 = 'first'
    int_6 = 1
    int_7 = 2000
    int_8 = {str_4: int_6, str_1: int_2, str_3: int_7}
    int_9 = 2
    int_10 = 3000
    int_11 = {str_4: int_9, str_2: int_10, str_3: int_7}
    int_12 = [int_8, int_11]
    int_13 = {str_1: int_12}
    int_14 = [int_13]
    bool_0 = False
    var_0 = {str_0: int_5, str_1: int_14, str_2: bool_0}
    var_1 = module_1.build_fragments_list(var_0)

def test_case_3():
    str_0 = 'segments'
    str_1 = 'fragments'
    str_2 = 'live'
    str_3 = 'segment_run'
    int_0 = 0
    int_1 = 5
    int_2 = (int_0, int_1)
    int_3 = [int_2, int_2]
    int_4 = {str_3: int_3}
    int_5 = [int_4]
    str_4 = 'first'
    str_5 = 'ts'
    str_6 = 'duration'
    int_6 = 1
    int_7 = 1000
    int_8 = 2000
    int_9 = {str_4: int_6, str_5: int_7, str_6: int_8}
    int_10 = 2
    int_11 = 3000
    int_12 = {str_4: int_10, str_5: int_11, str_6: int_8}
    int_13 = [int_9, int_12]
    int_14 = {str_1: int_13}
    int_15 = [int_14]
    bool_0 = True
    var_0 = {str_0: int_5, str_1: int_15, str_2: bool_0}
    var_1 = module_1.build_fragments_list(var_0)

def test_case_4():
    bytes_0 = b'<Media><SegmentURL media="s1m1" quality="high" '
    bytes_1 = b'drmAdditionalHeaderId="16" drmAdditionalHeaderSetId="1"/>'
    var_0 = bytes_0 + bytes_1
    bytes_2 = b'<SegmentURL media="s1m1" quality="low" '
    var_1 = var_0 + bytes_2
    bytes_3 = b'drmAdditionalHeaderId="16" drmAdditionalHeaderSetId="2"/></Media>'
    var_2 = var_1 + bytes_3
    var_3 = module_0.compat_etree_fromstring(var_2)
    var_4 = module_1.remove_encrypted_media(var_3)

def test_case_5():
    bytes_0 = b'<?xml version="1.0" encoding="UTF-8"?>\n<manifest xmlns="http://ns.adobe.com/f4m/1.0">\n  <baseURL>http://host.com/publishpoint/</baseURL>\n</manifest>'
    var_0 = module_0.compat_etree_fromstring(bytes_0)
    var_1 = module_1.get_base_url(var_0)

def test_case_6():
    bytes_0 = b'<Media><SegmentURL media="s1m1" quality="high" '
    bytes_1 = b'drmAdditionalHeaerId="16" drmAdditionalHeaderSetId="1"/>'
    var_0 = bytes_0 + bytes_1
    bytes_2 = b'<SegmentURL media="s1m1" quality="low" '
    var_1 = var_0 + bytes_2
    bytes_3 = b'drmAdditionalHeaderId="16" drmAdditionalHeaderSetId="2"/></Media>'
    var_2 = var_1 + bytes_3
    var_3 = module_0.compat_etree_fromstring(var_2)
    var_4 = module_1.remove_encrypted_media(var_3)