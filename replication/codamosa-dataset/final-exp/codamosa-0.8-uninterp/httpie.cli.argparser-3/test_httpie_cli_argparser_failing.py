# Automatically generated by Pynguin.
import httpie.cli.argparser as module_0

def test_case_0():
    try:
        list_0 = []
        str_0 = 'store_true'
        dict_0 = {str_0: list_0, str_0: str_0}
        h_t_t_pie_help_formatter_0 = module_0.HTTPieHelpFormatter(str_0, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        environment_0 = None
        list_0 = [environment_0, environment_0]
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser()
        namespace_0 = h_t_t_pie_argument_parser_0.parse_args(environment_0, list_0)
    except BaseException:
        pass