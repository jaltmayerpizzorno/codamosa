# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -637
    var_0 = module_0.quote(int_0)
    bool_0 = True
    str_0 = 'ansible_parent_role_names'
    filter_module_0 = module_0.FilterModule()
    var_1 = module_0.flatten(str_0, filter_module_0)
    var_2 = module_0.to_yaml(bool_0)

def test_case_2():
    str_0 = ''
    var_0 = module_0.to_bool(str_0)

def test_case_3():
    bytes_0 = b'L\xfaR\xb5M\xcb\xc5@'
    var_0 = module_0.fileglob(bytes_0)

def test_case_4():
    float_0 = -3744.6
    var_0 = module_0.regex_replace(float_0)

def test_case_5():
    bool_0 = None
    str_0 = ''
    var_0 = module_0.regex_search(bool_0, str_0)

def test_case_6():
    tuple_0 = ()
    var_0 = module_0.from_yaml_all(tuple_0)

def test_case_7():
    float_0 = 1754.0
    var_0 = module_0.randomize_list(float_0)

def test_case_8():
    str_0 = None
    list_0 = [str_0]
    var_0 = module_0.get_hash(list_0)
    var_1 = module_0.randomize_list(str_0)
    list_1 = [str_0]
    var_2 = module_0.combine(*list_1)

def test_case_9():
    filter_module_0 = module_0.FilterModule()
    var_0 = module_0.mandatory(filter_module_0)

def test_case_10():
    var_0 = module_0.combine()

def test_case_11():
    str_0 = ':2G?\n@Tl.`<Hl>xf'
    var_0 = module_0.comment(str_0)

def test_case_12():
    bool_0 = None
    str_0 = ''
    var_0 = module_0.regex_search(bool_0, str_0)
    list_0 = [var_0, var_0, str_0]
    dict_0 = {var_0: list_0}
    var_1 = module_0.b64encode(dict_0)

def test_case_13():
    str_0 = 'Collection'
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.comment(str_0, **dict_0)
    dict_1 = {}
    var_1 = module_0.from_yaml_all(dict_1)
    set_0 = set()
    var_2 = module_0.b64encode(set_0)
    filter_module_0 = None
    var_3 = module_0.b64decode(filter_module_0)

def test_case_14():
    str_0 = None
    var_0 = module_0.randomize_list(str_0)
    list_0 = [str_0]
    var_1 = module_0.combine(*list_0)

def test_case_15():
    float_0 = 1.0
    var_0 = module_0.to_bool(float_0)

def test_case_16():
    var_0 = module_0.combine()
    bool_0 = False
    var_1 = module_0.to_bool(bool_0)

def test_case_17():
    str_0 = 'ansible_%s_user'
    var_0 = module_0.quote(str_0)
    str_1 = '" \\a<n?`Iu7l.'
    list_0 = [str_1]
    var_1 = module_0.randomize_list(list_0)
    var_2 = module_0.combine(*list_0)
    var_3 = module_0.regex_escape(list_0)

def test_case_18():
    tuple_0 = ()
    var_0 = module_0.mandatory(tuple_0)
    var_1 = module_0.combine()
    list_0 = [var_1, var_1, tuple_0, var_0]
    str_0 = '/?{rn'
    var_2 = module_0.ternary(list_0, str_0, list_0)

def test_case_19():
    bytes_0 = None
    var_0 = module_0.quote(bytes_0)
    dict_0 = None
    str_0 = '`6{{kz\x0bhg9\t'
    str_1 = 'L\n\rRYk\x0cNE'
    var_1 = module_0.ternary(str_0, str_1, str_1)
    filter_module_0 = None
    list_0 = [filter_module_0]
    var_2 = module_0.ternary(dict_0, filter_module_0, list_0, dict_0)

def test_case_20():
    str_0 = " ?'+y^R2\rixf\x0c5WG"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.combine()
    tuple_0 = (dict_0, dict_0)
    list_0 = [tuple_0, dict_0]
    var_1 = module_0.combine(*list_0)

def test_case_21():
    bool_0 = None
    str_0 = '3zy"=ol{_CY\nwF'
    var_0 = module_0.regex_search(bool_0, str_0)

def test_case_22():
    str_0 = 'KI)/~E1Jr%Y'
    bytes_0 = b'X8\xc0\x00\xe6U\xb5\xf9c\x18'
    set_0 = set()
    var_0 = module_0.flatten(str_0, bytes_0, set_0)
    str_1 = '*G|M5'
    bytes_1 = b'\xdd\x168J\x1aE\xd0{'
    float_0 = -1861.0
    var_1 = module_0.ternary(str_1, bytes_1, float_0)

def test_case_23():
    bytes_0 = b'0\xd1\xae\x8d.j\x9f]\xb4 \xbe\xbb\xba,\xed\xd6'
    list_0 = []
    var_0 = module_0.subelements(list_0, list_0, bytes_0)

def test_case_24():
    str_0 = 'This is a test'
    str_1 = 'plain'
    var_0 = module_0.comment(str_0, str_1)
    str_2 = 'erlang'
    var_1 = module_0.comment(str_0, str_2)
    str_3 = 'c'
    var_2 = module_0.comment(str_0, str_3)
    str_4 = 'cblock'
    var_3 = module_0.comment(str_0, str_4)
    str_5 = 'xml'
    var_4 = module_0.comment(str_0, str_5)
    str_6 = '-- '
    var_5 = module_0.comment(str_0)
    str_7 = 'Line1\nLine2'
    var_6 = module_0.comment(str_7, str_1)

def test_case_25():
    str_0 = 'name'
    str_1 = 'groups'
    str_2 = 'authorized'
    str_3 = 'alice'
    str_4 = 'wheel'
    str_5 = 'users'
    str_6 = [str_4, str_5]
    str_7 = '/tmp/alice/onekey.pub'
    str_8 = [str_7]
    str_9 = {str_0: str_3, str_1: str_6, str_2: str_8}
    str_10 = [str_9]
    var_0 = module_0.subelements(str_10, str_1)