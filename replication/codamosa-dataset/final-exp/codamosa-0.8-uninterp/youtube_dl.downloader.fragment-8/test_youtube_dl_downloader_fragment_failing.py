# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        dict_0 = {}
        set_0 = set()
        int_0 = 1381789200
        float_0 = -2197.58164
        int_1 = -840
        float_1 = 1801.303109
        fragment_f_d_0 = module_0.FragmentFD(int_1, float_1)
        var_0 = fragment_f_d_0.report_retry_fragment(dict_0, set_0, int_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = -1822
        str_0 = 'https://www.bfmtv.com/sante/covid-19-un-responsable-de-l-institut-pasteur-se-demande-quand-la-france-va-se-reconfiner_AV-202101060198.html'
        list_0 = []
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(str_0, list_0)
        fragment_f_d_0 = module_0.FragmentFD(int_0, http_quiet_downloader_0)
        var_0 = fragment_f_d_0.report_skip_fragment(bool_0)
    except BaseException:
        pass