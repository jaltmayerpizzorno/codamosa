# Automatically generated by Pynguin.
import httpie.cli.definition as module_0

def test_case_0():
    try:
        bytes_0 = b'\xa8\x06\x95('
        list_0 = [bytes_0, bytes_0]
        list_1 = [bytes_0, bytes_0, list_0]
        list_2 = [list_1, list_0, list_1, list_1]
        auth_type_lazy_choices_0 = module_0._AuthTypeLazyChoices()
        var_0 = auth_type_lazy_choices_0.__contains__(list_2)
    except BaseException:
        pass