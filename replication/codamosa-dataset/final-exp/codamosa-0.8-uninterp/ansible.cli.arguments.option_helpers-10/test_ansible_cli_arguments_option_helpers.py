# Automatically generated by Pynguin.
import argparse as module_0
import ansible.cli.arguments.option_helpers as module_1

def test_case_0():
    pass

def test_case_1():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_module_options(argument_parser_0)

def test_case_2():
    var_0 = module_1.version()

def test_case_3():
    str_0 = './ansible'
    str_1 = 'test --vault-password-file vault-pass-file'
    var_0 = module_1.create_base_parser(str_0, str_1)
    var_1 = module_1.add_vault_options(var_0)

def test_case_4():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_connect_options(argument_parser_0)
    str_0 = '60'
    str_1 = '--connection-password-file'
    str_2 = [str_1, str_0, str_0, str_1, str_1, str_1, str_1]
    var_1 = argument_parser_0.parse_args(str_2)

def test_case_5():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_meta_options(argument_parser_0)
    str_0 = '--force-handlers'
    var_1 = argument_parser_0.parse_args(str_0)

def test_case_6():
    bytes_0 = None
    dict_0 = {}
    tuple_0 = (dict_0,)
    str_0 = 'e'
    argument_parser_0 = module_0.ArgumentParser(bytes_0, tuple_0, str_0)
    var_0 = module_1.add_output_options(argument_parser_0)
    var_1 = module_1.version()

def test_case_7():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_runas_options(argument_parser_0)
    var_1 = vars(argument_parser_0)

def test_case_8():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_subset_options(argument_parser_0)

def test_case_9():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_vault_options(argument_parser_0)

def test_case_10():
    namespace_0 = module_0.Namespace()
    str_0 = '--foo'
    str_1 = [str_0]
    str_2 = 'foo'
    prepend_list_action_0 = module_1.PrependListAction(str_1, str_2)
    var_0 = None
    str_3 = 'bar'
    str_4 = [str_3]
    str_5 = '-f'
    var_1 = prepend_list_action_0.__call__(var_0, namespace_0, str_4, str_5)

def test_case_11():
    str_0 = 'test_prog'
    var_0 = module_1.version(str_0)

def test_case_12():
    str_0 = '\\nDFBXuOe\tvSIq$7'
    set_0 = None
    list_0 = None
    float_0 = 592.00876
    var_0 = module_1.version()
    int_0 = -1149
    ansible_version_0 = module_1.AnsibleVersion(int_0, list_0, float_0)
    bool_0 = False
    float_1 = 1617.753353787468
    argument_parser_0 = module_0.ArgumentParser(list_0, ansible_version_0, bool_0)
    bytes_0 = b'\xe8Zu\xae\xf8\xfc\xc2\xf4%\xdd\xb2\x95\x89\x0f^\xc4\x9e/\x95'
    str_1 = 'D'
    tuple_0 = None
    ansible_version_1 = module_1.AnsibleVersion(int_0, argument_parser_0, str_1, tuple_0)
    argument_parser_1 = module_0.ArgumentParser(ansible_version_0, argument_parser_0, bytes_0, ansible_version_1)
    bytes_1 = b'"$\xff|'
    var_1 = ansible_version_0.__call__(argument_parser_1, list_0, tuple_0, bytes_1)
    bytes_2 = b'\x8e\xf0\xcd\xca*\xe2\x80\xe3\xfe\xd1\xa6\xd1\xe6^'
    unrecognized_argument_0 = None
    var_2 = module_1.maybe_unfrack_path(bool_0)
    dict_0 = {}
    sorting_help_formatter_0 = module_1.SortingHelpFormatter(unrecognized_argument_0)
    prepend_list_action_0 = module_1.PrependListAction(unrecognized_argument_0, dict_0, sorting_help_formatter_0, unrecognized_argument_0)
    prepend_list_action_1 = module_1.PrependListAction(bool_0, int_0, float_1, bytes_2, prepend_list_action_0, dict_0)
    tuple_1 = (unrecognized_argument_0, str_0)
    int_1 = 399
    str_2 = 'HAIu'
    float_2 = 3583.02
    set_1 = {float_2, var_0}
    ansible_version_2 = module_1.AnsibleVersion(tuple_1, int_1, set_0, ansible_version_0, str_2, set_1)
    var_3 = module_1.maybe_unfrack_path(sorting_help_formatter_0)
    var_4 = module_1.version()
    sorting_help_formatter_1 = module_1.SortingHelpFormatter(float_1)
    bool_1 = True
    var_5 = module_1.add_basedir_options(bool_1)
    var_6 = module_1.add_output_options(bool_1)
    bool_2 = True
    var_7 = module_1.add_tasknoplay_options(bool_2)

def test_case_13():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_check_options(argument_parser_0)
    str_0 = '--check'
    str_1 = [str_0]
    var_1 = argument_parser_0.parse_args(str_1)
    str_2 = '--syntax-check'
    str_3 = [str_2]
    var_2 = argument_parser_0.parse_args(str_3)
    str_4 = '--diff'
    str_5 = [str_4]
    var_3 = argument_parser_0.parse_args(str_5)