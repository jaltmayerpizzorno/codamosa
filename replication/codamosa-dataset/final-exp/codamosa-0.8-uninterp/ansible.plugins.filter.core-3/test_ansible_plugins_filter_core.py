# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    var_0 = module_0.regex_replace()

def test_case_1():
    str_0 = '_O*|~4Y'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.to_nice_yaml(list_0)
    var_1 = module_0.flatten(str_0)

def test_case_2():
    float_0 = 0.001
    var_0 = module_0.to_json(float_0)

def test_case_3():
    str_0 = '/usr/local/lib'
    var_0 = module_0.fileglob(str_0)

def test_case_4():
    bytes_0 = b'\xed\xde\x94n'
    str_0 = '#'
    var_0 = module_0.to_bool(str_0)
    var_1 = module_0.ternary(bytes_0, str_0, bytes_0)

def test_case_5():
    list_0 = None
    str_0 = None
    filter_module_0 = None
    dict_0 = {str_0: str_0, str_0: filter_module_0, str_0: str_0}
    list_1 = [dict_0, list_0, list_0, str_0]
    var_0 = module_0.ternary(list_0, dict_0, list_1)

def test_case_6():
    str_0 = '\twLq\x0b'
    set_0 = set()
    list_0 = [set_0, set_0, str_0]
    var_0 = module_0.regex_escape(list_0)
    var_1 = module_0.regex_search(set_0, str_0)

def test_case_7():
    dict_0 = {}
    bool_0 = True
    var_0 = module_0.to_nice_yaml(bool_0)
    bool_1 = True
    tuple_0 = (dict_0, bool_1)
    str_0 = 'O\nB4]Zn^<#<@~WIH0 ["'
    var_1 = module_0.fileglob(str_0)
    var_2 = module_0.from_yaml_all(tuple_0)

def test_case_8():
    str_0 = '\n        Common code for quickly building an ansible module in Python\n        (although you can write modules with anything that can return JSON).\n\n        See :ref:`developing_modules_general` for a general introduction\n        and :ref:`developing_program_flow_modules` for more detailed explanation.\n        '
    tuple_0 = ()
    var_0 = module_0.rand(str_0, str_0, tuple_0)

def test_case_9():
    int_0 = 1041
    var_0 = module_0.randomize_list(int_0)

def test_case_10():
    str_0 = '\n        Common code for quickly building an ansible module in Python\n        (although you can writ modules with anything that can return JSON).\n\n        See :ref:`developing_modules_general` for a general introduction\n        and :ref:`developing_program_flow_modules` for more detailed explanation.\n        '
    tuple_0 = ()
    var_0 = module_0.rand(str_0, str_0, tuple_0)
    list_0 = [tuple_0, str_0]
    var_1 = module_0.randomize_list(list_0)

def test_case_11():
    filter_module_0 = None
    var_0 = module_0.to_uuid(filter_module_0)
    str_0 = 'posix_basic'
    var_1 = module_0.comment(str_0)

def test_case_12():
    dict_0 = {}
    var_0 = module_0.mandatory(dict_0)

def test_case_13():
    var_0 = module_0.combine()

def test_case_14():
    str_0 = '|7"KGOQ1ft<R6'
    var_0 = module_0.b64encode(str_0)

def test_case_15():
    list_0 = None
    var_0 = module_0.b64decode(list_0)

def test_case_16():
    str_0 = '\n        Common code for quickly building an ansible module in Python\n        (although you can write modules with anything that can return JSON).\n\n        See :ref:`developing_modules_general` for a general introduction\n        and :ref:`developing_program_flow_modules` for more detailed explanation.\n        '
    var_0 = module_0.flatten(str_0)

def test_case_17():
    str_0 = 'b7'
    var_0 = module_0.mandatory(str_0)
    filter_module_0 = None
    list_0 = [filter_module_0]
    var_1 = module_0.combine(*list_0)
    var_2 = module_0.to_nice_json(filter_module_0)
    str_1 = 'posix_basic'
    var_3 = module_0.regex_escape(str_1)
    filter_module_1 = module_0.FilterModule()

def test_case_18():
    str_0 = 'posix_basic'
    var_0 = module_0.from_yaml(str_0)
    bytes_0 = b'\xdb\x1a\xd0\xea\xc3\xee-z\xf4%Y\xf6[\x01s\xb4X\x1a\xc9'
    dict_0 = {}
    str_1 = 'wzY'
    tuple_0 = ()
    var_1 = module_0.rand(str_1, str_1, tuple_0)
    var_2 = module_0.regex_escape(dict_0)
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_3 = module_0.regex_escape(list_0)

def test_case_19():
    str_0 = '\twLq\x0b'
    var_0 = module_0.comment(str_0)

def test_case_20():
    int_0 = 1041
    var_0 = module_0.randomize_list(int_0)
    set_0 = {int_0, var_0, var_0}
    var_1 = module_0.to_bool(set_0)

def test_case_21():
    bool_0 = True
    var_0 = module_0.to_bool(bool_0)
    bool_1 = False
    var_1 = module_0.to_bool(bool_1)
    str_0 = '1'
    var_2 = module_0.to_bool(str_0)
    bool_2 = None
    var_3 = module_0.regex_escape(bool_2)
    bool_3 = True
    list_0 = [bool_0, bool_3, bool_1, bool_3]
    var_4 = module_0.regex_escape(list_0)
    str_1 = ")P@@McvC~{'60G/\\I"
    var_5 = module_0.regex_escape(str_1)

def test_case_22():
    str_0 = '\twLq\x0b'
    set_0 = set()
    var_0 = module_0.regex_search(set_0, str_0)

def test_case_23():
    str_0 = 'python'
    list_0 = [str_0]
    var_0 = module_0.combine(*list_0)

def test_case_24():
    int_0 = 4
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.mandatory(int_0, set_0)
    var_1 = module_0.rand(bool_0, var_0)

def test_case_25():
    str_0 = 'hello'
    str_1 = 'l'
    str_2 = 'x'
    var_0 = module_0.regex_replace(str_0, str_1, str_2)
    str_3 = 'L'
    bool_0 = True
    var_1 = module_0.regex_replace(str_0, str_3, str_2, bool_0)

def test_case_26():
    str_0 = 'hello'
    str_1 = 'x'
    str_2 = 'L'
    bool_0 = True
    var_0 = module_0.regex_replace(str_0, str_2, str_1, bool_0)
    str_3 = 'hello\nhello'
    var_1 = module_0.regex_replace(str_3, str_2, str_1, bool_0, bool_0)

def test_case_27():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    var_0 = module_0.flatten(int_3)
    int_4 = [int_0, int_1, int_2]
    int_5 = [int_4]
    var_1 = module_0.flatten(int_5)
    int_6 = [int_0, int_1, int_2]
    int_7 = 4
    int_8 = 5
    int_9 = 6
    int_10 = [int_7, int_8, int_9]
    int_11 = [int_6, int_10]
    var_2 = module_0.flatten(int_11)
    int_12 = [int_0]
    int_13 = [int_12, int_1, int_2]
    var_3 = module_0.flatten(int_13)
    int_14 = [int_0]
    int_15 = [int_14, int_1]
    int_16 = [int_15, int_2]
    var_4 = module_0.flatten(int_16)
    int_17 = [int_0]
    int_18 = [int_1]
    int_19 = [int_17, int_18]
    int_20 = [int_19, int_2]
    var_5 = module_0.flatten(int_20)
    str_0 = 'one'
    str_1 = 'two'
    str_2 = [str_1]
    str_3 = [str_0, str_2]
    str_4 = 'three'
    str_5 = [str_3, str_4]
    var_6 = module_0.flatten(str_5)
    str_6 = [str_1]
    str_7 = [str_0, str_6]
    str_8 = [str_7]
    var_7 = module_0.flatten(str_8, int_0)

def test_case_28():
    int_0 = 1
    int_1 = -13
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    int_4 = [int_3]
    var_0 = module_0.flatten(int_4)
    int_5 = [int_0, int_1, int_2]
    var_1 = module_0.flatten(int_5)
    int_6 = [int_0]
    int_7 = [int_1]
    int_8 = [int_2]
    int_9 = [int_6, int_7, int_8]
    var_2 = module_0.flatten(int_9)
    str_0 = 'a'
    str_1 = 'b'
    str_2 = [str_1]
    str_3 = 'c'
    str_4 = [str_0, str_2, str_3]
    var_3 = module_0.flatten(str_4)
    int_10 = [int_1]
    int_11 = [int_2]
    int_12 = [int_11]
    str_5 = [str_1]
    str_6 = [str_5]
    var_4 = [int_0, int_10, int_12, str_0, str_6, str_3]
    var_5 = module_0.flatten(var_4)
    int_13 = [int_1]
    int_14 = [int_2]
    int_15 = [int_14]
    str_7 = [str_1]
    str_8 = [str_7]
    var_6 = [int_0, int_13, int_15, str_0, str_8, str_3]
    int_16 = 10
    var_7 = module_0.flatten(var_6, int_16)

def test_case_29():
    str_0 = '#'
    set_0 = {str_0}
    var_0 = module_0.regex_search(set_0, str_0)

def test_case_30():
    str_0 = 'foo.bar'
    var_0 = module_0.regex_escape(str_0)
    str_1 = 'fPoo-bar'
    var_1 = module_0.regex_escape(str_1)
    str_2 = '>A;t'
    var_2 = module_0.regex_escape(str_2)
    str_3 = 'posix_basic'
    var_3 = module_0.regex_escape(str_0, str_3)
    var_4 = module_0.regex_escape(str_1, str_3)
    var_5 = module_0.regex_escape(str_2, str_3)

def test_case_31():
    str_0 = '/bin/ls'
    var_0 = module_0.fileglob(str_0)
    var_1 = module_0.fileglob(str_0)