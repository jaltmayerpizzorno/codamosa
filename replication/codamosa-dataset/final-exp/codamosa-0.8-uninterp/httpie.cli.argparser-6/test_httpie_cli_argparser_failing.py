# Automatically generated by Pynguin.
import httpie.cli.argparser as module_0
import httpie.context as module_1

def test_case_0():
    try:
        h_t_t_pie_help_formatter_0 = module_0.HTTPieHelpFormatter()
    except BaseException:
        pass

def test_case_1():
    try:
        environment_0 = None
        bool_0 = True
        bool_1 = True
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser(formatter_class=bool_1)
        namespace_0 = h_t_t_pie_argument_parser_0.parse_args(environment_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        environment_0 = module_1.Environment()
        int_0 = -188
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser(formatter_class=int_0)
        namespace_0 = h_t_t_pie_argument_parser_0.parse_args(environment_0)
    except BaseException:
        pass

def test_case_3():
    try:
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser()
        str_0 = 'test error'
        var_0 = h_t_t_pie_argument_parser_0.error(str_0)
    except BaseException:
        pass