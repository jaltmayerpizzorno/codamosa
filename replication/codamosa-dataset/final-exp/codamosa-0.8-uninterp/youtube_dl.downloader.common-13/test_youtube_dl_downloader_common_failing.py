# Automatically generated by Pynguin.
import youtube_dl.downloader.common as module_0

def test_case_0():
    try:
        bool_0 = True
        dict_0 = None
        float_0 = -978.324558
        float_1 = -270.0
        file_downloader_0 = module_0.FileDownloader(float_0, float_1)
        var_0 = file_downloader_0.calc_percent(dict_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        int_0 = -398
        dict_0 = {bool_0: int_0}
        dict_1 = None
        file_downloader_0 = module_0.FileDownloader(dict_1, dict_0)
        str_0 = '3Ih)N{M#kh}xVUc2i'
        var_0 = file_downloader_0.calc_percent(str_0, dict_1)
        list_0 = [file_downloader_0]
        var_1 = file_downloader_0.format_eta(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -488
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
        str_0 = "'okcpgk8\t``A"
        set_0 = {int_0, str_0}
        bool_0 = True
        var_0 = file_downloader_0.calc_speed(set_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b"\xdd'\x89s\xf3\xa43\x1e\r\xad\x8d\xa9\xb7\xe7I\x94>}"
        str_0 = ''
        str_1 = 'ts-5727'
        str_2 = "Sq'Q`?K?a,\x0bkz"
        dict_0 = {str_0: str_0, str_1: str_2}
        dict_1 = {str_2: str_0, str_0: str_2}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_1)
        list_0 = [file_downloader_0]
        bool_0 = True
        tuple_0 = (str_0, list_0, bool_0, dict_1)
        file_downloader_1 = module_0.FileDownloader(str_2, tuple_0)
        var_0 = file_downloader_1.format_speed(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xc3o&h{\xf0'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        str_0 = 'P2y{\tlgmx."'
        set_0 = {str_0, str_0, str_0, str_0}
        file_downloader_0 = module_0.FileDownloader(str_0, set_0)
        var_0 = file_downloader_0.format_retries(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b"\xbaQ'\xc2\xfe\xd5\xd9\xb0\x01\xbf\x7fB\xbbx!<"
        dict_0 = {bytes_0: bytes_0}
        file_downloader_0 = module_0.FileDownloader(dict_0, bytes_0)
        file_downloader_1 = module_0.FileDownloader(bytes_0, file_downloader_0)
        str_0 = 'VLP\r0v'
        float_0 = 1516.1
        list_0 = [float_0, float_0, float_0]
        file_downloader_2 = module_0.FileDownloader(float_0, list_0)
        var_0 = file_downloader_2.best_block_size(file_downloader_1, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'c^z|(7>>Py)'
        set_0 = set()
        file_downloader_0 = module_0.FileDownloader(str_0, set_0)
        var_0 = file_downloader_0.report_file_already_downloaded(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Hockey: Davos décroche son 31e titre de champion de Suisse'
        str_1 = '`=bz2zk]mYg\r/-\\u'
        str_2 = 'http://abcnews.go.com/2020/video/2020-husband-stands-teacher-jail-student-affairs-26119478'
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_0, str_1: str_1}
        str_3 = '56&/F)l6IwD'
        str_4 = 'WOF%P^Wk_i'
        str_5 = '<span[^>]+\\bclass=["\\\']episode_title["\\\'][^>]*>(?P<title>[^<]+)'
        dict_1 = {str_3: str_3, str_4: str_4, str_3: str_3, str_5: str_5}
        file_downloader_0 = module_0.FileDownloader(str_3, dict_1)
        list_0 = [file_downloader_0, file_downloader_0, dict_1, str_4]
        file_downloader_1 = module_0.FileDownloader(file_downloader_0, list_0)
        var_0 = file_downloader_1.to_stderr(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Retrieving config URL'
        bytes_0 = b'\xd1\xc4\xafw\xa7\xbfT'
        float_0 = -891.0
        list_0 = [str_0]
        file_downloader_0 = module_0.FileDownloader(float_0, list_0)
        var_0 = file_downloader_0.to_console_title(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "kRN']26h9E"
        list_0 = [str_0, str_0, str_0]
        str_1 = " mE>4>'Xnari^"
        int_0 = -3987
        file_downloader_0 = module_0.FileDownloader(str_1, int_0)
        var_0 = file_downloader_0.report_error(*list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '>'
        file_downloader_0 = module_0.FileDownloader(str_0, str_0)
        str_1 = '#B3\nr4 enN\r'
        var_0 = file_downloader_0.try_utime(str_1, str_1)
        var_1 = file_downloader_0.ytdl_filename(file_downloader_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
        set_0 = set()
        var_0 = file_downloader_0.try_rename(dict_0, set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = None
        float_0 = 5024.566
        dict_0 = {}
        list_0 = [dict_0, dict_0, float_0]
        tuple_0 = (float_0, dict_0, list_0)
        list_1 = [tuple_0, list_0, float_0]
        str_0 = '%>y~XV.'
        dict_1 = {str_0: dict_0, float_0: dict_0, float_0: list_1, str_0: list_1}
        file_downloader_0 = module_0.FileDownloader(list_0, dict_1)
        tuple_1 = (str_0, tuple_0, file_downloader_0)
        file_downloader_1 = module_0.FileDownloader(list_1, tuple_1)
        var_0 = file_downloader_1.report_destination(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = None
        tuple_0 = (dict_0,)
        bytes_0 = b'\xf8\x0e\xf7\x809\xf2\xfa\x9c\x88H'
        int_0 = None
        list_0 = [bytes_0, int_0, bytes_0, bytes_0]
        tuple_1 = (list_0,)
        file_downloader_0 = module_0.FileDownloader(bytes_0, tuple_1)
        var_0 = file_downloader_0.report_progress(tuple_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bool_0 = False
        bytes_0 = b'Y\x07\xc12U\xeb\xc7\xfd!\xf6w\xd3'
        set_0 = {bool_0, bytes_0, bytes_0}
        file_downloader_0 = module_0.FileDownloader(bytes_0, set_0)
        file_downloader_1 = module_0.FileDownloader(bool_0, file_downloader_0)
        var_0 = file_downloader_0.report_resuming_byte(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '73.0.3643.0'
        set_0 = {str_0, str_0, str_0, str_0}
        bool_0 = False
        list_0 = [bool_0, str_0, str_0, str_0]
        file_downloader_0 = module_0.FileDownloader(bool_0, list_0)
        var_0 = file_downloader_0.report_retry(set_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_16():
    try:
        dict_0 = None
        tuple_0 = (dict_0,)
        set_0 = set()
        file_downloader_0 = module_0.FileDownloader(tuple_0, set_0)
        var_0 = file_downloader_0.report_unable_to_resume()
    except BaseException:
        pass

def test_case_17():
    try:
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
        var_0 = file_downloader_0.download(dict_0, dict_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = -488
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
        str_0 = ' '
        var_0 = file_downloader_0.download(str_0, int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = -486
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
        str_0 = '5a>\tm[z'
        var_0 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'NWu'
        dict_1 = {str_1: str_1}
        int_1 = -458
        var_1 = file_downloader_0.slow_down(str_1, dict_1, int_1)
        float_0 = 3868.517967
        var_2 = file_downloader_0.format_retries(float_0)
        var_3 = file_downloader_0.format_eta(float_0)
        var_4 = file_downloader_0.report_warning(**dict_1)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = -1943
        int_1 = 1613
        list_0 = [int_0, int_0, int_0]
        bytes_0 = b'1\xa56RC\x85\xe4\xd4D\xc5?l\xddh\xa5\xc9H\xd0|\x81'
        int_2 = 737
        tuple_0 = (list_0, bytes_0, int_2, list_0)
        str_0 = '\re+e1^8KD?u6+*4kEi6m'
        file_downloader_0 = module_0.FileDownloader(tuple_0, str_0)
        var_0 = file_downloader_0.format_eta(int_1)
        bool_0 = True
        bool_1 = False
        list_1 = [int_0, bool_0, int_0, bool_1]
        str_1 = '7unZT>#'
        list_2 = []
        file_downloader_1 = module_0.FileDownloader(str_1, list_2)
        var_1 = file_downloader_1.trouble(*list_1)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = -488
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
        str_0 = 'm'
        dict_1 = {str_0: str_0}
        var_0 = file_downloader_0.slow_down(str_0, dict_1, int_0)
        list_0 = None
        float_0 = -1.0
        var_1 = file_downloader_0.calc_eta(float_0, list_0, dict_1, int_0)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = -488
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
        float_0 = None
        bytes_0 = b'\xe2\xbb\xdf\x97b\xe7-\x80\xa8\x1e\xd0\xd8v\xad\xe5\x96\xbc'
        list_0 = [int_0, bytes_0, dict_0, int_0]
        str_0 = 'g_\x0cLwrc"d\t.()^C'
        file_downloader_1 = module_0.FileDownloader(list_0, str_0)
        var_0 = file_downloader_1.format_eta(float_0)
        float_1 = 1655219255.8840501
        str_1 = 'z1nZ&qj/'
        var_1 = file_downloader_0.try_utime(float_1, str_1)
    except BaseException:
        pass

def test_case_23():
    try:
        bool_0 = False
        int_0 = -438
        dict_0 = {bool_0: int_0}
        file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
        float_0 = 824.0
        var_0 = file_downloader_0.try_rename(float_0, float_0)
    except BaseException:
        pass

def test_case_24():
    try:
        int_0 = -488
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(int_0, dict_0)
        str_0 = 'm'
        dict_1 = {str_0: str_0}
        int_1 = -440
        var_0 = file_downloader_0.slow_down(str_0, dict_1, int_1)
        list_0 = None
        float_0 = -1.0
        str_1 = None
        var_1 = file_downloader_0.format_percent(str_1)
        var_2 = file_downloader_0.calc_eta(float_0, list_0, dict_1, int_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '@.K4!-[(u.'
        bool_0 = False
        int_0 = 2147483648
        int_1 = -1339
        bool_1 = False
        file_downloader_0 = module_0.FileDownloader(int_1, bool_1)
        var_0 = file_downloader_0.best_block_size(bool_0, int_0)
        bytes_0 = b'\xd1\xc4\xafw\xa7\xbfT'
        float_0 = -891.0
        list_0 = [str_0]
        file_downloader_1 = module_0.FileDownloader(float_0, list_0)
        var_1 = file_downloader_1.to_console_title(bytes_0)
    except BaseException:
        pass

def test_case_26():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'status'
        str_1 = 'finished'
        str_2 = 'downloaded_bytes'
        int_0 = 1
        var_1 = {str_0: str_1, str_2: int_0, str_2: int_0}
        var_2 = file_downloader_0.report_progress(var_1)
    except BaseException:
        pass

def test_case_27():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = '%.2f'
        var_1 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'status'
        str_2 = 'total_bytes'
        str_3 = 'finished'
        str_4 = 'downloaded_bytes'
        int_0 = 1234
        int_1 = 1
        var_2 = {str_1: str_3, str_4: int_0, str_2: int_1}
        var_3 = file_downloader_0.report_progress(var_2)
    except BaseException:
        pass

def test_case_28():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'status'
        str_1 = ' m%lot8\\5Zw1 v2\r_7'
        str_2 = 'downloading'
        str_3 = 'elapsed'
        int_0 = 1
        var_1 = {str_0: str_2, str_1: int_0, str_3: int_0}
        var_2 = file_downloader_0.report_progress(var_1)
    except BaseException:
        pass

def test_case_29():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'status'
        str_1 = 'downloaded_bytes'
        str_2 = 'downloading'
        str_3 = 'elapsed'
        int_0 = 1
        var_1 = {str_3: str_3, str_0: str_3, str_0: str_2, str_1: int_0, str_3: int_0, str_2: str_3}
        var_2 = file_downloader_0.report_progress(var_1)
    except BaseException:
        pass

def test_case_30():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'd\x0bu<)#WS^(,a=TR7V=F}'
        var_1 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'status'
        str_2 = 'downloaded_bytes'
        str_3 = 'downloading'
        int_0 = 1234
        int_1 = 1
        var_2 = {str_1: str_3, str_2: int_0, str_0: int_1}
        var_3 = file_downloader_0.report_progress(var_2)
    except BaseException:
        pass

def test_case_31():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'd_u<)#WS^U,a=TR7V=F}'
        str_1 = 'status'
        str_2 = 'total_bytes'
        str_3 = 'fHinithed'
        int_0 = 5208
        var_1 = {str_1: str_0, str_2: int_0}
        var_2 = file_downloader_0.report_progress(var_1)
        str_4 = 'total_bytes_estimate'
        var_3 = int_0 * int_0
        var_4 = {str_1: str_3, str_2: int_0, str_4: var_3}
        var_5 = file_downloader_0.report_progress(var_4)
        str_5 = 'downloaded_bytes'
        str_6 = 'downloading'
        var_6 = {str_1: str_6, str_5: int_0, str_2: int_0}
        var_7 = file_downloader_0.report_progress(var_6)
    except BaseException:
        pass

def test_case_32():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'd\x0bu<)#WS^(,a=TR7V=F}'
        var_1 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'status'
        str_2 = 'total_bytes_estimate'
        str_3 = 'downloading'
        int_0 = 1
        var_2 = {str_1: str_3, str_2: int_0, str_3: int_0}
        var_3 = file_downloader_0.report_progress(var_2)
    except BaseException:
        pass

def test_case_33():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = 'd_u)#hS^U,a=TR7V=F}'
        var_1 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'status'
        int_0 = 5208
        var_2 = {str_1: str_0, str_0: int_0}
        var_3 = file_downloader_0.report_progress(var_2)
        str_2 = 'total_bytes_estimate'
        var_4 = int_0 * int_0
        str_3 = 'downloaded_bytes'
        str_4 = 'downloading'
        int_1 = 987654321
        var_5 = {str_1: str_4, str_3: int_1, str_2: int_0}
        var_6 = file_downloader_0.report_progress(var_5)
    except BaseException:
        pass

def test_case_34():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = '%.2f'
        var_1 = file_downloader_0.parse_bytes(str_0)
        str_1 = 'status'
        str_2 = 'finished'
        str_3 = 'downloaded_bytes'
        str_4 = 'elapsed'
        int_0 = 1234
        int_1 = 1
        var_2 = {str_1: str_2, str_3: int_0, str_4: int_1}
        var_3 = file_downloader_0.report_progress(var_2)
    except BaseException:
        pass

def test_case_35():
    try:
        float_0 = 1655219365.5153418
        float_1 = 3999.11
        str_0 = '1%<QyV'
        file_downloader_0 = module_0.FileDownloader(float_1, str_0)
        var_0 = file_downloader_0.format_eta(float_0)
    except BaseException:
        pass

def test_case_36():
    try:
        int_0 = -467
        dict_0 = {int_0: int_0}
        bool_0 = True
        str_0 = ''
        file_downloader_0 = module_0.FileDownloader(str_0, dict_0)
        var_0 = file_downloader_0.parse_bytes(str_0)
        tuple_0 = ()
        list_0 = [tuple_0, dict_0, bool_0, dict_0]
        file_downloader_1 = module_0.FileDownloader(tuple_0, list_0)
        str_1 = 'r/'
        str_2 = 'bg/=\x0bf'
        int_1 = -3805
        bytes_0 = b''
        file_downloader_2 = module_0.FileDownloader(int_1, bytes_0)
        var_1 = file_downloader_2.try_rename(str_1, str_2)
    except BaseException:
        pass

def test_case_37():
    try:
        var_0 = {}
        file_downloader_0 = module_0.FileDownloader(var_0, var_0)
        str_0 = '%.2f'
        str_1 = 'd_u<)#WS^U,a=TR7V=F}'
        var_1 = file_downloader_0.parse_bytes(str_1)
        str_2 = 'status'
        str_3 = 'total_bytes'
        str_4 = 'fHinithed'
        int_0 = 5208
        var_2 = {str_2: str_1, str_3: int_0}
        var_3 = file_downloader_0.report_progress(var_2)
        str_5 = 'total_bytes_estimate'
        var_4 = int_0 * int_0
        var_5 = {str_2: str_4, str_3: int_0, str_5: var_4}
        var_6 = file_downloader_0.report_progress(var_5)
        float_0 = 248.0
        var_7 = file_downloader_0.format_seconds(float_0)
        str_6 = 'downloading'
        int_1 = 987654321
        var_8 = {str_2: str_6, str_0: int_1, str_3: int_0}
        var_9 = file_downloader_0.report_progress(var_8)
    except BaseException:
        pass