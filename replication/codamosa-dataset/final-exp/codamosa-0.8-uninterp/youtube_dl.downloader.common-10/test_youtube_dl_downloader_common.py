# Automatically generated by Pynguin.
import youtube_dl.downloader.common as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -650.66716
    bytes_0 = b'\x11vC\xf0"\x05\xf3\xcf\xef\xd9'
    file_downloader_0 = module_0.FileDownloader(float_0, bytes_0)

def test_case_2():
    bool_0 = True
    str_0 = 'mss'
    int_0 = -257
    file_downloader_0 = module_0.FileDownloader(str_0, int_0)
    var_0 = file_downloader_0.format_seconds(bool_0)

def test_case_3():
    int_0 = 293
    float_0 = 2442.9
    bool_0 = True
    file_downloader_0 = module_0.FileDownloader(float_0, bool_0)
    var_0 = file_downloader_0.format_retries(int_0)

def test_case_4():
    var_0 = None
    str_0 = 'continuedl'
    bool_0 = False
    bool_1 = {str_0: bool_0}
    file_downloader_0 = module_0.FileDownloader(var_0, bool_1)
    str_1 = 'foo.part'
    var_1 = file_downloader_0.undo_temp_name(str_1)
    str_2 = 'foo'
    var_2 = file_downloader_0.undo_temp_name(str_2)

def test_case_5():
    var_0 = {}
    file_downloader_0 = module_0.FileDownloader(var_0, var_0)
    str_0 = 'Your copy of %s is outdated, update %s to version %s or newer ifhyou encounter any errors.'
    var_1 = file_downloader_0.try_utime(str_0, str_0)

def test_case_6():
    str_0 = 'BK?Fs\\*/x&\x0bt^1R\t`'
    int_0 = -1979
    bool_0 = True
    str_1 = 'QC2($~;=bT+W-7b'
    str_2 = None
    dict_0 = {str_1: int_0, str_2: str_2}
    file_downloader_0 = module_0.FileDownloader(bool_0, dict_0)
    file_downloader_1 = module_0.FileDownloader(int_0, file_downloader_0)
    var_0 = file_downloader_1.ytdl_filename(str_0)
    bool_1 = True
    str_3 = 'mss'
    int_1 = -257
    file_downloader_2 = module_0.FileDownloader(str_3, int_1)
    var_1 = file_downloader_2.format_seconds(bool_1)

def test_case_7():
    list_0 = []
    bytes_0 = b'|'
    dict_0 = {bytes_0: list_0}
    file_downloader_0 = module_0.FileDownloader(bytes_0, dict_0)
    str_0 = '.V-g4<'
    var_0 = file_downloader_0.temp_name(str_0)

def test_case_8():
    bool_0 = False
    float_0 = 356.7695
    str_0 = 'a8\rp>9qr"W-1!\x0cA5Z'
    file_downloader_0 = module_0.FileDownloader(float_0, str_0)
    var_0 = file_downloader_0.format_eta(bool_0)
    bool_1 = True
    str_1 = 'Q>w4t$ZnOt)a4T>%'
    int_0 = -257
    file_downloader_1 = module_0.FileDownloader(str_1, int_0)
    var_1 = file_downloader_1.format_seconds(bool_1)

def test_case_9():
    list_0 = []
    bytes_0 = b'\xa0\xac\x12\x06'
    dict_0 = {bytes_0: list_0}
    str_0 = 'vieo:iframe'
    file_downloader_0 = module_0.FileDownloader(bytes_0, dict_0)
    file_downloader_1 = None
    var_0 = file_downloader_0.format_speed(file_downloader_1)
    var_1 = file_downloader_0.try_utime(str_0, bytes_0)

def test_case_10():
    list_0 = []
    str_0 = 'video:iframe'
    set_0 = {str_0}
    file_downloader_0 = module_0.FileDownloader(str_0, set_0)
    complex_0 = None
    var_0 = file_downloader_0.try_utime(list_0, complex_0)

def test_case_11():
    list_0 = []
    bytes_0 = b''
    dict_0 = {bytes_0: list_0}
    float_0 = -3521.633102167042
    file_downloader_0 = module_0.FileDownloader(bytes_0, dict_0)
    int_0 = 1330956000
    file_downloader_1 = module_0.FileDownloader(float_0, bytes_0)
    str_0 = 'https?://(?:www\\.)?vidbit\\.co/(?:watch|embed)\\?.*?\\bv=(?P<id>[\\da-zA-Z]+)'
    var_0 = file_downloader_0.calc_speed(int_0, int_0, str_0)

def test_case_12():
    float_0 = 227.155
    str_0 = '\\cxaB9mlh]K6{XDO'
    bytes_0 = b'\xf4\xdf\xf3L\xecOY\xdd\xc2\xb4\x86\x07qGg\x07'
    dict_0 = {str_0: bytes_0}
    list_0 = [dict_0, dict_0, dict_0]
    tuple_0 = (list_0,)
    file_downloader_0 = module_0.FileDownloader(dict_0, tuple_0)
    var_0 = file_downloader_0.try_rename(float_0, float_0)

def test_case_13():
    list_0 = []
    bytes_0 = b'\xa0\xac\x12\x06'
    dict_0 = {bytes_0: list_0}
    str_0 = 'vieo:ifram5e'
    float_0 = -3521.633102167042
    file_downloader_0 = module_0.FileDownloader(bytes_0, dict_0)
    var_0 = file_downloader_0.try_utime(str_0, bytes_0)
    str_1 = 'k\rRjcb`\x0b| }eU2"o$4H'
    dict_1 = {str_1: var_0}
    bool_0 = None
    int_0 = 1330956000
    var_1 = file_downloader_0.calc_eta(dict_1, float_0, bool_0, int_0)

def test_case_14():
    bytes_0 = b'\xf2Gd(K\xf5g'
    float_0 = -2447.0
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    str_0 = None
    str_1 = 'Tp(v\x0b{k *Un'
    dict_1 = {str_0: str_0, str_1: bool_0, str_0: dict_0, str_0: str_0}
    file_downloader_0 = module_0.FileDownloader(dict_0, dict_1)
    var_0 = file_downloader_0.slow_down(bytes_0, float_0, bytes_0)

def test_case_15():
    int_0 = 1429
    dict_0 = {}
    file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
    float_0 = 1087.921101
    bytes_0 = b'7\x8b\xf3\xf4\x82\xec\xf0\x12\xe8Y\xc8\\U'
    int_1 = -375
    str_0 = 'xBRxF!RpHWbP/j>BAzz'
    var_0 = file_downloader_0.calc_eta(float_0, int_1, str_0, bytes_0)

def test_case_16():
    list_0 = []
    bytes_0 = b'\xa0\xac\x12\x06'
    dict_0 = {bytes_0: list_0}
    str_0 = 'vieo:iframe'
    list_1 = [list_0, list_0, dict_0, str_0]
    float_0 = -5849.8772
    str_1 = '-d8/Z5g\nk]Ux{vdK.'
    int_0 = None
    file_downloader_0 = module_0.FileDownloader(dict_0, int_0)
    file_downloader_1 = module_0.FileDownloader(file_downloader_0, list_1)
    str_2 = None
    dict_1 = {str_1: int_0, str_2: str_0, str_2: file_downloader_1, str_1: list_1}
    file_downloader_2 = module_0.FileDownloader(list_0, dict_1)
    bytes_1 = b'O\xd9\r\x85TZ\xd8`'
    str_3 = '9NL 8'
    var_0 = file_downloader_2.slow_down(list_0, bytes_1, str_3)
    set_0 = None
    str_4 = 'f'
    file_downloader_3 = module_0.FileDownloader(set_0, str_4)
    bool_0 = False
    var_1 = file_downloader_2.calc_eta(float_0, int_0, list_1, bool_0)

def test_case_17():
    list_0 = []
    bytes_0 = b'|'
    dict_0 = {bytes_0: list_0}
    float_0 = -1474.1
    str_0 = 'Ks8#m>"maEe'
    str_1 = '^JIqrrcs,TP1lw_W&!\n.'
    dict_1 = {str_0: bytes_0, str_1: str_0}
    set_0 = set()
    file_downloader_0 = module_0.FileDownloader(dict_1, set_0)
    var_0 = file_downloader_0.format_eta(float_0)
    file_downloader_1 = module_0.FileDownloader(bytes_0, dict_0)
    var_1 = file_downloader_1.try_utime(str_0, bytes_0)
    str_2 = 'k\rRjcb`\x0b7 C}eU2"oW4D'
    dict_2 = {}
    set_1 = {str_0, bytes_0, str_2, var_1}
    int_0 = -265
    complex_0 = None
    tuple_0 = (dict_2, set_1, int_0, complex_0)
    var_2 = file_downloader_1.slow_down(tuple_0, complex_0, file_downloader_1)
    str_3 = '4'
    var_3 = file_downloader_1.parse_bytes(str_3)