# Automatically generated by Pynguin.
import thefuck.conf as module_0

def test_case_0():
    try:
        float_0 = -2506.82
        bytes_0 = b'\x04$\xbal'
        settings_0 = module_0.Settings()
        var_0 = settings_0.__setattr__(float_0, bytes_0)
        str_0 = 'My'
        bytes_1 = b'\x9a'
        dict_0 = {str_0: str_0}
        settings_1 = module_0.Settings(**dict_0)
        var_1 = settings_1.init(bytes_1)
    except BaseException:
        pass