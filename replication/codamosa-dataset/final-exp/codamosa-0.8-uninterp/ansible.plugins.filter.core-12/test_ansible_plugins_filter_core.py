# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    str_0 = None
    var_0 = module_0.quote(str_0)

def test_case_2():
    str_0 = '/etc/*conf'
    var_0 = module_0.fileglob(str_0)

def test_case_3():
    list_0 = []
    var_0 = module_0.regex_replace(list_0)

def test_case_4():
    filter_module_0 = module_0.FilterModule()
    var_0 = module_0.randomize_list(filter_module_0)
    bytes_0 = b"2a\xd4\x90Zo\r\x9a~~\xb2\xe4wN'~("
    str_0 = ";\x0by'\nJ~4=kd=f FTCn|"
    dict_0 = {str_0: filter_module_0, str_0: var_0, str_0: str_0, str_0: str_0}
    str_1 = ')M!)IPU.zo,'
    var_1 = module_0.ternary(bytes_0, str_1, dict_0)
    var_2 = module_0.quote(dict_0)
    var_3 = filter_module_0.filters()

def test_case_5():
    set_0 = set()
    list_0 = [set_0]
    dict_0 = {}
    dict_1 = None
    var_0 = module_0.ternary(set_0, list_0, dict_0, dict_1)

def test_case_6():
    bytes_0 = None
    var_0 = module_0.from_yaml(bytes_0)

def test_case_7():
    str_0 = '\\5g.*QsD>=?'
    var_0 = module_0.from_yaml(str_0)

def test_case_8():
    str_0 = 'w'
    int_0 = 25
    bool_0 = True
    var_0 = module_0.rand(int_0, bool_0)
    var_1 = module_0.to_bool(str_0)

def test_case_9():
    int_0 = 2
    dict_0 = {}
    var_0 = module_0.randomize_list(int_0, dict_0)

def test_case_10():
    str_0 = ':$2&\\gCho{H'
    str_1 = '%s%s\r\n%s    + CategoryInfo          : %s\r\n    + FullyQualifiedErrorId : %s'
    list_0 = [str_0, str_0]
    var_0 = module_0.randomize_list(str_1, list_0)

def test_case_11():
    int_0 = -2013
    var_0 = module_0.mandatory(int_0)
    str_0 = 'python python python'
    dict_0 = None
    var_1 = module_0.regex_escape(dict_0)
    str_1 = 'py'
    list_0 = [str_0]
    var_2 = module_0.combine(*list_0)
    var_3 = module_0.combine()
    var_4 = module_0.regex_search(str_0, str_1)
    var_5 = module_0.randomize_list(list_0)

def test_case_12():
    list_0 = None
    var_0 = module_0.mandatory(list_0)

def test_case_13():
    var_0 = module_0.combine()

def test_case_14():
    str_0 = ''
    var_0 = module_0.regex_search(str_0, str_0)
    set_0 = {str_0, var_0}
    var_1 = module_0.b64encode(set_0)

def test_case_15():
    dict_0 = None
    dict_1 = {dict_0: dict_0, dict_0: dict_0}
    var_0 = module_0.flatten(dict_1, dict_1)

def test_case_16():
    dict_0 = {}
    str_0 = '--metadata-dump'
    var_0 = module_0.subelements(dict_0, str_0, str_0)

def test_case_17():
    var_0 = module_0.combine()
    str_0 = None
    str_1 = 'I]'
    var_1 = module_0.fileglob(str_1)
    dict_0 = {str_0: str_0, str_1: var_0, str_0: var_0}
    int_0 = -271
    var_2 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, int_0)

def test_case_18():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_19():
    list_0 = []
    str_0 = '=>'
    dict_0 = {}
    var_0 = module_0.regex_search(list_0, str_0, **dict_0)
    list_1 = [var_0]
    var_1 = module_0.quote(list_1)

def test_case_20():
    str_0 = '^GROUP=(.*)'
    float_0 = -236.733496
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.to_nice_yaml(str_0, *list_0)
    str_1 = ''
    var_1 = module_0.combine()
    var_2 = module_0.regex_search(str_1, str_1)

def test_case_21():
    str_0 = 'py'
    var_0 = module_0.regex_search(str_0, str_0)

def test_case_22():
    int_0 = -2013
    var_0 = module_0.mandatory(int_0)
    str_0 = 'python python python'
    str_1 = 'py'
    list_0 = [str_0]
    var_1 = module_0.combine(*list_0)
    var_2 = module_0.combine()
    var_3 = module_0.regex_search(str_0, str_1)

def test_case_23():
    str_0 = 'Hzn'
    var_0 = module_0.to_bool(str_0)

def test_case_24():
    str_0 = 'py'
    var_0 = module_0.comment(str_0)

def test_case_25():
    float_0 = -236.733496
    list_0 = [float_0, float_0]
    var_0 = module_0.mandatory(list_0)
    int_0 = -1622
    str_0 = '<5=L\t*'
    var_1 = module_0.regex_findall(int_0, str_0, float_0)
    str_1 = '/etc/*conf'
    var_2 = module_0.fileglob(str_1)

def test_case_26():
    list_0 = []
    str_0 = '=>'
    dict_0 = {str_0: str_0}
    var_0 = module_0.regex_search(list_0, str_0, **dict_0)

def test_case_27():
    list_0 = []
    bytes_0 = b'\xd0\x07\t\xb1q{"z\x05\x1e'
    var_0 = module_0.list_of_dict_key_value_elements_to_dict(list_0, bytes_0)

def test_case_28():
    float_0 = None
    var_0 = module_0.to_bool(float_0)
    list_0 = []
    str_0 = '=>'
    dict_0 = {str_0: str_0}
    var_1 = module_0.regex_search(list_0, str_0, **dict_0)
    var_2 = module_0.regex_replace(list_0)
    bytes_0 = b'"\xfe\xab\xaf\xe56\xf4~'
    var_3 = module_0.fileglob(bytes_0)

def test_case_29():
    bool_0 = True
    str_0 = ':$2j^gCho{H'
    str_1 = '%s%s\r\n%s    + CategoryInfo          : %s\r\n    + FullyQualifiedErrorId : %s'
    list_0 = None
    tuple_0 = None
    str_2 = "'8jDFSG\t}y@M' L#(&-"
    dict_0 = {list_0: str_2, bool_0: str_2}
    bytes_0 = b'\xb1\x06v'
    tuple_1 = (list_0, tuple_0, dict_0, bytes_0)
    tuple_2 = (tuple_1, tuple_1)
    float_0 = 1987.0
    var_0 = module_0.flatten(tuple_2, float_0)
    list_1 = [str_0, str_0]
    var_1 = module_0.randomize_list(str_1, list_1)

def test_case_30():
    str_0 = 'hello, world!'
    str_1 = 'plain'
    var_0 = module_0.comment(str_0, str_1)
    str_2 = 'erlang'
    var_1 = module_0.comment(str_0, str_2)
    str_3 = 'c'
    var_2 = module_0.comment(str_0, str_3)
    str_4 = 'cblock'
    var_3 = module_0.comment(str_0, str_4)