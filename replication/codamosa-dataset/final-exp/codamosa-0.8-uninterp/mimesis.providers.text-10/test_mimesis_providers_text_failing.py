# Automatically generated by Pynguin.
import mimesis.providers.text as module_0

def test_case_0():
    try:
        text_0 = module_0.Text()
        str_0 = text_0.sentence()
        str_1 = "\r@s'CCE]ELUj2gZW3G"
        str_2 = text_0.title()
        list_0 = [str_1, str_1]
        text_1 = module_0.Text(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        text_0 = module_0.Text()
        str_0 = text_0.color()
        bool_0 = False
        str_1 = text_0.swear_word()
        str_2 = text_0.sentence()
        tuple_0 = text_0.rgb_color(bool_0)
        int_0 = 666
        str_3 = text_0.text(int_0)
        str_4 = text_0.sentence()
        dict_0 = {str_2: str_3}
        text_1 = module_0.Text(**dict_0)
    except BaseException:
        pass