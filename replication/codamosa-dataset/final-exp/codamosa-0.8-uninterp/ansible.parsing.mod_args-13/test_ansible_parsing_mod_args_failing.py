# Automatically generated by Pynguin.
import ansible.parsing.mod_args as module_0

def test_case_0():
    try:
        str_0 = '5Fg5jWh>A(Df/J;e+'
        module_args_parser_0 = module_0.ModuleArgsParser(str_0)
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
        str_0 = 'test_action_plugin'
        str_1 = {str_0: str_0}
        module_args_parser_0 = module_0.ModuleArgsParser(str_1, str_1)
        var_0 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'action'
        str_1 = 'args'
        str_2 = 'name'
        str_3 = {str_0: str_0, str_1: str_0, str_2: str_0}
        str_4 = [str_0]
        module_args_parser_0 = module_0.ModuleArgsParser(str_3, str_4)
        var_0 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'something'
        var_0 = dict(module=str_0)
        var_1 = dict(action=var_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_1)
        var_2 = module_args_parser_0.parse()
        var_3 = dict(action=var_2)
        module_args_parser_1 = module_0.ModuleArgsParser(var_3)
        var_4 = module_args_parser_1.parse()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'something'
        var_0 = dict(module=str_0)
        var_1 = dict(action=var_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_1)
        var_2 = dict(action=var_1)
        module_args_parser_1 = module_0.ModuleArgsParser(var_2)
        var_3 = module_args_parser_1.parse()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'i]M 8\nBdc!P^pPn\nL_g}'
        var_0 = dict(action=str_0)
        module_args_parser_0 = module_0.ModuleArgsParser(var_0)
        var_1 = module_args_parser_0.parse()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'test_action_plugin'
        str_1 = {str_0: str_0}
        module_args_parser_0 = module_0.ModuleArgsParser(str_1, str_1)
        var_0 = module_args_parser_0.parse(module_args_parser_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '%tH$_k-N{Yaj&QRQ"}e'
        str_1 = 'YF^e)fz|vu&/.'
        bool_0 = True
        var_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_0, str_0: str_0, str_0: str_1, str_0: str_0, str_0: bool_0, str_1: str_0}
        module_args_parser_0 = module_0.ModuleArgsParser(var_0, str_1)
        var_1 = module_args_parser_0.parse(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'nam3'
        str_1 = 'local_action'
        str_2 = 'my task'
        str_3 = 'copyhsrc=z dest=b'
        str_4 = {str_0: str_2, str_1: str_3}
        var_0 = []
        module_args_parser_0 = module_0.ModuleArgsParser(str_4, var_0)
        var_1 = module_args_parser_0.parse(str_4)
    except BaseException:
        pass