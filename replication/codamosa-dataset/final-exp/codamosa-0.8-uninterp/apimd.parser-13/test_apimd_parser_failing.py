# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1
import collections.abc as module_2

def test_case_0():
    try:
        str_0 = 'r'
        dict_0 = {str_0: str_0}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        str_1 = None
        str_2 = module_0.parent(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        attribute_0 = None
        str_0 = 'k2piP9^4lvsm*T\t'
        str_1 = 'collections.abc.MutableMapping'
        str_2 = 'Sw-c`A '
        dict_0 = {str_1: str_1, str_0: str_2}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)
    except BaseException:
        pass

def test_case_2():
    try:
        constant_0 = module_1.Constant()
        str_0 = '6m]*]?7-o'
        str_1 = '-.vNoH!J,.!o_'
        str_2 = 'g$\t'
        str_3 = '?$_Qw\r'
        dict_0 = {str_0: str_0, str_0: str_1, str_2: str_3}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '-'
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0)
        parser_0.parse(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        str_1 = 's^R[^eA,TqYm3#2'
        dict_0 = {str_1: str_1}
        import_0 = module_1.Import(**dict_0)
        str_2 = '0'
        str_3 = ' N&`"VQXMS\x0b3r'
        dict_1 = {str_3: str_2, str_3: str_3}
        parser_0 = module_0.Parser(dict_1, dict_1)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        str_1 = '3`'
        dict_0 = {str_0: str_1, str_1: str_0}
        import_from_0 = module_1.ImportFrom()
        parser_0 = module_0.Parser(dict_0)
        str_2 = 'm%ORl5}^[y'
        assign_0 = module_1.Assign()
        parser_0.globals(str_2, assign_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'PEnPCjB\x0bpm>'
        str_1 = '~Y<'
        str_2 = module_0.code(str_1)
        list_0 = [str_0, str_0, str_0]
        class_def_0 = module_1.ClassDef(*list_0)
        str_3 = module_0.doctest(str_2)
        parser_0 = module_0.Parser()
        parser_0.api(str_0, class_def_0)
    except BaseException:
        pass

def test_case_7():
    try:
        expr_0 = None
        str_0 = module_0.const_type(expr_0)
        str_1 = '%{sKkOQB@NdE!t\ty.LL'
        str_2 = "AX'/-x|@Js:"
        dict_0 = {str_1: str_1, str_0: str_1, str_2: str_1}
        import_from_0 = module_1.ImportFrom(**dict_0)
        str_3 = module_0.doctest(str_1)
        parser_0 = module_0.Parser()
        expr_1 = module_1.expr()
        ann_assign_0 = module_1.AnnAssign()
        str_4 = '3`'
        module_x_var_0 = None
        parser_0.load_docstring(str_4, module_x_var_0)
        str_5 = '@Kq+(w9N='
        str_6 = parser_0.resolve(str_5, expr_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        bool_1 = True
        str_0 = 'ct'
        set_0 = None
        dict_0 = {str_0: set_0}
        parser_0 = module_0.Parser(bool_0, bool_1, dict_0)
        bool_2 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        str_0 = 'ct'
        str_1 = None
        list_0 = [str_1, bool_0, str_0]
        arguments_0 = module_1.arguments(*list_0)
        dict_0 = {}
        bool_1 = False
        bool_2 = True
        bool_3 = True
        str_2 = 'EP`X\x0c.[l8tq&Puy\r\\@F'
        str_3 = '0k\x0bxB&#iM\n'
        dict_1 = {str_2: str_2, str_3: str_2}
        parser_0 = module_0.Parser(bool_3, dict_1)
        parser_0.func_api(str_1, str_0, arguments_0, dict_0, has_self=bool_1, cls_method=bool_2)
    except BaseException:
        pass

def test_case_10():
    try:
        iterable_0 = None
        str_0 = module_0.table(items=iterable_0)
    except BaseException:
        pass

def test_case_11():
    try:
        ann_assign_0 = module_1.AnnAssign()
        str_0 = 'De'
        dict_0 = {str_0: str_0}
        str_1 = 'typing.MutableSet'
        set_0 = {str_1}
        dict_1 = {str_0: set_0}
        parser_0 = module_0.Parser(dict_0, dict_1)
        var_0 = parser_0.__post_init__()
        str_2 = 'hT?kL#~Bs'
        int_0 = 1
        str_3 = 'i`<>\x0b9:]-'
        dict_2 = {}
        str_4 = 'I_?D_vZ'
        str_5 = 'ng'
        str_6 = "7' Z[exV"
        dict_3 = {str_2: str_3, str_4: str_5, str_2: str_6, str_2: str_4}
        parser_1 = module_0.Parser(int_0, dict_3, dict_3)
        list_0 = [str_1]
        str_7 = ',;?<\x0c4"\x0cq[e}\r+]'
        str_8 = ''
        import_0 = module_1.Import(*list_0)
        str_9 = "E=o{az'#pNm6OzSt?;0q"
        dict_4 = {str_7: int_0, str_8: dict_2, str_8: import_0, str_9: parser_0}
        class_def_0 = module_1.ClassDef(*list_0, **dict_4)
        parser_1.api(str_5, class_def_0, prefix=str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        str_0 = ''
        str_1 = '3=*Z\nESUb,\n P03/RT=o'
        dict_0 = {str_0: str_1}
        parser_0 = module_0.Parser(bool_0, bool_0, dict_0, dict_0)
        list_0 = [str_0, str_0, parser_0]
        attribute_0 = module_1.Attribute(*list_0)
        str_2 = '\x0bL*^8}p!a>e\x0cK?'
        resolver_0 = module_0.Resolver(str_0, dict_0, str_2)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)
        function_def_0 = module_1.FunctionDef()
        parser_0.api(str_2, function_def_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = False
        str_0 = '=\nbt\x0cP#'
        str_1 = ''
        dict_0 = {str_0: str_0, str_1: str_0}
        parser_0 = module_0.Parser(bool_0, dict_0)
        expr_0 = module_1.expr()
        list_0 = [expr_0, expr_0, expr_0, expr_0]
        dict_1 = {}
        name_0 = module_1.Name(**dict_1)
        list_1 = [name_0]
        int_0 = 1422
        str_2 = '"Ig'
        int_1 = -702
        str_3 = "Ykps+iG'lx$}QZ"
        int_2 = -1014
        dict_2 = {str_1: int_0, str_2: int_1, str_3: int_2}
        parser_1 = module_0.Parser(int_0, dict_2, dict_0)
        parser_1.class_api(str_1, str_1, list_0, list_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'PEnPCjB\x0bpm>'
        str_1 = '~Y<'
        str_2 = module_0.code(str_1)
        list_0 = [str_0, str_0, str_0]
        class_def_0 = module_1.ClassDef(*list_0)
        str_3 = module_0.doctest(str_2)
        list_1 = [str_3, str_0]
        import_from_0 = module_1.ImportFrom(*list_1)
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0, dict_0)
        parser_0.imports(str_1, import_from_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '+Mml=/=~{&I'
        bool_0 = module_0.is_public_family(str_0)
        str_1 = 'Acw4oB\r'
        str_2 = module_0.doctest(str_1)
        parser_0 = module_0.Parser()
        str_3 = 'XQ8H3zF8W?/9'
        expr_0 = module_1.expr()
        str_4 = '\r*Ir"\'iX$P(K9tl>\x0bk c'
        list_0 = [str_3]
        import_0 = module_1.Import(*list_0)
        parser_0.imports(str_4, import_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = True
        int_0 = 1273
        str_0 = 'XF6p x%`y0.$-6\\hkTv='
        dict_0 = {str_0: str_0, str_0: str_0}
        parser_0 = module_0.Parser(bool_0, int_0, dict_0, dict_0)
        str_1 = parser_0.compile()
        expr_0 = None
        str_2 = module_0.const_type(expr_0)
        str_3 = '%{sKkOQB@NdE!t\ty.LL'
        str_4 = 'Acw4oB\r'
        str_5 = "AX'/-x|@J:"
        str_6 = 'C0>"kYBKhVMF_BOI5&Ow'
        str_7 = module_0.doctest(str_6)
        dict_1 = {str_3: str_3, str_4: str_3, str_5: str_3}
        import_from_0 = module_1.ImportFrom(**dict_1)
        str_8 = module_0.doctest(str_4)
        parser_1 = module_0.Parser()
        expr_1 = module_1.expr()
        str_9 = None
        parser_1.imports(str_9, import_from_0)
        var_0 = parser_1.__repr__()
        ann_assign_0 = module_1.AnnAssign()
        str_10 = 'collections.abc.Container'
        bool_1 = module_0.is_public_family(str_10)
        str_11 = '__'
        str_12 = module_0.esc_underscore(str_11)
        str_13 = 'd#36MSsg'
        parser_0.globals(str_13, ann_assign_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = True
        str_0 = '\x0c~@&pd'
        dict_0 = {str_0: str_0}
        expr_0 = module_1.expr(**dict_0)
        str_1 = module_0.const_type(expr_0)
        set_0 = {expr_0}
        list_0 = [set_0, str_1, expr_0]
        subscript_0 = module_1.Subscript(*list_0)
        str_2 = '1{'
        dict_1 = {}
        resolver_0 = module_0.Resolver(str_2, dict_1)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
        int_0 = 1273
        dict_2 = {str_0: str_0, str_0: str_0}
        parser_0 = module_0.Parser(bool_0, int_0, dict_2, dict_2)
        str_3 = parser_0.compile()
        expr_1 = None
        str_4 = module_0.const_type(expr_1)
        str_5 = '%{sKkOQB@NdE!t\ty.LL'
        str_6 = 'Acw4oB\r'
        str_7 = "AX'/-x|@J:"
        dict_3 = {str_5: str_5, str_6: str_5, str_7: str_5}
        import_from_0 = module_1.ImportFrom(**dict_3)
        parser_1 = module_0.Parser()
        expr_2 = module_1.expr()
        str_8 = '3`'
        str_9 = module_0.esc_underscore(str_8)
        import_from_1 = module_1.ImportFrom(*list_0, **dict_3)
        str_10 = 'i\x0b\x0b'
        parser_0.imports(str_10, import_from_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'PEnPCjB\x0bpm>'
        str_1 = '~Y<'
        str_2 = module_0.code(str_1)
        list_0 = [str_0, str_0, str_0]
        class_def_0 = module_1.ClassDef(*list_0)
        str_3 = module_0.doctest(str_2)
        dict_0 = {}
        arguments_0 = module_1.arguments(*list_0, **dict_0)
        list_1 = [str_0]
        bool_0 = False
        bool_1 = False
        dict_1 = {}
        set_0 = None
        dict_2 = {str_2: set_0}
        str_4 = None
        str_5 = "&9A6\x0b'Bh\x0c}5%T"
        dict_3 = {str_4: str_5, str_5: str_3}
        parser_0 = module_0.Parser(bool_1, dict_1, dict_2, dict_3)
        parser_0.func_api(str_1, str_1, arguments_0, list_1, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'r:8D'
        list_0 = [str_0, str_0]
        assign_0 = module_1.Assign(*list_0)
        str_1 = '5A},'
        dict_0 = {str_1: str_1}
        parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
        parser_0.globals(str_0, assign_0)
        bool_0 = False
        bool_1 = True
        str_2 = 'ct'
        set_0 = None
        dict_1 = {str_2: set_0}
        parser_1 = module_0.Parser(bool_0, bool_1, dict_1)
        bool_2 = parser_1.is_public(str_2)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'w>x?6'
        list_0 = [str_0, str_0]
        constant_0 = module_1.Constant(*list_0)
        str_1 = "8VSsy&dNa\n}WXF'1XqF"
        dict_0 = {}
        resolver_0 = module_0.Resolver(str_1, dict_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
        str_2 = '*8'
        bool_0 = module_0.is_public_family(str_2)
        dict_1 = {}
        iterable_0 = module_2.Iterable(**dict_1)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = ''
        var_0 = {}
        resolver_0 = module_0.Resolver(str_0, var_0)
        int_0 = 0
        str_1 = 'typing.Tuple'
        var_1 = module_1.parse(str_1)
        var_2 = var_1.body[int_0]
        var_3 = resolver_0.visit(var_2)
        var_4 = module_1.unparse(var_3)
        str_2 = '\rC'
        var_5 = module_1.parse(str_2)
        var_6 = var_5.body[int_0]
        var_7 = resolver_0.visit(var_6)
        str_3 = 'typing.Optional[int]'
        var_8 = module_1.parse(str_3)
        var_9 = var_5.body[resolver_0]
    except BaseException:
        pass

def test_case_22():
    try:
        iterable_0 = None
        str_0 = '!'
        list_0 = [str_0, str_0]
        str_1 = module_0.table(*list_0, items=iterable_0)
    except BaseException:
        pass

def test_case_23():
    try:
        iterable_0 = None
        str_0 = ';1u_'
        str_1 = '</code>'
        list_0 = [str_0, str_1]
        str_2 = module_0.table(*list_0, items=iterable_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '\n-t'
        dict_0 = {str_0: str_0}
        list_0 = [dict_0]
        str_1 = 'w-Q(!wnXE}5C8%"'
        bool_0 = False
        str_2 = '$C+>J'
        dict_1 = {str_2: str_2, str_1: bool_0, str_2: str_2, str_2: str_2}
        assign_0 = module_1.Assign(*list_0, **dict_1)
        bool_1 = False
        parser_0 = module_0.Parser(bool_1)
        parser_0.globals(str_1, assign_0)
    except BaseException:
        pass