# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        int_0 = 998
        tuple_0 = (int_0,)
        set_0 = {int_0, tuple_0, tuple_0, tuple_0}
        str_0 = 'C!YAH0W"z:H4'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = ')k{'
        bytes_0 = b'\xa5\x07\xe1\xc2BHi#\xf3\xc2\xff'
        float_0 = -1198.91
        dict_0 = {bytes_0: float_0}
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_1, bytes_0, dict_0)
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(tuple_0, set_0, generic_bsd_ifconfig_network_0)
        bytes_1 = b'\xbe\xd4i/\x98\x9f'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bytes_1, bytes_1)
        str_2 = 'j'
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_2, set_0)
        var_2 = generic_bsd_ifconfig_network_2.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Iwg6/7~o<\\+{ d$t'
        int_0 = 5456
        tuple_0 = None
        str_1 = 'zYagRx2r%'
        tuple_1 = (int_0, tuple_0, str_0, str_1)
        bytes_0 = b'\xcc\x18\x8e\xd6\x01\x1c\x02\x9b\xa5\x0b49oy'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(tuple_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'2tE\xfa2\xee\x04\xb6'
        str_0 = '$<^7ZR/eVQw*SLD4H3mq'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        dict_0 = {bool_0: str_0, bytes_0: generic_bsd_ifconfig_network_0, str_0: generic_bsd_ifconfig_network_0, str_0: bytes_0}
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        bytes_0 = b'M\x0e[\x1f\x9b`&\xc6b'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0, bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        float_0 = -1069.0
        tuple_0 = (bool_0, float_0)
        str_0 = 'Nnzx'
        int_0 = 93
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0, int_0)
        bytes_0 = b'\xca\xb3\xc1w\x85\x81y\x85cA\x89(\xba$\xdf\xb3'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0, bytes_0)
        var_0 = generic_bsd_ifconfig_network_1.get_interfaces_info(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        str_0 = '\\bU\\(([^)]+)\\)'
        list_0 = [bool_0, bool_0, str_0]
        tuple_0 = (list_0,)
        str_1 = '>{Dm!:'
        str_2 = '\n    This is a OpenBSD family Hostname manipulation strategy class - it edits\n    the /etc/myname file.\n    '
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_2)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(str_0, tuple_0, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        generic_bsd_ifconfig_network_0 = None
        str_0 = '*d;.(Sd"a'
        list_0 = []
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_nd6_line(generic_bsd_ifconfig_network_0, str_0, generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 998
        tuple_0 = (int_0,)
        set_0 = {int_0, tuple_0, tuple_0, tuple_0}
        str_0 = None
        str_1 = 'C!YAH0W"z:H4'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        set_1 = {generic_bsd_ifconfig_network_0, str_1}
        bool_0 = True
        bytes_0 = b'\xb8"mu\x9c\xe4\x15/\xef\x9a\x86s7_-'
        tuple_1 = (set_1, tuple_0, bool_0, bytes_0)
        dict_0 = {}
        var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(tuple_1, dict_0, set_0)
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(tuple_0, set_0, generic_bsd_ifconfig_network_0)
        var_2 = generic_bsd_ifconfig_network_0.get_default_interfaces(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        bytes_0 = b''
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, bytes_0)
        list_0 = [generic_bsd_ifconfig_network_0]
        str_0 = "\x0cA1y~%'s.Y5t"
        dict_0 = {}
        set_0 = set()
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(dict_0, set_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_status_line(generic_bsd_ifconfig_network_0, list_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 1257.2
        str_0 = 'sJwI|%R=4\t'
        str_1 = '+_o"'
        bytes_0 = b'\xc0\x01\x02\xdf\x88'
        str_2 = 'file already exists'
        set_0 = {float_0}
        tuple_0 = (str_2, set_0)
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_lladdr_line(str_0, str_1, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "e'|[Y+x6.EM"
        int_0 = 146
        tuple_0 = ()
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '$ji>ya+V:u>rYOm'
        int_0 = -172
        dict_0 = {}
        set_0 = {str_0, str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        float_0 = 356.7623
        str_1 = ''
        str_2 = ')VfNU@1d(wA'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_2)
        var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(str_0, float_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        bytes_0 = b'M\x0e[\x1f\x9b`&\xc6b'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0, bytes_0)
        float_0 = 0.2
        str_0 = 'uwUJ+t]A\n|H9-2fbt1'
        var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(float_0, generic_bsd_ifconfig_network_0, str_0)
        var_1 = generic_bsd_ifconfig_network_0.get_default_interfaces(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '^st'
        float_0 = -115.729
        set_0 = {float_0, float_0, float_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        int_0 = -2460
        str_0 = '\nJ98Wx|i{f^-$Vi=4m*$'
        tuple_0 = (int_0, str_0)
        dict_0 = {bool_0: tuple_0}
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(tuple_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "kaJb3'p:"
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        float_0 = 0.2
        str_1 = 'O3M\naW8RAStb\\-\x0c8-&v'
        bytes_0 = None
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_1, float_0, bytes_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b'2tE\xfa2\xee\x04\xb6'
        str_0 = '$<^7ZR/eVQw*SLD4H3mq'
        str_1 = 'H'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bytes_0, bool_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_1)
        dict_0 = {generic_bsd_ifconfig_network_2: str_0}
        var_1 = generic_bsd_ifconfig_network_2.merge_default_interface(str_0, bytes_0, dict_0)
        bytes_1 = b'P\x11c,\x9c\x04\xdf%\xd9\xbe\xa5'
        list_0 = [generic_bsd_ifconfig_network_1, str_0, str_1, bytes_1]
        float_0 = 0.001
        var_2 = generic_bsd_ifconfig_network_1.parse_inet_line(list_0, bytes_1, float_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 999
        tuple_0 = (int_0,)
        set_0 = {int_0, tuple_0, tuple_0, tuple_0}
        str_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = '\rW\r,soF=rb\\cHJ}Cc\rn'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_1)
        generic_bsd_ifconfig_network_2 = None
        bytes_0 = b'\x17\x8b\x0f\xfb*\x18h\x12\xac\t~\xee\xe3'
        str_2 = '#7&Xz`y@Sw2I|hqQZ'
        str_3 = 'dash'
        dict_0 = {}
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_3.parse_media_line(str_3, dict_0, tuple_0)
        dict_1 = {bytes_0: bytes_0, tuple_0: tuple_0, generic_bsd_ifconfig_network_0: str_0, generic_bsd_ifconfig_network_2: str_2}
        str_4 = 'h'
        var_1 = generic_bsd_ifconfig_network_1.merge_default_interface(dict_1, bytes_0, str_4)
        var_2 = generic_bsd_ifconfig_network_1.merge_default_interface(str_1, set_0, generic_bsd_ifconfig_network_2)
        var_3 = generic_bsd_ifconfig_network_1.get_default_interfaces(dict_1)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 999
        tuple_0 = (int_0,)
        set_0 = {int_0, tuple_0, tuple_0, tuple_0}
        str_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = '\rW\r,soF=r@\\\tHJ}Ct\rn'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_1)
        generic_bsd_ifconfig_network_2 = None
        bytes_0 = b'\x17\x8b\x0f\xfb*\x18h\x12\xac\t~\xee\xe3'
        str_2 = '#7&Xz`y@Sw2I|hqQZ'
        str_3 = 'da'
        dict_0 = {}
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_3.parse_media_line(str_3, dict_0, tuple_0)
        dict_1 = {bytes_0: bytes_0, tuple_0: tuple_0, generic_bsd_ifconfig_network_0: str_0, generic_bsd_ifconfig_network_2: str_2}
        str_4 = 'h'
        var_1 = generic_bsd_ifconfig_network_1.merge_default_interface(dict_1, bytes_0, str_4)
        var_2 = generic_bsd_ifconfig_network_1.merge_default_interface(str_1, set_0, generic_bsd_ifconfig_network_2)
        var_3 = generic_bsd_ifconfig_network_1.get_options(tuple_0)
    except BaseException:
        pass