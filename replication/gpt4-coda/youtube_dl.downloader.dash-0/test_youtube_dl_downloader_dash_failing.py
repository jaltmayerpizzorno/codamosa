# Automatically generated by Pynguin.
import youtube_dl.downloader.dash as module_0

def test_case_0():
    try:
        float_0 = -2266.29
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        dash_segments_f_d_0 = module_0.DashSegmentsFD(float_0, dict_0)
        set_0 = set()
        var_0 = dash_segments_f_d_0.real_download(set_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'test_video.mp4'
        str_1 = 'fragments'
        str_2 = 'fragment_base_url'
        str_3 = 'path'
        str_4 = 'url'
        str_5 = 'test_segment-1.mp4'
        str_6 = 'http://testserver/test_segment-1.mp4'
        str_7 = {str_3: str_5, str_4: str_6}
        str_8 = [str_7]
        str_9 = 'http://testserver/'
        str_10 = {str_1: str_8, str_2: str_9}
        str_11 = 'test'
        str_12 = 'fragment_retries'
        str_13 = 'skip_unavailable_fragments'
        bool_0 = True
        bool_1 = False
        bool_2 = {str_11: bool_0, str_12: bool_0, str_13: bool_1}
        var_0 = None
        dash_segments_f_d_0 = module_0.DashSegmentsFD(var_0, bool_2)
        var_1 = dash_segments_f_d_0.real_download(str_0, str_10)
    except BaseException:
        pass