# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import collections as module_1
import cookiecutter.environment as module_2

def test_case_0():
    try:
        bool_0 = False
        str_0 = '34C>~>=2Cra_YW[^?0tN'
        var_0 = module_0.read_user_variable(bool_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        var_0 = module_0.read_user_yes_no(dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        var_0 = module_0.read_repo_password(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "\n    Exception for un-cloneable repo.\n\n    Raised when a cookiecutter template can't be cloned.\n    "
        float_0 = -585.296
        list_0 = [str_0]
        var_0 = module_0.read_user_choice(float_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ':MI/4q$C}8o/1&m'
        bytes_0 = b''
        var_0 = module_0.read_user_choice(str_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '=Dmdc('
        float_0 = 887.683
        list_0 = []
        str_1 = 'L4z5>s`]1m=='
        str_2 = "\t'h"
        tuple_0 = (list_0, str_1, str_2)
        dict_0 = {}
        var_0 = module_0.prompt_choice_for_config(str_0, float_0, tuple_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 47.8284
        var_0 = module_0.process_json(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        ordered_dict_0 = module_1.OrderedDict()
        var_0 = module_0.read_user_dict(ordered_dict_0, ordered_dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        var_0 = module_0.read_user_dict(bool_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\nPvFoCw\xfdN\xf4\xd7'
        str_0 = "\n    Exception for un-cloneable repo.\n\n    Raised when a cookiecutter template can't be cloned.\n    "
        var_0 = module_0.render_variable(bytes_0, str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'$Gj\xbc\xe0'
        set_0 = {bytes_0}
        list_0 = [set_0, set_0, bytes_0]
        float_0 = None
        var_0 = module_0.render_variable(bytes_0, list_0, float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "\n    Exception for un-cloneable repo.\n\n    Raised when a cookiecutter template can't be cloned.\n    "
        var_0 = module_0.prompt_for_config(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "Render filename of infile as name of outfile, handle infile correctly.\n\n    Dealing with infile appropriately:\n\n        a. If infile is a binary file, copy it over without rendering.\n        b. If infile is a text file, render its contents and write the\n           rendered infile to outfile.\n\n    Precondition:\n\n        When calling `generate_file()`, the root template dir must be the\n        current working directory. Using `utils.work_in()` is the recommended\n        way to perform this directory change.\n\n    :param project_dir: Absolute path to the resulting generated project.\n    :param infile: Input file to generate the file from. Relative to the root\n        template dir.\n    :param context: Dict for populating the cookiecutter's variables.\n    :param env: Jinja2 template execution environment.\n    "
        bytes_0 = b'\xa8\xe4\xb0\xe0\xbd\xb1ptLz\xec'
        tuple_0 = (str_0, bytes_0)
        float_0 = -249.958
        str_1 = None
        bool_0 = True
        set_0 = {tuple_0}
        var_0 = module_0.prompt_choice_for_config(float_0, str_1, bool_0, str_0, set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -1422.75
        dict_0 = None
        var_0 = module_0.render_variable(float_0, dict_0, float_0)
        str_0 = 'IR(BD5W3%dxe'
        var_1 = module_0.process_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = -1422.75
        dict_0 = {}
        int_0 = 1024
        var_0 = module_0.render_variable(int_0, dict_0, float_0)
        var_1 = module_0.process_json(dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = None
        dict_0 = None
        dict_1 = {str_0: dict_0, str_0: str_0}
        var_0 = module_0.render_variable(dict_0, dict_1, dict_1)
        strict_environment_0 = module_2.StrictEnvironment()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'SjY5,7t'
        float_0 = 887.683
        list_0 = []
        str_1 = 'L4z5>s`]1m=='
        str_2 = "\t'h"
        tuple_0 = (list_0, str_1, str_2)
        dict_0 = {str_2: str_2}
        var_0 = module_0.prompt_choice_for_config(str_0, float_0, tuple_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"name": "test", "version": "1.0.0"}'
        var_0 = module_0.process_json(str_0)
        str_1 = '["test", "1.0.0"]'
        var_1 = module_0.process_json(str_1)
    except BaseException:
        pass