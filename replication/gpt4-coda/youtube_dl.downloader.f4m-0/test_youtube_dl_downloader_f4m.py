# Automatically generated by Pynguin.
import youtube_dl.downloader.f4m as module_0
import youtube_dl.compat as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    flv_reader_0 = module_0.FlvReader()
    var_0 = flv_reader_0.read_bytes(bool_0)

def test_case_2():
    list_0 = []
    var_0 = module_0.remove_encrypted_media(list_0)

def test_case_3():
    str_0 = 'live'
    str_1 = 'segments'
    str_2 = 'fragments'
    bool_0 = False
    str_3 = 'segment_run'
    int_0 = 5123
    int_1 = (int_0, int_0)
    int_2 = [int_1]
    int_3 = {str_3: int_2}
    int_4 = [int_3, int_3]
    str_4 = 'first'
    str_5 = 'duration'
    int_5 = 1000
    int_6 = 19
    var_0 = {str_4: int_3, str_4: int_5, str_5: int_6, str_5: int_4}
    int_7 = -2468
    var_1 = [var_0, str_5, var_0]
    var_2 = {int_7: str_4, str_2: var_1, str_1: int_7, str_5: int_7}
    var_3 = [var_2]
    var_4 = {str_0: bool_0, str_1: int_4, str_2: var_3}
    var_5 = module_0.build_fragments_list(var_4)

def test_case_4():
    str_0 = '\n    <media>\n        <stream drmAdditionalHeaderId="123" url="http://example.com/encrypted1" />\n        <stream url="http://example.com/non_encrypted1" />\n        <stream drmAdditionalHeaderSetId="456" url="http://example.com/encrypted2" />\n        <stream url="http://example.com/non_encrypted2" />\n    </media>\n    '
    var_0 = module_1.compat_etree_fromstring(str_0)
    var_1 = module_0.remove_encrypted_media(var_0)
    var_2 = len(var_1)

def test_case_5():
    str_0 = 'live'
    str_1 = 'segments'
    str_2 = 'fragments'
    bool_0 = True
    str_3 = 'segment_run'
    int_0 = 5123
    int_1 = (int_0, int_0)
    int_2 = [int_1]
    int_3 = {str_3: int_2}
    int_4 = [int_3]
    str_4 = 'first'
    str_5 = 'duration'
    int_5 = 1000
    var_0 = {str_4: int_3, str_4: int_5, str_5: int_2, str_5: int_4}
    int_6 = -2468
    var_1 = [var_0, str_5, var_0]
    var_2 = {int_6: str_4, str_2: var_1, str_1: int_6, str_5: int_6}
    var_3 = [var_2]
    var_4 = {str_0: bool_0, str_1: int_4, str_2: var_3}
    var_5 = module_0.build_fragments_list(var_4)

def test_case_6():
    bytes_0 = b'hello\x00world\x00'
    list_0 = [bytes_0]
    flv_reader_0 = module_0.FlvReader(*list_0)
    var_0 = flv_reader_0.read_string()