# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    str_0 = '"]1|:5rP0'
    var_0 = module_0.check_mutually_exclusive(str_0, str_0)

def test_case_1():
    str_0 = "Timout while waiting for the Galaxy importprocess to finish, check progress at '%s'"
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    float_0 = -4240.365485
    var_0 = module_0.safe_eval(float_0)

def test_case_3():
    str_0 = 'resource'
    dict_0 = {str_0: str_0}
    var_0 = module_0.check_required_by(dict_0, dict_0)

def test_case_4():
    dict_0 = {}
    bool_0 = True
    var_0 = module_0.check_required_arguments(dict_0, bool_0)

def test_case_5():
    tuple_0 = None
    str_0 = "-g1Q)'Lq\n~@["
    float_0 = 2972.5
    var_0 = module_0.check_required_arguments(tuple_0, str_0, float_0)

def test_case_6():
    bytes_0 = None
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.check_required_if(bytes_0, dict_0)

def test_case_7():
    str_0 = 'M!b\r]'
    var_0 = module_0.check_missing_parameters(str_0)

def test_case_8():
    str_0 = 'ziaAIT63H#8nFVFv(L5'
    var_0 = module_0.check_type_path(str_0)

def test_case_9():
    str_0 = 'win_basename'
    var_0 = module_0.check_type_list(str_0)

def test_case_10():
    int_0 = False
    var_0 = module_0.check_type_bool(int_0)

def test_case_11():
    bool_0 = False
    var_0 = module_0.check_type_float(bool_0)

def test_case_12():
    list_0 = []
    dict_0 = {}
    tuple_0 = (list_0, dict_0, list_0)
    var_0 = module_0.check_type_raw(tuple_0)
    bytes_0 = b''
    var_1 = module_0.check_mutually_exclusive(bytes_0, bytes_0)

def test_case_13():
    str_0 = '\n- name: Set default locale to fr_FR.UTF-8\n  ansible.builtin.debconf:\n    name: locales\n    question: locales/default_environment_locale\n    value: fr_FR.UTF-8\n    vtype: select\n\n- name: Set to generate locales\n  ansible.builtin.debconf:\n    name: locales\n    question: locales/locales_to_be_generated\n    value: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8\n    vtype: multiselect\n\n- name: Accept oracle license\n  ansible.builtin.debconf:\n    name: oracle-java7-installer\n    question: shared/accepted-oracle-license-v1-1\n    value: \'true\'\n    vtype: select\n\n- name: Specifying package you can register/return the list of questions and current values\n  ansible.builtin.debconf:\n    name: tzdata\n\n- name: Pre-configure tripwire site passphrase\n  ansible.builtin.debconf:\n    name: tripwire\n    question: tripwire/site-passphrase\n    value: "{{ site_passphrase }}"\n    vtype: password\n  no_log: True\n'
    var_0 = module_0.check_type_jsonarg(str_0)

def test_case_14():
    str_0 = 'resource'
    str_1 = 'default_value_1'
    tuple_0 = ()
    set_0 = {tuple_0, str_1, str_1, tuple_0}
    tuple_1 = (set_0,)
    var_0 = module_0.check_type_jsonarg(tuple_1)
    dict_0 = {str_0: str_0}
    var_1 = module_0.check_required_by(dict_0, dict_0)

def test_case_15():
    tuple_0 = ()
    bool_0 = False
    var_0 = module_0.check_required_if(tuple_0, bool_0)

def test_case_16():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    var_0 = module_0.check_missing_parameters(dict_0, tuple_0)
    int_0 = 4026
    var_1 = module_0.check_type_bytes(int_0)
    str_0 = ''
    var_2 = module_0.check_type_raw(str_0)
    var_3 = module_0.check_type_bits(int_0)

def test_case_17():
    str_0 = 'o=;Xc/:M+JT@I:3T^0.n'
    var_0 = module_0.check_type_dict(str_0)

def test_case_18():
    str_0 = "=W@(RC'l"
    var_0 = module_0.check_type_dict(str_0)

def test_case_19():
    str_0 = '&\\~kXV%a\\o$vX=ZJO'
    var_0 = module_0.check_type_dict(str_0)

def test_case_20():
    str_0 = 'present'
    str_1 = 'resource'
    str_2 = 'overridden_value_1'
    str_3 = 'default_value_1'
    var_0 = dict(state=str_0, name=str_1, want_value=str_2, default_value=str_3)
    str_4 = 'want_value'
    str_5 = 'default_value'
    str_6 = [str_4, str_5]
    str_7 = [str_6]
    var_1 = module_0.check_required_together(str_7, var_0)

def test_case_21():
    int_0 = 1
    int_1 = 2
    var_0 = dict(a=int_0, b=int_1)
    var_1 = dict(a=int_0, b=int_1)
    str_0 = 'a=1, b=2'
    var_2 = module_0.check_type_dict(str_0)
    var_3 = print(var_2)
    str_1 = '{"a":1, "b":2}'
    var_4 = module_0.check_type_dict(str_1)
    var_5 = print(var_4)
    var_6 = module_0.check_type_dict(str_1)
    var_7 = print(var_6)

def test_case_22():
    str_0 = '{}'
    var_0 = module_0.safe_eval(str_0)

def test_case_23():
    str_0 = "Timeout while waiting for the Galaxy import process to finish, check progress at '%s'"
    var_0 = module_0.safe_eval(str_0)

def test_case_24():
    str_0 = '0bc='
    var_0 = module_0.check_type_dict(str_0)
    str_1 = "{'a':'b','c':'d'}"
    var_1 = module_0.check_type_dict(str_1)

def test_case_25():
    str_0 = 'bar.update(ba)'
    var_0 = module_0.safe_eval(str_0)

def test_case_26():
    str_0 = 'pVAFjzTp?=wQ;@F\rW'
    str_1 = 'bar'
    str_2 = None
    var_0 = module_0.check_required_by(str_2, str_0)
    str_3 = 'fo'
    str_4 = 'bar'
    var_1 = module_0.safe_eval(str_3, str_1)
    str_5 = {}
    var_2 = None
    var_3 = {str_3: str_3, str_4: var_2}
    var_4 = module_0.check_required_by(str_5, var_3)
    bool_0 = False
    var_5 = module_0.check_type_int(bool_0)
    str_6 = 'foo'
    str_7 = 'bar'
    str_8 = [str_7, str_0]
    str_9 = {str_6: str_8}
    var_6 = None
    var_7 = {str_6: str_6, str_6: var_6}
    var_8 = module_0.check_required_by(str_9, var_7)