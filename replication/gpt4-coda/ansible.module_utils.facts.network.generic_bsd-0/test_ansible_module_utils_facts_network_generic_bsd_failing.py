# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        str_0 = 't^FEK\x0cl %M[G^b$qvDd'
        set_0 = set()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_0.populate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2
        str_0 = 'zlNC]&b2TG$'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'9w\xf8\x81\xdcd\xf9G'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        bytes_0 = b'4\x84*\xf3}\xc0\x08'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0, generic_bsd_ifconfig_network_0)
        tuple_0 = ()
        str_0 = 's'
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_0)
        float_0 = None
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_2, float_0)
        set_0 = {tuple_0, tuple_0, generic_bsd_ifconfig_network_3}
        generic_bsd_ifconfig_network_4 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_4.get_interfaces_info(generic_bsd_ifconfig_network_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b''
        str_0 = 'j'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'q.@g|RkC5^t[r@sE#yC|'
        list_0 = [str_0, str_0]
        float_0 = 1640.1
        int_0 = 480
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(str_0, list_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        dict_0 = {}
        bool_0 = False
        var_0 = generic_bsd_ifconfig_network_0.parse_nd6_line(dict_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = None
        float_0 = 235.5254
        tuple_1 = (tuple_0, float_0)
        dict_0 = None
        set_0 = set()
        float_1 = 1.0
        bool_0 = False
        list_0 = [float_1, float_1, bool_0]
        int_0 = -257
        tuple_2 = (int_0, float_1)
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0, tuple_2)
        var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(tuple_1, dict_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -1327
        bytes_0 = None
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        tuple_0 = (int_0, bytes_0, generic_bsd_ifconfig_network_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        set_0 = {generic_bsd_ifconfig_network_1, bytes_0, tuple_0, generic_bsd_ifconfig_network_0}
        str_0 = None
        str_1 = 'hpBn<$K`I-(!6Xf~\x0b?'
        bool_0 = True
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bool_0)
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_2)
        var_0 = generic_bsd_ifconfig_network_3.parse_lladdr_line(set_0, str_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'q.@g|RkC5^t[r@sE#yC|'
        int_0 = 480
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        bool_0 = False
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'address'
        bool_0 = False
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        set_0 = set()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        list_0 = []
        bool_0 = False
        var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(list_0, generic_bsd_ifconfig_network_0, bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "y%N=-f',n0xSAQ}f,('="
        set_0 = set()
        str_1 = '|H\n2\n/GuD!'
        int_0 = -1233
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        tuple_0 = (int_0, list_0, generic_bsd_ifconfig_network_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_unknown_line(set_0, str_0, str_1)
        bytes_0 = b'6\x0fE'
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        int_1 = 6
        bool_0 = False
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_1 = generic_bsd_ifconfig_network_3.parse_inet_line(str_0, generic_bsd_ifconfig_network_2, int_1)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -22.935320530948133
        str_0 = 'Ni%bOc">K/+'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0, bool_0)
        dict_0 = {float_0: str_0}
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        bytes_0 = b'\xa9'
        str_1 = '<[Eb-[\tQBYcF<@EM'
        var_1 = generic_bsd_ifconfig_network_0.get_options(str_1)
        var_2 = generic_bsd_ifconfig_network_0.get_default_interfaces(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'v4'
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        int_0 = -3403
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        dict_0 = {bool_0: int_0, generic_bsd_ifconfig_network_0: int_0, generic_bsd_ifconfig_network_0: list_0}
        float_0 = -3171.1
        var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(list_0, dict_0, float_0)
        str_0 = 'non_native_want_json'
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(list_0, int_0, str_0)
        var_2 = generic_bsd_ifconfig_network_0.detect_type_media(list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "*81b~%V2&' )U4{4%q=e"
        int_0 = 886
        tuple_0 = (str_0, str_0, int_0)
        str_1 = "zy8'TK\\EmYT07\x0btI-j1\n"
        set_0 = {int_0, str_0}
        float_0 = -1019.92163
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_inet6_line(tuple_0, str_1, set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = -22.935320530948133
        str_0 = 'Ni%COT">K/+'
        bool_0 = True
        set_0 = None
        tuple_0 = (set_0, str_0, float_0)
        int_0 = 20
        str_1 = "M3']/uEMKS(1"
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(tuple_0, int_0, str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = -22.935320530948133
        str_0 = 'Ni%bO">K/+'
        bool_0 = False
        bytes_0 = b'\x91C'
        dict_0 = {}
        bool_1 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0, bool_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(bytes_0, dict_0, bool_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0, bool_0)
        list_0 = [float_0, bool_0]
        dict_1 = {float_0: str_0}
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(dict_1)
        set_0 = None
        tuple_0 = (list_0, float_0, set_0, str_0)
        var_2 = generic_bsd_ifconfig_network_1.merge_default_interface(str_0, tuple_0, bool_0)
        var_3 = generic_bsd_ifconfig_network_1.parse_interface_line(str_0)
        var_4 = generic_bsd_ifconfig_network_1.parse_interface_line(str_0)
        bool_2 = False
        str_1 = '[P>sU5r)<<VSr|i'
        var_5 = generic_bsd_ifconfig_network_1.get_options(str_1)
        var_6 = generic_bsd_ifconfig_network_1.parse_unknown_line(list_0, tuple_0, bool_2)
        var_7 = generic_bsd_ifconfig_network_1.get_default_interfaces(list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        float_0 = -22.935320530948133
        str_0 = 'Ni%bO">K/+'
        bool_0 = False
        bytes_0 = b'\x1e\r\x1d'
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        bool_1 = True
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0, bool_1)
        dict_1 = {bool_1: dict_0, bool_1: str_0, bytes_0: bool_0}
        bool_2 = False
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(dict_1, bool_2, bytes_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '$859Wn8vVJ<QIL\x0bY)rd'
        int_0 = 480
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        bool_0 = False
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, int_0, bool_0)
    except BaseException:
        pass