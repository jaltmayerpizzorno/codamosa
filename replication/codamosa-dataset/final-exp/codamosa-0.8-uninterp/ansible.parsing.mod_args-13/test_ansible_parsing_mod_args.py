# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    pass

def test_case_1():
    module_args_parser_0 = module_0.ModuleArgsParser()

def test_case_2():
    str_0 = 'something'
    var_0 = dict(action=str_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()

def test_case_3():
    str_0 = 'src=a dest=b'
    var_0 = dict(module=str_0, args=str_0)
    var_1 = dict(action=var_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_1)
    var_2 = module_args_parser_0.parse()

def test_case_4():
    str_0 = 'command'
    str_1 = '8odc!P^pPn\nL_gM}'
    str_2 = {str_0: str_1, str_0: str_0}
    var_0 = None
    module_args_parser_0 = module_0.ModuleArgsParser(str_2, var_0)
    var_1 = module_args_parser_0.parse()

def test_case_5():
    str_0 = 'include_role'
    str_1 = 'tasks'
    str_2 = 'handlers'
    str_3 = 'pre_tasks'
    str_4 = 'name'
    str_5 = {str_4: str_0}
    str_6 = 'action'
    str_7 = {str_6: str_6}
    str_8 = {str_6: str_6}
    str_9 = {str_0: str_5, str_1: str_3, str_2: str_7, str_3: str_8}
    module_args_parser_0 = module_0.ModuleArgsParser(str_9)
    bool_0 = False
    var_0 = module_args_parser_0.parse(bool_0)

def test_case_6():
    str_0 = 'local_action'
    str_1 = {str_0: str_0, str_0: str_0}
    module_args_parser_0 = module_0.ModuleArgsParser(str_1, str_1)
    var_0 = module_args_parser_0.parse()

def test_case_7():
    str_0 = 'localhost'
    str_1 = 'xyz=1'
    var_0 = dict(chdir=str_1, args=str_1)
    var_1 = dict(action=str_1, delegate_to=str_0, args=var_0)
    module_args_parser_0 = module_0.ModuleArgsParser(var_1)
    var_2 = module_args_parser_0.parse()

def test_case_8():
    str_0 = "{'delegate_to': None, 'register': 'logger_result', 'action': 'command', 'local_action': 'command', 'args': {'_raw_params': '{{ abc }}', '_uses_shell': True, 'chdir': None}, 'ignore_errors': False, 'warn': True}"
    str_1 = 'action'
    str_2 = 'localhost'
    str_3 = '/tmp'
    str_4 = 'xyz=1'
    var_0 = dict(chdir=str_3, args=str_4)
    var_1 = dict(action=str_1, delegate_to=str_2, args=str_0)
    var_2 = dict(chdir=str_3, args=str_4)
    module_args_parser_0 = module_0.ModuleArgsParser(var_1)
    var_3 = module_args_parser_0.parse()