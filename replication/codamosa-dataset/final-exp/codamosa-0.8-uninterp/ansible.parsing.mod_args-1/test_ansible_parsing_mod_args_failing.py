# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    try:
        bytes_0 = b'\x7f\xb5Q\x16\x9b9'
        module_args_parser_0 = module_0.ModuleArgsParser(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_args_parser_0 = module_0.ModuleArgsParser()
        var_0 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'bar'
        var_0 = dict(foo=str_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'bar'
        var_0 = dict(action=str_0, args=str_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'bar'
        var_0 = dict(foo=str_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_0.parse(var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'st-module'
        module_args_parser_0 = module_0.ModuleArgsParser()
        var_0 = dict(action=module_args_parser_0)
        module_args_parser_1 = module_0.ModuleArgsParser(var_0, str_0)
        var_1 = module_args_parser_1.parse()
    except BaseException:
        pass

def test_case_6():
    try:
        module_args_parser_0 = module_0.ModuleArgsParser()
        str_0 = 'test-module'
        var_0 = dict(action=str_0)
        module_args_parser_1 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_1.parse()
        var_2 = dict(action=module_args_parser_0, args=module_args_parser_1)
        module_args_parser_2 = module_0.ModuleArgsParser(var_2, var_0)
        var_3 = module_args_parser_2.parse()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'bar'
        var_0 = dict(foo=str_0)
        var_1 = dict(action=var_0, args=var_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_1, var_0)
        var_2 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '6P2P0Tn.\n,S0H'
        var_0 = dict(action=str_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'action'
        str_1 = 'module'
        str_2 = 'args'
        str_3 = 'warn'
        str_4 = 'echo hi'
        bool_0 = False
        var_0 = {str_1: str_3, str_2: str_4, str_3: bool_0}
        var_1 = {str_0: var_0}
        var_2 = None
        module_args_parser_0 = module_0.ModuleArgsParser()
        module_args_parser_1 = module_0.ModuleArgsParser(var_1, var_2)
        var_3 = module_args_parser_1.parse()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'b'
        module_args_parser_0 = module_0.ModuleArgsParser()
        str_1 = 'shell'
        str_2 = 'localhost'
        int_0 = 80
        str_3 = 'x'
        var_0 = {str_2: str_0, str_1: int_0, str_1: str_3, str_3: int_0}
        module_args_parser_1 = module_0.ModuleArgsParser(var_0)
        var_1 = module_args_parser_1.parse()
        float_0 = 607.9
        var_2 = module_args_parser_1.parse(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        module_args_parser_0 = module_0.ModuleArgsParser()
        var_0 = dict(foo=module_args_parser_0)
        module_args_parser_1 = module_0.ModuleArgsParser(var_0, var_0)
        var_1 = module_args_parser_1.parse(var_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'local_action'
        str_1 = 'test_name'
        str_2 = 'test_delegate_to'
        var_0 = {}
        var_1 = {}
        var_2 = {str_0: str_1, str_0: str_0, str_0: str_2, str_0: var_0, str_1: var_1}
        str_3 = 'test_collection_list'
        str_4 = [str_3, var_0, str_1]
        module_args_parser_0 = module_0.ModuleArgsParser(var_2, str_4)
        var_3 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'action'
        str_1 = 'module'
        str_2 = 'args'
        str_3 = 'command'
        str_4 = 'echo hi'
        bool_0 = False
        var_0 = {str_1: str_3, str_2: str_4, str_2: bool_0}
        var_1 = {str_0: var_0}
        var_2 = None
        module_args_parser_0 = module_0.ModuleArgsParser(var_1, var_2)
        var_3 = module_args_parser_0.parse()
    except BaseException:
        pass