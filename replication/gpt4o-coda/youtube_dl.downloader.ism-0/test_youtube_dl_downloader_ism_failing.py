# Automatically generated by Pynguin.
import youtube_dl.downloader.ism as module_0

def test_case_0():
    try:
        bytes_0 = b'M\xc1\x7f\x13OS\x92\xb8tlHU\x97\x12\xad\x8c\xb0\xdc\x9c\xe6'
        float_0 = -1051.519694
        var_0 = module_0.box(bytes_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = [bool_0]
        int_0 = -3586
        dict_0 = {int_0: bool_0, int_0: list_0, int_0: list_0}
        str_0 = '"kG{FuGM'
        var_0 = module_0.full_box(list_0, int_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        var_0 = module_0.write_piff_header(set_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '~T<tnvBB,\rn!nIt3|6'
        bytes_0 = b'\x94\x00K\xd4\xf2\xc1\xad\xd7\xfe'
        var_0 = module_0.extract_box_data(bytes_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = set()
        dict_0 = {}
        ism_f_d_0 = module_0.IsmFD(set_0, dict_0)
        var_0 = ism_f_d_0.real_download(ism_f_d_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'test'
        var_0 = module_0.box(bytes_0, bytes_0)
        bytes_1 = [bytes_0]
        var_1 = module_0.extract_box_data(var_0, bytes_1)
        bytes_2 = b'inner'
        bytes_3 = b'567\xd5\xd68'
        var_2 = module_0.box(bytes_2, bytes_3)
        bytes_4 = b'level1'
        bytes_5 = b'level2'
        bytes_6 = b'level3'
        bytes_7 = b'91011'
        var_3 = module_0.box(bytes_6, bytes_7)
        var_4 = module_0.box(bytes_5, var_3)
        var_5 = module_0.box(bytes_4, var_4)
        bytes_8 = [bytes_4, bytes_5, bytes_6]
        var_6 = module_0.extract_box_data(var_5, bytes_8)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'test'
        bytes_1 = b'123&4'
        var_0 = module_0.box(bytes_0, bytes_1)
        bytes_2 = [bytes_0, var_0]
        var_1 = module_0.extract_box_data(var_0, bytes_2)
    except BaseException:
        pass