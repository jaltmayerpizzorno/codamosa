# Automatically generated by Pynguin.
import argparse as module_0
import ansible.cli.arguments.option_helpers as module_1

def test_case_0():
    pass

def test_case_1():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_vault_options(argument_parser_0)

def test_case_2():
    int_0 = 906
    var_0 = module_1.maybe_unfrack_path(int_0)

def test_case_3():
    var_0 = module_1.version()

def test_case_4():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_inventory_options(argument_parser_0)
    str_0 = '-i'
    str_1 = 'invent1,invent2'
    str_2 = '-l'
    str_3 = 'lim1'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = argument_parser_0.parse_args(str_4)

def test_case_5():
    str_0 = 'Test function add_tasknoplay_options'
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_tasknoplay_options(argument_parser_0)
    var_1 = print(str_0)

def test_case_6():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_vault_options(argument_parser_0)
    str_0 = '--vault-id'
    str_1 = 'passwd'
    str_2 = '--ask-vault-password'
    str_3 = '--vault-password-file'
    str_4 = 'passfile'
    str_5 = [str_0, str_1, str_2, str_3, str_4]
    var_1 = argument_parser_0.parse_args(str_5)

def test_case_7():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_output_options(argument_parser_0)
    var_1 = argument_parser_0.parse_args()

def test_case_8():
    str_0 = 'ansible-inventory'
    argument_parser_0 = module_0.ArgumentParser(str_0)
    var_0 = module_1.add_runas_options(argument_parser_0)
    str_1 = '--become'
    str_2 = '--become-method'
    str_3 = 'sudo'
    str_4 = 'root'
    str_5 = '--become-ask-pass'
    str_6 = '--ask-su-pass'
    str_7 = [str_1, str_2, str_3, str_1, str_4, str_5, str_4, str_6]
    var_1 = argument_parser_0.parse_args(str_7)

def test_case_9():
    str_0 = '_$'
    var_0 = module_1.maybe_unfrack_path(str_0)
    bool_0 = True
    str_1 = ''
    var_1 = module_1.create_base_parser(bool_0)
    int_0 = 10240
    sorting_help_formatter_0 = module_1.SortingHelpFormatter(int_0, int_0)
    var_2 = sorting_help_formatter_0.add_arguments(str_1)
    set_0 = {int_0, bool_0, bool_0, var_1, var_1, bool_0}
    var_3 = module_1.version(set_0)
    sorting_help_formatter_1 = module_1.SortingHelpFormatter(bool_0)
    ansible_version_0 = None
    bytes_0 = b'\n\x05<\x15\xb8\x15\xd3'
    unrecognized_argument_0 = module_1.UnrecognizedArgument(int_0, bytes_0, bool_0, sorting_help_formatter_1)
    tuple_0 = (bytes_0,)
    str_2 = 'o'
    var_4 = module_1.maybe_unfrack_path(str_2)
    int_1 = -1041
    str_3 = 'TF~)\te'
    ansible_version_1 = module_1.AnsibleVersion(int_1, ansible_version_0, str_3, unrecognized_argument_0, unrecognized_argument_0)
    str_4 = '1'
    bool_1 = None
    namespace_0 = module_0.Namespace()
    bool_2 = False
    argument_parser_0 = module_0.ArgumentParser(tuple_0, namespace_0, bool_2, str_1)
    var_5 = module_1.add_check_options(argument_parser_0)
    prepend_list_action_0 = module_1.PrependListAction(bool_0, ansible_version_1, str_4, bool_1)

def test_case_10():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_meta_options(argument_parser_0)
    var_1 = argument_parser_0.parse_args()

def test_case_11():
    namespace_0 = module_0.Namespace()
    str_0 = 'x'
    str_1 = 'valx'
    var_0 = module_1.ensure_value(namespace_0, str_0, str_1)
    str_2 = 'valy'
    str_3 = [str_2]
    var_1 = module_1.ensure_value(namespace_0, str_0, str_3)

def test_case_12():
    argument_parser_0 = module_0.ArgumentParser()
    var_0 = module_1.add_connect_options(argument_parser_0)
    str_0 = '--private-key'
    str_1 = './mykey.key'
    str_2 = '--ssh-common-args'
    str_3 = 'C:\\Windows\\System32\\cmd.exe'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = argument_parser_0.parse_args(str_4)
    str_5 = '--user'
    str_6 = 'administrator'
    str_7 = '--ssh-extra-args'
    str_8 = '-v'
    str_9 = [str_5, str_6, str_7, str_8]
    var_2 = argument_parser_0.parse_args(str_9)
    str_10 = '-k'
    str_11 = '--connection'
    str_12 = 'local'
    str_13 = '--connection-password-file'
    str_14 = 'mypass.txt'
    str_15 = '-c'
    str_16 = 'paramiko'
    str_17 = '--sftp-extra-args'
    str_18 = '-f'
    str_19 = [str_10, str_11, str_12, str_13, str_14, str_15, str_16, str_17, str_18]
    var_3 = argument_parser_0.parse_args(str_19)
    str_20 = '--timeout'
    str_21 = '-9'
    str_22 = [str_20, str_21]
    var_4 = argument_parser_0.parse_args(str_22)
    str_23 = '--scp-extra-args'
    str_24 = '-l'
    str_25 = [str_23, str_24]
    var_5 = argument_parser_0.parse_args(str_25)

def test_case_13():
    str_0 = 'ansible-test'
    argument_parser_0 = module_0.ArgumentParser(str_0)
    var_0 = module_1.add_async_options(argument_parser_0)
    str_1 = '-P'
    str_2 = '42'
    str_3 = '-B'
    str_4 = '666'
    str_5 = [str_1, str_2, str_3, str_4]
    var_1 = argument_parser_0.parse_args(str_5)

def test_case_14():
    str_0 = 'rQkC;y]@w$hnJG\n'
    str_1 = '.'
    var_0 = module_1.maybe_unfrack_path(str_1)
    var_1 = map(var_0, str_0)
    var_2 = list(var_1)

def test_case_15():
    str_0 = '.'
    str_1 = './'
    str_2 = '..'
    str_3 = '../'
    str_4 = './a'
    str_5 = '../a'
    str_6 = './a/b'
    str_7 = '../a/b'
    str_8 = [str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7]
    str_9 = '.'
    var_0 = module_1.maybe_unfrack_path(str_9)
    var_1 = map(var_0, str_8)
    var_2 = list(var_1)