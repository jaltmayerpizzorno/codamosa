# Automatically generated by Pynguin.
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'krQp\njyXq1'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    prepend_list_action_0 = module_0.PrependListAction(str_0, dict_0)
    list_0 = []
    argument_parser_0 = module_1.ArgumentParser(prepend_list_action_0, list_0)
    var_0 = module_0.add_runas_options(argument_parser_0)

def test_case_2():
    var_0 = module_0.version()

def test_case_3():
    bool_0 = True
    int_0 = 2148
    list_0 = []
    ansible_version_0 = module_0.AnsibleVersion(bool_0, int_0, list_0)
    str_0 = 'T#`[QzEn'
    str_1 = '?+J.se\x0c@F\x0b?BJl-u1TmJ'
    bytes_0 = b'\x82\xebEB\xd4\xf2\xfb\xb6\x13\xbe#\x8c\x86\x98\x0cVL\xae'
    str_2 = '@_p#\\;|K\x0bx\\\nrT@(\n'
    dict_0 = {str_1: bytes_0, str_0: list_0, str_2: bytes_0}
    bool_1 = False
    argument_parser_0 = module_1.ArgumentParser(str_0, dict_0, bool_1)
    str_3 = '&eCM'
    var_0 = ansible_version_0.__call__(argument_parser_0, str_3, int_0)

def test_case_4():
    str_0 = 'Test Parser'
    argument_parser_0 = module_1.ArgumentParser(str_0)
    var_0 = module_0.add_inventory_options(argument_parser_0)
    str_1 = '--inventory'
    str_2 = '--list-hosts'
    var_1 = None
    var_2 = var_0 is not var_1
    var_3 = str_1 is not var_1
    var_4 = str_2 is not var_1
    str_3 = 'All tests passed for add_inventory_options function.'
    var_5 = print(str_3)

def test_case_5():
    var_0 = module_0.unfrack_path()
    ansible_version_0 = None
    list_0 = []
    set_0 = {ansible_version_0, ansible_version_0}
    list_1 = None
    str_0 = None
    prepend_list_action_0 = None
    dict_0 = {str_0: prepend_list_action_0, str_0: list_0}
    unrecognized_argument_0 = module_0.UnrecognizedArgument(set_0, list_1, dict_0)
    tuple_0 = (unrecognized_argument_0,)
    argument_parser_0 = module_1.ArgumentParser(ansible_version_0, list_0, tuple_0)
    var_1 = module_0.add_check_options(argument_parser_0)

def test_case_6():
    str_0 = 'Test parser for add_connect_options'
    argument_parser_0 = module_1.ArgumentParser(str_0)
    var_0 = module_0.add_connect_options(argument_parser_0)
    str_1 = '--private-key'
    str_2 = '/path/to/private/key'
    str_3 = '-u'
    str_4 = '-c'
    str_5 = 'ssh'
    str_6 = '-o ProxyCommand="ssh -W %h:%p gateway.example.com"'
    str_7 = '-v'
    str_8 = [str_1, str_2, str_3, str_6, str_4, str_5, str_3, str_0, str_0, str_6, str_1, str_3, str_0, str_3, str_6, str_7, str_1]
    var_1 = argument_parser_0.parse_args(str_8)

def test_case_7():
    str_0 = 'Test parser for async options'
    argument_parser_0 = module_1.ArgumentParser(str_0)
    var_0 = module_0.add_async_options(argument_parser_0)
    str_1 = '--background'
    str_2 = '60'
    str_3 = '--poll'
    str_4 = '10'
    str_5 = [str_1, str_2, str_3, str_4]
    var_1 = argument_parser_0.parse_args(str_5)
    var_2 = []
    var_3 = argument_parser_0.parse_args(var_2)