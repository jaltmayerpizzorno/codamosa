# Automatically generated by Pynguin.
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        a_s_t_0 = None
        iterable_0 = module_0.find_variables(a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        class_def_0 = None
        str_0 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = None
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        arg_0 = module_1.arg()
        str_0 = 'F5+~D}`_LG-!0:<a\x0bgj;'
        list_0 = [variables_replacer_0, str_0]
        function_def_0 = module_1.FunctionDef(*list_0)
        function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        arg_0 = module_1.arg()
        str_0 = 'F5+~D}`_LG-!0:<a\x0bgj;'
        dict_1 = {str_0: str_0}
        variables_replacer_1 = module_0.VariablesReplacer(dict_1)
        arg_1 = variables_replacer_1.visit_arg(arg_0)
        name_0 = None
        name_1 = variables_replacer_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_4():
    try:
        import_from_0 = None
        str_0 = 'tkinter.colorchooser'
        list_0 = []
        str_1 = None
        dict_0 = {str_0: str_0, str_0: list_0, str_1: str_1}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'extend(abc)\nx = 123\nprint(x)'
        var_0 = module_2.parse(str_0)
        str_1 = 'extenp(abc)\npr4nt(x)'
        module_0.extend_tree(var_0, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        a_s_t_0 = module_1.AST()
        a_s_t_1 = module_1.AST()
        iterable_0 = module_0.find_variables(a_s_t_0)
        snippet_0 = module_0.snippet(iterable_0)
        a_s_t_2 = module_1.AST()
        list_0 = snippet_0.get_body()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'let(x); oo(x)'
        var_0 = module_2.parse(str_0)
        iterable_0 = module_0.find_variables(var_0)
        var_1 = list(iterable_0)
        str_1 = None
        list_0 = [var_1, str_0]
        except_handler_0 = module_1.ExceptHandler(*list_0)
        str_2 = 'X1\n,%RTm%1\x0b3?1Ni'
        dict_0 = {str_2: str_0, str_2: str_2}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
        dict_1 = {str_1: str_0, str_0: str_1, str_0: str_1}
        variables_replacer_1 = module_0.VariablesReplacer(dict_1)
        except_handler_2 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
        dict_2 = {}
        variables_replacer_2 = module_0.VariablesReplacer(dict_2)
        except_handler_3 = variables_replacer_2.visit_ExceptHandler(except_handler_2)
        dict_3 = {}
        variables_replacer_3 = module_0.VariablesReplacer(dict_3)
        except_handler_4 = variables_replacer_3.visit_ExceptHandler(except_handler_3)
        dict_4 = {str_0: str_1}
        variables_replacer_4 = module_0.VariablesReplacer(dict_4)
        a_s_t_0 = module_1.AST()
        module_0.extend_tree(a_s_t_0, dict_4)
        list_1 = [str_0, var_0]
        alias_0 = module_1.alias(*list_1)
        variables_replacer_5 = module_0.VariablesReplacer(dict_4)
        alias_1 = variables_replacer_5.visit_alias(alias_0)
        alias_2 = module_1.alias(*list_1)
        dict_5 = {str_1: str_0, str_0: str_0}
        variables_replacer_6 = module_0.VariablesReplacer(dict_5)
        arg_0 = module_1.arg()
        arg_1 = variables_replacer_4.visit_arg(arg_0)
        attribute_0 = module_1.Attribute()
        snippet_0 = module_0.snippet(alias_2)
        list_2 = snippet_0.get_body()
    except BaseException:
        pass