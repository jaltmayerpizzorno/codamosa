# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import ansible.template as module_1

def test_case_0():
    try:
        str_0 = 'T'
        list_0 = []
        var_0 = module_0.to_nice_yaml(str_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ')R~d`5B'
        str_1 = 'OpenStack Nova'
        var_0 = module_0.to_nice_json(str_1)
        set_0 = {str_0, str_0, str_0, str_0}
        float_0 = 3137.0397
        var_1 = module_0.mandatory(set_0, float_0)
        var_2 = module_0.strftime(str_0)
        str_2 = 'KhXKBRUNf'
        list_0 = [str_2]
        var_3 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'F@Q\\\n<PbjsV]Iq.K{d='
        var_0 = module_0.to_datetime(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'~\xb8\x13\x1a\x15\xa8'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        var_0 = module_0.strftime(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'PL'
        float_0 = -634.8971
        var_0 = module_0.quote(float_0)
        list_0 = [str_0]
        var_1 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        var_0 = module_0.quote(tuple_0)
        int_0 = 1
        var_1 = module_0.mandatory(int_0)
        filter_module_0 = module_0.FilterModule()
        var_2 = module_0.randomize_list(filter_module_0)
        dict_0 = {filter_module_0: var_1, var_2: filter_module_0, var_2: filter_module_0, filter_module_0: var_1, filter_module_0: filter_module_0}
        var_3 = module_0.to_yaml(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xfb\xde\xa9t\x87\xff)\x84\xc0\x13T'
        set_0 = {bytes_0, bytes_0}
        var_0 = module_0.regex_findall(bytes_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        bool_0 = True
        var_0 = module_0.regex_findall(dict_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '8<P]Rep'
        var_0 = module_0.mandatory(str_0)
        str_1 = 'plugin_load_context'
        str_2 = ' }ovKIAd-{"4<'
        str_3 = 'F3OHZ{i\trRf="ycps'
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_3: str_2}
        float_0 = 389.807
        tuple_0 = (float_0,)
        var_1 = module_0.ternary(dict_0, tuple_0, str_3)
        str_4 = 'PL'
        list_0 = [str_4]
        var_2 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        bool_0 = True
        var_0 = module_0.regex_escape(list_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        filter_module_0 = module_0.FilterModule()
        list_0 = [filter_module_0, filter_module_0, filter_module_0]
        var_0 = module_0.regex_escape(list_0)
        str_0 = 'KhXKBRUNf'
        list_1 = [str_0]
        var_1 = module_0.subelements(list_1, list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        set_0 = None
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.rand(set_0, filter_module_0)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.get_hash(list_0, filter_module_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -210.6835
        bytes_0 = b'\x1f\x06\x83\xd0:Q\xb0\xe3e\x9b\x98hk\xce'
        var_0 = module_0.get_encrypted_password(float_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        var_0 = module_0.combine()
        str_0 = 'PL'
        list_0 = [str_0]
        var_1 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'\x9e\x86/\x9a1\xa2y\xe5\xb0V\x1eZZ\xb5\x8d\xb4\xd3y-'
        list_0 = [bytes_0]
        str_0 = '\n        Get the information items from the lsb_release command output.\n\n        Returns:\n            A dictionary containing all information items.\n        '
        dict_0 = {str_0: list_0}
        var_0 = module_0.combine(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "1CYW?'Crs%dq\t\x0b8r\t"
        list_0 = [str_0, str_0]
        set_0 = set()
        var_0 = module_0.extract(str_0, list_0, list_0, set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = -2514.8
        bool_0 = False
        var_0 = module_0.extract(float_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '%YT,f'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = '21kX4\\'
        dict_0 = {str_1: list_0, str_0: str_0, str_0: list_0, str_1: str_0}
        var_0 = module_0.comment(str_0, **dict_0)
        filter_module_0 = module_0.FilterModule()
        int_0 = -6
        set_0 = None
        bytes_0 = b'\xfd&\\\x0e\xeb\x1b\xa6J\x01\xc2\x88\x04h#8\xdb]\xaa'
        var_1 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, set_0, bytes_0)
        var_2 = module_0.flatten(list_0)
        dict_1 = None
        list_1 = [int_0, filter_module_0, dict_1, str_0]
        bytes_1 = b'\x16\xdbL\xe4\xeeXo\x90As\xec\x7f\xd3J'
        float_0 = -330.0
        var_3 = module_0.extract(bytes_1, float_0, set_0, list_1)
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b'\xd4\xf6`\x94a\xbdC\xf6\x15\x15\x90\xb8;\xbb2\xb9N'
        list_0 = [bytes_0, bytes_0]
        float_0 = 1066.386377
        var_0 = module_0.do_groupby(bytes_0, list_0, float_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = None
        int_0 = -964
        var_0 = module_0.b64encode(int_0)
        list_0 = [str_0, str_0, str_0, str_0, str_0]
        var_1 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = "K\x0cqkXZ0kK'6"
        set_0 = {str_0, str_0, str_0, str_0}
        var_0 = module_0.b64decode(set_0)
        str_1 = '?#,'
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        var_1 = filter_module_0.filters()
        list_0 = [str_1, str_1, str_1, str_1]
        var_2 = module_0.extract(str_0, str_1, list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'lhXKB.UNf'
        list_0 = [str_0]
        var_0 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_23():
    try:
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b'\xb7M\xa3\xc6a\x06'
        var_0 = module_0.subelements(filter_module_0, bytes_0)
    except BaseException:
        pass

def test_case_24():
    try:
        float_0 = -795.8
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(float_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '%rT,f'
        list_0 = [str_0, str_0]
        str_1 = 'Xk4'
        dict_0 = {str_1: list_0, str_0: str_0, str_0: list_0, str_1: str_0}
        var_0 = module_0.comment(str_0, **dict_0)
        tuple_0 = ()
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(tuple_0)
        filter_module_0 = module_0.FilterModule()
        var_2 = module_0.subelements(list_0, list_0)
    except BaseException:
        pass

def test_case_26():
    try:
        int_0 = 69
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(int_0, int_0)
    except BaseException:
        pass

def test_case_27():
    try:
        list_0 = []
        var_0 = module_0.path_join(list_0)
    except BaseException:
        pass

def test_case_28():
    try:
        int_0 = 384
        var_0 = module_0.path_join(int_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = "K\x0cqkXZ0kK'6"
        str_1 = '?#,'
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        var_0 = filter_module_0.filters()
        list_0 = [str_1, str_1, str_1, str_1]
        var_1 = module_0.extract(str_0, str_1, list_0)
    except BaseException:
        pass

def test_case_30():
    try:
        list_0 = None
        list_1 = [list_0, list_0, list_0, list_0]
        filter_module_0 = module_0.FilterModule()
        int_0 = -1273
        tuple_0 = (list_1, filter_module_0, int_0)
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(tuple_0)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'lhXKB.UNf'
        list_0 = [str_0, str_0]
        bool_0 = False
        var_0 = module_0.subelements(list_0, bool_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = '6@'
        list_0 = [str_0, str_0, str_0]
        float_0 = -1847.4
        dict_0 = {}
        var_0 = module_0.regex_search(list_0, float_0, *list_0, **dict_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = "BWeYbkXX'\r-S<GJb3ATE"
        bool_0 = None
        filter_module_0 = module_0.FilterModule()
        dict_0 = {str_0: filter_module_0}
        var_0 = module_0.regex_escape(dict_0)
        tuple_0 = (str_0,)
        bytes_0 = b'oW\xfd\x01K\xbcm'
        var_1 = module_0.ternary(bool_0, tuple_0, bytes_0)
        int_0 = 604800
        int_1 = 752
        var_2 = module_0.extract(dict_0, int_0, int_1)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'J^zb*7\x0b%5\x0bj'
        var_0 = module_0.from_yaml_all(str_0)
        list_0 = None
        bytes_0 = b'7*\xf8\xf4q\xbe7-\x02\xbd'
        int_0 = -730
        tuple_0 = (int_0,)
        int_1 = 200
        str_1 = 'h).'
        var_1 = module_0.from_yaml_all(str_1)
        var_2 = module_0.ternary(list_0, bytes_0, tuple_0, int_1)
    except BaseException:
        pass

def test_case_35():
    try:
        int_0 = 86
        list_0 = [int_0]
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.randomize_list(list_0, filter_module_0)
        str_0 = '}\x0b'
        var_1 = module_0.strftime(str_0)
        str_1 = 'lhXKB.OU'
        list_1 = [str_1]
        var_2 = module_0.subelements(list_1, list_1)
    except BaseException:
        pass

def test_case_36():
    try:
        bool_0 = None
        var_0 = module_0.to_uuid(bool_0)
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b'\xdb\x03}v\xe5\xcb!\x872'
        dict_0 = {}
        var_1 = module_0.rand(filter_module_0, bytes_0, dict_0)
        str_0 = 'Dl.)Rk[1Niw^..ml:C'
        dict_1 = {str_0: bytes_0}
        tuple_0 = ()
        var_2 = module_0.to_uuid(dict_1, tuple_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = 'Hello'
        var_0 = module_0.regex_search(str_0, str_0)
        tuple_0 = ()
        int_0 = 1773
        var_1 = module_0.rand(tuple_0, tuple_0, int_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'Iq;~b&LK)7D2T\tPR[\x0b!'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0]
        int_0 = 1706
        var_0 = module_0.subelements(dict_0, list_0, int_0)
    except BaseException:
        pass

def test_case_39():
    try:
        bool_0 = None
        var_0 = module_0.to_uuid(bool_0)
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b'\xdb\x03\xb6}v\xe5\x02!2'
        var_1 = module_0.b64encode(bytes_0)
        float_0 = -72.51
        var_2 = module_0.get_encrypted_password(float_0)
    except BaseException:
        pass

def test_case_40():
    try:
        bytes_0 = None
        var_0 = module_0.to_bool(bytes_0)
        dict_0 = {}
        str_0 = ']YAJ'
        int_0 = 4294967295
        dict_1 = {var_0: int_0}
        dict_2 = {str_0: dict_0, str_0: int_0, str_0: dict_1, str_0: int_0}
        var_1 = module_0.to_nice_yaml(dict_0, **dict_2)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'python'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = 'hexdigest'
        var_0 = module_0.randomize_list(str_0)
        int_0 = 92
        filter_module_0 = module_0.FilterModule()
        list_0 = [var_0, filter_module_0, str_0, str_0]
        filter_module_1 = module_0.FilterModule()
        list_1 = [list_0, str_0, int_0]
        var_1 = module_0.combine(*list_1)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = '#'
        var_0 = module_0.from_yaml(str_0)
        list_0 = []
        filter_module_0 = module_0.FilterModule()
        str_1 = 'DQRZI|}\'?%63Z\n"G'
        var_1 = module_0.subelements(list_0, filter_module_0, str_1)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = '%YT,f'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = '21kX4\\'
        dict_0 = {str_1: list_0, str_0: str_0, str_0: list_0, str_1: str_0}
        var_0 = module_0.comment(str_0, **dict_0)
        filter_module_0 = module_0.FilterModule()
        int_0 = -6
        set_0 = None
        bytes_0 = b'\xfd&\\\x0e\xeb\x1b\xa6J\x01\xc2\x88\x04h#8\xdb]\xaa'
        var_1 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, set_0, bytes_0)
        var_2 = module_0.flatten(list_0)
        dict_1 = {var_0: filter_module_0, var_0: set_0, str_0: int_0, str_1: list_0}
        var_3 = module_0.regex_search(dict_1, list_0, *list_0, **dict_0)
    except BaseException:
        pass

def test_case_45():
    try:
        complex_0 = None
        str_0 = 'Failed to log to syslog (%s). To proceed anyway, disable syslog logging by setting no_target_syslog to True in your Ansible config.'
        str_1 = 'k5fLTi)4Tj1y'
        dict_0 = {str_0: str_0, str_1: str_1}
        var_0 = module_0.to_bool(dict_0)
        var_1 = module_0.comment(complex_0)
    except BaseException:
        pass

def test_case_46():
    try:
        var_0 = module_0.regex_replace()
        str_0 = '$08\\Q'
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        int_0 = 5826
        var_1 = module_0.rand(filter_module_0, int_0, str_0, filter_module_0)
    except BaseException:
        pass

def test_case_47():
    try:
        bool_0 = True
        bytes_0 = b'\x998\xf9.\x13L\xa2'
        var_0 = module_0.quote(bytes_0)
        bool_1 = False
        var_1 = module_0.regex_replace(bool_1)
        var_2 = module_0.regex_replace(bool_0)
        var_3 = module_0.to_bool(var_2)
    except BaseException:
        pass

def test_case_48():
    try:
        ansible_undefined_0 = module_1.AnsibleUndefined()
        list_0 = []
        var_0 = module_0.to_yaml(ansible_undefined_0, *list_0)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = 'N\\Q\n#C>Z&'
        int_0 = -169
        bytes_0 = b'\x99\xb2\x15\xacc=\xf2\xe7\x9a\x04\x862\xef\xc6\xcfL\x0f'
        float_0 = -174.45
        str_1 = "b'i&ZBy;."
        str_2 = 'OyFVLnCI'
        str_3 = '*NU0.M46\x0cXjB'
        dict_0 = {str_2: str_0, str_3: int_0}
        var_0 = module_0.regex_search(float_0, str_1, **dict_0)
        tuple_0 = (int_0, bytes_0, str_0)
        bool_0 = True
        var_1 = module_0.mandatory(tuple_0, bool_0)
        str_4 = ';,vQ^rA"'
        bool_1 = None
        var_2 = module_0.to_uuid(str_4, bool_1)
    except BaseException:
        pass

def test_case_50():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = 'mm0!"bX(ma3#^'
        var_0 = module_0.strftime(str_0, filter_module_0)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = 'a.b[c]d.^e$f*g\\\\h|i'
        var_0 = module_0.regex_escape(str_0)
        str_1 = 'a.b[c]d.^e$f*g\\h|i'
        str_2 = 'posix_basic'
        var_1 = module_0.regex_escape(str_1, str_2)
        str_3 = 'posix_extended'
        var_2 = module_0.regex_escape(str_0, str_3)
    except BaseException:
        pass

def test_case_52():
    try:
        str_0 = 'Hello'
        bytes_0 = b'\xbc\x92g\x92\xa0\x89'
        var_0 = module_0.combine()
        set_0 = {bytes_0, str_0}
        var_1 = module_0.quote(set_0)
        dict_0 = {}
        var_2 = module_0.mandatory(dict_0)
        bool_0 = False
        str_1 = '^d-r'
        bool_1 = False
        int_0 = 2026
        var_3 = module_0.rand(bool_0, str_1, bool_1, int_0)
    except BaseException:
        pass

def test_case_53():
    try:
        str_0 = 'Hllo'
        str_1 = '% \n4hf~>V+WUk,VE9*'
        dict_0 = {}
        list_0 = [str_1]
        int_0 = 96
        var_0 = module_0.mandatory(list_0, int_0)
        var_1 = module_0.regex_search(str_0, str_0)
        bytes_0 = b'7'
        var_2 = module_0.quote(bytes_0)
        var_3 = module_0.combine(*list_0, **dict_0)
        tuple_0 = ()
        var_4 = module_0.combine()
        list_1 = [str_0, bytes_0, str_1]
        var_5 = module_0.regex_search(tuple_0, list_1, *list_1)
    except BaseException:
        pass

def test_case_54():
    try:
        float_0 = 1.5
        list_0 = [float_0, float_0, float_0, float_0]
        str_0 = "FY\x0bD#kA=|yh61'd#>X"
        filter_module_0 = module_0.FilterModule()
        bool_0 = False
        tuple_0 = (str_0, filter_module_0, bool_0)
        list_1 = []
        var_0 = module_0.rand(float_0, list_0, tuple_0, tuple_0, list_1)
    except BaseException:
        pass

def test_case_55():
    try:
        ansible_undefined_0 = module_1.AnsibleUndefined()
        ansible_undefined_1 = module_1.AnsibleUndefined()
        str_0 = 'my custom message'
        var_0 = module_0.mandatory(ansible_undefined_1, str_0)
    except BaseException:
        pass

def test_case_56():
    try:
        str_0 = 'my custom message'
        int_0 = 2
        var_0 = module_0.mandatory(int_0, str_0)
        ansible_undefined_0 = module_1.AnsibleUndefined()
        var_1 = module_0.mandatory(ansible_undefined_0)
    except BaseException:
        pass

def test_case_57():
    try:
        str_0 = 'name'
        str_1 = 'groups'
        str_2 = 'authorized'
        str_3 = '/tmp/alice/onekey.pub'
        str_4 = [str_3]
        str_5 = {str_0: str_1, str_1: str_1, str_2: str_4}
        str_6 = [str_5]
        var_0 = module_0.subelements(str_6, str_1)
    except BaseException:
        pass

def test_case_58():
    try:
        str_0 = '50K'
        bytes_0 = b'\x9a+\xd5\x835e\xf7\xde'
        var_0 = module_0.flatten(bytes_0)
        var_1 = module_0.strftime(str_0)
        var_2 = module_0.combine()
        str_1 = '!:dw'
        type_0 = None
        ansible_undefined_0 = module_1.AnsibleUndefined(str_0, str_1, str_1, type_0)
        var_3 = module_0.mandatory(ansible_undefined_0)
    except BaseException:
        pass

def test_case_59():
    try:
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b'\xd9'
        set_0 = {bytes_0, filter_module_0}
        dict_0 = None
        var_0 = module_0.flatten(bytes_0, set_0, dict_0)
        list_0 = []
        var_1 = module_0.regex_findall(filter_module_0, list_0)
    except BaseException:
        pass

def test_case_60():
    try:
        str_0 = 'name'
        str_1 = 'authorized'
        str_2 = 'alice'
        str_3 = '/tmp/alice/nekey.pub'
        str_4 = {str_0: str_2, str_1: str_3}
        str_5 = [str_4]
        var_0 = module_0.subelements(str_5, str_2)
    except BaseException:
        pass