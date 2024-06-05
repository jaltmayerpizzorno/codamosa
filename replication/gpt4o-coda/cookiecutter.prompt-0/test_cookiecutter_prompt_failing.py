# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import cookiecutter.environment as module_1

def test_case_0():
    try:
        str_0 = '\n    Run Cookiecutter just as if using it from the command line.\n\n    :param template: A directory containing a project template directory,\n        or a URL to a git repository.\n    :param checkout: The branch, tag or commit ID to checkout after clone.\n    :param no_input: Prompt the user at command line for manual configuration?\n    :param extra_context: A dictionary of context that overrides default\n        and user configuration.\n    :param replay: Do not prompt for input, instead read from saved json. If\n        ``True`` read from the ``replay_dir``.\n        if it exists\n    :param output_dir: Where to output the generated project dir into.\n    :param config_file: User configuration file path.\n    :param default_config: Use default values rather than a config file.\n    :param password: The password to use when extracting the repository.\n    :param directory: Relative path to a cookiecutter template in a repository.\n    :param accept_hooks: Accept pre and post hooks if set to `True`.\n    '
        complex_0 = None
        bytes_0 = b'\xf82D;\xa7\x00+\xbd\x02\xaa'
        tuple_0 = ()
        tuple_1 = (str_0, complex_0, bytes_0, tuple_0)
        var_0 = module_0.read_user_variable(tuple_1, complex_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        list_0 = [str_0, str_0]
        bytes_0 = b'Z\xf3\xa4^\x7f\x94!\xd0}1\xee.g\xb1XB\x05\xd0'
        tuple_0 = (list_0, list_0, bytes_0)
        int_0 = None
        var_0 = module_0.read_user_yes_no(tuple_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'a10\x0b_\t'
        var_0 = module_0.read_repo_password(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xd4\x9e\xea=\x12'
        list_0 = [bytes_0]
        var_0 = module_0.read_user_choice(list_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1432
        str_0 = 'Xg6@*fl\x0c'
        bool_0 = True
        float_0 = None
        float_1 = 1786.73804
        int_1 = 1111
        tuple_0 = (float_0, float_1, str_0, int_1)
        list_0 = [float_1, int_1, str_0, float_0]
        tuple_1 = (bool_0, tuple_0, list_0, int_0)
        var_0 = module_0.read_user_choice(int_0, tuple_1)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        var_0 = module_0.process_json(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'm9px0&k#'
        var_0 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'x5M47MNC7QzTy!}T'
        dict_0 = {str_0: str_0}
        template_0 = None
        var_0 = module_0.render_variable(dict_0, str_0, template_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -1212.71646
        list_0 = [float_0, float_0, float_0, float_0]
        bool_0 = None
        template_expression_0 = None
        var_0 = module_0.render_variable(list_0, bool_0, template_expression_0)
        strict_environment_0 = module_1.StrictEnvironment()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 1024
        list_0 = [int_0, int_0]
        str_0 = ">'l"
        var_0 = module_0.render_variable(str_0, list_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'x5M47MNC7QzTy!}T'
        dict_0 = {str_0: str_0}
        bool_0 = True
        var_0 = module_0.prompt_choice_for_config(dict_0, dict_0, bool_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b''
        var_0 = module_0.prompt_for_config(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '3uJ\tJdAtm$OA]!'
        str_1 = 'e x\nhI`%DS]Y-6.GL'
        set_0 = {str_1, str_0, str_0, str_1}
        ordered_dict_0 = None
        dict_0 = {ordered_dict_0: ordered_dict_0}
        bytes_0 = b'6B\xf1\xeb\x00\x92\xcd'
        var_0 = module_0.prompt_choice_for_config(str_1, set_0, ordered_dict_0, dict_0, bytes_0)
        var_1 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        var_0 = module_0.read_user_dict(dict_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\xe1\x15\x1es'
        set_0 = None
        bool_0 = False
        dict_0 = {bool_0: bytes_0, set_0: bool_0, bytes_0: bool_0, bool_0: bool_0}
        list_0 = []
        var_0 = module_0.prompt_choice_for_config(bytes_0, dict_0, list_0, list_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'x5M47MNC7QzTy!}T'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        template_0 = None
        var_0 = module_0.render_variable(str_0, dict_0, template_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'BsqQR(\tim Z2U(\x0b,l'
        bytes_0 = None
        list_0 = []
        dict_0 = {bytes_0: str_0, bytes_0: list_0}
        var_0 = module_0.render_variable(bytes_0, dict_0, str_0)
        set_0 = set()
        tuple_0 = ()
        var_1 = module_0.read_user_dict(set_0, tuple_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '74'
        var_0 = module_0.process_json(str_0)
    except BaseException:
        pass