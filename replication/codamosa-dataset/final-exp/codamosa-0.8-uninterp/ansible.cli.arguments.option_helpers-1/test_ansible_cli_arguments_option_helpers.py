# Automatically generated by Pynguin.
import argparse as module_0
import ansible.cli.arguments.option_helpers as module_1

def test_case_0():
    pass

def test_case_1():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_module_options(argument_parser_0)

def test_case_2():
    var_0 = module_1.unfrack_path()

def test_case_3():
    var_0 = module_1.version()

def test_case_4():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_connect_options(argument_parser_0)
    var_1 = []
    var_2 = argument_parser_0.parse_args(var_1)

def test_case_5():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_runas_options(argument_parser_0)
    str_0 = '-b'
    var_1 = module_1.add_fork_options(argument_parser_0)
    str_1 = [str_0]
    var_2 = argument_parser_0.parse_args(str_1)
    var_3 = var_2.become
    str_2 = '--become'
    str_3 = [str_2]
    var_4 = argument_parser_0.parse_args(str_3)
    var_5 = var_4.become
    str_4 = '--become-method'
    str_5 = 'sudo'
    str_6 = [str_4, str_5]
    var_6 = argument_parser_0.parse_args(str_6)
    var_7 = var_6.become_method
    str_7 = '--become-user'
    str_8 = 'root'
    str_9 = [str_7, str_8]
    var_8 = argument_parser_0.parse_args(str_9)
    var_9 = var_8.become_user
    str_10 = '--ask-become-pass'
    str_11 = [str_10]
    var_10 = argument_parser_0.parse_args(str_11)
    var_11 = var_10.become_ask_pass

def test_case_6():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_vault_options(argument_parser_0)

def test_case_7():
    int_0 = 5747
    var_0 = module_1.version(int_0)

def test_case_8():
    str_0 = ''
    var_0 = module_1.create_base_parser(str_0, str_0)
    var_1 = module_1.add_check_options(var_0)

def test_case_9():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_subset_options(argument_parser_0)
    var_1 = argument_parser_0.parse_args()

def test_case_10():
    str_0 = '-F'
    str_1 = [str_0]
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_meta_options(argument_parser_0)
    var_1 = argument_parser_0.parse_args(str_1)
    str_2 = '--flush-cache'
    str_3 = [str_0, str_2]
    var_2 = argument_parser_0.parse_args(str_3)
    str_4 = [str_2]
    var_3 = argument_parser_0.parse_args(str_4)

def test_case_11():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_async_options(argument_parser_0)
    var_1 = []
    var_2 = argument_parser_0.parse_args(var_1)
    var_3 = var_2.poll_interval
    var_4 = []
    var_5 = argument_parser_0.parse_args(var_4)
    var_6 = var_5.seconds
    str_0 = '-P'
    str_1 = '1000'
    str_2 = [str_0, str_1]
    var_7 = argument_parser_0.parse_args(str_2)
    var_8 = var_7.poll_interval
    str_3 = [str_0, str_1]
    var_9 = argument_parser_0.parse_args(str_3)
    var_10 = var_9.seconds
    str_4 = '-B'
    str_5 = [str_4, str_1]
    var_11 = argument_parser_0.parse_args(str_5)
    var_12 = var_11.poll_interval
    str_6 = [str_4, str_1]
    var_13 = argument_parser_0.parse_args(str_6)
    var_14 = var_13.seconds

def test_case_12():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_runas_options(argument_parser_0)
    str_0 = '-b'
    str_1 = [str_0]
    var_1 = argument_parser_0.parse_args(str_1)
    var_2 = var_1.become
    str_2 = '--become'
    str_3 = [str_2]
    var_3 = argument_parser_0.parse_args(str_3)
    var_4 = var_3.become
    str_4 = '--become-method'
    str_5 = 'sudo'
    str_6 = [str_4, str_5]
    var_5 = argument_parser_0.parse_args(str_6)
    var_6 = var_5.become_method
    str_7 = '--become-user'
    str_8 = [str_7, str_5]
    var_7 = argument_parser_0.parse_args(str_8)
    var_8 = var_7.become_user
    str_9 = '--ask-become-pass'
    str_10 = [str_9]
    var_9 = argument_parser_0.parse_args(str_10)
    var_10 = var_9.become_ask_pass

def test_case_13():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_runas_prompt_options(argument_parser_0)
    str_0 = '-K --become-pass-file sample_password_file'
    var_1 = argument_parser_0.parse_args(str_0)

def test_case_14():
    bytes_0 = b'\xe5u/e}\xd5EVf\xf5\x95\xda%\xef-\x1a\x1b\x8b'
    bool_0 = True
    str_0 = 'gX_~'
    str_1 = 'SD!;B oiKW=>FX'
    prepend_list_action_0 = module_1.PrependListAction(bool_0, str_0, str_1)
    float_0 = 0.1
    argument_parser_0 = None
    bool_1 = False
    sorting_help_formatter_0 = module_1.SortingHelpFormatter(bool_0, bool_0)
    argument_parser_1 = module_0.ArgumentParser(bool_1, sorting_help_formatter_0)
    unrecognized_argument_0 = module_1.UnrecognizedArgument(float_0, argument_parser_0, argument_parser_1)
    str_2 = '5`~<j]7<Zr,)osc`=gUe'
    argument_parser_2 = module_0.ArgumentParser(unrecognized_argument_0, str_2, bytes_0, sorting_help_formatter_0)
    argument_parser_3 = module_0.ArgumentParser(float_0, argument_parser_2, prepend_list_action_0, float_0)
    var_0 = module_1.add_basedir_options(argument_parser_3)

def test_case_15():
    int_0 = 5734
    var_0 = module_1.version(int_0)
    bytes_0 = b'\x1dT\x13|\xefX1\x84\xe19\x88\xb81\x05\x93\x1aL\xda\xca'
    bool_0 = False
    str_0 = 'gX_~'
    list_0 = [bool_0, int_0, bool_0, int_0]
    dict_0 = {}
    argument_parser_0 = module_0.ArgumentParser(bytes_0, list_0, dict_0, list_0)
    var_1 = module_1.add_runas_prompt_options(argument_parser_0, argument_parser_0)
    prepend_list_action_0 = module_1.PrependListAction(bool_0, str_0, str_0)
    set_0 = {str_0, int_0}
    int_1 = 619
    sorting_help_formatter_0 = module_1.SortingHelpFormatter(int_1)
    str_1 = 'uW`w'
    ansible_version_0 = module_1.AnsibleVersion(set_0, bytes_0, sorting_help_formatter_0, str_1)
    var_2 = prepend_list_action_0.__call__(bool_0, ansible_version_0, str_1)
    dict_1 = {str_0: str_0}
    var_3 = module_1.add_tasknoplay_options(argument_parser_0)
    bool_1 = True
    complex_0 = None
    prepend_list_action_1 = module_1.PrependListAction(str_0, bool_1, complex_0)
    bool_2 = True
    list_1 = [prepend_list_action_0]
    tuple_0 = (list_1,)
    float_0 = -214.794
    float_1 = 750.7255
    list_2 = None
    ansible_version_1 = module_1.AnsibleVersion(float_0, bool_2, float_1, bool_0, prepend_list_action_0, list_2)
    ansible_version_2 = module_1.AnsibleVersion(tuple_0, ansible_version_0, list_1, dict_1, tuple_0, list_2)

def test_case_16():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_output_options(argument_parser_0)
    str_0 = '-o'
    str_1 = [str_0]
    var_1 = argument_parser_0.parse_args(str_1)
    str_2 = '-t'
    str_3 = '/tmp/test_add_output_options/'
    str_4 = [str_2, str_3]
    var_2 = argument_parser_0.parse_args(str_4)
    var_3 = []
    var_4 = argument_parser_0.parse_args(var_3)
    str_5 = '-o'
    str_6 = '-t'
    str_7 = '/tmp/test_add_output_options/'
    str_8 = [str_5, str_6, str_7]
    var_5 = argument_parser_0.parse_args(str_8)

def test_case_17():
    str_0 = 'xASS@|CNFJ<JyN\x0b@#O'
    bool_0 = True
    list_0 = [str_0, bool_0, str_0, bool_0]
    bytes_0 = b'#2\x0e\xectx\x8a\xa4m\xf0\xbed\x15\x06\x1e\xbd^'
    list_1 = [bool_0]
    int_0 = -456
    int_1 = -298
    list_2 = [list_0, int_1, bytes_0]
    tuple_0 = (list_1, int_0, list_2, list_0)
    sorting_help_formatter_0 = module_1.SortingHelpFormatter(tuple_0)
    str_1 = '8.y*Y/}cJ`s$<(B[L'
    ansible_version_0 = None
    argument_parser_0 = module_0.ArgumentParser(str_1, ansible_version_0)
    set_0 = None
    str_2 = 'sb\'\'"|Qw3G'
    dict_0 = {str_2: list_2}
    set_1 = {bytes_0, bool_0}
    float_0 = -3660.88327
    bytes_1 = b'~$\xf8\t\xf8\xe5\x88&$\x92w\xcd\x02\x06\x03!\x80\xd4\xb3'
    bool_1 = True
    list_3 = [bool_0, float_0, sorting_help_formatter_0]
    argument_parser_1 = module_0.ArgumentParser(bool_1, list_3)
    str_3 = 'uQo{:n'
    list_4 = [float_0, sorting_help_formatter_0, str_3, list_1]
    dict_1 = {argument_parser_1: list_4}
    bool_2 = False
    unrecognized_argument_0 = module_1.UnrecognizedArgument(argument_parser_1, tuple_0, dict_1, bool_2)
    unrecognized_argument_1 = module_1.UnrecognizedArgument(bytes_1, list_2, unrecognized_argument_0)
    ansible_version_1 = module_1.AnsibleVersion(set_1, float_0, unrecognized_argument_1, tuple_0)
    var_0 = ansible_version_1.__call__(argument_parser_0, set_0, dict_0)
    set_2 = set()
    prepend_list_action_0 = module_1.PrependListAction(bool_0, list_0, bytes_0, set_2)
    var_1 = module_1.add_async_options(str_0)