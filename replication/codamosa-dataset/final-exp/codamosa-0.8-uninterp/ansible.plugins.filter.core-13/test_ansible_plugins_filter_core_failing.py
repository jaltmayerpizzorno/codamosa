# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    try:
        list_0 = []
        filter_module_0 = module_0.FilterModule(*list_0)
        var_0 = module_0.to_yaml(filter_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'XAl?ulq9w,'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
        tuple_0 = ()
        float_0 = None
        float_1 = None
        var_0 = module_0.randomize_list(float_0, float_1)
        var_1 = module_0.to_yaml(tuple_0, *list_0)
        var_2 = module_0.regex_escape(str_0)
        var_3 = module_0.regex_search(str_0, str_0, *list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        str_0 = 'dS9KA"M7,6M*QgC'
        dict_0 = {str_0: bool_0}
        var_0 = module_0.to_nice_yaml(bool_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        filter_module_0 = None
        list_0 = []
        var_0 = module_0.to_nice_yaml(list_0)
        var_1 = module_0.regex_escape(bool_0, filter_module_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '%\x0c8 t6,0sfEEeS'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = 'posix_extended'
        str_2 = '0jV2`:!jof |{I!]\tjp'
        dict_1 = {str_1: str_1, str_2: str_2, str_0: dict_0, str_0: list_0}
        var_0 = module_0.to_nice_json(dict_1, str_1)
        list_1 = [dict_0, list_0, dict_0, list_0, list_0, list_0, str_0]
        var_1 = module_0.regex_search(dict_0, list_1, *list_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'b"ccY|B|K'
        var_0 = module_0.comment(str_0)
        str_1 = 'z 368X'
        dict_0 = None
        var_1 = module_0.to_bool(dict_0)
        list_0 = [str_0, str_1, str_0, str_0]
        var_2 = module_0.to_bool(list_0)
        str_2 = 'f-LUe4\x0cX)cgu6s$Wgu'
        bytes_0 = b'\x1bS\xe8'
        var_3 = module_0.subelements(str_2, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        var_0 = module_0.to_datetime(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Kz*9{%[9io+[Cb`'
        var_0 = module_0.strftime(str_0)
        str_1 = '//l?ul9w,'
        list_0 = [str_1, str_1, str_1, str_1, str_1, str_1, str_1, str_1, str_1, str_1, str_1]
        var_1 = module_0.regex_search(str_1, str_1, *list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        str_0 = '?)A'
        var_0 = module_0.strftime(list_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'GmONf\x0bJ*UF^TTy*8+'
        list_0 = None
        var_0 = module_0.quote(list_0)
        var_1 = module_0.path_join(str_0)
        bytes_0 = b'c\xef\xaeAy\x86"k\xe8J<b\xd6'
        list_1 = []
        list_2 = [list_1, str_0, bytes_0]
        var_2 = module_0.combine(*list_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '5\r@j?g"'
        var_0 = module_0.comment(str_0)
        str_1 = 'J2@yBk\x0b0iU\x0c'
        var_1 = module_0.regex_search(str_1, str_1)
        str_2 = '0:m([\x0cFVE'
        bytes_0 = b'*\x92\x93\x86\x1f\xf9\x90\xff\xe0\xce\x19}\x87\xbb/\x19\xb7\xb2\x83'
        var_2 = module_0.regex_findall(str_2, bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'o\\tAwh'
        bytes_0 = b'\xda>\xb9\xdd\x9e\x9d\xf30\x92\x0b\x0b\xce\xfb\xae\xad\x99M\xf6\x190'
        var_0 = module_0.regex_escape(bytes_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = -1962
        set_0 = {int_0, int_0}
        var_0 = module_0.rand(int_0, set_0, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '3#>-'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.rand(str_0, filter_module_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'vV Ymvs\x0c2_\n#Q%0"m'
        int_0 = -4971
        var_0 = module_0.get_hash(int_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        var_0 = module_0.get_hash(bool_0)
        str_0 = '~S'
        bytes_0 = b''
        var_1 = module_0.regex_escape(bytes_0)
        list_0 = [str_0, str_0]
        var_2 = module_0.subelements(list_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = -3561.196934
        str_0 = 'LL{GFZ"#=8EH'
        var_0 = module_0.get_encrypted_password(float_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'Fvakk]w50/%J'
        str_1 = 'q$}95ZYp^9menBo\n&~'
        dict_0 = {str_0: str_0, str_1: str_1}
        var_0 = module_0.to_uuid(str_0, dict_0)
    except BaseException:
        pass

def test_case_18():
    try:
        var_0 = module_0.combine()
        str_0 = '\tij|DqNdVe56h7\\0<'
        var_1 = module_0.to_uuid(str_0)
        bool_0 = True
        bool_1 = None
        var_2 = module_0.to_bool(bool_1)
        var_3 = module_0.to_json(bool_0)
        float_0 = 511.5967
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0}
        var_4 = module_0.get_hash(float_0, set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        tuple_0 = ()
        var_0 = module_0.extract(filter_module_0, tuple_0, filter_module_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '"cnY|B|K'
        var_0 = module_0.comment(str_0)
        set_0 = set()
        bool_0 = True
        list_0 = [set_0, set_0, str_0]
        tuple_0 = None
        var_1 = module_0.do_groupby(bool_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        var_0 = module_0.combine()
        str_0 = '\tj|DqNVe5h7\\0<'
        var_1 = module_0.to_uuid(str_0)
        bool_0 = None
        var_2 = module_0.to_json(bool_0)
        var_3 = module_0.mandatory(bool_0)
        float_0 = 511.5967
        bytes_0 = b'\xb6\xf3'
        list_0 = [var_2, var_2]
        var_4 = module_0.b64encode(list_0)
        set_0 = {bytes_0, bytes_0}
        var_5 = module_0.get_hash(float_0, set_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '5\r4%'
        list_0 = []
        dict_0 = {str_0: str_0, str_0: list_0, str_0: str_0, str_0: list_0, str_0: str_0}
        list_1 = [dict_0, dict_0]
        var_0 = module_0.b64decode(list_0)
        int_0 = -524
        var_1 = module_0.subelements(list_1, str_0, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '~S'
        list_0 = [str_0, str_0]
        var_0 = module_0.subelements(list_0, str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'JUR2@vBk\x0b0iU\x0c'
        list_0 = [str_0, str_0]
        dict_0 = {str_0: list_0, str_0: list_0, str_0: str_0}
        var_0 = module_0.subelements(dict_0, list_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '3#>-'
        filter_module_0 = module_0.FilterModule()
        list_0 = [filter_module_0, str_0, str_0, filter_module_0]
        bool_0 = True
        var_0 = module_0.subelements(list_0, bool_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bytes_0 = b'\x00\xf2\xcc\xf6\xa8y\x96\x9bZ\xbb'
        str_0 = 'J2@yBk\x0b0iU\x0c'
        var_0 = module_0.regex_search(str_0, str_0)
        var_1 = module_0.subelements(bytes_0, str_0)
    except BaseException:
        pass

def test_case_27():
    try:
        bytes_0 = b'PS_hj Q'
        str_0 = 'NUW}<GMIN#c'
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(bytes_0, str_0, str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'JURF22@vB\x0b0U\x0c'
        var_0 = module_0.regex_search(str_0, str_0)
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(str_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'JUR2@vBk\x0b0iU\x0c'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.path_join(dict_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = '^]%jX'
        var_0 = module_0.to_bool(str_0)
        list_0 = [str_0]
        var_1 = module_0.path_join(list_0)
        filter_module_0 = module_0.FilterModule()
        var_2 = module_0.fileglob(filter_module_0)
    except BaseException:
        pass

def test_case_31():
    try:
        filter_module_0 = module_0.FilterModule()
        tuple_0 = None
        var_0 = filter_module_0.filters()
        var_1 = module_0.comment(tuple_0)
    except BaseException:
        pass

def test_case_32():
    try:
        bool_0 = True
        var_0 = module_0.to_bool(bool_0)
        float_0 = 2255.55311
        bytes_0 = b'\xa4'
        var_1 = module_0.mandatory(float_0, bytes_0)
        str_0 = 'nHoA<%V?y5kBXHt9*`'
        var_2 = module_0.dict_to_list_of_dict_key_value_elements(str_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'YZxef'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        dict_0 = {str_0: list_0, str_0: list_0, str_0: list_0}
        list_1 = [dict_0, list_0, str_0]
        var_0 = module_0.combine(*list_1)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'vV Ymvs\x0c2_\n#Q%0"m'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        var_0 = module_0.regex_search(str_0, str_0, *list_0)
    except BaseException:
        pass

def test_case_35():
    try:
        bool_0 = True
        var_0 = module_0.comment(bool_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'pa!+miko_s'
        list_0 = [str_0, str_0]
        var_0 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = "'fx5_N$w"
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.flatten(list_0)
        var_1 = module_0.to_json(str_0)
        dict_0 = {str_0: str_0, str_0: var_1}
        var_2 = module_0.combine(**dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        filter_module_0 = None
        bytes_0 = b'A\xd0\xb5g\x97\xb8\xab'
        str_0 = '\rL(j>3B\x0cH&o(PqX#G5'
        float_0 = -1115.54785
        var_0 = module_0.extract(filter_module_0, bytes_0, str_0, float_0)
    except BaseException:
        pass

def test_case_39():
    try:
        float_0 = 0.3873921938443942
        var_0 = module_0.to_bool(float_0)
        filter_module_0 = module_0.FilterModule()
        str_0 = '$\\\\^WI;IiX=:ubn\x0b rD'
        bytes_0 = b'\x9a\xe3v\xca\xe6\xbf\x85}/\xad\x10\x9a'
        str_1 = '>-3N0PnFeewCj'
        bool_0 = None
        var_1 = module_0.ternary(bytes_0, str_1, bool_0)
        tuple_0 = (str_0,)
        list_0 = [bool_0, str_1, tuple_0, float_0]
        var_2 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = '3#>-'
        list_0 = [str_0]
        var_0 = module_0.combine(*list_0)
        filter_module_0 = module_0.FilterModule()
        var_1 = module_0.rand(str_0, filter_module_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = '3#>-'
        list_0 = [str_0]
        tuple_0 = None
        list_1 = []
        bool_0 = True
        var_0 = module_0.regex_findall(tuple_0, list_1, list_0, bool_0)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = ',DgJG\r>\\,TkPi'
        int_0 = -622
        dict_0 = {}
        var_0 = module_0.rand(str_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = ',DgJG\r>\\,TkPi'
        int_0 = -622
        dict_0 = {str_0: int_0, str_0: str_0}
        var_0 = module_0.rand(str_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_44():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        var_0 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_45():
    try:
        bool_0 = True
        str_0 = 'c@]#(n;4u\tfO('
        set_0 = {bool_0, bool_0}
        tuple_0 = ()
        dict_0 = {}
        tuple_1 = (set_0, str_0, tuple_0, dict_0)
        bytes_0 = b'\xef\xb4\x0e\xcb'
        dict_1 = {}
        var_0 = module_0.rand(tuple_1, bytes_0, dict_1, bool_0)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = '{f/|i\n`$[wPQ+`>'
        var_0 = module_0.from_yaml(str_0)
    except BaseException:
        pass

def test_case_47():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        str_0 = 'f=O0Qczf51WgG\r'
        bytes_0 = b'\xb3Q\xfa\xd5\xbeI\x87\xcc'
        str_1 = 's7Av9a?mV}*)~s2N,'
        var_0 = module_0.from_yaml_all(str_1)
        list_1 = [list_0, bytes_0]
        str_2 = '_~3xx9; \nQ^<a\x0bt/vZ~b'
        str_3 = '# \\(/tmp/.*installed on.*\\)'
        dict_0 = {str_0: list_0, str_2: str_0, str_2: list_0, str_3: list_0}
        var_1 = module_0.subelements(bytes_0, list_1, dict_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'pHnosix_etended'
        str_1 = '$5\rH%'
        list_0 = [str_1, str_0, str_1]
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
    except BaseException:
        pass

def test_case_49():
    try:
        bytes_0 = b'\xad\xea\x1d'
        var_0 = module_0.get_encrypted_password(bytes_0)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = '5\r\x0c4%'
        list_0 = []
        dict_0 = {str_0: str_0, str_0: list_0, str_0: list_0, str_0: str_0, str_0: list_0}
        list_1 = [dict_0, dict_0, dict_0, dict_0, str_0]
        int_0 = -545
        var_0 = module_0.subelements(list_1, str_0, int_0)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = '5\r4%'
        list_0 = []
        dict_0 = {str_0: str_0, str_0: list_0, str_0: str_0, str_0: list_0, str_0: str_0}
        list_1 = [dict_0, dict_0]
        int_0 = -524
        var_0 = module_0.subelements(list_1, str_0, int_0)
    except BaseException:
        pass

def test_case_52():
    try:
        bytes_0 = b'a'
        dict_0 = {bytes_0: bytes_0}
        str_0 = 'pyDL p)\r'
        str_1 = 'he\x0cNmpv6p!W'
        list_0 = [str_0]
        var_0 = module_0.randomize_list(str_1, list_0)
        dict_1 = {str_0: dict_0, str_0: dict_0}
        int_0 = -1378
        var_1 = module_0.quote(int_0)
        var_2 = module_0.regex_replace(dict_0, dict_1)
    except BaseException:
        pass

def test_case_53():
    try:
        str_0 = 'GmONf\x0bJ*UF^TTy*8+'
        var_0 = module_0.path_join(str_0)
        bytes_0 = b'c\xef\xaeAy\x86"k\xe8J<b\xd6'
        list_0 = []
        list_1 = [list_0, str_0, bytes_0]
        var_1 = module_0.combine(*list_1)
    except BaseException:
        pass

def test_case_54():
    try:
        bytes_0 = b"\x04\xf0'm\xd2}s\xa1\x85\x10b\re\xb5\xa8\xe2Ao\xa6\xf8"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        var_0 = module_0.get_hash(list_0)
        list_1 = []
        int_0 = 1086
        set_0 = {bytes_0, int_0, bytes_0}
        var_1 = module_0.ternary(bytes_0, list_1, int_0, set_0)
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(*list_1, **dict_0)
        bool_0 = None
        var_2 = module_0.to_uuid(filter_module_0, bool_0)
    except BaseException:
        pass

def test_case_55():
    try:
        list_0 = []
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
        float_0 = -2105.0
        var_1 = module_0.flatten(float_0)
    except BaseException:
        pass

def test_case_56():
    try:
        str_0 = '5\r\x0c4%'
        list_0 = []
        dict_0 = {str_0: str_0, str_0: list_0, str_0: list_0, str_0: str_0, str_0: list_0}
        list_1 = [dict_0, dict_0, dict_0, dict_0, str_0]
        bytes_0 = b'\xbf\x92'
        bool_0 = False
        var_0 = module_0.ternary(str_0, bytes_0, bool_0)
        str_1 = None
        var_1 = module_0.b64decode(str_1)
        var_2 = module_0.combine(*list_0)
        str_2 = '4Tn\x0c\r\rqu~\r>scF'
        var_3 = module_0.subelements(list_1, str_2)
    except BaseException:
        pass

def test_case_57():
    try:
        str_0 = 'infiniband'
        filter_module_0 = None
        dict_0 = None
        tuple_0 = ()
        var_0 = module_0.rand(str_0, filter_module_0, dict_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_58():
    try:
        str_0 = '5\r\x0c4%'
        list_0 = []
        var_0 = module_0.regex_escape(str_0)
        dict_0 = {str_0: str_0, str_0: list_0, str_0: list_0, str_0: str_0, str_0: list_0}
        list_1 = [dict_0, dict_0, dict_0, dict_0, str_0]
        bool_0 = True
        var_1 = module_0.combine()
        str_1 = None
        var_2 = module_0.b64decode(str_1)
        var_3 = module_0.combine(*list_0)
        str_2 = '"$[D:})I3j'
        var_4 = module_0.subelements(list_1, str_2, bool_0)
    except BaseException:
        pass

def test_case_59():
    try:
        str_0 = 'o\\tAwh'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
        var_0 = module_0.flatten(list_0)
        str_1 = 'A\x0b@\nUIo6Q'
        dict_0 = {str_0: list_0, str_0: list_0, str_1: list_0, str_0: str_0, str_0: str_0}
        var_1 = module_0.combine()
        complex_0 = None
        var_2 = module_0.randomize_list(complex_0)
        bytes_0 = b'>\x8ae\x8a\xd6\x17x'
        var_3 = module_0.from_yaml(var_2)
        str_2 = '@.H\x0c\rHnxu$`AQ1<%qy'
        str_3 = 'AamJN*+c'
        dict_1 = {str_2: dict_0, str_2: var_3, str_3: str_0}
        var_4 = module_0.regex_escape(bytes_0)
        list_1 = [str_3, list_0, list_0, list_0]
        tuple_0 = ()
        var_5 = module_0.extract(dict_1, complex_0, tuple_0, list_1)
    except BaseException:
        pass

def test_case_60():
    try:
        float_0 = 0.001
        var_0 = module_0.regex_replace()
        var_1 = module_0.to_bool(float_0)
        bytes_0 = b'\xbf\x92'
        bool_0 = True
        set_0 = None
        list_0 = [bytes_0, var_1, bytes_0]
        filter_module_0 = None
        list_1 = [bytes_0, filter_module_0, bool_0]
        tuple_0 = (set_0,)
        tuple_1 = (list_1, tuple_0, filter_module_0)
        str_0 = ']DS@N6#sq'
        var_2 = module_0.ternary(set_0, list_0, tuple_1, str_0)
    except BaseException:
        pass

def test_case_61():
    try:
        bytes_0 = None
        bool_0 = False
        set_0 = set()
        list_0 = [set_0, bool_0]
        var_0 = module_0.rand(bytes_0, bool_0, set_0, list_0)
    except BaseException:
        pass

def test_case_62():
    try:
        str_0 = '52\x0c4%'
        list_0 = [str_0]
        dict_0 = {str_0: str_0, str_0: list_0, str_0: list_0, str_0: str_0, str_0: str_0, str_0: list_0}
        list_1 = [dict_0, dict_0, dict_0, dict_0, str_0]
        int_0 = -573
        var_0 = module_0.subelements(list_1, str_0, int_0)
    except BaseException:
        pass

def test_case_63():
    try:
        str_0 = 'foo'
        str_1 = 'foo'
        var_0 = module_0.mandatory(str_1)
        str_2 = 'Hello World\nHello World'
        int_0 = 2174
        list_0 = [str_2, int_0, str_0]
        str_3 = '1R!nSOP8S'
        var_1 = module_0.regex_replace(int_0, list_0, list_0, str_3)
    except BaseException:
        pass

def test_case_64():
    try:
        str_0 = '\\1\\1'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
        var_0 = module_0.regex_search(str_0, str_0, *list_0)
    except BaseException:
        pass

def test_case_65():
    try:
        str_0 = '[a-z]'
        str_1 = 'python'
        var_0 = module_0.regex_escape(str_0, str_1)
        str_2 = 'posix_basic'
        var_1 = module_0.regex_escape(str_0, str_2)
        str_3 = '[a-z]'
        str_4 = 'posix_extended'
        var_2 = module_0.regex_escape(str_3, str_4)
    except BaseException:
        pass