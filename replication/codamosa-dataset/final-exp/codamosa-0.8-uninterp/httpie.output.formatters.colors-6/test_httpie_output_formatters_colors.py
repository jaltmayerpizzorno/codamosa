# Automatically generated by Pynguin.
import httpie.output.formatters.colors as module_0
import httpie.context as module_1
import pygments.lexers as module_2

def test_case_0():
    solarized256_style_0 = module_0.Solarized256Style()

def test_case_1():
    str_0 = 'xzq\x0cH9tZ6/4xG*,cT'
    optional_0 = module_0.get_lexer(str_0)

def test_case_2():
    str_0 = 'M/xp'
    optional_0 = module_0.get_lexer(str_0, str_0)

def test_case_3():
    environment_0 = module_1.Environment()
    str_0 = '^bytes (?P<first_byte_pos>\\d+)-(?P<last_b.te_pos>\\d+)/(\\*|(?P<instance_eenh>\\d+)),'
    optional_0 = module_0.get_lexer(str_0, environment_0, str_0)

def test_case_4():
    str_0 = 'foo/bar'
    bool_0 = False
    optional_0 = module_0.get_lexer(str_0, bool_0)
    str_1 = 'foo/bar+json'
    optional_1 = module_0.get_lexer(str_1)
    str_2 = 'json'
    optional_2 = module_0.get_lexer(str_1)
    str_3 = 'application/json'
    optional_3 = module_0.get_lexer(str_3)
    var_0 = module_2.get_lexer_by_name(str_2)
    str_4 = '{}'
    optional_4 = module_0.get_lexer(str_3, str_4)
    var_1 = module_2.get_lexer_by_name(str_2)
    str_5 = 'text/plain'
    bool_1 = True
    optional_5 = module_0.get_lexer(str_5, bool_1, str_4)
    var_2 = module_2.get_lexer_by_name(str_2)

def test_case_5():
    str_0 = 'foo/bar+json'
    optional_0 = module_0.get_lexer(str_0)
    str_1 = 'json'
    str_2 = 'application/json'
    optional_1 = module_0.get_lexer(str_2)
    var_0 = module_2.get_lexer_by_name(str_1)
    str_3 = '{}'
    optional_2 = module_0.get_lexer(str_2, str_3)
    var_1 = module_2.get_lexer_by_name(str_1)
    bool_0 = True
    optional_3 = module_0.get_lexer(str_0, bool_0, str_3)