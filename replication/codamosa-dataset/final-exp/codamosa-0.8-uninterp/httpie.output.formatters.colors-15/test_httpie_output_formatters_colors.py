# Automatically generated by Pynguin.
import httpie.output.formatters.colors as module_0
import httpie.context as module_1
import pygments.formatters.terminal256 as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = '<html/>'
    optional_0 = module_0.get_lexer(str_0, str_0)

def test_case_2():
    str_0 = 'hm/>'
    optional_0 = module_0.get_lexer(str_0)

def test_case_3():
    str_0 = 'application/json'
    bool_0 = True
    optional_0 = module_0.get_lexer(str_0, bool_0, str_0)

def test_case_4():
    str_0 = 'hm/>'
    optional_0 = module_0.get_lexer(str_0, str_0, str_0)

def test_case_5():
    str_0 = 'application/json'
    str_1 = '_o{/</Km\x0b '
    optional_0 = module_0.get_lexer(str_0, str_1)
    optional_1 = module_0.get_lexer(str_1)
    environment_0 = module_1.Environment()
    str_2 = 'format_options'
    bool_0 = True
    dict_0 = {str_2: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, bool_0, **dict_0)
    str_3 = color_formatter_0.format_body(str_2, str_1)
    terminal256_formatter_0 = module_2.Terminal256Formatter()
    solarized256_style_0 = module_0.Solarized256Style()
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()

def test_case_6():
    str_0 = 'application/json'
    str_1 = '_o{/</Km\x0b '
    optional_0 = module_0.get_lexer(str_0, str_1)
    optional_1 = module_0.get_lexer(str_1)
    environment_0 = module_1.Environment()
    str_2 = 'format_options'
    str_3 = ':Hq'
    bool_0 = True
    dict_0 = {str_2: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, bool_0, **dict_0)
    str_4 = color_formatter_0.format_body(str_3, str_0)
    solarized256_style_0 = module_0.Solarized256Style()
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    dict_1 = None
    set_0 = set()
    optional_2 = module_0.get_lexer(str_0, dict_1, set_0)