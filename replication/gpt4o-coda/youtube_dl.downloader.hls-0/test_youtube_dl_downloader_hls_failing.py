# Automatically generated by Pynguin.
import youtube_dl.downloader.hls as module_0

def test_case_0():
    try:
        int_0 = None
        str_0 = "Q`\n6C^Q\x0b-1>bDB'i6"
        hls_f_d_0 = module_0.HlsFD(int_0, str_0)
        var_0 = hls_f_d_0.can_download(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        bool_1 = False
        str_0 = '(?P<base>https?://(?:www\\.)?raiplay\\.it/.+?-(?P<id>%s))\\.(?:html|json)'
        hls_f_d_0 = module_0.HlsFD(bool_1, str_0)
        float_0 = -119.553
        bytes_0 = b'\x8b\x7f\x9d\xb4o'
        hls_f_d_1 = module_0.HlsFD(float_0, bytes_0)
        var_0 = hls_f_d_1.real_download(set_0, hls_f_d_0)
    except BaseException:
        pass