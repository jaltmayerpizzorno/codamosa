# Automatically generated by Pynguin.
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'x./G'
    optional_0 = module_0.get_lexer(str_0)

def test_case_2():
    str_0 = '\n    Translate `max-age` into `expires` for Requests to take it into account.\n\n    HACK/FIXME: <https://github.com/psf/requests/issues/5743>\n\n    '
    environment_0 = module_1.Environment()
    optional_0 = module_0.get_lexer(str_0, environment_0)

def test_case_3():
    solarized256_style_0 = module_0.Solarized256Style()
    str_0 = '\n    Translate `ax-age` into `expires` for Requests to take it nto account.\n\n    ACK/FIXME: <https://github.com/psf/requsts/issues/5743>\n\n    '
    optional_0 = module_0.get_lexer(str_0)
    environment_0 = module_1.Environment()
    var_0 = environment_0.__repr__()
    var_1 = environment_0.__str__()
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    str_1 = 'S)z/6Bm+{\\\x0b9T'
    optional_1 = module_0.get_lexer(str_1)

def test_case_4():
    str_0 = '\n    Translate `max-age` into `expires` for Requests to take it into account.\n\n    HACK/FIXME: <https://github.com/psf/requests/issues/5743>\n\n    '
    optional_0 = module_0.get_lexer(str_0)
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    int_0 = -310
    environment_0 = module_1.Environment()
    str_1 = 'format_options'
    dict_0 = {str_1: simplified_h_t_t_p_lexer_0, str_1: int_0, str_0: environment_0, str_0: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, dict_0, **dict_0)
    optional_1 = color_formatter_0.get_lexer_for_body(str_0, str_1)

def test_case_5():
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    int_0 = -310
    environment_0 = module_1.Environment()
    str_0 = 'format_options'
    dict_0 = {str_0: simplified_h_t_t_p_lexer_0, str_0: int_0, str_0: environment_0, str_0: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, dict_0, **dict_0)

def test_case_6():
    solarized256_style_0 = module_0.Solarized256Style()
    str_0 = '\n    Translate `max-age` into `expires` fo} Requests to take it into account.\n\n i  HACK/FIXME: <https://github.com/psf/requests/issues/5743>\n\n    '
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    int_0 = -310
    environment_0 = module_1.Environment()
    str_1 = 'format_options'
    dict_0 = {str_1: simplified_h_t_t_p_lexer_0, str_1: int_0, str_0: environment_0, str_1: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, dict_0, **dict_0)
    optional_0 = color_formatter_0.get_lexer_for_body(str_0, str_0)
    str_2 = '%'
    type_0 = color_formatter_0.get_style_class(str_2)

def test_case_7():
    solarized256_style_0 = module_0.Solarized256Style()
    str_0 = '\n    Translate `max-age` into `expires` for Requests to take it into account.\n\n    HACK/FIXME: <https://github.com/psf/requests/issues/5743>\n\n    '
    optional_0 = module_0.get_lexer(str_0)
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    int_0 = -310
    environment_0 = module_1.Environment()
    str_1 = 'format_options'
    str_2 = 'xBEfc9{XhV>\x0cH7Y'
    str_3 = '<}p!+L#L0#36l_^1;?\\"'
    dict_0 = {str_1: simplified_h_t_t_p_lexer_0, str_1: int_0, str_2: environment_0, str_3: str_2}
    color_formatter_0 = module_0.ColorFormatter(environment_0, dict_0, **dict_0)
    str_4 = '\t_1x'
    str_5 = color_formatter_0.format_headers(str_4)

def test_case_8():
    str_0 = '\n    Translate `max-age` into `expires` for Requests to take it into account.\n\n    HACK/FIXME: <https://github.com/psf/requests/issues/5743>\n\n    '
    optional_0 = module_0.get_lexer(str_0)
    optional_1 = module_0.get_lexer(str_0)
    simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer()
    int_0 = -310
    environment_0 = module_1.Environment()
    str_1 = 'format_options'
    dict_0 = {str_1: simplified_h_t_t_p_lexer_0, str_1: int_0, str_0: environment_0, str_0: str_0}
    color_formatter_0 = module_0.ColorFormatter(environment_0, dict_0, **dict_0)
    optional_2 = color_formatter_0.get_lexer_for_body(str_0, str_1)
    str_2 = color_formatter_0.format_body(str_0, str_0)

def test_case_9():
    str_0 = 'application/problem+json'
    str_1 = '{"name": "value"}'
    bool_0 = True
    optional_0 = module_0.get_lexer(str_0, bool_0, str_1)
    str_2 = 'not a json'
    optional_1 = module_0.get_lexer(str_0, bool_0, str_2)
    str_3 = 'text/html'
    str_4 = '<html></html>'
    bool_1 = False
    optional_2 = module_0.get_lexer(str_3, bool_1, str_4)