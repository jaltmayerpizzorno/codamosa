# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    pass

def test_case_1():
    module_args_parser_0 = module_0.ModuleArgsParser()

def test_case_2():
    bytes_0 = b'\xf4\x8d\xb9\xf3\x94\xceKo<4O\xfc\xe8\xaf'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_args_parser_0 = module_0.ModuleArgsParser(dict_0)

def test_case_3():
    str_0 = 'shell echo hi'
    var_0 = dict(action=str_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()

def test_case_4():
    str_0 = 'action'
    str_1 = 'args'
    str_2 = 'shell'
    str_3 = 'chdir'
    str_4 = 'h'
    str_5 = {str_3: str_4, str_4: str_4}
    str_6 = {str_0: str_2, str_1: str_5}
    module_args_parser_0 = module_0.ModuleArgsParser(str_6)
    var_0 = module_args_parser_0.parse()

def test_case_5():
    str_0 = 'y'
    var_0 = dict(local_action=str_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()
    str_1 = 'otherhost'
    var_2 = dict(local_action=str_0, delegate_to=str_1)

def test_case_6():
    str_0 = 'w7_jC`eBi[@\x0c 1-@=='
    var_0 = dict(local_action=str_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()
    var_2 = dict(local_action=str_0, delegate_to=str_0)

def test_case_7():
    str_0 = 'j+\x0b\t/s^;sp6O\r/9)-'
    var_0 = dict(shell=str_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()

def test_case_8():
    str_0 = 'action'
    str_1 = 'module'
    str_2 = 'ec2'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    module_args_parser_0 = module_0.ModuleArgsParser(str_4)
    str_5 = 'local_action'
    str_6 = {str_1: str_2}
    var_0 = module_args_parser_0.parse()
    str_7 = {str_1: str_2}
    str_8 = {str_0: str_6, str_5: str_7}
    module_args_parser_1 = module_0.ModuleArgsParser(str_8)