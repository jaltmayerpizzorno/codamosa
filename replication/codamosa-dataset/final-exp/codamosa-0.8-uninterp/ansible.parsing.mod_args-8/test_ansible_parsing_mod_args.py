# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    pass

def test_case_1():
    module_args_parser_0 = module_0.ModuleArgsParser()

def test_case_2():
    str_0 = 'action'
    str_1 = {str_0: str_0}
    module_args_parser_0 = module_0.ModuleArgsParser(str_1)
    var_0 = module_args_parser_0.parse()

def test_case_3():
    str_0 = 'action'
    str_1 = 'copy: src=a dest=b'
    str_2 = {str_0: str_1}
    module_args_parser_0 = module_0.ModuleArgsParser(str_2)
    var_0 = module_args_parser_0.parse()

def test_case_4():
    str_0 = 'action'
    str_1 = 'module'
    str_2 = 'src'
    str_3 = 'dest'
    str_4 = 'copy'
    str_5 = 'a'
    str_6 = 'b'
    str_7 = {str_1: str_4, str_2: str_5, str_3: str_6}
    str_8 = {str_0: str_7}
    var_0 = None
    module_args_parser_0 = module_0.ModuleArgsParser(str_8, var_0)
    var_1 = module_args_parser_0.parse()
    str_9 = 'copy src=a dest=b'
    str_10 = {str_0: str_9}
    module_args_parser_1 = module_0.ModuleArgsParser(str_10, str_9)
    var_2 = module_args_parser_1.parse()

def test_case_5():
    str_0 = 'name'
    str_1 = 'local_action'
    str_2 = 'E13#4:y<n8a!'
    str_3 = 'copy file to the node'
    str_4 = 'shell sleep 10'
    str_5 = {str_3: str_2, str_0: str_3, str_1: str_4}
    var_0 = []
    module_args_parser_0 = module_0.ModuleArgsParser(str_5, var_0)
    var_1 = module_args_parser_0.parse()

def test_case_6():
    str_0 = 'mdul'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    module_args_parser_0 = module_0.ModuleArgsParser(dict_0)
    str_1 = 'args'
    str_2 = 'echo hi'
    str_3 = {str_2: str_2}
    str_4 = {str_0: str_3, str_1: str_3}
    module_args_parser_1 = module_0.ModuleArgsParser(str_4, str_1)
    int_0 = -1636
    var_0 = module_args_parser_1.parse(int_0)
    int_1 = 3606
    var_1 = module_args_parser_1.parse(int_1)

def test_case_7():
    str_0 = 'action'
    str_1 = 'shell echo hi'
    str_2 = {str_0: str_1}
    module_args_parser_0 = module_0.ModuleArgsParser(str_2)
    var_0 = module_args_parser_0.parse()