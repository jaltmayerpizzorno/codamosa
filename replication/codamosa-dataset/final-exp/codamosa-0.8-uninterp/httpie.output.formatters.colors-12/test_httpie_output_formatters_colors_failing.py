# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.output.formatters.colors as module_1
import pygments.formatters.terminal as module_2

def test_case_0():
    try:
        environment_0 = module_0.Environment()
        str_0 = '\nDownload mode implementation.\n\n'
        dict_0 = {str_0: environment_0, str_0: str_0}
        color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\\>#ooO/f_7sQ|ZW.@+N'
        dict_0 = {str_0: str_0}
        optional_0 = module_1.get_lexer(str_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "\n    Return he path to the httpie configuration directory.\n\n    This directory isn't guaranteed to exist, and nor are any of its\n    ancestors (only te legacy ~/.httpie, if returned, is guaranteed to exist).\n\n    XDG Base Directory Specification support:\n\n        <https://wiki.archlinux.org/index.php/XDG_Base_Directory>\n\n       $XDG_CONFIG_HOME is supported; $XDG_CONFIG_DIRS is not\n\n    "
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        str_1 = 'application/json'
        set_0 = set()
        optional_0 = module_1.get_lexer(str_1, set_0)
        optional_1 = module_1.get_lexer(str_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        environment_0 = module_0.Environment()
        str_0 = '\n    Show this help message and exit.\n\n    '
        str_1 = 'format_options'
        dict_0 = {str_0: str_1, str_0: str_0, str_1: str_1, str_1: str_1, str_0: str_0}
        color_formatter_0 = module_1.ColorFormatter(environment_0, environment_0, **dict_0)
        str_2 = 'H'
        str_3 = color_formatter_0.format_headers(str_2)
        type_0 = color_formatter_0.get_style_class(str_3)
        optional_0 = color_formatter_0.get_lexer_for_body(str_1, str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '9;)RWd7\rv9QFpmr'
        simplified_h_t_t_p_lexer_0 = module_1.SimplifiedHTTPLexer()
        environment_0 = module_0.Environment()
        str_1 = 'format_options'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: environment_0, str_1: str_1}
        color_formatter_0 = module_1.ColorFormatter(environment_0, environment_0, **dict_0)
        type_0 = color_formatter_0.get_style_class(str_0)
        str_2 = ')[(PE_|:,C%/DVkJD'
        str_3 = '(.JLf\t6lj4oY.'
        type_1 = color_formatter_0.get_style_class(str_2)
        str_4 = color_formatter_0.format_body(str_3, str_2)
        set_0 = {str_2}
        str_5 = 'W2:4=l//zegG6_Ofb-"s'
        str_6 = '3'
        optional_0 = color_formatter_0.get_lexer_for_body(str_5, str_6)
        color_formatter_1 = module_1.ColorFormatter(environment_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        environment_0 = module_0.Environment()
        str_0 = 'format_options'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: environment_0, str_0: str_0}
        str_1 = ')[(PE_|:,wRAC%/DVkJD'
        terminal_formatter_0 = module_2.TerminalFormatter()
        list_0 = [str_0, str_1, str_0]
        list_1 = []
        solarized256_style_0 = module_1.Solarized256Style(*list_1)
        color_formatter_0 = module_1.ColorFormatter(environment_0, list_0, solarized256_style_0, **dict_0)
    except BaseException:
        pass