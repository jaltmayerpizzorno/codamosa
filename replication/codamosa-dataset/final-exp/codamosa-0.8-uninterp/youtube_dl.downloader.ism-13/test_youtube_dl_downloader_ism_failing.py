# Automatically generated by Pynguin.
import youtube_dl.downloader.ism as module_0

def test_case_0():
    try:
        bytes_0 = b')\x9e\xf3\x1a'
        bool_0 = True
        var_0 = module_0.box(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -657.8
        bytes_0 = None
        bytes_1 = None
        dict_0 = {float_0: float_0}
        complex_0 = None
        str_0 = 'aX'
        tuple_0 = (complex_0, str_0)
        list_0 = [bytes_0, tuple_0, tuple_0, complex_0]
        tuple_1 = (bytes_1, float_0, dict_0, list_0)
        int_0 = -1464
        ism_f_d_0 = module_0.IsmFD(list_0, int_0)
        var_0 = module_0.full_box(float_0, bytes_0, tuple_1, ism_f_d_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'u4hp|R"Y0+-$_M9i'
        tuple_0 = ()
        var_0 = module_0.write_piff_header(str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x00\x00\x00\x0cftypiso2\x00\x00\x00\x1cmoov\x00\x00\x00\x0ctrak\x00\x00\x00\x08mdia'
        bytes_1 = b'moov'
        bytes_2 = b'mdia'
        bytes_3 = (bytes_1, bytes_2)
        var_0 = module_0.extract_box_data(bytes_0, bytes_3)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'wd>E\x0cKawuev'
        str_1 = '"\tb7y7BunP#b>Z'
        var_0 = module_0.extract_box_data(str_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ohtp://test.bsm'
        var_0 = {}
        ism_f_d_0 = module_0.IsmFD(str_0, var_0)
        var_1 = ism_f_d_0.real_download(str_0, str_0)
    except BaseException:
        pass