# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        bytes_0 = b'sDD\xf4\xc5\xab\xc5\x97"mg\xd6\xf7\xed\x12\x03'
        tuple_0 = (bytes_0,)
        set_0 = {bytes_0, bytes_0, bytes_0}
        str_0 = '|$'
        str_1 = '8X.\x0cVxZU'
        var_0 = module_0.append_param(tuple_0, set_0, str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        bytes_0 = b'&\x87s.\x8a~\xa2s\xa7x\xa6\xb4\xd8'
        str_0 = "K\x0c'kalk3SVp51@4'nx"
        tuple_0 = ()
        var_0 = module_0.append_match_flag(list_0, str_0, bytes_0, tuple_0)
        str_1 = 'p+4+1W5<=*tK'
        var_1 = module_0.append_tcp_flags(list_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        dict_0 = {set_0: set_0, set_0: set_0, set_0: set_0}
        bytes_0 = b''
        tuple_0 = (dict_0, bytes_0)
        var_0 = module_0.append_csv(dict_0, tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\\4sMG7X^\nrqt$1=\r9['
        float_0 = -1388.0
        float_1 = -2196.9
        var_0 = module_0.append_match(str_0, float_0, float_1)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = None
        bytes_0 = b'\x12\xa7\x8d\x8b'
        str_0 = 'D5=z|FPv\n328th'
        var_0 = module_0.append_jump(float_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        str_0 = 'd'
        tuple_0 = None
        var_0 = module_0.append_wait(bool_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xbc\xfc\x84^\x0f\x95\xaa\xc8r^\x1f\x02\xd5\xbd0\xa3'
        var_0 = module_0.construct_rule(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'a'
        str_1 = 'table'
        str_2 = 'chain'
        str_3 = {str_1: str_1, str_2: str_2, str_2: str_2}
        var_0 = module_0.set_chain_policy(str_0, str_0, str_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        list_0 = [str_0, str_0, str_0, str_0]
        list_1 = [list_0, str_0]
        tuple_0 = ()
        float_0 = 245.59
        var_0 = module_0.insert_rule(list_1, tuple_0, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'filter'
        str_1 = 'INPUT'
        str_2 = 'tcp'
        str_3 = 'ACCEPT'
        var_0 = dict(table=str_0, chain=str_1, protocol=str_2, destination=str_3, jump=str_3)
        str_4 = 'iptables'
        str_5 = 'module'
        var_1 = module_0.remove_rule(str_4, str_5, var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = {str_0: str_0, str_1: str_0}
        str_3 = 'ix'
        var_0 = None
        var_1 = module_0.flush_table(str_3, var_0, str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        var_0 = None
        str_0 = 'chain'
        str_1 = 'table'
        str_2 = 'INPUT'
        str_3 = 'filter'
        str_4 = {str_0: str_2, str_1: str_3}
        var_1 = module_0.get_chain_policy(var_0, var_0, str_4)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'h`WR ^#Z(aP'
        int_0 = 115
        var_0 = module_0.get_iptables_version(str_0, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        str_0 = 'b'
        bytes_0 = b'\x869f\xe8\xb0\xfaTy\x19\xb1\x96\xefF\x05:\xfc\x03'
        bytes_1 = b'T\x02\x8b\x023,\xcc`\xabO\xe4\xf9'
        int_0 = -705
        float_0 = -405.922
        var_0 = module_0.append_match_flag(bytes_1, int_0, float_0, bytes_0)
        set_0 = {bytes_0}
        bool_0 = False
        float_1 = -1000.6
        var_1 = module_0.append_match(set_0, bool_0, float_1)
        bytes_2 = b'oq\x10?\xe2\xb1f9zr'
        var_2 = module_0.push_arguments(dict_0, str_0, bytes_2)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = {}
        str_0 = 'b'
        float_0 = None
        set_0 = None
        var_0 = module_0.append_jump(float_0, set_0, str_0)
        bytes_0 = b'T\x02\x8b\x023,\xcc`\xabO\xe4\xf9'
        int_0 = -705
        float_1 = -405.922
        var_1 = module_0.append_match_flag(bytes_0, int_0, float_1, bytes_0)
        bytes_1 = b'oq\x10?\xe2\xb1f9zr'
        var_2 = module_0.push_arguments(dict_0, str_0, bytes_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = ''
        bytes_0 = b'\xa9E}\xdc\xe4'
        bool_0 = False
        set_0 = {bool_0}
        var_0 = module_0.append_tcp_flags(bytes_0, bool_0, set_0)
        str_1 = 'table'
        str_2 = 'chain'
        str_3 = 'INPUT'
        float_0 = -2902.0
        ansible_module_0 = None
        dict_0 = {str_3: str_0, str_0: str_0, str_2: str_0}
        bytes_1 = b'\xbb\xc7\xdbF:+Z\x1e\xd7:K~\x1c\xe5]\x84'
        tuple_0 = (dict_0, bytes_1)
        var_1 = module_0.append_match_flag(str_0, ansible_module_0, float_0, tuple_0)
        set_1 = set()
        var_2 = module_0.append_match_flag(str_1, str_2, float_0, set_1)
        str_4 = {str_1: str_2, str_2: str_3, str_0: str_0}
        var_3 = module_0.set_chain_policy(str_0, str_0, str_4)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'\x869f\xe8\xb0\xfaTy\x19\xb1\x96\xefF\x05:\xfc\x03'
        bytes_1 = b'T\x02\x8b\x023,\xcc`\xabO\xe4\xf9'
        int_0 = -705
        float_0 = -405.922
        var_0 = module_0.append_match_flag(bytes_1, int_0, float_0, bytes_0)
        var_1 = module_0.check_present(int_0, int_0, bytes_1)
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b'sDD\xf4\xc5\xab\xc5\x97"mg\xd6\xf7\xed\x12\x03'
        tuple_0 = (bytes_0,)
        set_0 = {bytes_0, bytes_0, bytes_0}
        str_0 = '8X.\x0cVxZU'
        str_1 = '&\t\x0bE z_rf'
        int_0 = 420
        dict_0 = {bytes_0: int_0, str_0: str_1}
        var_0 = module_0.append_rule(dict_0, set_0, tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'Incorrect type for success_msg, expected a string or list and got %s'
        str_1 = '!g5\njT\tkLz#s?^G'
        str_2 = 'td-[ae-\x0b2.r?&WpRJE-'
        str_3 = 'R(y(A_ "Owj%QH'
        var_0 = module_0.append_param(str_0, str_1, str_2, str_3)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'policy'
        str_3 = {str_0: str_0, str_1: str_1, str_2: str_1}
        var_0 = module_0.set_chain_policy(str_0, str_0, str_3)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'tesi5t-chain'
        str_1 = '1.1.1.1'
        str_2 = 'ACCEPT'
        str_3 = "H\tJG'+SkJS;z>"
        var_0 = dict(chain=str_0, protocol=str_0, source=str_1, destination=str_0, jump=str_2, table=str_0, ip_version=str_3)
        str_4 = 'iptables'
        str_5 = '-I'
        bool_0 = False
        var_1 = module_0.push_arguments(str_4, str_5, var_0, bool_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'filter'
        str_1 = '1'
        str_2 = 'tcp'
        str_3 = '80'
        str_4 = 'ACCEPT'
        str_5 = 'accept new SSH connections'
        var_0 = dict(table=str_0, chain=str_2, rule_num=str_1, protocol=str_2, destination_port=str_3, jump=str_4, comment=str_5)
        str_6 = '-I'
        var_1 = module_0.push_arguments(str_4, str_6, var_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'filter'
        str_1 = 'INPUT'
        str_2 = 'localhost'
        var_0 = dict(table=str_0, chain=str_1, protocol=str_0, destination=str_2, jump=str_2)
        str_3 = 'iptables'
        str_4 = '-D'
        var_1 = module_0.push_arguments(str_3, str_4, var_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '/sbin/iptables'
        str_1 = 'filter'
        str_2 = 'INPUT'
        str_3 = ''
        str_4 = '80'
        str_5 = 'ACCEPT'
        str_6 = 'accept new SSH connections'
        var_0 = dict(table=str_1, chain=str_2, rule_num=str_3, protocol=str_2, destination_port=str_4, jump=str_5, comment=str_6)
        str_7 = '-I'
        var_1 = module_0.push_arguments(str_0, str_7, var_0)
    except BaseException:
        pass