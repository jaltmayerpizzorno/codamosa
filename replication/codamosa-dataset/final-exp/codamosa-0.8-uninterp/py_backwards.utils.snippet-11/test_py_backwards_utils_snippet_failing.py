# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        attribute_0 = module_0.Attribute()
        str_0 = 'dbm.gnu'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)
        a_s_t_0 = None
        iterable_0 = module_1.find_variables(a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_s_t_0 = module_0.AST()
        iterable_0 = module_1.find_variables(a_s_t_0)
        list_0 = [iterable_0]
        keyword_0 = module_0.keyword(*list_0)
        dict_0 = {}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        keyword_1 = variables_replacer_0.visit_keyword(keyword_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'let(x); y; x.z; x(); let(z); let(x);'
        var_0 = module_2.parse(str_0)
        iterable_0 = module_1.find_variables(var_0)
        var_1 = list(str_0)
        a_s_t_0 = module_0.AST()
        str_1 = 'v\tWG'
        str_2 = ';8?\r4NS/`U-FwYhwmiw'
        str_3 = 'su\tpn].\x0bpI:0'
        dict_0 = {str_1: str_0, str_0: str_0, str_2: a_s_t_0, str_3: str_1}
        module_1.let(var_1)
        import_from_0 = module_0.ImportFrom()
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_3():
    try:
        alias_0 = None
        dict_0 = {}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        alias_1 = variables_replacer_0.visit_alias(alias_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b' \xc6\xc2'
        set_0 = {bytes_0}
        snippet_0 = module_1.snippet(set_0)
        list_0 = snippet_0.get_body()
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        list_1 = [list_0]
        name_0 = module_0.Name(*list_1)
        str_0 = '?s5g\\QzsJ\n\x0bE_ph}'
        dict_0 = {str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        name_1 = variables_replacer_0.visit_Name(name_0)
        str_1 = '>3'
        str_2 = None
        dict_1 = {str_1: str_1, str_2: str_2}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        name_2 = variables_replacer_1.visit_Name(name_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'a = 18'
        str_1 = 'let(a) + extend(a)'
        str_2 = '3.1'
        function_def_0 = module_0.FunctionDef()
        str_3 = '+}dMP36rBHb!LKrut$H'
        dict_0 = {str_3: str_2, str_1: str_1, str_1: str_3}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        str_4 = 'tkMessageBox'
        dict_1 = {str_4: str_1}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        str_5 = 'C^l9~AF=<\t>DY\x0c)9i?'
        a_s_t_0 = module_0.AST()
        iterable_0 = module_1.find_variables(a_s_t_0)
        dict_2 = {str_2: str_1, str_1: str_2, str_5: str_2}
        var_0 = module_2.parse(str_1)
        list_0 = [str_2, str_1, iterable_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        variables_replacer_2 = module_1.VariablesReplacer(dict_2)
        import_from_1 = variables_replacer_2.visit_ImportFrom(import_from_0)
        variables_replacer_3 = module_1.VariablesReplacer(dict_2)
        import_from_2 = variables_replacer_3.visit_ImportFrom(import_from_1)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "\n2inSD'4i"
        str_1 = ''
        function_def_0 = None
        str_2 = None
        dict_0 = {str_2: str_2, str_1: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\nx = 1\nextend(vars)\n    '
        var_0 = module_2.parse(str_0)
        int_0 = 0
        var_1 = module_2.parse(str_0)
        var_2 = var_0.body[int_0]
        var_3 = var_2.value
        var_4 = {str_0: var_3}
        module_1.extend_tree(var_0, var_4)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'let(a)'
        var_0 = module_2.parse(str_0)
        str_1 = 'a = 1'
        var_1 = module_2.parse(str_1)
        str_2 = 'let(a) + extend(a)'
        var_2 = module_2.parse(str_2)
        module_1.extend_tree(var_2, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\ny = let(x) + let(y)\n'
        var_0 = module_2.parse(str_0)
        iterable_0 = module_1.find_variables(var_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'a = 18'
        str_1 = 'let(a) + extend(a)'
        attribute_0 = module_0.Attribute()
        str_2 = 'QJ9\tMF\x0b3o'
        dict_0 = {str_2: str_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)
        function_def_0 = module_0.FunctionDef()
        str_3 = ':f^rts6\nyo*>y#zvl'
        dict_1 = {str_3: str_1}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        function_def_1 = variables_replacer_1.visit_FunctionDef(function_def_0)
        str_4 = '+}dMP36rBHb!LKrut$H'
        dict_2 = {str_4: str_1, str_1: str_4}
        except_handler_0 = module_0.ExceptHandler()
        except_handler_1 = variables_replacer_1.visit_ExceptHandler(except_handler_0)
        except_handler_2 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
        except_handler_3 = variables_replacer_1.visit_ExceptHandler(except_handler_2)
        except_handler_4 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
        except_handler_5 = variables_replacer_1.visit_ExceptHandler(except_handler_2)
        except_handler_6 = variables_replacer_1.visit_ExceptHandler(except_handler_3)
        variables_replacer_2 = module_1.VariablesReplacer(dict_2)
        str_5 = 'tkMessageBox'
        dict_3 = {str_5: str_1}
        variables_replacer_3 = module_1.VariablesReplacer(dict_3)
        function_def_2 = variables_replacer_3.visit_FunctionDef(function_def_0)
        str_6 = 'C^l9~AF=<\t>DY~\x0c=9\n?'
        a_s_t_0 = module_0.AST()
        iterable_0 = module_1.find_variables(a_s_t_0)
        dict_4 = {str_6: a_s_t_0, str_3: str_1, str_2: str_3, str_5: str_3}
        var_0 = module_2.parse(str_1)
        list_0 = [str_6, str_1, iterable_0]
        class_def_0 = module_0.ClassDef()
        class_def_1 = variables_replacer_1.visit_ClassDef(class_def_0)
        class_def_2 = variables_replacer_1.visit_ClassDef(class_def_1)
        class_def_3 = variables_replacer_2.visit_ClassDef(class_def_2)
        import_from_0 = module_0.ImportFrom(*list_0)
        variables_replacer_4 = module_1.VariablesReplacer(dict_4)
        import_from_1 = variables_replacer_4.visit_ImportFrom(import_from_0)
        module_1.let(variables_replacer_3)
        import_from_2 = variables_replacer_3.visit_ImportFrom(import_from_1)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'a = 18'
        str_1 = 'L.let(a) + extend(a)'
        attribute_0 = module_0.Attribute()
        str_2 = 'QJ9\tMF\x0b3o'
        dict_0 = {str_2: str_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)
        function_def_0 = module_0.FunctionDef()
        str_3 = ':f^rts6\nyo*>y#zvl'
        dict_1 = {str_3: str_1}
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        function_def_1 = variables_replacer_1.visit_FunctionDef(function_def_0)
        except_handler_0 = module_0.ExceptHandler()
        except_handler_1 = variables_replacer_1.visit_ExceptHandler(except_handler_0)
        except_handler_2 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
        except_handler_3 = variables_replacer_1.visit_ExceptHandler(except_handler_2)
        except_handler_4 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
        except_handler_5 = variables_replacer_1.visit_ExceptHandler(except_handler_2)
        except_handler_6 = variables_replacer_1.visit_ExceptHandler(except_handler_3)
        function_def_2 = variables_replacer_1.visit_FunctionDef(function_def_1)
        str_4 = 'tkMessageBox'
        dict_2 = {str_4: str_1}
        variables_replacer_2 = module_1.VariablesReplacer(dict_2)
        function_def_3 = variables_replacer_2.visit_FunctionDef(function_def_2)
        str_5 = 'C^l9~AF=<\t>DY~\x0c=9\n?'
        a_s_t_0 = module_0.AST()
        iterable_0 = module_1.find_variables(a_s_t_0)
        dict_3 = {str_3: str_1, str_1: str_3, str_5: str_3}
        var_0 = module_2.parse(str_1)
        list_0 = [str_5, str_1, iterable_0]
        class_def_0 = module_0.ClassDef()
        class_def_1 = variables_replacer_1.visit_ClassDef(class_def_0)
        class_def_2 = variables_replacer_1.visit_ClassDef(class_def_1)
        class_def_3 = variables_replacer_1.visit_ClassDef(class_def_2)
        import_from_0 = module_0.ImportFrom(*list_0)
        variables_replacer_3 = module_1.VariablesReplacer(dict_3)
        import_from_1 = variables_replacer_3.visit_ImportFrom(import_from_0)
        module_1.let(variables_replacer_2)
        import_from_2 = variables_replacer_2.visit_ImportFrom(import_from_1)
        module_1.extend_tree(var_0, str_0)
    except BaseException:
        pass