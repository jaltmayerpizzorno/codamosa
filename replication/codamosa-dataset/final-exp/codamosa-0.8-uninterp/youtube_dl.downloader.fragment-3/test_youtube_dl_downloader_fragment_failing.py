# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        int_0 = 440
        str_0 = '8__'
        float_0 = 1049.0
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(float_0, float_0)
        http_quiet_downloader_1 = module_0.HttpQuietDownloader(http_quiet_downloader_0, float_0)
        list_1 = [http_quiet_downloader_1, http_quiet_downloader_1, float_0]
        bool_0 = True
        fragment_f_d_0 = module_0.FragmentFD(list_1, bool_0)
        var_0 = fragment_f_d_0.report_retry_fragment(dict_0, list_0, int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "}jrX-'AS%EU=^O@IK#W\t"
        str_1 = None
        list_0 = [str_1, str_1]
        int_0 = 494
        fragment_f_d_0 = module_0.FragmentFD(list_0, int_0)
        var_0 = fragment_f_d_0.report_skip_fragment(str_0)
    except BaseException:
        pass