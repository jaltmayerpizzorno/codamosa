# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast._ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'let(x); x = 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)

def test_case_2():
    str_0 = 'YGl]b8acacByJVR'
    dict_0 = {str_0: str_0, str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)

def test_case_3():
    str_0 = 'let(x); x= 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    dict_0 = {str_0: str_0}
    dict_1 = {str_0: str_0, str_0: str_0}
    a_s_t_0 = module_2.AST(**dict_1)
    module_1.extend_tree(a_s_t_0, dict_0)
    keyword_0 = module_2.keyword()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    float_0 = -3110.0
    list_0 = [float_0, keyword_0, float_0]
    list_1 = [str_0, list_0, a_s_t_0]
    class_def_0 = module_2.ClassDef(*list_1)
    class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)

def test_case_4():
    arg_0 = module_2.arg()
    str_0 = ',|?'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    arg_1 = variables_replacer_0.visit_arg(arg_0)

def test_case_5():
    str_0 = 'let(x); x = 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    var_1 = list(iterable_0)
    import_from_0 = module_2.ImportFrom()
    dict_0 = {str_0: iterable_0, str_0: import_from_0}
    class_def_0 = module_2.ClassDef(**dict_0)
    str_1 = None
    a_s_t_0 = module_2.AST()
    dict_1 = {str_0: str_0, str_1: str_1, str_0: a_s_t_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_1)
    class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)
    dict_2 = {}
    a_s_t_1 = module_2.AST(**dict_0)
    module_1.extend_tree(a_s_t_1, dict_2)
    function_def_0 = module_2.FunctionDef()

def test_case_6():
    str_0 = 'let(x); x = 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    dict_0 = {}
    a_s_t_0 = module_2.AST()
    name_0 = module_2.Name()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    variables_replacer_1 = module_1.VariablesReplacer(dict_0)
    name_1 = variables_replacer_1.visit_Name(name_0)
    module_1.extend_tree(a_s_t_0, dict_0)
    attribute_0 = module_2.Attribute()

def test_case_7():
    str_0 = 'Y?ah`{XwCUpm9i5.\nbU'
    dict_0 = {str_0: str_0, str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    dict_1 = None
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    attribute_0 = module_2.Attribute()
    attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)

def test_case_8():
    str_0 = 'let(x); x= 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    dict_0 = {str_0: str_0}
    dict_1 = {str_0: str_0, str_0: str_0}
    a_s_t_0 = module_2.AST(**dict_1)
    module_1.extend_tree(a_s_t_0, dict_0)
    keyword_0 = module_2.keyword()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)

def test_case_9():
    str_0 = '-r'
    class_def_0 = module_2.ClassDef()
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)
    dict_1 = {str_0: str_0}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)

def test_case_10():
    str_0 = 'let(x); x= 1'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    dict_0 = {str_0: str_0}
    dict_1 = {str_0: str_0, str_0: str_0}
    a_s_t_0 = module_2.AST(**dict_1)
    module_1.extend_tree(a_s_t_0, dict_0)
    keyword_0 = module_2.keyword()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    float_0 = -3110.0
    list_0 = [float_0, keyword_0, float_0]
    list_1 = [str_0, list_0, a_s_t_0]
    class_def_0 = module_2.ClassDef(*list_1)
    import_from_0 = module_2.ImportFrom(*list_1)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)
    module_1.let(iterable_0)

def test_case_11():
    str_0 = 'k'
    except_handler_0 = module_2.ExceptHandler()
    str_1 = 'J\rHK7GO=x>A=w0'
    str_2 = ':=|[BE'
    dict_0 = {str_1: str_0, str_1: str_1, str_0: str_0, str_2: str_1}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
    str_3 = ']uOxF"z^'
    list_0 = None
    dict_1 = {str_3: str_3, str_3: list_0}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    except_handler_2 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
    dict_2 = {}
    variables_replacer_2 = module_1.VariablesReplacer(dict_2)
    except_handler_3 = variables_replacer_2.visit_ExceptHandler(except_handler_2)
    dict_3 = {str_0: str_0}
    variables_replacer_3 = module_1.VariablesReplacer(dict_3)

def test_case_12():
    str_0 = 'YGl]b8acacByJVR'
    dict_0 = {str_0: str_0, str_0: str_0}
    a_s_t_0 = module_2.AST()
    module_1.extend_tree(a_s_t_0, dict_0)
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)

def test_case_13():
    a_s_t_0 = module_2.AST()
    function_def_0 = module_2.FunctionDef()
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    module_1.extend(a_s_t_0)
    iterable_0 = module_1.find_variables(a_s_t_0)

def test_case_14():
    str_0 = '\nlet(x)\nlet(y)\nx += 1\ny += 2\nprint(x, y)\n'
    var_0 = module_0.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)
    var_1 = module_0.dump(var_0)

def test_case_15():
    str_0 = 'Vxten(varsQ)'
    var_0 = module_0.parse(str_0)
    var_1 = {str_0: str_0}
    module_1.extend_tree(var_0, var_1)

def test_case_16():
    str_0 = 'exten.d(vars_)'
    var_0 = module_0.parse(str_0)
    str_1 = 'extend(vars__)'
    str_2 = ' = 0'
    str_3 = "cZ8T5 (T(u;\nO4'\\Eu,3"
    dict_0 = {str_2: str_0, str_1: str_3, str_0: str_3}
    list_0 = [str_2]
    alias_0 = module_2.alias(*list_0)
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    alias_1 = variables_replacer_0.visit_alias(alias_0)
    import_from_0 = module_2.ImportFrom(*list_0)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    import_from_2 = variables_replacer_0.visit_ImportFrom(import_from_1)
    variables_replacer_1 = module_1.VariablesReplacer(dict_0)
    variables_replacer_2 = module_1.VariablesReplacer(dict_0)
    alias_2 = variables_replacer_2.visit_alias(alias_1)
    variables_replacer_3 = module_1.VariablesReplacer(dict_0)
    str_4 = 'CX:V./\ru\x0b'
    dict_1 = {str_4: str_4}
    variables_replacer_4 = module_1.VariablesReplacer(dict_1)
    str_5 = 'x = 200'
    var_1 = {str_2: str_5}
    str_6 = 'X9'
    dict_2 = {str_6: str_6, str_5: str_5, str_1: var_0, str_1: str_1}
    a_s_t_0 = module_2.AST(**dict_2)
    iterable_0 = module_1.find_variables(a_s_t_0)
    module_1.extend_tree(var_0, var_1)
    module_1.extend_tree(a_s_t_0, dict_1)
    module_1.let(dict_2)