# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        str_0 = None
        dict_0 = {str_0: str_0}
        list_0 = [str_0]
        name_0 = module_0.Name(*list_0)
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        name_1 = variables_replacer_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'P`0qXbu!d'
        dict_0 = {}
        list_0 = [str_0, dict_0]
        alias_0 = module_0.alias(*list_0)
        str_1 = 'h x V[H(R9kz@'
        dict_1 = {str_1: str_1, str_0: str_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_1)
        alias_1 = variables_replacer_0.visit_alias(alias_0)
    except BaseException:
        pass

def test_case_2():
    try:
        import_from_0 = None
        str_0 = 'HTTPPasswordMgr'
        dict_0 = {str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_3():
    try:
        except_handler_0 = None
        dict_0 = {}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'R\n'
        dict_0 = {}
        name_0 = module_0.Name()
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        name_1 = variables_replacer_0.visit_Name(name_0)
        variables_replacer_1 = module_1.VariablesReplacer(dict_0)
        str_1 = 'Y(0*]C`gJIL\x0ce\x0b#zZ1n\x0b'
        str_2 = '?;x9I;%3\x0cawwH\\('
        list_0 = []
        import_from_0 = module_0.ImportFrom(*list_0)
        snippet_0 = module_1.snippet(import_from_0)
        dict_1 = {str_0: str_0, str_0: str_0, str_1: str_2}
        variables_replacer_2 = module_1.VariablesReplacer(dict_1)
        snippet_1 = module_1.snippet(variables_replacer_2)
        list_1 = snippet_1.get_body()
    except BaseException:
        pass

def test_case_5():
    try:
        except_handler_0 = module_0.ExceptHandler()
        str_0 = "H\x0c}gDB|~.9'\t"
        list_0 = [str_0, except_handler_0]
        alias_0 = module_0.alias(*list_0)
        dict_0 = {str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        alias_1 = variables_replacer_0.visit_alias(alias_0)
        str_1 = ''
        dict_1 = {str_1: str_1, str_0: str_0, str_0: str_0, str_1: str_0}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        alias_2 = variables_replacer_1.visit_alias(alias_1)
        dict_2 = {str_0: str_0}
        variables_replacer_2 = module_1.VariablesReplacer(dict_2)
        alias_3 = variables_replacer_2.visit_alias(alias_2)
        dict_3 = {str_0: str_0}
        variables_replacer_3 = module_1.VariablesReplacer(dict_3)
        except_handler_1 = variables_replacer_3.visit_ExceptHandler(except_handler_0)
        arg_0 = module_0.arg()
        arg_1 = variables_replacer_3.visit_arg(arg_0)
        function_def_0 = None
        str_2 = 'copy_reg'
        str_3 = 'copyreg'
        dict_4 = {str_2: str_2, str_3: str_3, str_3: str_3, str_2: str_2}
        variables_replacer_4 = module_1.VariablesReplacer(dict_4)
        function_def_1 = variables_replacer_4.visit_FunctionDef(function_def_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'g>oaD'
        function_def_0 = module_0.FunctionDef()
        dict_0 = {str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
        str_1 = None
        str_2 = '8`Zy?K'
        str_3 = '\x0brH'
        dict_1 = {str_1: str_1, str_2: str_0, str_3: str_3}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        arg_0 = None
        variables_replacer_2 = module_1.VariablesReplacer(dict_1)
        arg_1 = variables_replacer_2.visit_arg(arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\nlet(vars)\nextend(vars)\nlet(vars)\nextend(vars)\nlet(vars)\nextend(vars)\n'
        var_0 = module_2.parse(str_0)
        iterable_0 = module_1.find_variables(var_0)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\nlet(vars)\nextend(vars)\nlet(vars)\nextend(vars)\nlet(vars)\nextend(vars)\n'
        var_0 = module_2.parse(str_0)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\nlet(vars)\nextend(vars)\nlet(vars)\nextend(vars)\ng.t(vars)\nextend(vars)\n'
        var_0 = module_2.parse(str_0)
        iterable_0 = module_1.find_variables(var_0)
        list_0 = []
        except_handler_0 = module_0.ExceptHandler(*list_0)
        dict_0 = {str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        module_1.let(except_handler_0)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass