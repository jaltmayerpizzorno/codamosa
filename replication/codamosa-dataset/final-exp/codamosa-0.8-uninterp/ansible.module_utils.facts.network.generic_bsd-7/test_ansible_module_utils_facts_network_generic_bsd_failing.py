# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        str_0 = 'ssh_extra_args'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = ":='\x0bn/JCI+JvoL0+Z`Xq"
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_1.detect_type_media(generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2352
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        str_0 = '6K\\'
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(str_0)
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
        bytes_0 = b'\x9b\x8fL\xc6=j\x91\x85\x12\x0b\x83'
        set_0 = set()
        list_0 = [set_0, set_0, set_0, bytes_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
        var_0 = generic_bsd_ifconfig_network_0.get_interfaces_info(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '+yN`#.S(=8m9DM\n%D<ZD'
        bool_0 = False
        float_0 = -3087.22
        int_0 = 14
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(str_0, bool_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1090
        str_0 = 'N<l+;'
        list_0 = [str_0, int_0, int_0]
        str_1 = ' - '
        int_1 = 2882
        set_0 = {str_0, str_1}
        bytes_0 = b'\xe5\xc2\xe400\xec\xd6\x80\x86\x07'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0, list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_nd6_line(int_1, set_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1409.05834
        str_0 = 'uH\x0cGS/tIsR:`O'
        bytes_0 = None
        float_1 = -1623.588636
        tuple_0 = (float_0, str_0, bytes_0, float_1)
        str_1 = 'w\tJ<0mq'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(tuple_0, float_1, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        float_0 = 1687.0
        list_0 = []
        str_0 = 'W""^\\+So'
        set_0 = {str_0, str_0}
        bytes_0 = None
        int_0 = 313
        bool_0 = None
        float_1 = 3475.0
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, float_1)
        tuple_1 = (bytes_0, int_0, generic_bsd_ifconfig_network_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0, tuple_1)
        var_0 = generic_bsd_ifconfig_network_1.parse_status_line(tuple_0, float_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'password_expire_max'
        int_0 = -2008
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
        bool_0 = True
        var_1 = generic_bsd_ifconfig_network_0.parse_lladdr_line(str_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'G3\\;7'
        set_0 = {str_0, str_0, str_0}
        int_0 = -376
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, set_0, set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '(\\:KvF\n_w%Oce-5r\t0k4'
        set_0 = {str_0, str_0}
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0, bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, set_0, set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -1896
        list_0 = [int_0, int_0, int_0, int_0]
        str_0 = 'DG2+]nbLC&Fk&Z}?7w=V'
        str_1 = 'qC'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        float_0 = None
        dict_0 = {str_1: float_0, int_0: list_0, int_0: str_1, str_0: str_1}
        int_1 = 3935
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_0)
        tuple_0 = (dict_0, int_1, list_0, generic_bsd_ifconfig_network_1)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(float_0, float_0, generic_bsd_ifconfig_network_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'eH?|G67GDV!C('
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.populate()
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = 1.0
        str_0 = '%s is kept for backwards compatibility but usage is discouraged. The module documentation details page may explain more about this rationale.'
        dict_0 = {float_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (float_0, str_0, dict_0)
        list_0 = []
        bytes_0 = b'\\\xf9\xb1;9'
        str_1 = ''
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(tuple_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Lz'
        float_0 = -14.83146125759793
        bytes_0 = b'\x9euF\xdb\x03#7\x19d~:\xd3\xa4\x0f\xfc'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0, bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\n---\nauthor: Ansible Core Team (@ansible)\nmodule: import_playbook\nshort_description: Import a playbook\ndescription:\n  - Includes a file with a list of plays to be executed.\n  - Files with a list of plays can only be included at the top level.\n  - You cannot use this action inside a play.\nversion_added: "2.4"\noptions:\n  free-form:\n    description:\n      - The name of the imported playbook is specified directly without any other option.\nextends_documentation_fragment:\n  - action_common_attributes\n  - action_common_attributes.conn\n  - action_common_attributes.flow\n  - action_core\n  - action_core.import\nattributes:\n    check_mode:\n        support: full\n    diff_mode:\n        support: none\n    platform:\n        platforms: all\nnotes:\n  - This is a core feature of Ansible, rather than a module, and cannot be overridden like a module.\nseealso:\n- module: ansible.builtin.import_role\n- module: ansible.builtin.import_tasks\n- module: ansible.builtin.include_role\n- module: ansible.builtin.include_tasks\n- ref: playbooks_reuse_includes\n  description: More information related to including and importing playbooks, roles and tasks.\n'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = 'Mapping is required, cannot be type %s'
        dict_0 = {str_1: str_1, str_1: str_1}
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(dict_0)
        bytes_0 = b'\xc1\xecR\x1fSa|\xf6\xb8\xdef\x97\xbb'
        list_0 = [str_1, str_0, generic_bsd_ifconfig_network_1, str_0]
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(dict_0, list_0)
        var_0 = generic_bsd_ifconfig_network_2.detect_type_media(dict_0)
        var_1 = generic_bsd_ifconfig_network_1.get_options(bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'\x044\xa1K\xdf\xb7\x82\x01\x00\x12'
        str_0 = 'Y|}n{F%a'
        int_0 = 52
        list_0 = [bytes_0, int_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0, list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
        set_0 = set()
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0)
        dict_0 = {generic_bsd_ifconfig_network_1: str_0, generic_bsd_ifconfig_network_0: str_0, generic_bsd_ifconfig_network_0: generic_bsd_ifconfig_network_0, bytes_0: bytes_0}
        var_1 = generic_bsd_ifconfig_network_0.parse_media_line(list_0, dict_0, int_0)
        bool_0 = True
        bytes_1 = b''
        var_2 = generic_bsd_ifconfig_network_1.merge_default_interface(bool_0, bytes_1, list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        str_0 = 'm1S0l\rfKJEMBJ}fhi:0'
        bytes_0 = b"\xdc~\xaa\x15\xeafE\x19\x98i\xd6\xb7'\x05\x0e"
        int_0 = 40
        dict_0 = {bytes_0: bytes_0, generic_bsd_ifconfig_network_0: int_0}
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'Orf>yu/=\\\x0bb\x0bwGP?l'
        float_0 = 1432.32337
        tuple_0 = (str_0, float_0)
        list_0 = [tuple_0, str_0]
        int_0 = -1213
        float_1 = -131.45
        list_1 = [float_1]
        dict_0 = {}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_1, dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(list_0, str_0, int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b'0\x08\xda\x8bF\xde\xe3\xfar]\x84\xe8a\xa6\x19\x07c\xc1\x1eT'
        str_0 = 'Y|}n{F%a'
        int_0 = 52
        list_0 = [bytes_0, int_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0, list_0)
        set_0 = set()
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0)
        dict_0 = {generic_bsd_ifconfig_network_1: str_0, generic_bsd_ifconfig_network_0: str_0, generic_bsd_ifconfig_network_0: generic_bsd_ifconfig_network_0, bytes_0: bytes_0}
        bool_0 = True
        var_0 = generic_bsd_ifconfig_network_1.parse_media_line(str_0, dict_0, bool_0)
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, dict_0, int_0)
        var_2 = generic_bsd_ifconfig_network_1.parse_ether_line(str_0, dict_0, int_0)
        dict_1 = {str_0: str_0}
        var_3 = generic_bsd_ifconfig_network_0.detect_type_media(dict_1)
        var_4 = generic_bsd_ifconfig_network_0.get_default_interfaces(generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_20():
    try:
        list_0 = []
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(list_0)
        str_0 = '0/K9^^U_/'
        bytes_0 = b"\x15\xad\xdb'\xc0\xb4\x8b)\xcesWA\x1c\xa0\xeb"
        var_1 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, list_0, bytes_0)
    except BaseException:
        pass