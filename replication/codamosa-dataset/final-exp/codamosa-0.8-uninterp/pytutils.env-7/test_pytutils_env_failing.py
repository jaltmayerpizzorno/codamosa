# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    try:
        str_0 = ',]w5\x0c00Ev28'
        str_1 = module_0.expand(str_0)
        str_2 = 'm&<:\\Y'
        str_3 = 'xb=+l7gge3Q{'
        str_4 = module_0.expand(str_3)
        generator_0 = module_0.parse_env_file_contents()
        set_0 = {str_4, str_0, str_0, str_2}
        ordered_dict_0 = module_0.load_env_file(set_0)
        iterable_0 = None
        ordered_dict_1 = module_0.load_env_file(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        generator_0 = module_0.parse_env_file_contents()
        str_0 = 'y]\\tBR\rQ,]fCJbM2'
        str_1 = ',]w5\x0c00Ev28'
        str_2 = module_0.expand(str_0)
        int_0 = 492
        generator_1 = module_0.parse_env_file_contents(int_0)
        str_3 = 'xb=+l7gDe3Q{'
        str_4 = module_0.expand(str_3)
        generator_2 = module_0.parse_env_file_contents()
        str_5 = module_0.expand(str_3)
        generator_3 = module_0.parse_env_file_contents()
        generator_4 = module_0.parse_env_file_contents()
        set_0 = {str_5, str_1, str_0, str_4}
        mutable_mapping_0 = None
        ordered_dict_0 = module_0.load_env_file(set_0, mutable_mapping_0)
        ordered_dict_1 = module_0.load_env_file(ordered_dict_0)
        generator_5 = module_0.parse_env_file_contents()
        bytes_0 = b'\xedEy7\xff'
        ordered_dict_2 = module_0.load_env_file(bytes_0)
    except BaseException:
        pass