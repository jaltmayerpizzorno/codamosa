# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        float_0 = 3165.95
        list_0 = [float_0, float_0, float_0, float_0]
        list_1 = [list_0]
        str_0 = 'system-bitrate'
        fragment_f_d_0 = module_0.FragmentFD(list_1, str_0)
        bytes_0 = b'o\xbbZ\xe6\x14\x178\x9a\xb5'
        tuple_0 = None
        bool_0 = True
        var_0 = fragment_f_d_0.report_retry_fragment(tuple_0, tuple_0, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        float_0 = 2235.93
        list_0 = [float_0, float_0, float_0, float_0]
        set_1 = set()
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(list_0, set_1)
        fragment_f_d_0 = module_0.FragmentFD(float_0, http_quiet_downloader_0)
        var_0 = fragment_f_d_0.report_skip_fragment(set_0)
    except BaseException:
        pass