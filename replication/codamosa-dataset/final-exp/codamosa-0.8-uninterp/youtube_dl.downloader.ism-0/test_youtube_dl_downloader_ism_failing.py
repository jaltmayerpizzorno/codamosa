# Automatically generated by Pynguin.
import youtube_dl.downloader.ism as module_0

def test_case_0():
    try:
        str_0 = ''
        list_0 = []
        var_0 = module_0.box(str_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "W' \t,\x0c'\n YD/%t!p6"
        set_0 = {str_0, str_0}
        float_0 = None
        bytes_0 = b'\xf4+\xd8\x08\xee(\x15q\x97\xc0g\x99\x9d\x99c\xeb'
        var_0 = module_0.full_box(set_0, float_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "* ?'f9/r"
        tuple_0 = ()
        var_0 = module_0.write_piff_header(str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'R\x89\xfb\xa5\xa7\xd7\xa5i\xa6 \x1dq\xd2= \xd9@\xa3\x0e'
        list_0 = [bytes_0]
        bool_0 = False
        ism_f_d_0 = module_0.IsmFD(list_0, bool_0)
        var_0 = module_0.extract_box_data(bytes_0, ism_f_d_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        str_0 = 'j2\rT6()l9F[s'
        var_0 = module_0.extract_box_data(tuple_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '^QNidgje7ulEMqg'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        ism_f_d_0 = module_0.IsmFD(str_0, dict_0)
        var_0 = ism_f_d_0.real_download(str_0, ism_f_d_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\x00\x00\x00,'
        bytes_1 = b'moov'
        bytes_2 = b'\x00\x00\x00('
        bytes_3 = b'mvhd'
        var_0 = bytes_2 + bytes_3
        var_1 = var_0 + bytes_0
        var_2 = var_1 + bytes_1
        var_3 = var_2 + bytes_0
        var_4 = var_3 + bytes_3
        bytes_4 = (bytes_3,)
        var_5 = module_0.extract_box_data(var_4, bytes_4)
        bytes_5 = (bytes_1, bytes_3)
        var_6 = module_0.extract_box_data(var_4, bytes_5)
    except BaseException:
        pass