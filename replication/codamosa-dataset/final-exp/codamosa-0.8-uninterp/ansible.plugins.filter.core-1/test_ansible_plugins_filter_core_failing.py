# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import datetime as module_1
import builtins as module_2

def test_case_0():
    try:
        str_0 = 'qu*.OK_D^y/Q?;e*Gu5['
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.to_nice_yaml(str_0, *list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'whfDD).'
        list_0 = [bytes_0, bytes_0, bytes_0]
        list_1 = []
        var_0 = module_0.to_nice_json(bytes_0, list_0, *list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 184
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.to_datetime(int_0, filter_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'pUfILQ2$f;A q4^'
        time_0 = module_1.time()
        var_0 = module_0.strftime(str_0, time_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        bytes_0 = b'\xad~\x83+I\xbb\xcd\x86\xbe8\x95\x86\xb8N\x96\x92n~\xa4'
        filter_module_0 = module_0.FilterModule()
        bytes_1 = None
        tuple_0 = (filter_module_0, bytes_1)
        var_0 = module_0.regex_findall(list_0, bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 100.0
        list_0 = [float_0]
        set_0 = None
        var_0 = module_0.regex_escape(list_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        var_0 = module_0.b64decode(dict_0)
        str_0 = '\t^d$J=11'
        list_0 = [dict_0, var_0, str_0]
        list_1 = [str_0]
        tuple_0 = (list_0, list_1)
        var_1 = module_0.from_yaml(tuple_0)
        var_2 = module_0.combine(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '#'
        dict_0 = {str_0: str_0, str_0: str_0}
        dict_1 = {str_0: dict_0}
        var_0 = module_0.from_yaml_all(dict_1)
        var_1 = module_0.subelements(dict_1, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '}5-74O6<;'
        bool_0 = True
        var_0 = module_0.mandatory(bool_0)
        var_1 = module_0.flatten(str_0)
        str_1 = 'k%>f"_ac6?y'
        var_2 = module_0.from_yaml_all(str_1)
        var_3 = module_0.comment(str_1)
        time_0 = module_1.time()
        dict_0 = {}
        list_0 = [time_0, var_1, dict_0, str_0]
        var_4 = module_0.to_yaml(time_0, *list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        int_0 = -4688
        var_0 = module_0.rand(int_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'pUfILQ2$f;A q4^'
        str_1 = '[ ^\x0cQ'
        var_0 = module_0.randomize_list(str_1)
        time_0 = module_1.time()
        var_1 = module_0.strftime(str_0, time_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1375
        str_0 = 'posix_basic'
        dict_0 = {str_0: int_0, str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = ()
        var_0 = module_0.get_encrypted_password(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        str_0 = '\t^d$J=11'
        list_0 = [dict_0, str_0, str_0]
        var_0 = module_0.combine(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -152.4149
        list_0 = []
        dict_0 = {}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, dict_0)
        str_0 = '|((Z0^pTT'
        dict_1 = {str_0: float_0, str_0: float_0}
        var_1 = module_0.combine(*list_0, **dict_1)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 967.3528
        bool_0 = None
        list_0 = []
        var_0 = module_0.extract(float_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 401
        var_0 = module_0.randomize_list(int_0)
        bool_0 = False
        float_0 = -25.151
        bytes_0 = b'\x99\x0f\xefX\x94,\x95\x0f\tw\xf0k'
        var_1 = module_0.do_groupby(bool_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '|@A7J*+@8a#\\'
        var_0 = module_0.b64encode(str_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 32700
        bytes_0 = None
        list_0 = [int_0, bytes_0]
        list_1 = []
        var_0 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = None
        float_0 = 1086.3028911359613
        var_0 = module_0.subelements(bytes_0, float_0)
    except BaseException:
        pass

def test_case_19():
    try:
        filter_module_0 = None
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(filter_module_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = ''
        set_0 = {str_0, str_0, str_0, str_0}
        bytes_0 = b'k\xe1k\x06\xd4v#\r\x8d\xaf'
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(set_0, bytes_0)
    except BaseException:
        pass

def test_case_21():
    try:
        bytes_0 = b'!\x0f'
        var_0 = module_0.path_join(bytes_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '2Kr$K>\tzC\t('
        str_1 = '#'
        str_2 = '4l}'
        dict_0 = {str_2: str_2}
        var_0 = module_0.comment(str_1, **dict_0)
        str_3 = '$\x0b\r<iBDi{W{xc'
        var_1 = module_0.path_join(str_3)
        list_0 = [str_0, str_0]
        int_0 = 1237
        list_1 = [str_0]
        var_2 = module_0.regex_search(list_0, int_0, *list_1)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'arch-release'
        str_1 = 'E'
        dict_0 = {str_0: str_0, str_1: str_1}
        list_0 = [dict_0]
        var_0 = module_0.to_bool(list_0)
        str_2 = 'pUfILQ2$f;A q4^'
        time_0 = module_1.time()
        var_1 = module_0.strftime(str_2, time_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bytes_0 = b'q\x87\xe2\x953\xe0\xca\x04\x8cj\x13\xcar'
        str_0 = 'Contrasenya'
        dict_0 = {str_0: bytes_0, str_0: bytes_0}
        var_0 = module_0.to_yaml(bytes_0, **dict_0)
    except BaseException:
        pass

def test_case_25():
    try:
        bool_0 = False
        int_0 = -830
        float_0 = -2959.6004
        var_0 = module_0.to_yaml(float_0)
        bytes_0 = None
        list_0 = [int_0, bool_0, bool_0, bytes_0, bytes_0]
        list_1 = [int_0, int_0]
        var_1 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '\x0c<?>'
        var_0 = module_0.to_yaml(str_0)
        int_0 = 1
        var_1 = module_0.to_bool(int_0)
        filter_module_0 = module_0.FilterModule()
        var_2 = module_0.combine()
        str_1 = None
        dict_0 = None
        str_2 = 'd^0/as\ta'
        var_3 = module_0.from_yaml(str_2)
        var_4 = module_0.randomize_list(str_1, dict_0)
        float_0 = 416.12241741772954
        var_5 = module_0.dict_to_list_of_dict_key_value_elements(float_0, filter_module_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = '1]Fm^5Aw9Lf=+`sZ|af'
        list_0 = []
        int_0 = 1237
        list_1 = [str_0]
        var_0 = module_0.regex_search(list_0, int_0, *list_1)
    except BaseException:
        pass

def test_case_28():
    try:
        dict_0 = {}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0)
        filter_module_0 = module_0.FilterModule()
        str_0 = 'e~*7SX\rzDs)o+'
        list_0 = [filter_module_0, filter_module_0, filter_module_0, var_0, str_0]
        var_1 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_29():
    try:
        list_0 = []
        filter_module_0 = module_0.FilterModule(*list_0)
        list_1 = [filter_module_0, list_0]
        set_0 = None
        dict_0 = {}
        var_0 = module_0.to_nice_yaml(set_0, *list_0, **dict_0)
        int_0 = 2114
        list_2 = [list_1, list_0, list_1, int_0]
        var_1 = module_0.to_bool(list_2)
        str_0 = ' --no-tty --batch --with-colons --fixed-list-mode -'
        float_0 = -2200.25196
        var_2 = module_0.to_uuid(str_0, float_0)
    except BaseException:
        pass

def test_case_30():
    try:
        float_0 = 479.01876363970206
        str_0 = 'Failed to bring service out of %s status.'
        var_0 = module_0.to_uuid(str_0, float_0)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = '(?P<spam>(.*)) and (?P<eggs>(.*))'
        var_0 = module_0.regex_search(str_0, str_0)
        str_1 = ''
        time_0 = module_1.time()
        list_0 = [var_0, str_1]
        set_0 = set()
        var_1 = module_0.extract(time_0, list_0, set_0, set_0)
    except BaseException:
        pass

def test_case_32():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.to_uuid(filter_module_0)
        var_1 = filter_module_0.filters()
        var_2 = filter_module_0.filters()
        int_0 = -1637
        dict_0 = {}
        list_0 = []
        float_0 = 0.2
        var_3 = module_0.ternary(list_0, float_0, list_0, float_0)
        float_1 = None
        list_1 = [dict_0]
        var_4 = module_0.extract(float_1, int_0, dict_0, list_1)
    except BaseException:
        pass

def test_case_33():
    try:
        list_0 = []
        str_0 = '.Z`'
        str_1 = 'python'
        dict_0 = {}
        tuple_0 = (str_1, str_0, list_0, dict_0)
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(tuple_0)
    except BaseException:
        pass

def test_case_34():
    try:
        bool_0 = False
        int_0 = -830
        bytes_0 = None
        list_0 = [int_0, bool_0, bool_0, bytes_0, bytes_0]
        list_1 = [int_0, int_0]
        var_0 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = '}\nR+-hAQ 0mn'
        list_0 = [str_0, str_0]
        str_1 = 'python'
        bool_0 = False
        var_0 = module_0.subelements(list_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = '#'
        str_1 = '4l}'
        dict_0 = {str_0: str_0, str_0: str_0}
        dict_1 = {str_0: dict_0}
        list_0 = None
        var_0 = module_0.subelements(dict_1, str_1, list_0)
    except BaseException:
        pass

def test_case_37():
    try:
        bool_0 = True
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.mandatory(filter_module_0)
        int_0 = -816
        str_0 = 'e~*7SX\rzDs)o+'
        dict_0 = {str_0: str_0, str_0: bool_0}
        var_1 = module_0.subelements(dict_0, int_0)
    except BaseException:
        pass

def test_case_38():
    try:
        dict_0 = None
        dict_1 = {dict_0: dict_0}
        var_0 = module_0.regex_escape(dict_1)
        set_0 = set()
        bool_0 = None
        var_1 = module_0.rand(set_0, bool_0)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = ''
        list_0 = [str_0, str_0, str_0, str_0]
        bytes_0 = b'\x9a\xf7\x16\xc1'
        var_0 = module_0.rand(str_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_40():
    try:
        float_0 = -152.4149
        dict_0 = {float_0: float_0}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, dict_0)
    except BaseException:
        pass

def test_case_41():
    try:
        bool_0 = False
        var_0 = module_0.to_bool(bool_0)
        bool_1 = False
        list_0 = [bool_1, var_0]
        filter_module_0 = module_0.FilterModule(*list_0)
    except BaseException:
        pass

def test_case_42():
    try:
        float_0 = None
        str_0 = 'pUfILQ2$f;A q4^'
        list_0 = [float_0, float_0, float_0, str_0]
        var_0 = module_0.flatten(list_0, str_0)
        str_1 = '[ ^\x0cQ'
        var_1 = module_0.randomize_list(str_1)
        time_0 = module_1.time()
        var_2 = module_0.strftime(str_0, time_0)
    except BaseException:
        pass

def test_case_43():
    try:
        list_0 = []
        bytes_0 = b'I8\xf9\x01\xec\xa4R`\xbe\xc9\xb7\x14f\xa8\x12\x1bl'
        var_0 = module_0.rand(list_0, list_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_44():
    try:
        filter_module_0 = module_0.FilterModule()
        bool_0 = False
        var_0 = module_0.rand(filter_module_0, bool_0)
    except BaseException:
        pass

def test_case_45():
    try:
        str_0 = 'ucQxZo(H(OEt\x0c'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.path_join(list_0)
        filter_module_0 = module_0.FilterModule()
        str_1 = '!cj|8D`"35 3RBFZZ{h('
        dict_0 = {str_0: str_1, str_0: str_0}
        list_1 = None
        float_0 = 1855.90022
        bytes_0 = b'\x9fR\xfe'
        var_1 = filter_module_0.filters()
        var_2 = module_0.extract(dict_0, list_1, float_0, bytes_0)
    except BaseException:
        pass

def test_case_46():
    try:
        dict_0 = {}
        filter_module_0 = None
        var_0 = module_0.quote(filter_module_0)
        var_1 = module_0.dict_to_list_of_dict_key_value_elements(dict_0)
        filter_module_1 = module_0.FilterModule()
        str_0 = '.R0V?q.ck%p,_k3'
        list_0 = [filter_module_1, filter_module_1, filter_module_1, var_1, str_0]
        var_2 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = None
        dict_0 = {str_0: str_0}
        var_0 = module_0.b64decode(dict_0)
        var_1 = module_0.combine()
        bool_0 = False
        bytes_0 = b'\xd7\x99|\xdc\x0e\x17\xf0{\x8daM'
        int_0 = -4344
        set_0 = {bool_0}
        var_2 = module_0.rand(bytes_0, int_0, set_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = '1_f9_B~:zX\r'
        filter_module_0 = None
        var_0 = module_0.get_encrypted_password(str_0, filter_module_0)
    except BaseException:
        pass

def test_case_49():
    try:
        bool_0 = False
        int_0 = -801
        bytes_0 = None
        complex_0 = None
        list_0 = [bool_0, int_0, complex_0, complex_0]
        list_1 = [list_0]
        str_0 = 'B^#/}TXjw6)'
        dict_0 = {str_0: str_0, str_0: list_0, str_0: str_0, str_0: bool_0}
        var_0 = module_0.randomize_list(list_1, dict_0)
        list_2 = [int_0, bool_0, bool_0, bytes_0, bytes_0]
        var_1 = module_0.subelements(list_2, list_0)
    except BaseException:
        pass

def test_case_50():
    try:
        bytes_0 = b''
        float_0 = None
        var_0 = module_0.to_uuid(bytes_0, float_0)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = 'vsUMg7&!O@y'
        time_0 = module_1.time()
        var_0 = module_0.get_hash(str_0, time_0)
    except BaseException:
        pass

def test_case_52():
    try:
        dict_0 = {}
        list_0 = []
        int_0 = 3
        dict_1 = {}
        var_0 = module_0.rand(list_0, int_0, dict_1, int_0)
        float_0 = -1385.28
        var_1 = module_0.regex_search(dict_0, float_0)
    except BaseException:
        pass

def test_case_53():
    try:
        float_0 = -1854.252
        str_0 = '\x0c((+-Us7)bt'
        list_0 = [float_0, str_0]
        set_0 = None
        dict_0 = None
        tuple_0 = (dict_0,)
        var_0 = module_0.rand(float_0, str_0, list_0, set_0, tuple_0)
    except BaseException:
        pass

def test_case_54():
    try:
        bytes_0 = b'\xaf\xef\xe2xv\xacv\xb9j'
        var_0 = module_0.regex_replace()
        list_0 = [bytes_0, bytes_0, bytes_0]
        list_1 = []
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(list_1)
        str_0 = 'M0y\x0b7T(1{g9Bp"V%s'
        dict_0 = {str_0: bytes_0, str_0: list_0, str_0: list_0, str_0: str_0, str_0: list_0}
        var_2 = module_0.randomize_list(list_0, dict_0)
        str_1 = 'ak}5-74O6<'
        bool_0 = True
        var_3 = module_0.mandatory(bool_0)
        var_4 = module_0.flatten(str_1)
        var_5 = module_0.regex_search(bool_0, str_1)
        var_6 = module_0.comment(str_1)
        dict_1 = module_2.dict()
        var_7 = module_0.b64encode(list_0)
        filter_module_0 = module_0.FilterModule()
        var_8 = module_0.to_yaml(filter_module_0)
    except BaseException:
        pass

def test_case_55():
    try:
        bool_0 = False
        list_0 = [bool_0]
        var_0 = module_0.combine(*list_0)
        bool_1 = True
        int_0 = -829
        bytes_0 = None
        list_1 = [list_0, int_0, bool_1, bytes_0, bytes_0]
        list_2 = [int_0, int_0]
        var_1 = module_0.subelements(list_1, list_2)
    except BaseException:
        pass

def test_case_56():
    try:
        bool_0 = True
        str_0 = None
        str_1 = 'N&~-WtY;1OJHw/]\n~T8g'
        bool_1 = True
        int_0 = -645
        var_0 = module_0.ternary(str_0, str_1, bool_1, int_0)
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        dict_0 = {bool_0: bool_0, bool_0: list_0}
        var_1 = module_0.get_hash(list_0, dict_0)
    except BaseException:
        pass

def test_case_57():
    try:
        str_0 = '1]Fm^5Aw9Lf=+`sZ|af'
        str_1 = 'JP&\t'
        str_2 = 'Pl>8en!%&;b46;\\xdBke'
        var_0 = module_0.regex_search(str_1, str_2)
        list_0 = []
        int_0 = 1260
        list_1 = [str_0]
        var_1 = module_0.regex_search(list_0, int_0, *list_1)
    except BaseException:
        pass

def test_case_58():
    try:
        str_0 = '/etc/passwd'
        var_0 = module_0.fileglob(str_0)
        var_1 = module_0.combine()
        dict_0 = {}
        var_2 = module_0.from_yaml(dict_0)
        str_1 = ','
        str_2 = 'oi='
        dict_1 = {str_2: var_0, str_0: str_1, str_2: var_1}
        str_3 = 'i_Y<C1-jI3H>K\tR'
        float_0 = 1521.0
        var_3 = module_0.subelements(dict_1, str_3, float_0)
    except BaseException:
        pass

def test_case_59():
    try:
        bool_0 = False
        str_0 = 'fposix_extended'
        var_0 = module_0.to_bool(str_0)
        var_1 = module_0.randomize_list(bool_0, bool_0)
        bool_1 = False
        bytes_0 = None
        list_0 = [bytes_0, bool_1, bool_1]
        tuple_0 = (bool_1, bytes_0, list_0)
        var_2 = module_0.mandatory(tuple_0)
        bool_2 = True
        list_1 = [list_0, bool_2]
        list_2 = []
        var_3 = module_0.subelements(list_1, list_2)
    except BaseException:
        pass

def test_case_60():
    try:
        str_0 = 'HM#F'
        set_0 = {str_0, str_0, str_0}
        dict_0 = {}
        tuple_0 = (str_0, set_0, dict_0)
        bytes_0 = b'a$\x1b\xff\xd4\xa9\x0e\x04\xe4+'
        var_0 = module_0.get_hash(bytes_0)
        float_0 = -403.168
        var_1 = module_0.randomize_list(tuple_0, float_0)
        bool_0 = False
        var_2 = module_0.randomize_list(bool_0, bool_0)
        filter_module_0 = module_0.FilterModule(**dict_0)
        bool_1 = False
        var_3 = module_0.to_uuid(filter_module_0, bool_1)
    except BaseException:
        pass

def test_case_61():
    try:
        bool_0 = True
        int_0 = -829
        filter_module_0 = None
        list_0 = [filter_module_0]
        list_1 = [list_0, bool_0, int_0]
        bytes_0 = b'\x0f\x93\xd8U\xd2\xce\x82\xbf\xdf\x02\xb6\x97'
        list_2 = [bytes_0, filter_module_0, list_1]
        str_0 = 'P(Qiz3'
        var_0 = module_0.regex_findall(bytes_0, filter_module_0, list_2, str_0)
    except BaseException:
        pass

def test_case_62():
    try:
        str_0 = 'foo/bar'
        str_1 = 'posix_basic'
        var_0 = module_0.regex_escape(str_0, str_1)
        var_1 = module_0.regex_escape(str_0, str_0)
    except BaseException:
        pass

def test_case_63():
    try:
        str_0 = '\\ # $ ^ . [ ] + ( ) ? * { } |'
        var_0 = module_0.regex_escape(str_0)
        str_1 = 'foo/bar'
        str_2 = 'posix_basic'
        var_1 = module_0.regex_escape(str_1, str_2)
        str_3 = 'posix_extended'
        var_2 = module_0.regex_escape(str_1, str_3)
    except BaseException:
        pass

def test_case_64():
    try:
        str_0 = ',\\N\x0c\x0bvdV/pP1EPg"}\n"'
        var_0 = module_0.regex_escape(str_0)
        dict_0 = {}
        filter_module_0 = module_0.FilterModule()
        list_0 = [dict_0, dict_0, dict_0]
        var_1 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_65():
    try:
        int_0 = -2460
        var_0 = module_0.mandatory(int_0)
        str_0 = 'foo'
        var_1 = module_0.regex_search(str_0, str_0)
        list_0 = None
        var_2 = module_0.randomize_list(list_0)
        str_1 = '\\1'
        int_1 = 1624
        list_1 = [str_1]
        var_3 = module_0.regex_search(list_0, int_1, *list_1)
    except BaseException:
        pass