# Automatically generated by Pynguin.
import youtube_dl.downloader.dash as module_0

def test_case_0():
    try:
        dict_0 = {}
        dash_segments_f_d_0 = module_0.DashSegmentsFD(dict_0, dict_0)
        var_0 = dash_segments_f_d_0.real_download(dash_segments_f_d_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'fragments'
        str_1 = 'url'
        str_2 = 'http://foo/bar/frag1.mp4'
        bytes_0 = b'\xfc\xad\xedx\xa6\x81\x17\re%S\x9f\xd2\x05\xee\xde'
        str_3 = '0:%*I?yt"(IKvz\n$6'
        dash_segments_f_d_0 = module_0.DashSegmentsFD(bytes_0, str_3)
        tuple_0 = None
        dict_0 = {dash_segments_f_d_0: tuple_0, bytes_0: dash_segments_f_d_0, str_0: str_0}
        set_0 = {str_2, str_1}
        dict_1 = {str_1: set_0}
        dash_segments_f_d_1 = module_0.DashSegmentsFD(set_0, dict_1)
        var_0 = dash_segments_f_d_1.real_download(bytes_0, dict_0)
    except BaseException:
        pass