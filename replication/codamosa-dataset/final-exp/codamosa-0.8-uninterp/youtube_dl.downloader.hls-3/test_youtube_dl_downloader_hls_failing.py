# Automatically generated by Pynguin.
import youtube_dl.downloader.hls as module_0

def test_case_0():
    try:
        str_0 = 'L%MPN\t\\z@-2'
        hls_f_d_0 = module_0.HlsFD(str_0, str_0)
        var_0 = hls_f_d_0.can_download(str_0, hls_f_d_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'lNOz\x0ch%h'
        int_0 = -1101
        bytes_0 = b'\xe9DQ\x02\xdc2'
        tuple_0 = (bytes_0,)
        bool_0 = True
        hls_f_d_0 = module_0.HlsFD(tuple_0, bool_0)
        var_0 = hls_f_d_0.real_download(str_0, int_0)
    except BaseException:
        pass