# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        set_0 = set()
        int_0 = -395
        list_0 = []
        tuple_0 = (list_0, set_0)
        float_0 = 1103.0
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, float_0)
        var_0 = generic_bsd_ifconfig_network_0.populate(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 102.4
        set_0 = {float_0}
        float_1 = 336.0
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_1)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.detect_type_media(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        bytes_0 = b'\x8b\xdd\x9e\x9e\x05\xbd\xf8\xba\x0c\x1a'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, bytes_0)
        str_0 = "r\rw_6cU |7'u|6}\tG{"
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, str_0, tuple_0)
        var_1 = generic_bsd_ifconfig_network_0.get_interfaces_info(str_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x1f0\xac\x02\xacS\xf5'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        tuple_0 = None
        list_0 = []
        set_0 = None
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(list_0, tuple_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xb2O\xff5\xc7\x14K\xc4F^\xc3o\x98a\xd7\xf7R\xa2'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        str_0 = 'Cd D.{F3Y'
        set_0 = set()
        str_1 = '@'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_1.parse_nd6_line(generic_bsd_ifconfig_network_0, str_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'F>"0tGKs]:9Q z~s'
        str_1 = ''
        tuple_0 = (str_0, str_1)
        set_0 = {str_1, str_0}
        str_2 = 'done with local.exec_command()'
        str_3 = 'Function to create a deep copy of module response data\n\n    Designed to be used within the Ansible "engine" to improve performance\n    issues where ``copy.deepcopy`` was used previously, largely with CPU\n    and memory contention.\n\n    This only supports the following data types, and was designed to only\n    handle specific workloads:\n\n    * ``dict``\n    * ``list``\n\n    The data we pass here will come from a serialization such\n    as JSON, so we shouldn\'t have need for other data types such as\n    ``set`` or ``tuple``.\n\n    Take note that this function should not be used extensively as a\n    replacement for ``deepcopy`` due to the naive way in which this\n    handles other data types.\n\n    Do not expect uses outside of those listed below to maintain\n    backwards compatibility, in case we need to extend this function\n    to handle our specific needs:\n\n    * ``ansible.executor.task_result.TaskResult.clean_copy``\n    * ``ansible.vars.clean.clean_facts``\n    * ``ansible.vars.namespace_facts``\n    '
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_3)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_2, generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_ether_line(tuple_0, tuple_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -296
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        float_0 = None
        bool_0 = True
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(float_0, float_0, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\x0bDP'
        bool_0 = True
        str_1 = "I~R?Ir#n'i X,&\x0cv\t("
        float_0 = 751.7512
        str_2 = 'w.pb";.nAo0sMc'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0, str_2)
        var_0 = generic_bsd_ifconfig_network_0.parse_status_line(str_0, bool_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\x9f\xca\xa3K\xfa\x8d'
        list_0 = [bytes_0]
        float_0 = None
        float_1 = 2.0
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_lladdr_line(bytes_0, list_0, float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -585
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        str_0 = '">kH'
        bytes_0 = b'f\xf2G\xc5T\xcc\x15\r\xce\xdb'
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, generic_bsd_ifconfig_network_0, bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = None
        set_0 = {bytes_0}
        bool_0 = True
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(bytes_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'RLNnc8y}%[s&i['
        bytes_0 = b'\x89\xec'
        str_1 = 'I}XhjcFH\r3'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        str_0 = 'ejL^'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = 'XslDfBXVpJgPv'
        var_0 = generic_bsd_ifconfig_network_1.parse_tunnel_line(dict_0, str_1, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'qg|'
        float_0 = -3297.8
        dict_0 = {}
        str_1 = '[N~]'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, float_0, dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'OXH\x0b}'
        tuple_0 = (str_0,)
        complex_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, tuple_0, complex_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '-'
        str_1 = ',3`/7s%_c}ISEi\x0cHYLX'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        str_2 = ',y._xT|"'
        list_0 = []
        set_0 = {str_0, str_0}
        tuple_0 = (list_0, list_0, set_0)
        tuple_1 = (str_2, tuple_0)
        str_3 = 'xXV-"Oefv"'
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(tuple_1, str_3, list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'jJ!7yHZ:F{Th0~<'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        bytes_0 = b'Q\xdd\x94\xcd\x07[\x16\x0c\xfd\x1b\x8b\xc8\xe4\x14\x8b\x98te\xa9'
        float_0 = None
        float_1 = 1082.973474
        float_2 = None
        list_0 = [float_1, float_2, dict_0, str_0]
        bool_0 = False
        tuple_0 = (float_0, list_0, bool_0)
        tuple_1 = (str_0, bytes_0, tuple_0)
        str_1 = '<1l}Mk`Dz^q3/Ha-'
        set_0 = set()
        bytes_1 = b'b%I4\x194G4}'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(tuple_1, str_1, set_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'w>\xf1\xabn\x862\xb1'
        bool_0 = True
        str_0 = '-TQv'
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0, bytes_0)
        tuple_0 = ()
        str_1 = '%),?l;s|yk'
        var_1 = generic_bsd_ifconfig_network_1.get_options(str_1)
        int_0 = -1922
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(tuple_0, int_0)
        var_2 = generic_bsd_ifconfig_network_1.detect_type_media(generic_bsd_ifconfig_network_2)
    except BaseException:
        pass

def test_case_19():
    try:
        tuple_0 = ()
        bytes_0 = b'\x8b\xdd\x9e\x9e\x05\xbd\xf8\xba\x0c\x1a'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, bytes_0)
        str_0 = "r\rw_6cU |7'u|6}\tG{"
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, str_0, tuple_0)
        dict_0 = {generic_bsd_ifconfig_network_0: str_0}
        var_1 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        var_2 = generic_bsd_ifconfig_network_0.get_default_interfaces(generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = -1600
        str_0 = 'b qF@a#"{ rFN@-Xwt'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = '\\c|6'
        bool_0 = True
        dict_0 = {str_1: bool_0}
        int_1 = -1048
        str_2 = 'kd*;o'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_2)
        set_0 = {generic_bsd_ifconfig_network_1, int_0}
        tuple_0 = (dict_0, int_1, set_0, dict_0)
        str_3 = '9BO\x0b1%%[,9GG'
        var_0 = generic_bsd_ifconfig_network_1.parse_ether_line(str_3, dict_0, int_1)
        int_2 = 405
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(int_2)
        var_1 = generic_bsd_ifconfig_network_2.parse_nd6_line(str_1, bool_0, tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'\xca)\xa7\xfc\xa6\x94\x03'
        bytes_1 = b'"\xc8\xcftI\xf1\x98a\xb8\xb9e{\x82\xb2\xb2\x18\x8e@\x96W'
        int_0 = -2356
        str_0 = 'v\x0c3H.Q1RiUeH/(oR/%'
        dict_0 = {int_0: int_0, str_0: bytes_1}
        tuple_0 = (int_0, str_0, bytes_0, dict_0)
        str_1 = '2BZS6mY;'
        str_2 = '\rjB'
        tuple_1 = (str_1, str_2)
        generic_bsd_ifconfig_network_0 = None
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        bool_0 = True
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bool_0, bytes_0)
        var_0 = generic_bsd_ifconfig_network_2.parse_inet6_line(tuple_0, tuple_1, generic_bsd_ifconfig_network_1)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = "Y9%dkV-'\n"
        str_1 = "jaOUeD5zpjAg1'm "
        int_0 = -682
        str_2 = '3*X$aO9K'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_2)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'interface'
        str_1 = 'uX%O,2'
        set_0 = {str_0, str_1}
        str_2 = 'wl,J#c#?W7~7n!9s{&'
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(set_0, str_2, list_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bytes_0 = b'w>\xabn\xb1'
        str_0 = 'r<=M\\`e@4z+N*eqcbr)'
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_interface_line(str_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bool_0, bytes_0)
        tuple_0 = ()
        set_0 = {bytes_0, tuple_0, generic_bsd_ifconfig_network_2}
        var_1 = generic_bsd_ifconfig_network_2.get_options(str_0)
        str_1 = '*g!.]Y}C Dqi\r:r2K'
        bool_1 = False
        var_2 = generic_bsd_ifconfig_network_2.merge_default_interface(str_1, str_1, bool_1)
        int_0 = -1435
        var_3 = generic_bsd_ifconfig_network_2.detect_type_media(tuple_0)
        dict_0 = {int_0: str_0}
        str_2 = '+Rkt{FxG68uch6$j'
        var_4 = generic_bsd_ifconfig_network_1.parse_tunnel_line(str_2, dict_0, set_0)
        str_3 = "B/2C '"
        float_0 = 340.61016
        str_4 = 'p]KduGcEif5Id'
        var_5 = generic_bsd_ifconfig_network_2.parse_inet_line(str_3, float_0, str_4)
    except BaseException:
        pass