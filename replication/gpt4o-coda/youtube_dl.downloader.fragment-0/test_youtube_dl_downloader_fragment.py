# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = None
    tuple_0 = (int_0,)
    list_0 = [tuple_0, tuple_0, int_0]
    bool_0 = False
    fragment_f_d_0 = module_0.FragmentFD(bool_0, bool_0)
    fragment_f_d_1 = module_0.FragmentFD(list_0, fragment_f_d_0)
    str_0 = 'Y1>'
    fragment_f_d_2 = module_0.FragmentFD(fragment_f_d_1, str_0)
    float_0 = 146.333
    http_quiet_downloader_0 = module_0.HttpQuietDownloader(fragment_f_d_2, float_0)
    var_0 = http_quiet_downloader_0.to_screen()