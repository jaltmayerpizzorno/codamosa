# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    pass

def test_case_1():
    internet_0 = module_0.Internet()

def test_case_2():
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image()
    internet_1 = module_0.Internet()
    str_0 = internet_1.home_page()
    str_1 = internet_1.content_type()
    internet_2 = module_0.Internet()
    str_2 = internet_2.user_agent()
    str_3 = internet_1.home_page()
    str_4 = internet_1.emoji()

def test_case_3():
    internet_0 = module_0.Internet()
    str_0 = internet_0.ip_v6()
    str_1 = internet_0.http_method()
    str_2 = internet_0.http_status_message()
    bool_0 = True
    str_3 = internet_0.mac_address()
    port_range_0 = module_1.PortRange.REGISTERED
    int_0 = internet_0.port()
    internet_1 = module_0.Internet()
    optional_0 = None
    str_4 = internet_1.content_type(optional_0)
    str_5 = internet_1.ip_v4(bool_0, port_range_0)
    str_6 = internet_1.emoji()

def test_case_4():
    internet_0 = module_0.Internet()
    int_0 = internet_0.port()
    i_pv4_address_0 = internet_0.ip_v4_object()

def test_case_5():
    str_0 = 'e;:pl'
    list_0 = [str_0, str_0, str_0, str_0]
    internet_0 = module_0.Internet()
    str_1 = internet_0.emoji()
    bool_0 = True
    i_pv4_address_0 = internet_0.ip_v4_object()
    var_0 = internet_0.stock_image(str_1, str_1, list_0, bool_0)
    internet_1 = module_0.Internet()
    str_2 = internet_1.http_status_message()
    str_3 = internet_1.ip_v4(bool_0)
    str_4 = internet_1.image_placeholder(str_1)
    str_5 = internet_1.ip_v4()
    str_6 = internet_0.top_level_domain()
    str_7 = internet_1.image_placeholder(str_5)
    str_8 = internet_0.top_level_domain()

def test_case_6():
    port_range_0 = module_1.PortRange.ALL
    internet_0 = module_0.Internet()
    str_0 = '$r5-tn]pw<'
    str_1 = internet_0.image_placeholder(str_0, str_0)
    str_2 = internet_0.ip_v4(port_range_0)

def test_case_7():
    internet_0 = module_0.Internet()
    i_pv6_address_0 = internet_0.ip_v6_object()

def test_case_8():
    internet_0 = module_0.Internet()
    internet_1 = module_0.Internet()
    str_0 = internet_0.ip_v6()

def test_case_9():
    str_0 = '4"i%VT @ &ZZ._mr&as'
    str_1 = "-e860'/@]!vU"
    list_0 = [str_0, str_1]
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image(list_0)
    internet_1 = module_0.Internet()
    str_2 = internet_1.mac_address()

def test_case_10():
    str_0 = '4"i%VT @ &ZZ._mr&as'
    list_0 = [str_0, str_0, str_0]
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image(list_0)
    internet_1 = module_0.Internet()

def test_case_11():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()

def test_case_12():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    str_0 = internet_0.home_page()

def test_case_13():
    str_0 = '4"i%VT @ &ZZ._mr&as'
    str_1 = "-e860'/@]!vU"
    list_0 = [str_0, str_1]
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image(list_0)
    internet_1 = module_0.Internet()
    str_2 = internet_1.user_agent()

def test_case_14():
    internet_0 = module_0.Internet()
    int_0 = internet_0.port()

def test_case_15():
    list_0 = []
    internet_0 = module_0.Internet()
    str_0 = internet_0.mac_address()
    internet_1 = module_0.Internet(*list_0)
    i_pv6_address_0 = internet_1.ip_v6_object()
    str_1 = internet_1.home_page()
    str_2 = internet_1.ip_v6()
    int_0 = 1
    t_l_d_type_0 = module_1.TLDType.STLD
    str_3 = internet_1.home_page()
    internet_2 = module_0.Internet(*list_0)
    var_0 = internet_2.hashtags()
    str_4 = internet_1.emoji()
    internet_3 = module_0.Internet()
    str_5 = internet_3.top_level_domain(t_l_d_type_0)
    internet_4 = module_0.Internet()
    i_pv6_address_1 = internet_4.ip_v6_object()
    bool_0 = True
    str_6 = internet_4.mac_address()
    var_1 = internet_1.stock_image(bool_0)
    dict_0 = {}
    internet_5 = module_0.Internet(**dict_0)
    i_pv6_address_2 = internet_3.ip_v6_object()
    internet_6 = module_0.Internet()
    var_2 = internet_6.hashtags(int_0)
    str_7 = internet_6.home_page()
    internet_7 = module_0.Internet()
    var_3 = internet_1.hashtags()
    bool_1 = False
    str_8 = internet_7.ip_v4(bool_1)
    int_1 = internet_7.port()