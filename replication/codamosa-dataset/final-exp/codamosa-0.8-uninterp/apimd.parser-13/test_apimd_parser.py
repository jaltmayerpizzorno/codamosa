# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'typing.Tuple'
    bool_0 = module_0.is_public_family(str_0)

def test_case_2():
    str_0 = 'a'
    bool_0 = module_0.is_public_family(str_0)
    str_1 = '_a'
    bool_1 = module_0.is_public_family(str_1)
    str_2 = 'a.b'
    bool_2 = module_0.is_public_family(str_2)
    str_3 = 'a.__b__'
    bool_3 = module_0.is_public_family(str_3)
    str_4 = 'a._b'
    bool_4 = module_0.is_public_family(str_4)

def test_case_3():
    str_0 = ''
    dict_0 = {}
    parser_0 = module_0.Parser(dict_0)
    parser_0.parse(str_0, str_0)

def test_case_4():
    str_0 = ']%,I'
    bool_0 = module_0.is_magic(str_0)
    str_1 = 'dx'
    parser_0 = module_0.Parser()
    parser_0.parse(str_1, str_1)

def test_case_5():
    str_0 = 'O'
    str_1 = module_0.code(str_0)

def test_case_6():
    str_0 = '4$\x0cX6|R5re;"'
    str_1 = ''
    str_2 = "y$R'$:JM"
    dict_0 = {str_0: str_0, str_1: str_2}
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0, dict_0)
    str_3 = parser_0.compile()
    str_4 = module_0.code(str_0)

def test_case_7():
    str_0 = 'E\t7"m\x0bf\tjfo\n7'
    str_1 = module_0.esc_underscore(str_0)

def test_case_8():
    str_0 = 'f;UL!O/\nnxfn|vZo='
    str_1 = module_0.doctest(str_0)

def test_case_9():
    expr_0 = module_1.expr()
    str_0 = module_0.const_type(expr_0)

def test_case_10():
    str_0 = ''
    var_0 = {}
    resolver_0 = module_0.Resolver(str_0, var_0)
    int_0 = 0
    str_1 = 'typing.Union[int, float]'
    var_1 = module_1.parse(str_1)
    var_2 = var_1.body[int_0]
    var_3 = module_1.unparse(var_2)
    str_2 = '\rC'
    var_4 = module_1.parse(str_2)
    var_5 = resolver_0.visit(var_1)
    str_3 = 'typing.Optional[fnt]'
    var_6 = module_1.parse(str_3)
    var_7 = var_4.body[int_0]
    var_8 = resolver_0.visit(var_7)
    str_4 = 'Optional[int]'
    var_9 = module_1.parse(str_4)
    var_10 = var_9.body[int_0]

def test_case_11():
    parser_0 = module_0.Parser()
    str_0 = parser_0.compile()

def test_case_12():
    int_0 = -2550
    str_0 = None
    str_1 = None
    dict_0 = {str_0: str_1, str_1: str_1, str_1: str_1}
    parser_0 = module_0.Parser(int_0, dict_0, dict_0)
    str_2 = parser_0.compile()

def test_case_13():
    str_0 = ',[^2-g\r'
    import_from_0 = module_1.ImportFrom()
    str_1 = '@|?qyM'
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1}
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0, dict_0)
    parser_0.imports(str_0, import_from_0)
    str_2 = 'XQ'
    bool_0 = module_0.is_magic(str_2)

def test_case_14():
    str_0 = "f^7&Up}6'*"
    str_1 = 'dx'
    parser_0 = module_0.Parser()
    str_2 = module_0.esc_underscore(str_1)
    str_3 = 'collections.abc.Awaitable'
    list_0 = [str_0, parser_0]
    dict_0 = {}
    ann_assign_0 = module_1.AnnAssign(*list_0, **dict_0)
    parser_0.globals(str_3, ann_assign_0)

def test_case_15():
    str_0 = ''
    bool_0 = True
    parser_0 = module_0.Parser(bool_0)
    module_x_var_0 = None
    parser_0.load_docstring(str_0, module_x_var_0)
    var_0 = parser_0.__repr__()

def test_case_16():
    str_0 = ''
    str_1 = module_0.code(str_0)

def test_case_17():
    str_0 = 'yping.Tu'
    bool_0 = module_0.is_public_family(str_0)

def test_case_18():
    str_0 = '#'
    bool_0 = True
    parser_0 = module_0.Parser(bool_0)
    parser_0.parse(str_0, str_0)
    var_0 = parser_0.__repr__()
    str_1 = parser_0.compile()

def test_case_19():
    str_0 = '<'
    str_1 = None
    str_2 = '\x0bH8p^N'
    str_3 = 'g6'
    dict_0 = {str_0: str_1, str_0: str_2, str_0: str_3}
    list_0 = [dict_0, str_1, str_0]
    subscript_0 = module_1.Subscript(*list_0)
    str_4 = 'j'
    dict_1 = {}
    resolver_0 = module_0.Resolver(str_4, dict_1)
    a_s_t_0 = resolver_0.visit_Subscript(subscript_0)

def test_case_20():
    str_0 = 'SfJsq:uI2gQ Y1r}/JE'
    dict_0 = {str_0: str_0, str_0: str_0}
    parser_0 = module_0.Parser(dict_0, dict_0)
    str_1 = '\x0b7'
    list_0 = []
    list_1 = []
    parser_0.class_api(str_1, str_0, list_0, list_1)

def test_case_21():
    list_0 = []
    subscript_0 = module_1.Subscript()
    list_1 = [list_0, subscript_0]
    constant_0 = module_1.Constant(*list_1)
    str_0 = '<\r3'
    str_1 = '|%n8nL'
    dict_0 = {str_1: str_1}
    resolver_0 = module_0.Resolver(str_0, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)

def test_case_22():
    str_0 = 'SfJsq:uI2gQ Y1r}/JE'
    str_1 = 'D7^ Sn)xk"e'
    dict_0 = {str_1: str_0, str_0: str_0}
    parser_0 = module_0.Parser(dict_0, dict_0)
    str_2 = '*:'
    list_0 = []
    dict_1 = {}
    list_1 = [dict_1]
    parser_0.class_api(str_2, str_0, list_0, list_1)

def test_case_23():
    str_0 = 'int[3]'
    str_1 = '__main__'
    str_2 = 'typing'
    str_3 = '{"List":"List"}'
    str_4 = {str_1: str_2, str_2: str_3}
    resolver_0 = module_0.Resolver(str_1, str_4)
    int_0 = 0
    var_0 = module_1.parse(str_0)
    var_1 = var_0.body[int_0]
    var_2 = resolver_0.visit(var_1)
    var_3 = module_1.unparse(var_2)
    var_4 = print(var_3)

def test_case_24():
    str_0 = '__main__'
    str_1 = '__main__.abc'
    str_2 = '__main__.decimal'
    str_3 = 'W7aWF2%~'
    str_4 = '__main__.numbyrs'
    str_5 = 'decial.Deciml'
    str_6 = 'fractions.Fraction'
    str_7 = {str_1: str_1, str_2: str_5, str_3: str_6, str_4: str_1}
    resolver_0 = module_0.Resolver(str_0, str_7)
    int_0 = 0
    var_0 = module_1.parse(str_5)
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    var_3 = resolver_0.visit(var_2)