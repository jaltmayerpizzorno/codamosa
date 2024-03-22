# Automatically generated by Pynguin.
import youtube_dl.downloader.f4m as module_0
import youtube_dl.compat as module_1

def test_case_0():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_box_info()
    except BaseException:
        pass

def test_case_1():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_abst()
    except BaseException:
        pass

def test_case_2():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_string()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        var_0 = module_1.compat_etree_fromstring(bytes_0)
        var_1 = module_0.get_base_url(var_0)
        flv_reader_0 = module_0.FlvReader()
        var_2 = flv_reader_0.read_asrt()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_5():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = flv_reader_0.read_bootstrap_info()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'?\\\xe2\xdb\xca\xd7\xae\xf2K\x9c\x0f\x06ZT#'
        var_0 = module_0.read_bootstrap_info(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        var_0 = module_1.compat_etree_fromstring(bytes_0)
        list_0 = [var_0, var_0]
        var_1 = module_0.remove_encrypted_media(list_0)
        var_2 = module_0.build_fragments_list(bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = None
        str_0 = 'h{o(95l$g'
        list_1 = [str_0, list_0]
        var_0 = module_0.write_flv_header(list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '2&&}y]C4'
        str_1 = 'orf:fm4'
        dict_0 = {str_0: str_0, str_1: str_0, str_0: str_1}
        f4m_f_d_0 = module_0.F4mFD(str_0, dict_0)
        str_2 = '<5m3gQV5E'
        var_0 = module_0.remove_encrypted_media(str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'http://live-1-1.rutube.ru/stream/1024/HDS/SD/C2NKsS85HQNckgn5HdEmOQ/1454167650/S-s604419906/move/four/dirs/upper/1024-576p.f4m'
        str_1 = 'format'
        str_2 = 'f4m_test'
        str_3 = {str_1: str_2}
        int_0 = 1
        f4m_f_d_0 = module_0.F4mFD(int_0, str_3)
        var_0 = None
        str_4 = 'url'
        str_5 = {str_4: str_0}
        var_1 = f4m_f_d_0.real_download(var_0, str_5)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = False
        bytes_0 = b'r\x82\x89\xb3\n\x17^\x87\x83\xa5\xcd\x1eR\\\x1e\x80a'
        var_0 = module_0.write_unsigned_int_24(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'JP\xee\x95\x81\xcf\xb9\\9\x82\xe4\xba/\x12 \xeb\x16\xb0{\x8b'
        list_0 = []
        var_0 = module_0.write_metadata_tag(bytes_0, list_0)
        data_truncated_error_0 = module_0.DataTruncatedError()
        flv_reader_0 = module_0.FlvReader()
        var_1 = flv_reader_0.read_box_info()
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        var_0 = module_1.compat_etree_fromstring(bytes_0)
        var_1 = module_0.get_base_url(var_0)
        flv_reader_0 = module_0.FlvReader()
        var_2 = flv_reader_0.read_unsigned_long_long()
    except BaseException:
        pass

def test_case_14():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = module_0.write_metadata_tag(flv_reader_0, flv_reader_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        var_0 = module_1.compat_etree_fromstring(bytes_0)
        var_1 = module_0.get_base_url(var_0)
        list_0 = [var_1, var_1, var_1]
        var_2 = module_0.write_unsigned_int(list_0, bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        flv_reader_0 = module_0.FlvReader()
        var_0 = module_0.write_flv_header(flv_reader_0)
        var_1 = flv_reader_0.read_asrt()
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b'<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_abst()
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'?\\\xe2\xdb\xca\xd7\xae\xf2K\x9c\x0f\x06ZT#'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b'<manifest xmlns="http://n.adobe.com/f4m/1.0"><baseURL>/base/path</baseURL><media url="/foo.mp4"><bootstrapInfo><bootstrapVersion>0</bootstrapVersion><state>0</state></bootstrapInfo></media></manifest>'
        var_0 = module_1.compat_etree_fromstring(bytes_0)
        var_1 = module_0.get_base_url(var_0)
        flv_reader_0 = module_0.FlvReader()
        var_2 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = b'?\\\xe2\xdb\xca\xd7\xae\xf2\x9c\x0f\x06ZT#'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_asrt()
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'?\\\xe2\xdb\xca\xd7G\xf2\x9c\x00\x06ZT#'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_22():
    try:
        flv_reader_0 = module_0.FlvReader()
        dict_0 = {flv_reader_0: flv_reader_0}
        var_0 = module_0.write_metadata_tag(flv_reader_0, dict_0)
    except BaseException:
        pass

def test_case_23():
    try:
        bytes_0 = b'?\xe2\xdb\xca\xd7G\xf2\x9c\x00\x06ZT1'
        list_0 = [bytes_0]
        flv_reader_0 = module_0.FlvReader(*list_0)
        var_0 = flv_reader_0.read_afrt()
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'segments'
        str_1 = 'fragments'
        str_2 = 'segment_run'
        int_0 = 4971
        int_1 = (int_0, int_0)
        int_2 = [int_1, int_0]
        int_3 = {str_1: str_0, str_2: int_2}
        int_4 = [int_3]
        str_3 = 'first'
        str_4 = 'duration'
        int_5 = {str_4: int_0, str_1: int_0, str_3: int_0, str_4: int_1, str_4: str_4}
        int_6 = [int_5]
        int_7 = {str_1: int_6}
        int_8 = [int_7]
        bool_0 = False
        var_0 = {str_0: int_4, str_1: int_8, str_3: bool_0}
        var_1 = module_0.build_fragments_list(var_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'segments'
        str_1 = 'fragments'
        str_2 = 'segment_run'
        int_0 = 0
        int_1 = (int_0, int_0)
        int_2 = [int_1]
        int_3 = {str_2: int_2}
        int_4 = [int_3]
        str_3 = 'discontinuity_indicator'
        str_4 = 'first'
        int_5 = 4
        int_6 = {str_1: int_0, str_3: int_0, str_4: int_0, str_0: int_5}
        int_7 = [int_6]
        int_8 = {str_1: int_7}
        int_9 = [int_8]
        bool_0 = False
        var_0 = {str_0: int_4, str_1: int_9, str_4: bool_0}
        var_1 = module_0.build_fragments_list(var_0)
    except BaseException:
        pass