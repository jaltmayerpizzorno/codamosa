# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    dict_0 = {}
    str_0 = '4J/N38^+F"3"&G}j|\'3'
    tuple_0 = (dict_0, str_0)
    list_0 = [dict_0, tuple_0, dict_0]
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_1():
    float_0 = 1565.80498
    bytes_0 = b'\x85\x90\xae\x84\x9b\xb6\x06\xfc\xe5H\x8a<\x93\x13\x1a'
    float_1 = 1.0
    str_0 = 'సంకేతపదము'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(float_0, bytes_0, float_1)

def test_case_2():
    str_0 = 'bbr*CBA>(C\x0c%CK]GZ\n'
    set_0 = set()
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
    list_0 = []
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, generic_bsd_ifconfig_network_0, list_0)

def test_case_3():
    bytes_0 = b'\xb5\x07\x9f>\x14\x17\x0b9I\x98'
    str_0 = "'&Z9\nB/sObw"
    str_1 = '7RP^'
    float_0 = 1.0
    dict_0 = {bytes_0: str_0}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
    tuple_0 = (float_0, str_1, generic_bsd_ifconfig_network_0, bytes_0)
    bool_0 = False
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0)
    var_0 = generic_bsd_ifconfig_network_1.parse_media_line(tuple_0, dict_0, str_1)
    dict_1 = {str_1: str_1}
    generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_1, dict_1)

def test_case_4():
    bytes_0 = b'\xb5\x07\x9f>\x14\x17\x0b9I\x98'
    str_0 = "'&Z'\nB sOLw"
    str_1 = '7RP^'
    dict_0 = {bytes_0: str_0}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
    bool_0 = False
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0)
    str_2 = 'KZTFUPQd><b3> vJ'
    generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
    var_0 = generic_bsd_ifconfig_network_2.get_options(str_2)
    dict_1 = {str_1: str_1}
    generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(str_1, dict_1)

def test_case_5():
    str_0 = '\r:o|o_<dD}o '
    int_0 = -540
    dict_0 = {str_0: int_0}
    list_0 = None
    set_0 = {str_0}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(dict_0, int_0, list_0)
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_0)
    var_1 = generic_bsd_ifconfig_network_1.get_options(str_0)

def test_case_6():
    str_0 = 'a'
    str_1 = '5'
    var_0 = []
    var_1 = dict(interface=str_0, a=str_0, b=str_1, ipv4=str_1, ipv6=var_0)
    str_2 = 'ixvA'
    str_3 = 'address'
    str_4 = "N{V='VQN ]2?"
    str_5 = 'netmask'
    str_6 = '192.168.0.1'
    str_7 = {str_3: str_5, str_2: str_6, str_1: str_4, str_4: str_6, str_5: str_6, str_5: str_5}
    str_8 = [str_7]
    str_9 = [str_8]
    str_10 = {str_0: str_0, str_2: str_8, str_5: str_9}
    var_2 = dict(a=str_10)
    var_3 = dict()
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_3)
    var_4 = generic_bsd_ifconfig_network_0.merge_default_interface(var_1, var_2, str_2)
    var_5 = var_1[str_2]

def test_case_7():
    str_0 = 'a'
    str_1 = '5'
    var_0 = []
    var_1 = dict(interface=str_0, a=str_0, b=str_1, ipv4=str_1, ipv6=var_0)
    str_2 = 'ixvA'
    str_3 = 'ipv6'
    str_4 = 'address'
    str_5 = "N{V='VQN ]2?"
    str_6 = 'netmask'
    str_7 = '192.168.0.1'
    str_8 = {str_4: str_3, str_2: str_7, str_1: str_5, str_5: str_7, str_6: str_7, str_3: str_3}
    str_9 = [str_8]
    str_10 = [str_9]
    str_11 = {str_0: str_0, str_2: str_9, str_3: str_10}
    var_2 = dict(a=str_11)
    var_3 = dict()
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_3)
    var_4 = generic_bsd_ifconfig_network_0.merge_default_interface(var_1, var_2, str_2)
    var_5 = var_1[str_2]

def test_case_8():
    str_0 = 'b'
    var_0 = []
    var_1 = []
    var_2 = dict(interface=str_0, a=str_0, b=str_0, ipv4=var_0, ipv6=var_1)
    str_1 = 'device'
    str_2 = 'ipv4'
    str_3 = 'ipv6'
    str_4 = 'address'
    str_5 = 'broadcast'
    str_6 = '10.0.0.1'
    str_7 = '192.168.0.1'
    str_8 = '255.0.0.0'
    str_9 = {str_4: str_6, str_5: str_7, str_3: str_8}
    str_10 = [str_9]
    str_11 = '2001:db8::1'
    str_12 = {str_4: str_11}
    str_13 = [str_12]
    str_14 = {str_1: str_6, str_2: str_10, str_3: str_13}
    var_3 = dict(a=str_14)
    var_4 = dict()
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_4)
    var_5 = generic_bsd_ifconfig_network_0.merge_default_interface(var_2, var_3, str_2)
    var_6 = var_2[str_2]
    var_7 = len(var_6)

def test_case_9():
    str_0 = 'V[\x0cT3>\x0byezqtwHSi\\'
    tuple_0 = ()
    int_0 = 195
    list_0 = [int_0, str_0]
    str_1 = 'O'
    dict_0 = {tuple_0: str_1}
    bytes_0 = b'\xbf~'
    int_1 = 8
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_1)
    var_0 = generic_bsd_ifconfig_network_0.parse_media_line(list_0, dict_0, bytes_0)
    float_0 = 3865.28
    list_1 = [str_0, str_0, str_0, float_0]
    set_0 = {tuple_0, str_0, str_0, tuple_0}
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0)
    var_1 = generic_bsd_ifconfig_network_1.parse_interface_line(list_1)
    var_2 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
    generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_0)