# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import ansible.template as module_1

def test_case_0():
    try:
        bool_0 = True
        str_0 = '?'
        list_0 = [str_0, bool_0]
        list_1 = [list_0, list_0, bool_0, str_0]
        dict_0 = {str_0: bool_0}
        var_0 = module_0.to_yaml(bool_0, *list_1, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 4215
        str_0 = 'SC\r~kD1!5k2w#j'
        var_0 = module_0.regex_search(int_0, str_0)
        list_0 = [str_0]
        list_1 = [var_0]
        dict_0 = {}
        var_1 = module_0.to_json(list_0, *list_1, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'qi0'
        var_0 = module_0.from_yaml_all(str_0)
        set_0 = None
        str_1 = "\n7('\\8="
        str_2 = '[!gV9n*8f:!\\XK]XO\r'
        str_3 = 'Z$w)r/'
        str_4 = 'failed to retrieve selinux context'
        dict_0 = {str_2: str_0, str_2: str_3, str_4: str_1}
        var_1 = module_0.to_nice_json(set_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '*'
        var_0 = module_0.fileglob(str_0)
        str_1 = 'AB$q0sCU\nF3yse[v=00'
        var_1 = module_0.to_datetime(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'x4428315.0'
        var_0 = module_0.strftime(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        str_0 = ''
        var_0 = module_0.regex_search(bool_0, str_0)
        str_1 = None
        var_1 = module_0.strftime(str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = None
        var_0 = module_0.fileglob(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -3519.99
        set_0 = None
        var_0 = module_0.mandatory(set_0)
        list_0 = [float_0, float_0, float_0]
        var_1 = module_0.regex_findall(float_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        var_0 = module_0.mandatory(bool_0)
        str_0 = '0'
        str_1 = 'B;O(w|p{ \th6}m#'
        bytes_0 = b'\x17'
        var_1 = module_0.fileglob(bytes_0)
        str_2 = '{0}:'
        str_3 = '#/Rk\n'
        dict_0 = {str_0: str_0, str_1: var_0, str_2: str_0, str_3: str_0}
        str_4 = 'mX\r'
        list_0 = [dict_0, str_2]
        var_2 = module_0.regex_findall(dict_0, str_4, list_0)
        var_3 = module_0.combine(**dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 4215
        str_0 = 'a{uK8\x0bgWA\t)rs\r1'
        list_0 = [str_0, int_0, int_0]
        bytes_0 = b'\xd1\xbf\xb3\x00\x0e\xffz\xf6\xbfW\x0e\xe8\x00\x14\xcb'
        var_0 = module_0.regex_search(bytes_0, list_0, *list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'foo.*'
        var_0 = module_0.regex_escape(str_0)
        var_1 = module_0.regex_escape(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'AB$q0sCU\nF3yse[v=00'
        bool_0 = True
        var_0 = module_0.from_yaml_all(bool_0)
        set_0 = {str_0, str_0, str_0, str_0}
        var_1 = module_0.regex_replace(set_0)
        list_0 = [str_0, str_0, str_0, str_0, var_1]
        var_2 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        tuple_0 = ()
        bool_0 = True
        set_0 = {bool_0}
        str_0 = '&9\\H\tGK55P)9X'
        str_1 = 'posix_extended'
        var_0 = module_0.rand(set_0, str_0, dict_0, str_1, tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = -552
        tuple_0 = (int_0,)
        float_0 = 1960.790041
        set_0 = {float_0, int_0, tuple_0}
        var_0 = module_0.rand(tuple_0, set_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ''
        int_0 = 257
        dict_0 = {str_0: str_0, str_0: int_0}
        list_0 = [str_0, dict_0, str_0, dict_0]
        var_0 = module_0.get_hash(dict_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'QT19376cv8.12345j0N'
        list_0 = [str_0, str_0, str_0]
        int_0 = 1966
        var_0 = module_0.get_hash(int_0)
        str_1 = '/cd~bu*,aA5R\\p\txd'
        var_1 = module_0.flatten(list_0, str_1)
        var_2 = module_0.strftime(str_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '4Rp,WtM'
        list_0 = [str_0, str_0]
        var_0 = module_0.to_bool(list_0)
        bool_0 = False
        var_1 = module_0.get_encrypted_password(list_0, bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '*'
        var_0 = module_0.fileglob(str_0)
        list_0 = [str_0, var_0]
        float_0 = 1.5
        var_1 = module_0.to_uuid(list_0, float_0)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = 932.7926
        dict_0 = {float_0: float_0}
        var_0 = module_0.comment(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        set_0 = set()
        int_0 = 1457
        dict_0 = {int_0: int_0}
        var_0 = module_0.extract(set_0, int_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 1576
        str_0 = 'y:@'
        var_0 = module_0.extract(int_0, str_0, int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 2004
        list_0 = [int_0]
        dict_0 = {}
        tuple_0 = (list_0, dict_0)
        bytes_0 = None
        var_0 = module_0.ternary(tuple_0, tuple_0, int_0, bytes_0)
        float_0 = 1273.3213
        var_1 = module_0.randomize_list(float_0, float_0)
        dict_1 = {}
        var_2 = module_0.dict_to_list_of_dict_key_value_elements(dict_1, dict_1)
        str_0 = '--download-path'
        list_1 = []
        filter_module_0 = module_0.FilterModule(*list_1)
        var_3 = module_0.do_groupby(bytes_0, filter_module_0, str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = -5397
        var_0 = module_0.b64decode(int_0)
        bool_0 = False
        str_0 = ''
        list_0 = [str_0, bool_0]
        var_1 = module_0.subelements(list_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'y:@'
        float_0 = 401.985
        list_0 = [str_0, str_0]
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(float_0, list_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '$%E!='
        dict_0 = None
        var_0 = module_0.to_uuid(str_0, dict_0)
    except BaseException:
        pass

def test_case_25():
    try:
        float_0 = 1960.790041
        list_0 = None
        dict_0 = {}
        var_0 = module_0.rand(list_0, dict_0, float_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bool_0 = False
        str_0 = ''
        list_0 = [str_0, bool_0]
        var_0 = module_0.subelements(list_0, str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'x0"_1'
        bool_0 = True
        var_0 = module_0.subelements(str_0, bool_0)
    except BaseException:
        pass

def test_case_28():
    try:
        float_0 = 1960.790041
        dict_0 = None
        int_0 = None
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, int_0, float_0)
    except BaseException:
        pass

def test_case_29():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        var_0 = module_0.path_join(list_0)
    except BaseException:
        pass

def test_case_30():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = '*'
        var_0 = filter_module_0.filters()
        bytes_0 = b''
        var_1 = filter_module_0.filters()
        var_2 = module_0.ternary(filter_module_0, str_0, bytes_0)
        var_3 = filter_module_0.filters()
        var_4 = filter_module_0.filters()
        set_0 = set()
        list_0 = [filter_module_0, set_0, var_0]
        var_5 = module_0.ternary(bytes_0, set_0, bytes_0, list_0)
        var_6 = filter_module_0.filters()
        var_7 = module_0.b64encode(set_0)
        dict_0 = {str_0: var_2}
        var_8 = module_0.path_join(dict_0)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = '/etc'
        filter_module_0 = None
        dict_0 = {str_0: filter_module_0}
        complex_0 = None
        var_0 = module_0.to_nice_yaml(complex_0, **dict_0)
    except BaseException:
        pass

def test_case_32():
    try:
        list_0 = []
        float_0 = 1.0
        var_0 = module_0.to_bool(float_0)
        filter_module_0 = module_0.FilterModule(*list_0)
        var_1 = filter_module_0.filters()
        var_2 = filter_module_0.filters()
        list_1 = None
        str_0 = ''
        var_3 = filter_module_0.filters()
        var_4 = module_0.to_uuid(str_0)
        float_1 = 1487.2513
        var_5 = module_0.regex_search(list_1, float_1)
    except BaseException:
        pass

def test_case_33():
    try:
        int_0 = 1900
        bytes_0 = b''
        float_0 = -1689.383327
        var_0 = module_0.from_yaml(float_0)
        bool_0 = None
        list_0 = [float_0]
        var_1 = module_0.ternary(bool_0, list_0, list_0, float_0)
        var_2 = module_0.regex_replace(int_0)
        filter_module_0 = module_0.FilterModule()
        var_3 = module_0.dict_to_list_of_dict_key_value_elements(bytes_0, float_0)
    except BaseException:
        pass

def test_case_34():
    try:
        bool_0 = False
        str_0 = None
        str_1 = ': Uid differs$'
        dict_0 = None
        dict_1 = {str_0: bool_0, str_1: dict_0}
        var_0 = module_0.flatten(dict_1)
        str_2 = ''
        list_0 = [str_2, bool_0]
        var_1 = module_0.subelements(list_0, str_2)
    except BaseException:
        pass

def test_case_35():
    try:
        bytes_0 = b'lM\xf8\xf4g+\xf7 \x13\xd9k\x15\x94\x96\xbe'
        int_0 = 1443
        bytes_1 = None
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        list_0 = [bytes_0]
        bytes_2 = b'\xadV\xa7\xba\xf1F\xe1'
        var_1 = module_0.to_nice_yaml(bytes_2)
        var_2 = module_0.from_yaml_all(int_0)
        var_3 = module_0.rand(bytes_0, int_0, bytes_1, list_0)
    except BaseException:
        pass

def test_case_36():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = '((vzgI`HF'
        var_0 = module_0.path_join(str_0)
        var_1 = module_0.b64decode(filter_module_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = "C1}>9-P'r"
        list_0 = None
        float_0 = -105.07
        list_1 = [float_0, str_0, list_0]
        str_1 = ' +refs/heads/%s:refs/remotes/%s/%s'
        var_0 = module_0.from_yaml(str_1)
        var_1 = module_0.randomize_list(list_1)
        dict_0 = {str_0: list_0, str_0: str_0}
        var_2 = module_0.regex_search(list_0, list_0, *list_1, **dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        list_0 = []
        str_0 = ''
        var_0 = module_0.to_uuid(str_0)
        bytes_0 = b'&\xb7\x1d\xe0A\x05\xc4\xcf\x08\x80\xc2'
        bool_0 = True
        var_1 = module_0.mandatory(bool_0)
        var_2 = module_0.combine(*list_0)
        dict_0 = {}
        int_0 = 420
        str_1 = "1'4x\t%\nHh%"
        var_3 = module_0.rand(dict_0, int_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = '*!'
        list_0 = [str_0]
        list_1 = [list_0]
        var_0 = module_0.combine(*list_1)
        dict_0 = {}
        bytes_0 = None
        var_1 = module_0.subelements(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_40():
    try:
        int_0 = None
        dict_0 = None
        str_0 = '^inn\rua'
        int_1 = -2721
        var_0 = module_0.regex_findall(int_0, dict_0, str_0, int_1)
    except BaseException:
        pass

def test_case_41():
    try:
        filter_module_0 = None
        int_0 = 5985
        float_0 = 1559.80658
        var_0 = module_0.rand(int_0, float_0, filter_module_0)
    except BaseException:
        pass

def test_case_42():
    try:
        int_0 = -552
        tuple_0 = (int_0,)
        filter_module_0 = module_0.FilterModule()
        float_0 = 1960.790041
        set_0 = {float_0, int_0, tuple_0}
        var_0 = module_0.to_bool(tuple_0)
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(tuple_0, set_0)
    except BaseException:
        pass

def test_case_43():
    try:
        bool_0 = False
        var_0 = module_0.mandatory(bool_0)
        str_0 = '0'
        str_1 = 'B;O(w|p{ \th6}m#'
        str_2 = '{0}:'
        str_3 = '#/Rk\n'
        dict_0 = {str_0: str_0, str_1: var_0, str_2: str_0, str_3: str_0}
        var_1 = module_0.combine(**dict_0)
    except BaseException:
        pass

def test_case_44():
    try:
        int_0 = 4215
        str_0 = 'a{uK8\x0bgWA\t)rs\r1'
        list_0 = [str_0, int_0, int_0]
        list_1 = []
        var_0 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_45():
    try:
        int_0 = 2101
        str_0 = '\\hM\\*n2LFiHMmvg'
        var_0 = module_0.mandatory(str_0)
        str_1 = 'posix_extended'
        str_2 = 'jZ0X%\rVk1+_4<<'
        dict_0 = {str_1: str_1, str_2: int_0}
        tuple_0 = (dict_0,)
        var_1 = module_0.get_encrypted_password(tuple_0)
    except BaseException:
        pass

def test_case_46():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = '*'
        var_0 = filter_module_0.filters()
        bytes_0 = b''
        var_1 = filter_module_0.filters()
        var_2 = filter_module_0.filters()
        str_1 = None
        var_3 = module_0.ternary(filter_module_0, str_1, bytes_0)
        var_4 = filter_module_0.filters()
        set_0 = set()
        var_5 = filter_module_0.filters()
        tuple_0 = ()
        var_6 = module_0.b64encode(set_0)
        str_2 = "'G{o6BbXXecjf#Y{"
        str_3 = 'S)HL?O\x0bZ[>'
        dict_0 = {str_2: str_0, str_3: tuple_0}
        int_0 = 340
        str_4 = '\rF~4-e]'
        dict_1 = {str_2: set_0, str_4: dict_0}
        var_7 = module_0.rand(dict_0, int_0, dict_1)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = '.PZDm\x0b*>\x0c'
        dict_0 = {str_0: str_0}
        var_0 = module_0.mandatory(dict_0)
        int_0 = 86400
        var_1 = module_0.get_hash(int_0)
        str_1 = 'posix_extended'
        var_2 = module_0.from_yaml_all(str_1)
        list_0 = []
        list_1 = [var_1]
        var_3 = module_0.subelements(list_0, list_1, str_1)
        list_2 = []
        bytes_0 = None
        var_4 = module_0.to_bool(bytes_0)
        var_5 = module_0.strftime(list_2)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = '*'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_49():
    try:
        dict_0 = {}
        float_0 = 1273.3213
        var_0 = module_0.randomize_list(float_0, float_0)
        set_0 = {var_0, float_0, float_0}
        dict_1 = {}
        var_1 = module_0.dict_to_list_of_dict_key_value_elements(dict_1, dict_1)
        var_2 = module_0.combine()
        var_3 = module_0.subelements(dict_0, set_0)
    except BaseException:
        pass

def test_case_50():
    try:
        bool_0 = False
        str_0 = ''
        list_0 = [str_0, bool_0]
        list_1 = [list_0, bool_0, bool_0]
        var_0 = module_0.combine(*list_1)
    except BaseException:
        pass

def test_case_51():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        tuple_0 = ()
        str_0 = 'Op^Qci=|7)tBnd74KD1'
        str_1 = '%s="%s"\n'
        dict_1 = {str_0: str_0, str_1: dict_0}
        bytes_0 = b'\xaa\x02\x9a\xe1R\x85\x1b\xe9'
        float_0 = 168.85563
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_1, bytes_0, float_0)
        var_1 = module_0.to_uuid(list_0, tuple_0)
    except BaseException:
        pass

def test_case_52():
    try:
        int_0 = 2004
        list_0 = [int_0]
        dict_0 = {}
        tuple_0 = (list_0, dict_0)
        bool_0 = True
        dict_1 = {int_0: bool_0, bool_0: tuple_0}
        var_0 = module_0.ternary(bool_0, tuple_0, dict_1)
        bytes_0 = None
        var_1 = module_0.ternary(tuple_0, tuple_0, int_0, bytes_0)
        float_0 = 1273.3213
        var_2 = module_0.randomize_list(float_0, float_0)
        set_0 = {var_2, float_0, float_0}
        dict_2 = {}
        var_3 = module_0.dict_to_list_of_dict_key_value_elements(dict_2, dict_2)
        float_1 = 3470.5410630038864
        list_1 = []
        filter_module_0 = module_0.FilterModule(*list_1)
        var_4 = module_0.combine()
        var_5 = module_0.regex_escape(dict_0)
        var_6 = module_0.extract(set_0, bytes_0, float_1, list_1)
    except BaseException:
        pass

def test_case_53():
    try:
        tuple_0 = ()
        str_0 = 'y'
        str_1 = 'XM&|LiCS/Q\t2lCa'
        list_0 = [tuple_0, str_1]
        list_1 = [tuple_0, str_0, list_0, tuple_0]
        bool_0 = True
        var_0 = module_0.randomize_list(bool_0)
        var_1 = module_0.combine(*list_1)
    except BaseException:
        pass

def test_case_54():
    try:
        bytes_0 = b'p\xb2\xc4z\x0b\xc7\xbb'
        set_0 = {bytes_0, bytes_0, bytes_0}
        tuple_0 = (bytes_0,)
        dict_0 = {}
        list_0 = [tuple_0, set_0, bytes_0, tuple_0]
        list_1 = [list_0]
        int_0 = None
        var_0 = module_0.flatten(list_1, int_0)
        var_1 = module_0.rand(tuple_0, dict_0, list_0)
    except BaseException:
        pass

def test_case_55():
    try:
        tuple_0 = ()
        var_0 = module_0.combine()
        set_0 = {tuple_0, tuple_0, tuple_0}
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(tuple_0, set_0)
        str_0 = 'fjo'
        list_0 = [str_0, str_0, str_0, str_0, str_0]
        bytes_0 = b'\x94\xb4\x14\x9b|Z\xcb\xf8'
        var_2 = module_0.b64encode(bytes_0)
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        dict_1 = {str_0: filter_module_0, str_0: str_0}
        var_3 = module_0.comment(list_0, **dict_1)
    except BaseException:
        pass

def test_case_56():
    try:
        list_0 = []
        var_0 = module_0.mandatory(list_0)
        str_0 = ".BUy'@|I'Y\x0b8q|AhW0z"
        list_1 = []
        int_0 = 3723
        var_1 = module_0.regex_replace(str_0, list_1, list_1, int_0)
    except BaseException:
        pass

def test_case_57():
    try:
        ansible_undefined_0 = module_1.AnsibleUndefined()
        var_0 = module_0.mandatory(ansible_undefined_0)
    except BaseException:
        pass

def test_case_58():
    try:
        str_0 = 'error'
        ansible_undefined_0 = module_1.AnsibleUndefined()
        var_0 = module_0.mandatory(ansible_undefined_0, str_0)
    except BaseException:
        pass