# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    try:
        dict_0 = {}
        internet_0 = module_0.Internet(**dict_0)
        i_pv6_address_0 = internet_0.ip_v6_object()
        list_0 = [i_pv6_address_0, dict_0, internet_0]
        int_0 = internet_0.http_status_code()
        internet_1 = module_0.Internet(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        internet_0 = module_0.Internet()
        i_pv4_address_0 = internet_0.ip_v4_object()
        list_0 = [i_pv4_address_0, internet_0, internet_0]
        str_0 = "oR}'\\y|d"
        dict_0 = {str_0: i_pv4_address_0, str_0: str_0, str_0: i_pv4_address_0}
        internet_1 = module_0.Internet(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        internet_0 = module_0.Internet()
        str_0 = internet_0.ip_v4(bool_0)
        internet_1 = module_0.Internet()
        var_0 = internet_1.hashtags()
        i_pv4_address_0 = internet_1.ip_v4_object()
        i_pv6_address_0 = internet_1.ip_v6_object()
        list_0 = [internet_1, var_0, var_0, var_0]
        internet_2 = module_0.Internet(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'zZ\\\x0cv\x0cH\nl\tGr'
        str_1 = 'gb>c;&{O}-r'
        internet_0 = module_0.Internet()
        str_2 = internet_0.mac_address()
        str_3 = internet_0.image_placeholder(str_0)
        internet_1 = module_0.Internet()
        str_4 = internet_1.network_protocol()
        dict_0 = {str_1: str_1}
        internet_2 = module_0.Internet(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        internet_0 = module_0.Internet()
        i_pv6_address_0 = internet_0.ip_v6_object()
        list_0 = [i_pv6_address_0]
        internet_1 = module_0.Internet(*list_0)
        i_pv4_address_0 = internet_1.ip_v4_object()
        str_0 = None
        internet_2 = module_0.Internet()
        str_1 = internet_2.home_page(str_0)
        str_2 = 'slat(7mWU\\e\x0c1Igf\x0bgj;'
        list_1 = [str_2, str_2, str_2]
        internet_3 = module_0.Internet(*list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.emoji()
        str_1 = internet_0.mac_address()
        int_0 = internet_0.http_status_code()
        str_2 = internet_0.content_type()
        str_3 = internet_0.network_protocol()
        str_4 = internet_0.ip_v6()
        var_0 = internet_0.hashtags()
        port_range_0 = None
        int_1 = internet_0.port(port_range_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'G^/z'
        list_0 = [str_0, str_0]
        dict_0 = {}
        internet_0 = module_0.Internet(**dict_0)
        str_1 = internet_0.user_agent()
        internet_1 = module_0.Internet()
        bool_0 = True
        int_0 = -1098
        var_0 = internet_0.stock_image(str_1, int_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.emoji()
        str_1 = internet_0.image_placeholder(str_0)
        str_2 = '/M4"'
        list_0 = [str_0, str_2, str_2]
        var_0 = internet_0.stock_image(list_0)
        t_l_d_type_0 = module_1.TLDType.GTLD
        str_3 = internet_0.home_page(t_l_d_type_0)
        dict_0 = {}
        internet_1 = module_0.Internet(**dict_0)
        str_4 = internet_1.user_agent()
        internet_2 = module_0.Internet()
        bool_0 = True
        int_0 = -1098
        var_1 = internet_0.stock_image(str_0, int_0, list_0, bool_0)
    except BaseException:
        pass