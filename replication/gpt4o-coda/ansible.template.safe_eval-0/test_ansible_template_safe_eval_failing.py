# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    try:
        float_0 = 0.5
        var_0 = module_0.safe_eval(float_0)
        str_0 = 'q6'
        dict_0 = {str_0: float_0, str_0: float_0}
        str_1 = '3dJy|~'
        float_1 = -3996.0
        var_1 = module_0.safe_eval(float_1)
        var_2 = module_0.safe_eval(str_0, dict_0, str_1)
        str_2 = '0aH&4'
        var_3 = module_0.safe_eval(str_0, str_2)
        int_0 = -995
        float_2 = -2879.0389
        var_4 = module_0.safe_eval(int_0, float_2)
        bytes_0 = b'\xa6\xaa\xe3W'
        str_3 = '\x0cU`te~C3N\t;7bL,]\x0b'
        var_5 = module_0.safe_eval(bytes_0, str_3)
        set_0 = set()
        var_6 = module_0.safe_eval(set_0)
    except BaseException:
        pass