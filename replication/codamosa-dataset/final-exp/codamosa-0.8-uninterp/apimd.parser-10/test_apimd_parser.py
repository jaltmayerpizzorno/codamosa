# Automatically generated by Pynguin.
import ast as module_0
import apimd.parser as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'cQ=Be"F#'
    name_0 = module_0.Name()
    list_0 = [str_0, name_0]
    name_1 = module_0.Name(*list_0)
    str_1 = '0KNpdAQ\x0c=n!5A}'
    str_2 = None
    dict_0 = {str_1: str_1, str_1: str_1, str_2: str_2, str_1: str_2}
    resolver_0 = module_1.Resolver(str_1, dict_0)
    a_s_t_0 = resolver_0.visit_Name(name_1)
    bool_0 = False
    parser_0 = module_1.Parser(bool_0)
    var_0 = parser_0.__repr__()

def test_case_2():
    str_0 = '\x0c8aNy U'
    int_0 = 1572
    str_1 = module_1.parent(str_0, level=int_0)

def test_case_3():
    str_0 = 'BL.\tU^dw+LxTkc'
    bool_0 = module_1.is_magic(str_0)

def test_case_4():
    str_0 = 'BL.\tU^dw+LxTkc'
    bool_0 = module_1.is_magic(str_0)
    bool_1 = module_1.is_public_family(str_0)

def test_case_5():
    parser_0 = module_1.Parser()
    str_0 = parser_0.compile()
    str_1 = module_1.doctest(str_0)

def test_case_6():
    expr_0 = module_0.expr()
    str_0 = module_1.const_type(expr_0)

def test_case_7():
    str_0 = '+Tn!K/fOypK1'
    dict_0 = {}
    resolver_0 = module_1.Resolver(str_0, dict_0)

def test_case_8():
    str_0 = ')W'
    str_1 = module_1.doctest(str_0)
    list_0 = [str_1]
    constant_0 = module_0.Constant(*list_0)
    str_2 = 'x'
    dict_0 = {str_2: str_2, str_1: str_0, str_2: str_1, str_1: str_0}
    resolver_0 = module_1.Resolver(str_1, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    bool_0 = module_1.is_public_family(str_0)
    dict_1 = {}
    class_def_0 = module_0.ClassDef()
    str_3 = 'k~H\t'
    resolver_1 = module_1.Resolver(str_2, dict_1, str_3)
    a_s_t_1 = resolver_1.visit_Constant(constant_0)

def test_case_9():
    class_def_0 = None
    list_0 = [class_def_0, class_def_0, class_def_0]
    ann_assign_0 = module_0.AnnAssign(*list_0)
    list_1 = [class_def_0, class_def_0, ann_assign_0]
    subscript_0 = module_0.Subscript(*list_1)
    dict_0 = {}
    str_0 = 'dmrQ]"~ pd}MA'
    resolver_0 = module_1.Resolver(str_0, dict_0, str_0)
    a_s_t_0 = resolver_0.visit_Subscript(subscript_0)

def test_case_10():
    parser_0 = module_1.Parser()

def test_case_11():
    dict_0 = {}
    str_0 = 'QY'
    str_1 = None
    str_2 = '~'
    str_3 = '__'
    dict_1 = {str_0: str_0, str_1: str_2, str_2: str_3}
    parser_0 = module_1.Parser(dict_0, dict_1, dict_1)
    str_4 = parser_0.compile()

def test_case_12():
    bool_0 = True
    str_0 = "08Wa|@UP'\nnGrY.I2W8T"
    dict_0 = {str_0: str_0}
    parser_0 = module_1.Parser(bool_0, dict_0)
    import_from_0 = module_0.ImportFrom()
    parser_0.imports(str_0, import_from_0)

def test_case_13():
    parser_0 = module_1.Parser()
    str_0 = parser_0.compile()
    list_0 = [str_0]
    ann_assign_0 = module_0.AnnAssign(*list_0)
    parser_0.globals(str_0, ann_assign_0)

def test_case_14():
    list_0 = []
    stmt_0 = None
    list_1 = [stmt_0, stmt_0, stmt_0]
    bool_0 = True
    dict_0 = {}
    str_0 = None
    dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    parser_0 = module_1.Parser(bool_0, dict_0, dict_1, dict_1)
    parser_0.class_api(str_0, str_0, list_0, list_1)

def test_case_15():
    parser_0 = module_1.Parser()
    str_0 = '&\r eU\rhb%I.!h6{'
    str_1 = '0D\x0c.&,oq'
    str_2 = '!K/6E")}'
    str_3 = '# Module `{}`'
    dict_0 = {str_0: str_0, str_1: str_1, str_2: str_0, str_3: parser_0}
    expr_0 = module_0.expr(**dict_0)
    str_4 = parser_0.resolve(str_0, expr_0)
    str_5 = parser_0.compile()
    list_0 = [str_5]
    ann_assign_0 = module_0.AnnAssign(*list_0)
    parser_0.globals(str_5, ann_assign_0)

def test_case_16():
    parser_0 = module_1.Parser()
    str_0 = parser_0.compile()

def test_case_17():
    bool_0 = True
    dict_0 = {}
    str_0 = None
    str_1 = '~U!X\\3^jwWHI'
    dict_1 = {str_0: str_0, str_0: str_0, str_0: str_1, str_0: str_0}
    parser_0 = module_1.Parser(bool_0, dict_0, dict_1, dict_1)
    str_2 = '|\\\x0bRINQ}74WfM-]\n})#'
    list_0 = [str_2, bool_0]
    assign_0 = module_0.Assign(*list_0)
    parser_0.globals(str_2, assign_0)

def test_case_18():
    constant_0 = module_0.Constant()
    dict_0 = {constant_0: constant_0}
    str_0 = '07K+ 4=97\rIB]N4%'
    dict_1 = {str_0: dict_0}
    class_def_0 = module_0.ClassDef(**dict_1)
    list_0 = [dict_0, class_def_0]
    attribute_0 = module_0.Attribute(*list_0, **dict_1)
    str_1 = 'n\\~XO=\n`cj2kr'
    str_2 = 'Vgwre2'
    str_3 = '--version'
    str_4 = ''
    dict_2 = {str_2: str_1, str_2: str_2, str_3: str_4}
    str_5 = 'w>R)p\n'
    resolver_0 = module_1.Resolver(str_1, dict_2, str_5)
    a_s_t_0 = resolver_0.visit_Attribute(attribute_0)

def test_case_19():
    dict_0 = {}
    str_0 = 'g&jq'
    str_1 = module_1.code(str_0)
    resolver_0 = module_1.Resolver(str_0, dict_0)
    parser_0 = module_1.Parser()
    str_2 = parser_0.compile()
    list_0 = [str_2]
    ann_assign_0 = module_0.AnnAssign(*list_0)
    parser_0.globals(str_2, ann_assign_0)

def test_case_20():
    str_0 = 'v=ZM,C&^z'
    str_1 = '7\r#vhS'
    int_0 = -2292
    bool_0 = True
    parser_0 = module_1.Parser(int_0, bool_0)
    str_2 = module_1.code(str_1)
    var_0 = parser_0.__repr__()
    str_3 = module_1.doctest(str_0)
    str_4 = 'dUyfz!siWj\'"wzy2;'
    str_5 = 'et'
    parser_0.parse(str_4, str_5)

def test_case_21():
    str_0 = 'L|+m[8E\t(=r\x0cS`*\\Aa'
    int_0 = 80
    bool_0 = True
    parser_0 = module_1.Parser(int_0, bool_0)
    str_1 = module_1.parent(str_0, level=int_0)
    module_x_var_0 = None
    parser_0.load_docstring(str_1, module_x_var_0)
    str_2 = module_1.code(str_0)
    str_3 = module_1.doctest(str_2)
    str_4 = 'e'
    parser_0.parse(str_4, str_4)
    str_5 = parser_0.compile()

def test_case_22():
    str_0 = 'd^WKk2YR`'
    str_1 = 'f>i@:8U9B5hCC0'
    bool_0 = False
    dict_0 = {}
    parser_0 = module_1.Parser(bool_0, dict_0)
    import_from_0 = module_0.ImportFrom()
    parser_0.imports(str_0, import_from_0)
    str_2 = module_1.esc_underscore(str_1)
    str_3 = 'A`0_:PU{. "EyOD_*E'
    str_4 = module_1.esc_underscore(str_3)
    list_0 = [parser_0, str_1, str_2]
    ann_assign_0 = module_0.AnnAssign(*list_0)
    str_5 = 'Tf'
    parser_0.globals(str_5, ann_assign_0)
    str_6 = 'R4ACB3\x0c7i+(P3MrW|'
    str_7 = module_1.doctest(str_6)

def test_case_23():
    list_0 = []
    stmt_0 = None
    list_1 = [stmt_0, stmt_0, stmt_0]
    bool_0 = False
    str_0 = '__'
    str_1 = module_1.doctest(str_0)
    bool_1 = module_1.is_public_family(str_0)
    dict_0 = {}
    str_2 = None
    str_3 = 'k6`rS'
    str_4 = '/fi~@F{k{hJRn\\x^O\x0br'
    str_5 = module_1.esc_underscore(str_4)
    dict_1 = {str_2: str_2, str_2: str_2, str_2: str_3, str_2: str_2}
    str_6 = '\tG3xgC?Qxnv[`%>B\rS&'
    str_7 = module_1.esc_underscore(str_3)
    dict_2 = {str_2: str_6, str_3: str_2}
    parser_0 = module_1.Parser(bool_0, dict_0, dict_1, dict_2)
    parser_0.class_api(str_2, str_2, list_0, list_1)
    str_8 = '|\\\x0bRINQ}74WfM-]\n})#'
    list_2 = [str_8, bool_0]
    str_9 = None
    arguments_0 = module_0.arguments(*list_2)
    dict_3 = {str_8: arguments_0}
    constant_0 = module_0.Constant(*list_2, **dict_3)
    str_10 = '}02m}>g`?+]I/t6e'
    resolver_0 = module_1.Resolver(str_10, dict_2)
    bool_2 = module_1.is_public_family(str_4)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    dict_4 = {str_8: str_9}
    parser_1 = module_1.Parser(dict_0, dict_4, dict_4, dict_1)
    ann_assign_0 = module_0.AnnAssign(*list_2)
    str_11 = module_1.parent(str_10)

def test_case_24():
    str_0 = '>>> print("a")'
    str_1 = module_1.doctest(str_0)

def test_case_25():
    str_0 = '>>> print("a")'
    str_1 = module_1.doctest(str_0)
    str_2 = '>>> print("a")\nok'
    str_3 = module_1.doctest(str_2)
    str_4 = '>>> print("a")\n>>> print("b")'
    str_5 = module_1.doctest(str_4)
    str_6 = '>>> print("a")\nok\n>>> print("b")'
    str_7 = module_1.doctest(str_6)