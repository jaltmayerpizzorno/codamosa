# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    try:
        internet_0 = module_0.Internet()
        int_0 = 300
        str_0 = 'c1"'
        str_1 = 'dog'
        str_2 = [str_0, str_1]
        bool_0 = True
        str_3 = internet_0.emoji()
        var_0 = internet_0.stock_image(int_0, int_0, str_2, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.image_placeholder()
        str_1 = 'MneQD|kp='
        t_l_d_type_0 = None
        str_2 = internet_0.home_page(t_l_d_type_0)
        dict_0 = {str_1: str_1, str_1: str_1}
        internet_1 = module_0.Internet(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 852
        list_0 = []
        bool_0 = True
        internet_0 = module_0.Internet()
        var_0 = internet_0.stock_image(int_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        internet_0 = module_0.Internet()
        int_0 = 300
        str_0 = 'c1"'
        str_1 = '6lc 8\x0bJF'
        str_2 = internet_0.top_level_domain()
        str_3 = [str_0, str_1]
        str_4 = internet_0.home_page()
        bool_0 = True
        var_0 = internet_0.stock_image(int_0, int_0, str_3, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'6'
        internet_0 = module_0.Internet()
        str_0 = internet_0.top_level_domain(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.ip_v4()
        bool_0 = True
        int_0 = internet_0.port()
        var_0 = internet_0.stock_image(bool_0)
        str_1 = None
        bool_1 = True
        internet_1 = module_0.Internet()
        var_1 = internet_1.stock_image(str_1, bool_1)
        str_2 = internet_1.http_status_message()
        port_range_0 = None
        str_3 = internet_0.http_status_message()
        str_4 = internet_0.ip_v6()
        str_5 = internet_1.http_status_message()
        int_1 = internet_1.port(port_range_0)
    except BaseException:
        pass

def test_case_6():
    try:
        internet_0 = module_0.Internet()
        i_pv6_address_0 = internet_0.ip_v6_object()
        list_0 = [i_pv6_address_0]
        int_0 = -12
        var_0 = internet_0.hashtags(int_0)
        port_range_0 = module_1.PortRange.EPHEMERAL
        int_1 = internet_0.port(port_range_0)
        str_0 = None
        dict_0 = {str_0: list_0}
        internet_1 = module_0.Internet(**dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        internet_0 = module_0.Internet()
        int_0 = 300
        port_range_0 = module_1.PortRange.WELL_KNOWN
        str_0 = internet_0.ip_v4(port_range_0)
        str_1 = internet_0.ip_v6()
        var_0 = internet_0.stock_image(int_0)
        str_2 = 'ca"'
        str_3 = internet_0.network_protocol()
        str_4 = [str_2, str_2]
        bool_0 = True
        var_1 = internet_0.stock_image(int_0, int_0, str_4, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        internet_0 = module_0.Internet()
        int_0 = 300
        str_0 = 'ca"'
        str_1 = [str_0, str_0]
        bool_0 = True
        var_0 = internet_0.stock_image(int_0, int_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        internet_0 = module_0.Internet()
        int_0 = 300
        str_0 = 'cat'
        str_1 = 'dog'
        str_2 = [str_0, str_1]
        bool_0 = True
        var_0 = internet_0.stock_image(int_0, int_0, str_2, bool_0)
        var_1 = str_0.size
    except BaseException:
        pass