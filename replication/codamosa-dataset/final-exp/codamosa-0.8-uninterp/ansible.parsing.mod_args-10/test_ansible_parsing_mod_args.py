# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    pass

def test_case_1():
    module_args_parser_0 = module_0.ModuleArgsParser()

def test_case_2():
    str_0 = 'shell'
    str_1 = 'some'
    var_0 = dict(action=str_0, delegate_to=str_1)
    module_args_parser_0 = module_0.ModuleArgsParser(var_0)
    var_1 = module_args_parser_0.parse()

def test_case_3():
    str_0 = 'shell echo hi'
    var_0 = dict(module=str_0)
    var_1 = dict(action=var_0)
    var_2 = None
    module_args_parser_0 = module_0.ModuleArgsParser(var_1, var_2)
    var_3 = module_args_parser_0.parse()

def test_case_4():
    str_0 = 'test_task_name'
    str_1 = 'echo'
    str_2 = '"{{ test_task_name }}"'
    bool_0 = True
    var_0 = dict(_raw_params=str_2, _uses_shell=bool_0)
    var_1 = dict(module=str_1, args=var_0)
    bool_1 = False
    str_3 = 'root'
    str_4 = ''
    var_2 = dict(name=str_0, action=var_1, delegate_to=str_1, become=bool_1, become_user=str_3, async_val=var_1, poll=bool_1, when=str_4)
    module_args_parser_0 = module_0.ModuleArgsParser(var_2)
    var_3 = module_args_parser_0.parse()

def test_case_5():
    var_0 = dict()
    str_0 = 'setup'
    str_1 = 'no'
    var_1 = dict(gather_facts=str_1)
    var_2 = dict(module=str_0, args=var_1)
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = 4
    int_4 = 5
    int_5 = [int_0, int_1, int_2, int_3, int_4]
    bool_0 = False
    str_2 = '{{ out }}'
    var_3 = dict(result=str_2)
    var_4 = dict(action=var_2, with_items=int_5, changed_when=bool_0, register=var_3)
    var_5 = None
    module_args_parser_0 = module_0.ModuleArgsParser(var_4, var_5)
    var_6 = module_args_parser_0.parse()

def test_case_6():
    str_0 = 'action'
    str_1 = 'shell echo hi'
    str_2 = {str_0: str_1}
    module_args_parser_0 = module_0.ModuleArgsParser(str_2)
    var_0 = module_args_parser_0.parse()
    str_3 = 'b'
    str_4 = {str_0: str_3}
    module_args_parser_1 = module_0.ModuleArgsParser(str_4)
    var_1 = module_args_parser_1.parse()
    str_5 = 'action'
    str_6 = 'local_action'
    str_7 = 'copy'
    str_8 = {str_5: str_2, str_6: str_7}
    module_args_parser_2 = module_0.ModuleArgsParser()
    module_args_parser_3 = module_0.ModuleArgsParser(str_8)
    var_2 = module_args_parser_3.parse()

def test_case_7():
    str_0 = 'action'
    str_1 = 'delegate_to'
    str_2 = 'args'
    str_3 = 'copy src=test dest=test2'
    str_4 = 'localhost'
    str_5 = 'test'
    str_6 = 'a'
    str_7 = {str_5: str_6}
    str_8 = {str_0: str_3, str_1: str_4, str_2: str_7}
    module_args_parser_0 = module_0.ModuleArgsParser(str_8)
    var_0 = module_args_parser_0.parse()

def test_case_8():
    str_0 = 'conflicting action statements'
    str_1 = 'uObt'
    str_2 = 'aka*qp'
    str_3 = {str_0: str_1}
    str_4 = '|ozN}}I'
    dict_0 = {str_2: str_3}
    module_args_parser_0 = module_0.ModuleArgsParser(dict_0)
    var_0 = module_args_parser_0.parse(str_4)
    module_args_parser_1 = module_0.ModuleArgsParser(str_3)
    module_args_parser_2 = module_0.ModuleArgsParser()