# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        str_0 = 'k8,HCOg6&"r3:"?ds\'{\\'
        str_1 = 'UvAI0`Fs y\\@1tQ*'
        str_2 = 'Downloading video metadata JSON'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_0}
        list_0 = [str_2]
        str_3 = '2!>y\x0b9[\nmZ-*Y*Du'
        bytes_0 = None
        fragment_f_d_0 = module_0.FragmentFD(bytes_0, bytes_0)
        str_4 = ',d-5P\n>`V#zxE['
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(fragment_f_d_0, str_4)
        list_1 = [http_quiet_downloader_0]
        fragment_f_d_1 = module_0.FragmentFD(list_1, fragment_f_d_0)
        var_0 = fragment_f_d_1.report_retry_fragment(dict_0, list_0, str_3, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        bool_1 = False
        str_0 = '--fixup'
        dict_0 = {str_0: str_0, str_0: str_0}
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(str_0, dict_0)
        fragment_f_d_0 = module_0.FragmentFD(bool_1, http_quiet_downloader_0)
        var_0 = fragment_f_d_0.report_skip_fragment(bool_0)
    except BaseException:
        pass