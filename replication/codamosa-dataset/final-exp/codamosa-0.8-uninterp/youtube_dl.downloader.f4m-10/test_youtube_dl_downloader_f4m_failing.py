# Automatically generated by Pynguin.
import youtube_dl.downloader.f4m as module_0

def test_case_0():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_bootstrap_info()
    except BaseException:
        pass

def test_case_1():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_unsigned_long_long()
    except BaseException:
        pass

def test_case_2():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_unsigned_char()
    except BaseException:
        pass

def test_case_3():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_string()
    except BaseException:
        pass

def test_case_4():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_5():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_abst()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        var_0 = module_0.read_bootstrap_info(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = None
        var_0 = module_0.build_fragments_list(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        data_truncated_error_0 = module_0.DataTruncatedError()
        str_0 = ',s3&M:$1[~H>NK/P'
        bool_0 = False
        var_0 = module_0.write_unsigned_int(str_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        flv_reader_0 = module_0.FlvReader()
        list_0 = []
        float_0 = -1219.8211
        var_0 = module_0.write_unsigned_int_24(list_0, float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        data_truncated_error_0 = module_0.DataTruncatedError(*list_0)
        var_0 = module_0.remove_encrypted_media(data_truncated_error_0)
    except BaseException:
        pass

def test_case_11():
    try:
        flv_reader_0 = None
        list_0 = [flv_reader_0, flv_reader_0]
        bool_0 = True
        set_0 = set()
        f4m_f_d_0 = module_0.F4mFD(set_0, set_0)
        var_0 = f4m_f_d_0.real_download(list_0, bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_asrt()
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'jA'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0]
        var_0 = module_0.write_metadata_tag(dict_0, list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = None
        set_0 = {int_0, int_0}
        var_0 = module_0.get_base_url(set_0)
    except BaseException:
        pass

def test_case_15():
    try:
        data_truncated_error_0 = module_0.DataTruncatedError()
        list_0 = []
        var_0 = module_0.write_metadata_tag(data_truncated_error_0, list_0)
        flv_reader_0 = module_0.FlvReader()
        var_1 = flv_reader_0.read_abst()
    except BaseException:
        pass

def test_case_16():
    try:
        flv_reader_0 = module_0.FlvReader()
        list_0 = [flv_reader_0, flv_reader_0, flv_reader_0, flv_reader_0]
        var_0 = module_0.write_metadata_tag(flv_reader_0, list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b'&\x07\xce>Q\xb9\xeb\r\xc3\x07B\xfd\x84\xc8'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'&\x07\xce>Q\xb9\xeb\r\xc3\x07B\xfd\x84\xc8'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_box_info()
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b'&\x07\xce>Q\xb9\xeb\r\xc3\x07B\xfd\x84\xc8'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_abst()
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = b'i\xc39S+\xee\x08\xfa\xf3\x97#'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_asrt()
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'\x89Ns4\xd2\xacy\x98\xf65\xfcO\x00~'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_22():
    try:
        bytes_0 = b'\x89Ns4\xd2\xacy\x98\xf65\xfcO\x00~'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_unsigned_int()
        var_1 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'segments'
        str_1 = 'fragments'
        str_2 = 'segment_run'
        int_0 = 1
        int_1 = (int_0, int_0)
        int_2 = [int_1]
        int_3 = {str_2: int_2}
        int_4 = [int_3]
        str_3 = 'first'
        int_5 = {str_3: int_0}
        int_6 = [int_5]
        int_7 = {str_1: int_6}
        int_8 = [int_7, int_5]
        int_9 = {str_0: int_4, str_1: int_8}
        var_0 = module_0.build_fragments_list(int_9)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'url'
        str_1 = {str_0: str_0}
        str_2 = 'test.flv'
        f4m_f_d_0 = module_0.F4mFD(str_2, str_1)
        str_3 = ''
        var_0 = f4m_f_d_0.real_download(str_3, str_1)
    except BaseException:
        pass