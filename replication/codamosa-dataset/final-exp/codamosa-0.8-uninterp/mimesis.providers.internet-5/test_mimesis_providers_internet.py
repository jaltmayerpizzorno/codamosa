# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    pass

def test_case_1():
    internet_0 = module_0.Internet()
    str_0 = internet_0.top_level_domain()

def test_case_2():
    internet_0 = module_0.Internet()
    str_0 = internet_0.network_protocol()
    internet_1 = module_0.Internet()
    bool_0 = False
    str_1 = internet_0.ip_v4(bool_0)
    str_2 = internet_1.http_status_message()

def test_case_3():
    internet_0 = module_0.Internet()
    int_0 = internet_0.http_status_code()

def test_case_4():
    str_0 = None
    str_1 = 'CeVz_;q'
    internet_0 = module_0.Internet()
    str_2 = internet_0.image_placeholder(str_1)
    list_0 = [str_0, str_0]
    internet_1 = module_0.Internet()
    var_0 = internet_1.stock_image(list_0)
    str_3 = internet_0.user_agent()
    str_4 = internet_1.http_method()

def test_case_5():
    internet_0 = module_0.Internet()
    str_0 = internet_0.mac_address()
    str_1 = internet_0.ip_v4()
    int_0 = internet_0.port()
    var_0 = internet_0.hashtags()

def test_case_6():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    var_1 = internet_0.hashtags()
    var_2 = internet_0.hashtags()
    int_0 = 1
    var_3 = internet_0.hashtags(int_0)
    var_4 = internet_0.hashtags(int_0)
    int_1 = 0
    bool_0 = True
    str_0 = internet_0.ip_v4(bool_0)
    var_5 = internet_0.hashtags(int_1)

def test_case_7():
    internet_0 = module_0.Internet()
    str_0 = internet_0.home_page()
    str_1 = internet_0.mac_address()
    str_2 = internet_0.network_protocol()
    i_pv6_address_0 = internet_0.ip_v6_object()
    str_3 = internet_0.ip_v4()
    int_0 = internet_0.port()

def test_case_8():
    str_0 = 'Check if function ueturns a list of strings.'
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    str_1 = internet_0.mac_address()
    bool_0 = True
    var_1 = internet_0.stock_image(str_1, bool_0)
    int_0 = internet_0.port()
    str_2 = internet_0.image_placeholder(str_0)
    str_3 = internet_0.ip_v6()
    str_4 = internet_0.http_status_message()

def test_case_9():
    internet_0 = module_0.Internet()
    str_0 = internet_0.mac_address()

def test_case_10():
    internet_0 = module_0.Internet()
    i_pv6_address_0 = internet_0.ip_v6_object()
    t_l_d_type_0 = module_1.TLDType.STLD
    str_0 = internet_0.home_page(t_l_d_type_0)
    str_1 = internet_0.emoji()
    layer_0 = module_1.Layer.TRANSPORT
    str_2 = internet_0.network_protocol(layer_0)
    bool_0 = False
    str_3 = internet_0.ip_v4(bool_0)
    var_0 = internet_0.hashtags()

def test_case_11():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    int_0 = 1
    var_1 = internet_0.hashtags(int_0)

def test_case_12():
    str_0 = 'QNALckDOR'
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    str_1 = 'Not a list'
    list_0 = [str_1]
    internet_1 = module_0.Internet(*list_0)
    str_2 = internet_0.http_method()
    str_3 = internet_1.image_placeholder(str_2)
    str_4 = internet_1.mac_address()
    bool_0 = True
    list_1 = [str_3, str_0]
    var_1 = internet_0.stock_image(str_0, str_2, list_1, bool_0)
    int_0 = internet_0.port()
    str_5 = internet_0.image_placeholder(str_2)
    t_l_d_type_0 = module_1.TLDType.STLD
    str_6 = internet_0.top_level_domain(t_l_d_type_0)
    str_7 = internet_0.ip_v6()
    str_8 = internet_1.http_status_message()