# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    try:
        str_0 = '~gf\ra%cy]Jun86V. .'
        bool_0 = True
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        parser_0 = module_0.Parser(bool_0, dict_0, dict_0)
        parser_1 = module_0.Parser()
        bool_1 = module_0.is_magic(str_0)
        str_1 = module_0.code(str_0)
        parser_1.parse(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/($`Y`$cO,RNk"f&.'
        str_1 = '0ZUKXBHz\x0c!"D'
        expr_0 = None
        list_0 = [expr_0, expr_0]
        list_1 = None
        bool_0 = False
        list_2 = [bool_0]
        constant_0 = module_1.Constant(*list_2)
        str_2 = 'q5J.%]>\x0buAe^'
        str_3 = 'pKU2Q^9W+=dg'
        str_4 = None
        dict_0 = {str_2: str_0, str_1: str_3, str_0: str_3, str_4: str_3}
        resolver_0 = module_0.Resolver(str_1, dict_0, str_1)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
        str_5 = 'M]+KQ?AKvw?M>N'
        dict_1 = {str_5: str_5, str_3: str_3, str_3: str_0}
        parser_0 = module_0.Parser(dict_1, dict_1)
        parser_0.class_api(str_0, str_1, list_0, list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'typing.List[typing.List[int]]'
        str_1 = ''
        var_0 = {}
        resolver_0 = module_0.Resolver(str_1, var_0)
        var_1 = module_1.parse(str_0)
        list_0 = [str_1]
        constant_0 = module_1.Constant(*list_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
    except BaseException:
        pass

def test_case_3():
    try:
        name_0 = module_1.Name()
        str_0 = 'lK/Y)j'
        str_1 = 'LUYe w\t>$P\tA,07>Y5\n'
        str_2 = 'VI'
        str_3 = 'VI'
        str_4 = '.'
        dict_0 = {str_0: str_0, str_1: str_0, str_0: str_2, str_3: str_4}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "bw6eg\t.'>6R6h-"
        str_1 = 'Td.\nK*1P(\x0biu,#C'
        str_2 = '..g*?'
        str_3 = 'b&)<f bB:yT]'
        str_4 = '0\\Fqu1|-4E0U3IQew'
        list_0 = [str_0]
        import_0 = module_1.Import(*list_0)
        int_0 = 1
        bool_0 = True
        dict_0 = {str_2: str_2, str_1: str_2, str_3: str_1}
        parser_0 = module_0.Parser(int_0, bool_0, dict_0, dict_0)
        parser_0.imports(str_4, import_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'typingList[typing.List[int]]'
        var_0 = {}
        resolver_0 = module_0.Resolver(str_0, var_0)
        var_1 = module_1.parse(str_0)
        var_2 = resolver_0.visit(var_1)
        str_1 = 'fo15MN45ta1|}vcF]'
        import_0 = module_1.Import()
        bool_0 = False
        parser_0 = module_0.Parser(bool_0)
        parser_0.imports(str_1, import_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'K'
        async_function_def_0 = None
        int_0 = -920
        str_1 = '$;'
        str_2 = 'VI'
        str_3 = 'wUnS1'
        str_4 = "885{#z'\x0c@uF:X-"
        str_5 = 'SY;82*ZU+21%{^G'
        str_6 = None
        dict_0 = {str_1: str_2, str_3: str_3, str_3: str_4, str_5: str_6}
        parser_0 = module_0.Parser(int_0, dict_0)
        parser_0.api(str_0, async_function_def_0, prefix=str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        list_0 = [str_0, str_0, str_0]
        list_1 = [str_0, list_0]
        dict_0 = {}
        arguments_0 = module_1.arguments(*list_1, **dict_0)
        expr_0 = module_1.expr()
        bool_0 = False
        dict_1 = {}
        dict_2 = {}
        parser_0 = module_0.Parser(dict_1, dict_2, dict_2)
        parser_0.func_api(str_0, str_0, arguments_0, expr_0, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        int_0 = 328
        str_1 = 'Y}F@K=G$'
        str_2 = 'g:*=[+iv9#'
        dict_0 = {str_1: str_1, str_1: str_1, str_1: str_2}
        parser_0 = module_0.Parser(int_0, dict_0)
        bool_0 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '+ ['
        expr_0 = module_1.expr()
        bool_0 = False
        str_1 = 'Kd.QBawij:_Y[ l~p'
        int_0 = 371
        str_2 = 'typing.ItemsView'
        str_3 = 'K\r@rNU*X89WD7YN\\@GF'
        int_1 = 362
        dict_0 = {str_1: int_0, str_2: int_0, str_3: int_0, str_2: int_1}
        dict_1 = {}
        parser_0 = module_0.Parser(bool_0, dict_0, dict_1, dict_1)
        str_4 = parser_0.resolve(str_0, expr_0)
        sequence_0 = None
        iterator_0 = module_0.walk_body(sequence_0)
        dict_2 = {}
        ann_assign_0 = module_1.AnnAssign(**dict_2)
        list_0 = [str_1, dict_1, ann_assign_0, str_0]
        function_def_0 = module_1.FunctionDef(*list_0)
        parser_0.api(str_2, function_def_0)
    except BaseException:
        pass

def test_case_10():
    try:
        stmt_0 = None
        str_0 = 'typing.Abstract=et'
        parser_0 = module_0.Parser()
        parser_0.parse(str_0, str_0)
        expr_0 = module_1.expr()
        str_1 = module_0.const_type(expr_0)
        str_2 = 'JS_E`EbthVNrbA"&'
        list_0 = [expr_0, expr_0, expr_0]
        list_1 = [stmt_0, stmt_0, stmt_0, stmt_0]
        parser_0.class_api(str_2, str_2, list_0, list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Xx+<rBhb-BQ\\|$4<n'
        str_1 = module_0.code(str_0)
        str_2 = '[X'
        str_3 = module_0.code(str_2)
        list_0 = [str_3, str_0, str_3, str_3]
        import_from_0 = module_1.ImportFrom(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '5y3*A'
        str_1 = 'VI'
        dict_0 = {str_0: str_0, str_1: str_1, str_0: str_1}
        name_0 = module_1.Name(**dict_0)
        list_0 = [name_0, name_0]
        name_1 = module_1.Name(*list_0)
        str_2 = '\x0b%0+6\t454D#3#Qm:@8'
        dict_1 = {}
        resolver_0 = module_0.Resolver(str_2, dict_1)
        a_s_t_0 = resolver_0.visit_Name(name_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        str_1 = 'Z*'
        list_0 = [str_1, str_1, str_1]
        dict_0 = {str_1: str_1}
        arguments_0 = module_1.arguments(*list_0, **dict_0)
        none_type_0 = None
        bool_0 = True
        bool_1 = True
        str_2 = ''
        str_3 = '%~gv:mw'
        str_4 = 'I+'
        str_5 = 'Write file: '
        dict_1 = {str_2: str_3, str_4: str_3, str_4: str_5, str_5: str_5}
        parser_0 = module_0.Parser(bool_1, dict_1)
        parser_0.func_api(str_0, str_1, arguments_0, none_type_0, has_self=bool_0, cls_method=bool_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'tTqL`_j_Ef\\C{57z'
        str_1 = '|mV5^QR[`z0<4G_A'
        str_2 = 'typing.ChainMap'
        bool_0 = module_0.is_magic(str_1)
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2}
        dict_1 = {}
        ann_assign_0 = module_1.AnnAssign()
        bool_1 = module_0.is_public_family(str_1)
        bool_2 = True
        str_3 = '2Z0OGD:/Lo=>"{6'
        str_4 = module_0.esc_underscore(str_0)
        str_5 = 'k2p)"L b&Tw?&'
        str_6 = '~Vo\x0c~_4n3V()c1#f'
        str_7 = 'typing.Pattern'
        dict_2 = {str_6: str_1, str_6: str_2, str_3: str_2, str_7: bool_2, str_0: dict_0}
        import_from_0 = module_1.ImportFrom(**dict_2)
        bool_3 = False
        parser_0 = module_0.Parser(bool_3, dict_1)
        str_8 = parser_0.compile()
        int_0 = -2300
        int_1 = 0
        str_9 = None
        int_2 = -95
        dict_3 = {str_0: int_1, str_1: int_0, str_9: int_1, str_9: int_2}
        dict_4 = {}
        dict_5 = {}
        parser_1 = module_0.Parser(int_0, bool_3, dict_3, dict_0, dict_4, dict_5)
        parser_1.imports(str_6, import_from_0)
        str_10 = '5r2)ee\rcGZ\x0cg;'
        dict_6 = {str_2: str_3, str_5: str_3, str_0: str_10, str_1: str_1}
        parser_2 = module_0.Parser(bool_2, dict_6, dict_0)
        str_11 = 'pa<6'
        parser_2.globals(str_11, ann_assign_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = True
        str_0 = 'MAS,{8Mj4luT5:'
        str_1 = '@-:PeVHU%'
        dict_0 = {str_0: str_1}
        parser_0 = module_0.Parser(bool_0, dict_0, dict_0, dict_0, dict_0)
        str_2 = parser_0.compile()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'lT8dg\x0bk}Gh\\.h\\*#~6;'
        list_0 = [str_0, str_0, str_0]
        ann_assign_0 = module_1.AnnAssign(*list_0)
        function_def_0 = module_1.FunctionDef(*list_0)
        bool_0 = False
        str_1 = '/lyB^)g*P=\x0c|Z%y'
        str_2 = '?dsz'
        set_0 = {str_2}
        dict_0 = {str_0: set_0}
        dict_1 = {str_2: str_1}
        parser_0 = module_0.Parser(bool_0, bool_0, dict_1, dict_0, dict_1)
        parser_0.api(str_0, function_def_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'str'
        int_0 = -448
        bool_0 = False
        dict_0 = {}
        parser_0 = module_0.Parser(int_0, bool_0, dict_0, dict_0, dict_0)
        parser_1 = module_0.Parser(int_0)
        ann_assign_0 = None
        parser_1.globals(str_0, ann_assign_0)
        str_1 = 'HFmD[\nr#y(h9^u'
        dict_1 = {str_1: str_1}
        list_0 = [str_0, str_0]
        name_0 = module_1.Name(*list_0)
        resolver_0 = module_0.Resolver(str_1, dict_1)
        a_s_t_0 = resolver_0.visit_Name(name_0)
        expr_0 = None
        str_2 = module_0.const_type(expr_0)
        constant_0 = module_1.Constant(*list_0)
        a_s_t_1 = resolver_0.visit_Constant(constant_0)
        var_0 = parser_0.__repr__()
        str_3 = 'G=1=B'
        bool_1 = parser_1.is_public(str_3)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'CPJzF q-\t=\x0b.5'
        list_0 = [str_0, str_0]
        dict_0 = {}
        import_from_0 = module_1.ImportFrom(*list_0, **dict_0)
        bool_0 = True
        int_0 = 1661
        parser_0 = module_0.Parser(bool_0, int_0)
        parser_0.imports(str_0, import_from_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'lT8dg\x0bk}Gh\\.h\\*#~6;'
        list_0 = [str_0, str_0, str_0]
        ann_assign_0 = module_1.AnnAssign(*list_0)
        bool_0 = False
        str_1 = "Rr]7'_)"
        dict_0 = {str_1: str_1, str_1: str_1}
        parser_0 = module_0.Parser(bool_0, dict_0, dict_0, dict_0)
        parser_0.globals(str_0, ann_assign_0)
        parser_1 = module_0.Parser(dict_0)
        str_2 = '`w]{!@'
        str_3 = '@\\WPpRiK'
        dict_1 = {str_2: ann_assign_0, str_3: bool_0, str_1: str_3, str_1: list_0}
        import_from_0 = module_1.ImportFrom(*list_0, **dict_1)
        str_4 = '2e)6om}Q**D{R\tF8on'
        parser_0.imports(str_4, import_from_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '_\t@BlhnS<)H gX8'
        str_1 = module_0.doctest(str_0)
        bool_0 = module_0.is_public_family(str_0)
        str_2 = '/nQ[47lU?/Sfg'
        str_3 = '#D\ry'
        list_0 = []
        list_1 = []
        bool_1 = True
        str_4 = '&26`k\r~4R\x0cQz`'
        int_0 = 20
        int_1 = 143
        str_5 = 'ap'
        dict_0 = {str_4: int_0, str_1: int_1, str_5: int_1}
        str_6 = '_6'
        dict_1 = {str_1: str_2, str_1: str_6, str_1: str_2}
        parser_0 = module_0.Parser(dict_0, dict_1, dict_1)
        var_0 = parser_0.__eq__(list_1)
        bool_2 = False
        dict_2 = {str_3: str_1}
        parser_1 = module_0.Parser(bool_1, bool_2, dict_2)
        parser_1.class_api(str_0, str_3, list_0, list_1)
        bool_3 = False
        dict_3 = {}
        parser_2 = module_0.Parser(bool_3, dict_3)
        str_7 = parser_2.compile()
        subscript_0 = module_1.Subscript()
        resolver_0 = module_0.Resolver(str_7, dict_3)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
    except BaseException:
        pass