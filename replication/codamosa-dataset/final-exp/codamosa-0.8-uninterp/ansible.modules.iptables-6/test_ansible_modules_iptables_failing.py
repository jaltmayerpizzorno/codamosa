# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        int_0 = -919
        str_0 = 'QX"tOeU\'1'
        var_0 = module_0.append_param(int_0, str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1259
        set_0 = {int_0, int_0}
        str_0 = '&|2\x0bU"'
        var_0 = module_0.append_tcp_flags(set_0, int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0bEj*mxS'
        set_0 = {str_0}
        list_0 = [set_0, str_0, set_0, set_0]
        tuple_0 = (list_0,)
        bool_0 = False
        float_0 = -3165.0292
        var_0 = module_0.append_match_flag(tuple_0, bool_0, list_0, float_0)
        str_1 = "v'/}Z}F0uY`]jP"
        var_1 = module_0.flush_table(tuple_0, set_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        bytes_0 = b'\xd9yg\xd3\x8b$'
        var_0 = module_0.append_match_flag(bytes_0, bool_0, bytes_0, bytes_0)
        dict_0 = {}
        str_0 = '=/)au:Db^jLI&'
        bytes_1 = b'\xd4\xb5\x04h\xa2\xfb\\JjS\xb0X\xc4\xf0\x9b\x13'
        var_1 = module_0.append_csv(dict_0, str_0, bytes_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '@2hW1_u8}.'
        bool_0 = None
        var_0 = module_0.append_match(str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '?6R'
        float_0 = 2064.46
        dict_0 = {str_0: float_0}
        var_0 = module_0.append_jump(str_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'B\x7f\x87R\xbfy=4\x80&\xef\x94\xbf\xa4\xc6\x981'
        list_0 = [bytes_0]
        tuple_0 = (list_0,)
        tuple_1 = (tuple_0,)
        str_0 = 'yNmvM~\\V;PcWd8J:BAG'
        var_0 = module_0.append_wait(tuple_1, str_0, tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '-I'
        int_0 = 7
        var_0 = dict(table=str_0, chain=str_0, protocol=str_0, destination_port=str_0, jump=str_0, rule_num=int_0)
        var_1 = module_0.push_arguments(var_0, str_0, var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'INPUT'
        str_1 = 'iptables'
        var_0 = module_0.get_chain_policy(str_1, str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -161
        str_0 = '?lz<'
        str_1 = 'IkFy`Ib=@!j5,v S\r\\'
        var_0 = module_0.append_tcp_flags(int_0, str_0, str_1)
        list_0 = []
        str_2 = '(L/,HUy0n/'
        str_3 = '\\AT&'
        var_1 = module_0.check_present(list_0, str_2, str_3)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ''
        var_0 = ()
        int_0 = 0
        var_1 = (int_0, str_0, int_0)
        var_2 = lambda *args, **kwargs: var_1
        var_3 = dict(run_command=var_2)
        var_4 = type(str_0, var_0, var_3)
        str_1 = 'iptables'
        str_2 = 'INPUT'
        str_3 = 'filter'
        var_5 = dict(chain=str_2, table=str_3)
        var_6 = module_0.append_rule(str_1, var_4, var_5)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 3077
        str_0 = 'UAs%&'
        list_0 = []
        var_0 = module_0.insert_rule(int_0, str_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\x0bEj*mxS'
        set_0 = {str_0}
        list_0 = [set_0, str_0, set_0, set_0]
        tuple_0 = (list_0,)
        str_1 = "v'/}Z}F0uY`]jP"
        var_0 = module_0.flush_table(tuple_0, set_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = True
        int_0 = 254
        var_0 = module_0.get_iptables_version(bool_0, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\xd0\xd3\xd0'
        bool_0 = True
        bytes_1 = b'\xd9yg\xd3\x8b$'
        var_0 = module_0.append_match_flag(bytes_0, bool_0, bytes_1, bytes_0)
        dict_0 = {}
        str_0 = '=/)au:Db^jLI&'
        bytes_2 = b'\xd4\xb5\x04h\xa2\xfb\\JjS\xb0X\xc4\xf0\x9b\x13'
        bool_1 = False
        set_0 = set()
        var_1 = module_0.append_csv(bool_1, bool_1, set_0)
        var_2 = module_0.append_csv(dict_0, str_0, bytes_2)
    except BaseException:
        pass

def test_case_15():
    try:
        tuple_0 = ()
        set_0 = set()
        var_0 = module_0.append_match(tuple_0, set_0, set_0)
        list_0 = None
        int_0 = -1981
        var_1 = module_0.append_csv(list_0, set_0, int_0)
        list_1 = [set_0]
        bool_0 = True
        var_2 = module_0.append_csv(set_0, list_1, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        str_0 = '?0UC'
        int_0 = -898
        str_1 = 'A[_DL'
        tuple_0 = (str_0, int_0, str_1)
        str_2 = '-jXy\r0D"l%8K'
        var_0 = module_0.append_wait(tuple_0, bool_0, str_2)
        str_3 = '\nB\rQ6Z9RQLvR\nE8oZi1o'
        var_1 = module_0.check_present(dict_0, str_3, dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = -1875
        set_0 = {int_0}
        dict_0 = {}
        str_0 = '2b'
        var_0 = module_0.remove_rule(set_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'chain'
        str_1 = 'policy'
        str_2 = 'table'
        str_3 = 'ip_version'
        str_4 = 'INPUT'
        str_5 = 'DROP'
        str_6 = 'filter'
        str_7 = 'ipv4'
        str_8 = {str_0: str_4, str_1: str_5, str_2: str_6, str_3: str_7}
        str_9 = 'iptables'
        var_0 = None
        var_1 = module_0.set_chain_policy(str_9, var_0, str_8)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'iptables'
        str_1 = '-I'
        str_2 = 'INPUT'
        str_3 = '\n- name: raw result of running date command"\n  debug:\n    msg: "{{ lookup(\'pipe\', \'date\') }}"\n\n- name: Always use quote filter to make sure your variables are safe to use with shell\n  debug:\n    msg: "{{ lookup(\'pipe\', \'getent passwd \' + myuser | quote ) }}"\n'
        int_0 = None
        list_0 = []
        var_0 = module_0.append_match_flag(str_3, str_0, str_0, list_0)
        str_4 = 'tcp'
        var_1 = dict(table=str_1, chain=str_2, protocol=str_4, destination_port=str_1, jump=str_1, rule_num=int_0)
        var_2 = module_0.push_arguments(str_0, str_1, var_1)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = -3186
        tuple_0 = None
        bytes_0 = b'\xa1-\x1fX\xa7\xdc'
        bytes_1 = None
        tuple_1 = (tuple_0, bytes_0, bytes_1)
        bool_0 = False
        list_0 = [tuple_0, tuple_1, bool_0]
        bytes_2 = b'\xb3r\x1fu\xa6\x95R\xbfH[f'
        var_0 = module_0.append_param(int_0, tuple_1, list_0, bytes_2)
    except BaseException:
        pass

def test_case_21():
    try:
        set_0 = set()
        float_0 = -1580.55
        dict_0 = {}
        tuple_0 = (set_0, float_0, dict_0)
        list_0 = [tuple_0, tuple_0, set_0]
        str_0 = '4!);4lA;8\x0bM/iime*h'
        var_0 = module_0.append_param(list_0, str_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'filt'
        var_0 = dict(table=str_0, chain=str_0)
        var_1 = module_0.get_chain_policy(str_0, str_0, var_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'tcp'
        str_1 = '80'
        str_2 = 'ACCEPT'
        str_3 = '5'
        str_4 = 'ipv4'
        var_0 = dict(protocol=str_0, destination_port=str_1, jump=str_2, comment=str_2, wait=str_3, ip_version=str_4)
        var_1 = module_0.construct_rule(var_0)
    except BaseException:
        pass