# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    generator_0 = module_0.parse_env_file_contents()

def test_case_1():
    str_0 = 'HP+R:!{;6,_sl-HSjS'
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = 'A lazy object that will replace itself in the appropriate scope.\n\n    This object sits, ready to create the real object the first time it is\n    needed.\n    '
    generator_0 = module_0.parse_env_file_contents()
    ordered_dict_0 = module_0.load_env_file(str_0, generator_0)

def test_case_3():
    list_0 = []
    ordered_dict_0 = module_0.load_env_file(list_0)

def test_case_4():
    str_0 = 'TEST=${HOME}/yeee'
    str_1 = 'THISIS=~/a/test'
    str_2 = "YOLO='~/swaggins/'"
    str_3 = 'YOLO2="~/swaggins/"'
    str_4 = 'YOLO3="$HOME/swaggins/\\"'
    str_5 = [str_0, str_1, str_2, str_3, str_4]
    generator_0 = module_0.parse_env_file_contents(str_5)
    var_0 = list(generator_0)

def test_case_5():
    str_0 = 'TEST=${HOOKME}/ypee'
    list_0 = [str_0, str_0]
    mutable_mapping_0 = None
    ordered_dict_0 = module_0.load_env_file(list_0, mutable_mapping_0)
    ordered_dict_1 = module_0.load_env_file(ordered_dict_0)