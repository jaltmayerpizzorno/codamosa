# Automatically generated by Pynguin.
import mimesis.providers.structure as module_0

def test_case_0():
    try:
        structure_0 = module_0.Structure()
        str_0 = structure_0.css()
        str_1 = structure_0.html()
        str_2 = structure_0.css_property()
        structure_1 = module_0.Structure()
        str_3 = structure_0.html()
        str_4 = structure_1.css_property()
        str_5 = structure_1.html()
        str_6 = structure_0.html_attribute_value(str_4, str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Provides most popular social networks.\n\n    An argument for :meth:`~mimesis.Person.social_media_profile()``.\n    '
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        structure_0 = module_0.Structure()
        str_1 = structure_0.html_attribute_value(dict_0, str_0)
    except BaseException:
        pass