# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.ip_v4()
        str_1 = internet_0.content_type()
        var_0 = internet_0.hashtags()
        str_2 = internet_0.image_placeholder(str_0)
        str_3 = internet_0.user_agent()
        i_pv4_address_0 = internet_0.ip_v4_object()
        int_0 = None
        port_range_0 = module_1.PortRange.ALL
        str_4 = internet_0.ip_v4(port_range_0)
        internet_1 = module_0.Internet()
        str_5 = internet_0.mac_address()
        i_pv4_address_1 = internet_0.ip_v4_object()
        var_1 = internet_0.hashtags(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        internet_0 = module_0.Internet()
        str_0 = 'N93 a list'
        bool_0 = True
        list_0 = [str_0, str_0, str_0]
        var_0 = internet_0.stock_image(str_0, str_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.ip_v4()
        str_1 = internet_0.top_level_domain()
        str_2 = internet_0.content_type()
        var_0 = internet_0.hashtags()
        str_3 = internet_0.image_placeholder(str_0)
        str_4 = internet_0.user_agent()
        str_5 = internet_0.ip_v4()
        str_6 = internet_0.image_placeholder()
        str_7 = internet_0.mac_address()
        var_1 = internet_0.stock_image(str_5)
        port_range_0 = None
        internet_1 = module_0.Internet()
        int_0 = internet_1.port(port_range_0)
    except BaseException:
        pass

def test_case_3():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.image_placeholder()
        bool_0 = True
        str_1 = 'P9a'
        list_0 = [str_1, str_1, str_0]
        var_0 = internet_0.stock_image(str_0, str_0, list_0, bool_0)
    except BaseException:
        pass