# Automatically generated by Pynguin.
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = -765.0
    tuple_0 = None
    bool_0 = True
    bytes_0 = b';\x9d/\xb7\x0c'
    unrecognized_argument_0 = module_0.UnrecognizedArgument(float_0, tuple_0, bool_0, bytes_0)

def test_case_2():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_module_options(argument_parser_0)
    str_0 = '-M'
    str_1 = '/usr/share/ansible/plugins/modules:/usr/local/share/ansible/plugins/modules:/usr/share/ansible/plugins/module_utils:/usr/local/share/ansible/plugins/module_utils'
    str_2 = [str_0, str_1]
    var_1 = argument_parser_0.parse_args(str_2)

def test_case_3():
    namespace_0 = module_1.Namespace()
    str_0 = 'abc'
    var_0 = []
    var_1 = module_0.ensure_value(namespace_0, str_0, var_0)

def test_case_4():
    var_0 = module_0.unfrack_path()

def test_case_5():
    var_0 = module_0.version()

def test_case_6():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_vault_options(argument_parser_0)
    str_0 = '--vault-id'
    str_1 = '*'
    str_2 = [str_0, str_1]
    set_0 = set()
    var_1 = argument_parser_0.convert_arg_line_to_args(set_0)
    list_0 = [argument_parser_0, str_2, str_2, argument_parser_0]
    var_2 = module_0.version(list_0)
    var_3 = argument_parser_0.parse_args(str_2)
    str_3 = '--vault-password-file'
    str_4 = '*'
    str_5 = [str_3, str_4]
    var_4 = argument_parser_0.parse_args(str_5)
    sorting_help_formatter_0 = module_0.SortingHelpFormatter(str_1)

def test_case_7():
    str_0 = 'prog'
    str_1 = 'desc'
    str_2 = 'epilog'
    var_0 = module_0.create_base_parser(str_0, str_1, str_1, str_2)
    var_1 = module_0.add_inventory_options(var_0)

def test_case_8():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_fork_options(argument_parser_0)

def test_case_9():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_inventory_options(argument_parser_0)

def test_case_10():
    str_0 = 'add_meta_options'
    argument_parser_0 = module_1.ArgumentParser(str_0)
    var_0 = module_0.add_meta_options(argument_parser_0)

def test_case_11():
    str_0 = 'X\nMef<)q'
    str_1 = '1H,cD*'
    str_2 = '\n8w#`jfAq*xa/\nH\n\x0b*x'
    str_3 = 'ansibl_i.ndex_vad'
    dict_0 = {str_1: str_0, str_2: str_0, str_3: str_2}
    namespace_0 = module_1.Namespace(**dict_0)
    namespace_1 = None
    dict_1 = {str_0: str_1, str_0: str_3, str_3: str_1, namespace_1: str_1}
    list_0 = []
    ansible_version_0 = module_0.AnsibleVersion(namespace_0, dict_1, list_0)
    argument_parser_0 = module_1.ArgumentParser(str_0, ansible_version_0)
    var_0 = module_0.add_output_options(argument_parser_0)

def test_case_12():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_subset_options(argument_parser_0)
    var_1 = argument_parser_0.parse_args()

def test_case_13():
    str_0 = 'ansible'
    str_1 = 'resolve'
    argument_parser_0 = module_1.ArgumentParser(str_0, str_1)
    var_0 = module_0.add_check_options(argument_parser_0)

def test_case_14():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_async_options(argument_parser_0)

def test_case_15():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_connect_options(argument_parser_0)
    str_0 = '-u'
    var_1 = argument_parser_0.parse_args(str_0)

def test_case_16():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_vault_options(argument_parser_0)
    str_0 = '--vault-password-file'
    str_1 = 'bar'
    str_2 = [str_0, str_1]
    var_1 = argument_parser_0.parse_args(str_2)

def test_case_17():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_runtask_options(argument_parser_0)
    str_0 = '-e'
    str_1 = 'host=abc'
    str_2 = [str_0, str_1]
    var_1 = argument_parser_0.parse_args(str_2)

def test_case_18():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_tasknoplay_options(argument_parser_0)
    str_0 = '--task-timeout'
    var_1 = argument_parser_0.parse_args(str_0)
    var_2 = vars(var_1)

def test_case_19():
    var_0 = module_0.version()
    var_1 = module_0.unfrack_path()
    dict_0 = {}
    bool_0 = False
    unrecognized_argument_0 = module_0.UnrecognizedArgument(dict_0, dict_0, bool_0)
    float_0 = 1842.4812
    float_1 = 1.5
    var_2 = module_0.create_base_parser(float_1)
    ansible_version_0 = module_0.AnsibleVersion(bool_0, float_1, float_0)
    str_0 = 'ansibl_i.ndex_vad'
    bytes_0 = b'Y\x10a\xaf\xa7$\xc70'
    bool_1 = False
    float_2 = 1.5
    str_1 = '<m\\-7Xpv(^CV8ff'
    str_2 = 'J".wJp?yQB.-r'
    set_0 = {str_1, float_2, str_2}
    complex_0 = None
    float_3 = 2653.6
    tuple_0 = (complex_0, str_2, float_3)
    var_3 = module_0.maybe_unfrack_path(tuple_0)
    list_0 = None
    dict_1 = {str_0: var_1}
    argument_parser_0 = module_1.ArgumentParser(dict_1, str_1, unrecognized_argument_0)
    var_4 = ansible_version_0.__call__(argument_parser_0, tuple_0, argument_parser_0)
    tuple_1 = (list_0,)
    ansible_version_1 = module_0.AnsibleVersion(str_2, set_0, list_0, tuple_1)
    sorting_help_formatter_0 = module_0.SortingHelpFormatter(ansible_version_1, bool_1)
    tuple_2 = (str_1, sorting_help_formatter_0)
    ansible_version_2 = module_0.AnsibleVersion(bool_1, float_2, float_2, tuple_2, tuple_1)
    str_3 = ''
    prepend_list_action_0 = module_0.PrependListAction(list_0, ansible_version_2, str_3, str_3)
    var_5 = ansible_version_2.__call__(bytes_0, ansible_version_0, set_0, bytes_0)
    bytes_1 = b'L\x17B2O'
    sorting_help_formatter_1 = module_0.SortingHelpFormatter(list_0, bytes_1)

def test_case_20():
    namespace_0 = module_1.Namespace()
    str_0 = 'foo'
    str_1 = 'name'
    var_0 = module_0.ensure_value(namespace_0, str_1, str_0)
    str_2 = 'bar'
    var_1 = module_0.ensure_value(namespace_0, str_1, str_2)
    var_2 = module_0.ensure_value(namespace_0, str_1, str_0)

def test_case_21():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_vault_options(argument_parser_0)
    str_0 = '--vault-id'
    str_1 = '?'
    str_2 = [str_0, str_1]
    unrecognized_argument_0 = None
    var_1 = argument_parser_0.convert_arg_line_to_args(unrecognized_argument_0)
    set_0 = set()
    var_2 = argument_parser_0.convert_arg_line_to_args(set_0)
    list_0 = [str_2, argument_parser_0]
    var_3 = module_0.version(list_0)
    var_4 = argument_parser_0.parse_args(str_2)
    str_3 = '--vault-password-file'
    str_4 = '*'
    str_5 = [str_3, str_4]
    var_5 = argument_parser_0.parse_args(str_5)
    dict_0 = {}
    var_6 = module_0.create_base_parser(dict_0)
    bytes_0 = b'\xa4\x9d\x06\xd2,\xa6\xe5=\xbb\x83\x01\x036\x03'
    complex_0 = None
    var_7 = module_0.maybe_unfrack_path(complex_0)
    str_6 = '.}10FO93B~oW'
    sorting_help_formatter_0 = module_0.SortingHelpFormatter(str_6)
    prepend_list_action_0 = module_0.PrependListAction(list_0, bytes_0, str_1, str_2)