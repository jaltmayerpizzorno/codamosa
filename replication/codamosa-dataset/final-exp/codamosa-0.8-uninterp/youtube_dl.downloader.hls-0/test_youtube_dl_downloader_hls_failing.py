# Automatically generated by Pynguin.
import youtube_dl.downloader.hls as module_0

def test_case_0():
    try:
        str_0 = '1'
        list_0 = [str_0, str_0, str_0, str_0, str_0]
        hls_f_d_0 = module_0.HlsFD(list_0, list_0)
        var_0 = hls_f_d_0.can_download(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2595.04
        float_1 = -640.784998
        hls_f_d_0 = module_0.HlsFD(float_0, float_1)
        list_0 = [float_1, hls_f_d_0, float_1]
        hls_f_d_1 = module_0.HlsFD(hls_f_d_0, list_0)
        set_0 = None
        hls_f_d_2 = module_0.HlsFD(set_0, set_0)
        str_0 = '&K'
        var_0 = hls_f_d_0.real_download(str_0, hls_f_d_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1'
        str_1 = 'e'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_1}
        str_2 = 'B?&h}E%\x0b\r%q~Hy\t.]N'
        bytes_0 = b'\xafG${"\xd8'
        bytes_1 = b'i\xf9\xe4\x08i\xd3\xaeET{.\xb8\x94'
        hls_f_d_0 = module_0.HlsFD(bytes_0, bytes_1)
        bool_0 = True
        hls_f_d_1 = module_0.HlsFD(hls_f_d_0, bool_0)
        hls_f_d_2 = module_0.HlsFD(str_2, hls_f_d_1)
        var_0 = hls_f_d_2.can_download(str_1, dict_0)
        list_0 = [str_0, str_0, str_0, str_0]
        hls_f_d_3 = module_0.HlsFD(list_0, list_0)
        str_3 = 'trailer-notice'
        str_4 = '1,b)]"K;g<G'
        var_1 = hls_f_d_3.can_download(str_3, str_4)
    except BaseException:
        pass