# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.output.formatters.colors as module_1
import pygments.formatters.terminal as module_2

def test_case_0():
    try:
        environment_0 = module_0.Environment()
        color_formatter_0 = module_1.ColorFormatter(environment_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Hr.A,!8O}nC{`'
        optional_0 = module_1.get_lexer(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '`J\ti!R0C\'-"[Qh?\r;F/\r'
        int_0 = -1242
        float_0 = -955.80722
        optional_0 = module_1.get_lexer(str_0, float_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2132.0
        str_0 = '\n    Base auth plugin class.\n\n    See httpie-ntlm for an example auth plugin:\n\n        <https://github.com/httpie/httpie-ntlm>\n\n    See also `test_auth_plugins.py`\n\n    '
        optional_0 = module_1.get_lexer(str_0, float_0, str_0)
        str_1 = 'Oj,'
        bool_0 = False
        optional_1 = module_1.get_lexer(str_1, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "Return processed `content`.\n\n        :param mime: E.g., 'application/atom+xml'.\n        :param content: The body content as text\n\n        "
        float_0 = 2132.0
        str_1 = '\n    Base auth plugin class.\n\n    See httpie-ntlm for an example auth plugin:\n\n        <https://github.com/httpie/httpie-ntlm>\n\n    See also `test_auth_plugins.py`\n\n    '
        optional_0 = module_1.get_lexer(str_0, float_0, str_1)
        environment_0 = module_0.Environment()
        str_2 = 'Oj,'
        bool_0 = False
        optional_1 = module_1.get_lexer(str_2, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        environment_0 = module_0.Environment()
        str_0 = 'format_options'
        dict_0 = {str_0: str_0, str_0: environment_0, str_0: str_0}
        color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
        optional_0 = color_formatter_0.get_lexer_for_body(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'l<~*~\\=/k'
        environment_0 = module_0.Environment()
        str_1 = 'format_options'
        dict_0 = {str_1: str_1, str_1: environment_0, str_1: str_1}
        color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
        optional_0 = color_formatter_0.get_lexer_for_body(str_0, str_0)
        environment_1 = module_0.Environment()
        str_2 = 'EZ-:55C`/3>Iq\nXS'
        str_3 = 'vY% =yX{it"H%'
        str_4 = color_formatter_0.format_body(str_3, str_2)
        terminal_formatter_0 = module_2.TerminalFormatter()
        color_formatter_1 = module_1.ColorFormatter(environment_0, terminal_formatter_0, color_formatter_0, **dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'l<~*~\\=/k'
        environment_0 = module_0.Environment()
        str_1 = 'format_options'
        dict_0 = {str_1: str_1, str_1: environment_0, str_1: str_1}
        color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
        optional_0 = color_formatter_0.get_lexer_for_body(str_0, str_0)
        str_2 = "clT)vxk0bX'QZid'"
        type_0 = color_formatter_0.get_style_class(str_2)
        terminal_formatter_0 = module_2.TerminalFormatter()
        color_formatter_1 = module_1.ColorFormatter(environment_0, terminal_formatter_0, color_formatter_0, **dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'l<~*~\\=/k'
        float_0 = 2132.0
        optional_0 = module_1.get_lexer(str_0, float_0, str_0)
        environment_0 = module_0.Environment()
        str_1 = '~CYhMeB3(K{\x0bzO8q'
        str_2 = 'format_options'
        dict_0 = {str_2: str_2, str_1: environment_0, str_2: str_2}
        color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
        optional_1 = color_formatter_0.get_lexer_for_body(str_0, str_0)
        environment_1 = module_0.Environment()
        environment_2 = module_0.Environment()
        str_3 = 'n"2+k^N"\x0cH{'
        str_4 = 'EZ-:55C`/3>Iq\nXS'
        dict_1 = {str_0: float_0, str_4: str_3, str_4: str_4}
        str_5 = 'LKM1|IZMa[WQu'
        str_6 = color_formatter_0.format_headers(str_5)
        str_7 = 'n_.({HN4Ehlo"aAcy\'"'
        type_0 = color_formatter_0.get_style_class(str_7)
        str_8 = ';type='
        str_9 = color_formatter_0.format_body(str_8, str_0)
        terminal_formatter_0 = module_2.TerminalFormatter()
        tuple_0 = None
        color_formatter_1 = module_1.ColorFormatter(environment_2, tuple_0, **dict_1)
    except BaseException:
        pass