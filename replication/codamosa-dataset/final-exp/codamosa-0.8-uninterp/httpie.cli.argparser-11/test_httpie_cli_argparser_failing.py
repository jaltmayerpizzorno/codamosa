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
        environment_0 = module_1.Environment()
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser()
        tuple_0 = (h_t_t_pie_argument_parser_0,)
        list_0 = [environment_0, environment_0, environment_0, tuple_0]
        h_t_t_pie_argument_parser_1 = module_0.HTTPieArgumentParser()
        namespace_0 = h_t_t_pie_argument_parser_1.parse_args(environment_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        environment_0 = module_1.Environment()
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        bytes_0 = b'?\xcbf"\xe8\xfb\xd6v\xa4'
        var_0 = environment_0.__str__()
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser(*list_0, formatter_class=bytes_0)
        namespace_0 = h_t_t_pie_argument_parser_0.parse_args(environment_0)
    except BaseException:
        pass