# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        float_0 = -2166.8
        list_0 = [float_0, float_0, float_0]
        list_1 = []
        int_0 = 1593
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(list_1, int_0)
        var_0 = http_quiet_downloader_0.to_screen(*list_0)
        str_0 = 'N5Y\nmdc0/F&^9"('
        set_0 = set()
        fragment_f_d_0 = module_0.FragmentFD(str_0, set_0)
        var_1 = fragment_f_d_0.report_skip_fragment(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '><$4{Xy'
        tuple_0 = None
        fragment_f_d_0 = module_0.FragmentFD(str_0, tuple_0)
        int_0 = None
        dict_0 = None
        list_0 = [dict_0]
        str_1 = ''
        bytes_0 = b'U\xa2\xb8\xf8a\xf4\x88\x91\xce'
        list_1 = [bytes_0, bytes_0, bytes_0, bytes_0]
        fragment_f_d_1 = module_0.FragmentFD(bytes_0, list_1)
        var_0 = fragment_f_d_1.report_retry_fragment(fragment_f_d_0, int_0, list_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        float_0 = 1526.316156
        bytes_0 = b'mZx\xb7\xdd\xca\xa3m\xc37B'
        fragment_f_d_0 = module_0.FragmentFD(float_0, bytes_0)
        var_0 = fragment_f_d_0.report_skip_fragment(bool_0)
    except BaseException:
        pass