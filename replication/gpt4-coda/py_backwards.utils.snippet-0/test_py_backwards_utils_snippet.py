# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    iterable_0 = module_1.find_variables(a_s_t_0)

def test_case_2():
    str_0 = "3@;l'C77xt"
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)

def test_case_3():
    attribute_0 = module_0.Attribute()
    str_0 = 'K\x0b"u{zP{"l'
    str_1 = 'vf\\"DD4Jt'
    str_2 = None
    dict_0 = None
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    dict_1 = {str_0: str_0, str_1: str_1, str_2: str_1}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    attribute_1 = variables_replacer_1.visit_Attribute(attribute_0)

def test_case_4():
    arg_0 = module_0.arg()
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    arg_1 = variables_replacer_0.visit_arg(arg_0)

def test_case_5():
    function_def_0 = module_0.FunctionDef()
    str_0 = 'f8]U6w_="nYTB4Dn"i|'
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    dict_1 = {}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    function_def_2 = variables_replacer_1.visit_FunctionDef(function_def_1)
    str_1 = None
    dict_2 = {str_1: str_1}
    variables_replacer_2 = module_1.VariablesReplacer(dict_2)
    function_def_3 = variables_replacer_2.visit_FunctionDef(function_def_2)

def test_case_6():
    name_0 = module_0.Name()
    snippet_0 = module_1.snippet(name_0)
    list_0 = None
    list_1 = [name_0, list_0]
    function_def_0 = module_0.FunctionDef(*list_1)
    str_0 = 'N Sj,rI%p\x0cF\\:J]\r@$FW'
    str_1 = None
    a_s_t_0 = module_0.AST()
    dict_0 = {str_0: str_0, str_1: a_s_t_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    str_2 = 'd+/\x0b[eKU:s !-Te,,^='
    str_3 = None
    a_s_t_1 = module_0.AST()
    str_4 = 'Tkconstants'
    dict_1 = {str_2: str_3, str_3: a_s_t_1, str_4: a_s_t_1, str_2: str_3}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    function_def_2 = variables_replacer_1.visit_FunctionDef(function_def_1)
    str_5 = '\tVyy)XBgd_ J\rN3|l)*'
    dict_2 = {str_5: str_5, str_5: str_5, str_5: str_5}
    variables_replacer_2 = module_1.VariablesReplacer(dict_2)
    function_def_3 = variables_replacer_2.visit_FunctionDef(function_def_2)
    str_6 = '\rAp=wm:zGwl&@Qt12$'
    str_7 = 'to(]/BX\\\x0b'
    dict_3 = {str_6: str_6, str_6: str_6, str_6: str_6, str_7: str_6}
    variables_replacer_3 = module_1.VariablesReplacer(dict_3)
    function_def_4 = variables_replacer_3.visit_FunctionDef(function_def_3)

def test_case_7():
    tuple_0 = None
    snippet_0 = module_1.snippet(tuple_0)
    list_0 = [tuple_0, snippet_0]
    name_0 = module_0.Name(*list_0)
    str_0 = "3@;l'C77xt"
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    name_1 = variables_replacer_0.visit_Name(name_0)

def test_case_8():
    a_s_t_0 = module_0.AST()
    str_0 = 'f+\x0c^i>7$QhP'
    str_1 = "V'v,"
    str_2 = 'f#{Cm2~'
    dict_0 = {str_1: a_s_t_0, str_2: a_s_t_0, str_0: str_2, str_0: str_1}
    module_1.let(a_s_t_0)
    keyword_0 = module_0.keyword()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)
    iterable_0 = module_1.find_variables(a_s_t_0)

def test_case_9():
    str_0 = '|4Tb]5'
    dict_0 = {str_0: str_0, str_0: str_0}
    class_def_0 = module_0.ClassDef(**dict_0)
    str_1 = None
    dict_1 = {str_1: str_1, str_1: str_1, str_1: str_1}
    variables_replacer_0 = module_1.VariablesReplacer(dict_1)
    class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)
    class_def_2 = variables_replacer_0.visit_ClassDef(class_def_1)
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    class_def_3 = variables_replacer_0.visit_ClassDef(class_def_2)

def test_case_10():
    str_0 = "@1l'T77xt"
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    list_0 = [str_0]
    str_1 = 'edQ#.Sc'
    dict_1 = {str_0: variables_replacer_0, str_1: list_0, str_1: str_1, str_0: dict_0}
    import_from_0 = module_0.ImportFrom(*list_0, **dict_1)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)

def test_case_11():
    str_0 = "@1l'T77xt"
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    list_0 = [str_0]
    str_1 = 'configparser'
    except_handler_0 = module_0.ExceptHandler()
    except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
    str_2 = 'edQ#.Sc'
    dict_1 = {str_0: variables_replacer_0, str_1: list_0, str_2: str_2, str_0: dict_0}
    import_from_0 = module_0.ImportFrom(*list_0, **dict_1)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)

def test_case_12():
    a_s_t_0 = module_0.AST()
    dict_0 = {}
    module_1.extend_tree(a_s_t_0, dict_0)

def test_case_13():
    a_s_t_0 = module_0.AST()
    module_1.let(a_s_t_0)
    iterable_0 = module_1.find_variables(a_s_t_0)

def test_case_14():
    a_s_t_0 = module_0.AST()
    str_0 = 'f+\x0c^i>7$QhP'
    dict_0 = {str_0: str_0, str_0: str_0}
    keyword_0 = module_0.keyword(**dict_0)
    iterable_0 = module_1.find_variables(a_s_t_0)
    module_1.extend(a_s_t_0)