# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    internet_0 = module_0.Internet()

def test_case_1():
    list_0 = []
    internet_0 = module_0.Internet()
    str_0 = internet_0.network_protocol()
    str_1 = internet_0.top_level_domain()
    internet_1 = module_0.Internet(*list_0)
    var_0 = internet_0.hashtags()
    mime_type_0 = module_1.MimeType.AUDIO
    str_2 = internet_0.content_type(mime_type_0)
    i_pv6_address_0 = internet_0.ip_v6_object()
    str_3 = internet_1.http_status_message()

def test_case_2():
    dict_0 = {}
    internet_0 = module_0.Internet(**dict_0)
    str_0 = internet_0.http_method()

def test_case_3():
    layer_0 = None
    list_0 = [layer_0]
    internet_0 = module_0.Internet(*list_0)
    str_0 = internet_0.home_page()
    port_range_0 = module_1.PortRange.REGISTERED
    internet_1 = module_0.Internet()
    str_1 = internet_1.http_method()
    str_2 = internet_1.ip_v4(port_range_0)

def test_case_4():
    internet_0 = module_0.Internet()
    int_0 = 800
    list_0 = []
    var_0 = internet_0.stock_image(list_0)
    int_1 = 600
    str_0 = internet_0.ip_v4()
    str_1 = 'nature'
    str_2 = 'water'
    str_3 = [str_1, str_2]
    bool_0 = True
    var_1 = internet_0.stock_image(int_0, int_1, str_3, bool_0)
    var_2 = len(var_1)

def test_case_5():
    dict_0 = {}
    internet_0 = module_0.Internet(**dict_0)
    str_0 = internet_0.mac_address()
    str_1 = internet_0.network_protocol()

def test_case_6():
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image()

def test_case_7():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    i_pv4_address_0 = internet_0.ip_v4_object()
    internet_1 = module_0.Internet()
    port_range_0 = module_1.PortRange.EPHEMERAL
    bool_0 = False
    var_1 = internet_0.stock_image(port_range_0, bool_0)
    var_2 = internet_1.hashtags()

def test_case_8():
    list_0 = None
    list_1 = [list_0]
    internet_0 = module_0.Internet(*list_1)
    str_0 = internet_0.home_page()

def test_case_9():
    internet_0 = module_0.Internet()
    str_0 = internet_0.network_protocol()

def test_case_10():
    str_0 = 'love'
    str_1 = 'sky'
    str_2 = 'nice'
    str_3 = 'beautiful'
    str_4 = 'amazing'
    str_5 = 'fantastic'
    str_6 = [str_0, str_1, str_2, str_3, str_4, str_5]
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    int_0 = 1
    var_1 = internet_0.hashtags(int_0)
    int_1 = 4
    var_2 = internet_0.hashtags(int_1)
    int_2 = 0
    var_3 = internet_0.hashtags(int_2)
    var_4 = len(var_3)
    var_5 = len(str_6)
    var_6 = internet_0.hashtags(var_5)

def test_case_11():
    internet_0 = module_0.Internet()
    int_0 = 772
    int_1 = 1609
    str_0 = 'nature'
    str_1 = 'jungles'
    str_2 = [str_0, str_1]
    bool_0 = True
    var_0 = internet_0.stock_image(int_0, int_1, str_2, bool_0)
    var_1 = len(var_0)