# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 10.833
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        var_0 = generic_bsd_ifconfig_network_0.populate()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '5sKoSX\nL\to[+KJ.Kmk'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1488
        int_1 = -3661
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_1)
        var_0 = generic_bsd_ifconfig_network_0.get_interfaces_info(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '^2+}JP#yEcze&'
        float_0 = -1567.6174
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(str_0, float_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        set_0 = set()
        str_0 = ''
        int_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0, int_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        int_1 = 275
        bool_0 = None
        set_1 = {int_1, int_1, bool_0}
        bytes_0 = b'L\xa5\xdaL\x10\xde\x00\x8b\xf2\x8c\x19|\x19'
        tuple_0 = (bytes_0,)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(set_1, tuple_0)
        var_0 = generic_bsd_ifconfig_network_2.parse_ether_line(set_0, generic_bsd_ifconfig_network_1, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        bytes_0 = b'\x02\x87ol\xe6\xa6\xdc\xf2\x18\xc7at\x91#\xcb79\xd1'
        str_0 = '\\WR"9y&}&\\}'
        tuple_0 = ()
        var_0 = generic_bsd_ifconfig_network_0.parse_status_line(bytes_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        float_0 = -2139.63
        tuple_0 = ()
        complex_0 = None
        str_0 = 'wcnuW}G(d)~:|1d`Q\tfx'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_lladdr_line(float_0, tuple_0, complex_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '3Y* >iHTM;\t=_u@ESz'
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, generic_bsd_ifconfig_network_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '-7'
        str_1 = '{=QB0+(Kx+Lx6#!qq'
        float_0 = 1258.276885
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        float_1 = 470.67249
        set_0 = {float_1, generic_bsd_ifconfig_network_0}
        bytes_0 = b'\xaf%}\x14\xbf-X\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(set_0, bytes_0, list_0)
        var_1 = generic_bsd_ifconfig_network_0.parse_unknown_line(str_0, str_1, str_0)
        str_2 = '4JsVw'
        set_1 = {str_2, str_2}
        str_3 = '\x0bb@@qCl'
        var_2 = generic_bsd_ifconfig_network_0.parse_tunnel_line(str_2, set_1, str_3)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ''
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        str_1 = 'alias'
        tuple_0 = ()
        complex_0 = None
        var_0 = generic_bsd_ifconfig_network_1.parse_unknown_line(str_1, tuple_0, complex_0)
        list_0 = []
        var_1 = generic_bsd_ifconfig_network_1.get_default_interfaces(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ")D\\,p'#lDj=A"
        set_0 = set()
        int_0 = -1424
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, set_0, generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        int_0 = 4788
        dict_0 = {bool_0: generic_bsd_ifconfig_network_0, bool_0: generic_bsd_ifconfig_network_0}
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(int_0, generic_bsd_ifconfig_network_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'v4'
        float_0 = 2151.2
        list_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        bool_0 = True
        str_1 = 'r;:{6D'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0, str_1)
        dict_0 = {bool_0: bool_0, generic_bsd_ifconfig_network_1: bool_0, bool_0: generic_bsd_ifconfig_network_1, str_1: generic_bsd_ifconfig_network_1}
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_2.parse_inet6_line(str_0, float_0, generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = ']7'
        float_0 = 1258.276885
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        bytes_0 = b'\xcf\x990\xd7\x82'
        tuple_0 = ()
        tuple_1 = (bytes_0, tuple_0)
        bool_0 = False
        dict_0 = {bool_0: tuple_1, tuple_1: bool_0, generic_bsd_ifconfig_network_0: float_0, bytes_0: tuple_0}
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(tuple_1, dict_0, tuple_1)
        float_1 = 470.67249
        set_0 = {float_1, float_0, str_0, str_0, generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0}
        bytes_1 = b'\xaf%}\x14\xbf-X\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(set_0, bytes_1, list_0)
        var_2 = generic_bsd_ifconfig_network_0.parse_unknown_line(str_0, str_0, str_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_1, set_0)
        var_3 = generic_bsd_ifconfig_network_2.parse_interface_line(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '-7'
        str_1 = '{=QB0+(Kx+Lx6#!qq'
        float_0 = 1258.276885
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        float_1 = 470.67249
        set_0 = {float_1, str_0, generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0}
        bytes_0 = b'\xaf%}\x14\xbf-X\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(set_0, bytes_0, list_0)
        var_1 = generic_bsd_ifconfig_network_0.parse_unknown_line(str_0, str_1, str_0)
        str_2 = 'n[}'
        dict_0 = {bytes_0: generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0: var_1, bytes_0: str_0}
        var_2 = generic_bsd_ifconfig_network_0.parse_ether_line(str_2, dict_0, dict_0)
        str_3 = 'version number inconsistent with state=latest: %s'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_3)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_0, set_0)
        var_3 = generic_bsd_ifconfig_network_2.parse_interface_line(str_3)
        var_4 = generic_bsd_ifconfig_network_1.get_default_interfaces(str_3)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'rsYW'
        bool_0 = False
        str_1 = '3Y* >iHTMm;\t=un@ESz'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.439519438273
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_1: str_1}
        var_2 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, tuple_0)
        var_3 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        str_2 = '!SrsN;+R$\x0c_'
        bytes_0 = None
        var_4 = generic_bsd_ifconfig_network_0.parse_inet_line(str_2, str_0, bytes_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'b3Lt1(hAx7V(,l#^H'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        dict_0 = {}
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, generic_bsd_ifconfig_network_0, dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '\x0c'
        str_1 = ':Q26:Ki94/?'
        list_0 = [str_0, str_1, str_1]
        int_0 = 993
        float_0 = -2507.11
        bytes_0 = b' \x96\xd2\x90\xf1\xdfx\x11C\xb7\x9f5H\x1ct};'
        tuple_0 = (float_0, bytes_0)
        set_0 = {str_0, str_1, int_0, tuple_0}
        list_1 = [float_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(list_0, int_0, set_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bool_0 = False
        str_0 = '3Y* >iHTMm;\t=un@ESz'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_0)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.439519438273
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_1: str_0}
        var_2 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, tuple_0)
        var_3 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        set_0 = {float_0, generic_bsd_ifconfig_network_1, generic_bsd_ifconfig_network_1}
        bytes_0 = b'\xaf%}\x14\xbf-\xfb\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_0]
        var_4 = generic_bsd_ifconfig_network_1.merge_default_interface(set_0, bytes_0, list_0)
        str_1 = '`:1'
        str_2 = 'ia~nN8>,l'
        var_5 = generic_bsd_ifconfig_network_1.parse_interface_line(str_2)
        str_3 = 'akwc#<&'
        var_6 = generic_bsd_ifconfig_network_0.get_options(str_3)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_0)
        int_0 = 1754
        var_7 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_1, bytes_0, int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'rsY'
        bool_0 = False
        str_1 = '3Y* >iHTMm;\t=un@ESz'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.439519438273
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_1: str_1}
        var_2 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, tuple_0)
        var_3 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        float_1 = 1270.03
        set_0 = {float_1, generic_bsd_ifconfig_network_1, generic_bsd_ifconfig_network_1}
        bytes_0 = b'\xaf%}\x14\xbf-\xfb\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_4 = generic_bsd_ifconfig_network_1.merge_default_interface(set_0, bytes_0, list_0)
        set_1 = set()
        var_5 = generic_bsd_ifconfig_network_1.get_default_interfaces(set_1)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'm$'
        bool_0 = False
        str_1 = '3Y* >iHTMm;\t=un@ESz'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.439519438273
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_1: str_1}
        var_2 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, tuple_0)
        var_3 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        float_1 = 496.53056622992506
        set_0 = {float_1, generic_bsd_ifconfig_network_1, generic_bsd_ifconfig_network_1}
        bytes_0 = b'\xaf%}\x14\xbf-\xfb\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_4 = generic_bsd_ifconfig_network_1.merge_default_interface(set_0, bytes_0, list_0)
        str_2 = '!),)i,\nXeAT)];uZb9o'
        var_5 = generic_bsd_ifconfig_network_1.parse_interface_line(str_2)
        str_3 = 'akwc#<&'
        var_6 = generic_bsd_ifconfig_network_0.get_options(str_3)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_1)
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_7 = generic_bsd_ifconfig_network_1.merge_default_interface(var_5, list_0, dict_0)
        str_4 = '\x0c6%YAY'
        var_8 = generic_bsd_ifconfig_network_3.parse_inet6_line(str_2, str_4, bytes_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'rsY'
        bool_0 = False
        str_1 = '3Y* >iHTMm;\t=un@ESz'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.439519438273
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_1: str_1}
        var_2 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        float_1 = 496.53056622992506
        set_0 = {float_1, generic_bsd_ifconfig_network_1, generic_bsd_ifconfig_network_1}
        bytes_0 = b'\xaf%}\x14\xbf-\xfb\x04@\x89\xd7\x08\x85\x07\xd7\x16V`\xf3'
        list_0 = [float_1]
        var_3 = generic_bsd_ifconfig_network_1.merge_default_interface(set_0, bytes_0, list_0)
        str_2 = 'ia~nN8>,l'
        var_4 = generic_bsd_ifconfig_network_1.parse_interface_line(str_2)
        str_3 = 'akwc#<&'
        var_5 = generic_bsd_ifconfig_network_0.get_options(str_3)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(str_1)
        bool_1 = True
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        bool_2 = False
        str_4 = '/sys/devices/virtual/dmi/id/bios_date'
        bytes_1 = b'i'
        int_0 = 4328
        generic_bsd_ifconfig_network_4 = module_0.GenericBsdIfconfigNetwork(bytes_1, int_0)
        tuple_1 = (bool_1, str_4)
        var_6 = generic_bsd_ifconfig_network_2.parse_inet_line(tuple_1, bool_2, tuple_1)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'rsY'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_0)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        float_0 = 1257.43952
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(float_0)
        tuple_0 = ()
        var_1 = generic_bsd_ifconfig_network_1.detect_type_media(tuple_0)
        str_1 = 'i~nN>,l'
        var_2 = generic_bsd_ifconfig_network_1.parse_interface_line(str_1)
        str_2 = '\tn:(<lJ>('
        var_3 = generic_bsd_ifconfig_network_1.get_options(str_2)
    except BaseException:
        pass