# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        str_0 = '`ZTFUPQdcY<b3> vJ'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.get_options(str_0)
        int_0 = -1869
        str_1 = "N$h')"
        set_0 = {int_0}
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_1, set_0)
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_1 = generic_bsd_ifconfig_network_0.populate()
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = dict()
        str_0 = 'x'
        int_0 = 384
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_1 = generic_bsd_ifconfig_network_0.detect_type_media(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\rO'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -285
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.get_interfaces_info(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x1b,\x8a\xa9\x05\xd4\xdaIt~VK'
        float_0 = -1673.0
        float_1 = 1458.0361
        str_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(float_0, float_1, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'alias'
        float_0 = 0.2
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        list_0 = None
        int_0 = 1159
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_nd6_line(str_0, generic_bsd_ifconfig_network_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '>88oH0+!yqa\n^%s'
        int_0 = -1075
        str_1 = '7RP^'
        bytes_0 = b'sL'
        list_0 = [bytes_0, int_0, str_0]
        tuple_0 = (int_0, str_1, bytes_0, list_0)
        int_1 = 1024
        set_0 = {int_1, int_1, int_1, int_1}
        tuple_1 = ()
        bytes_1 = b'Kx\xf2m\xb8j\xe5\xa0\x14\xa1|n'
        dict_0 = {}
        float_0 = -557.0
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(bytes_1, dict_0, float_0)
        bool_1 = None
        tuple_2 = (int_1, set_0, tuple_1, bool_1)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(tuple_2)
        var_1 = generic_bsd_ifconfig_network_1.parse_inet_line(str_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        float_0 = 2.0
        str_0 = '[6{'
        int_0 = 438
        list_1 = []
        tuple_0 = (float_0, str_0, int_0, list_1)
        float_1 = 1942.88384
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_1, float_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(list_0, bool_0, tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -188
        tuple_0 = (int_0,)
        float_0 = 100.0
        str_0 = '5?bH?2?o!*~37\x0b)F,R1<'
        list_0 = [int_0, tuple_0, float_0]
        bool_0 = False
        bool_1 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, bool_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_status_line(str_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'V[\x0cT3>\x0byezqtwHSi\\'
        tuple_0 = ()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 3737.3
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(dict_0, float_0, float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        str_0 = 'cf{=2PQ$Y^LOUa#> }\tE'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        bytes_0 = None
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'V[\x0cT3>\x0byezqtwHSi\\'
        tuple_0 = ()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = '~lD%<gib\x0b'
        bytes_0 = b'\xae\x89\x98=F\xef\x8d)3c\xb0_\x07x\t'
        dict_0 = {bytes_0: tuple_0, tuple_0: str_0}
        int_0 = -1608
        var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(bytes_0, dict_0, int_0)
        bool_0 = False
        var_1 = generic_bsd_ifconfig_network_0.parse_inet_line(str_1, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'US'
        str_1 = 'c]'
        int_0 = -2265
        bool_0 = None
        set_0 = {bool_0, bool_0, bool_0}
        list_0 = [bool_0, set_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0, list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_lladdr_line(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'V[\x0cT3>\x0byezqtwHSi\\'
        tuple_0 = ()
        float_0 = 3865.28
        list_0 = [str_0, str_0, str_0, float_0]
        set_0 = {tuple_0, str_0, str_0, tuple_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(list_0)
        var_1 = generic_bsd_ifconfig_network_0.get_default_interfaces(list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = False
        tuple_0 = ()
        float_0 = 4584.62
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0, bool_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(tuple_0)
        int_0 = 1458
        set_0 = {bool_0, bool_0, bool_0, int_0}
        bytes_0 = b'\x01~\xd4\xb6\x03{f\x19\xa4\xa7_'
        int_1 = -1039
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bytes_0, int_1)
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        list_0 = []
        bytes_0 = None
        str_0 = '1/.BTz6U'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '58Hn!\r=5uxf32 '
        tuple_0 = ()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '3&'
        float_0 = 1729.0
        bytes_0 = b'\xc3\x7f$o\x94\x0fo'
        int_0 = 1087
        set_0 = set()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0, set_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = b'\xb5\x07\x9f>\x14\x17\x0b9I\x98'
        str_0 = "'&Z'\nB sOLw"
        dict_0 = {bytes_0: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        bool_0 = False
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0)
        str_1 = 'KZTFUPQd><3> vJ'
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
        var_0 = generic_bsd_ifconfig_network_2.get_options(str_1)
        int_0 = -1869
        str_2 = "N$h')"
        set_0 = {int_0}
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(str_2, set_0)
        var_1 = generic_bsd_ifconfig_network_3.get_default_interfaces(int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = None
        str_0 = 'N'
        dict_0 = {int_0: str_0}
        str_1 = 'JhL0S~$"U5bt'
        generic_bsd_ifconfig_network_0 = None
        int_1 = 233
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_1)
        var_0 = generic_bsd_ifconfig_network_1.parse_media_line(str_1, dict_0, int_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
        var_1 = generic_bsd_ifconfig_network_2.parse_options_line(str_1, dict_0, generic_bsd_ifconfig_network_0)
        float_0 = 1425.24447641828
        tuple_0 = ()
        var_2 = generic_bsd_ifconfig_network_2.detect_type_media(tuple_0)
        list_0 = [dict_0, str_1, int_0, float_0]
        str_2 = '|cU+'
        bytes_0 = b'Z\xdf|\xf3\x00\xbc\xb7\x94\x91\xe9\x80\xb7}*i'
        var_3 = generic_bsd_ifconfig_network_2.merge_default_interface(str_2, bytes_0, int_0)
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(list_0, str_1)
        var_4 = generic_bsd_ifconfig_network_3.get_default_interfaces(generic_bsd_ifconfig_network_3)
    except BaseException:
        pass

def test_case_22():
    try:
        tuple_0 = ()
        str_0 = 'yNJ:oT+~jPdc'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = '7e._LJ-/<@:.'
        list_0 = [tuple_0, str_1, generic_bsd_ifconfig_network_0]
        str_2 = ')zDO*2G'
        str_3 = 'y&=Av6]!zs'
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(list_0, str_2, str_3)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'a'
        str_1 = 'b'
        var_0 = []
        var_1 = []
        var_2 = dict(interface=str_0, a=str_0, b=str_1, ipv4=var_0, ipv6=var_1)
        str_2 = 'ipv4'
        str_3 = 'ipv6'
        str_4 = [str_0]
        str_5 = {str_0: str_0, str_2: str_4, str_3: str_2}
        var_3 = dict(a=str_5)
        var_4 = dict()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_4)
        var_5 = generic_bsd_ifconfig_network_0.merge_default_interface(var_2, var_3, str_2)
    except BaseException:
        pass