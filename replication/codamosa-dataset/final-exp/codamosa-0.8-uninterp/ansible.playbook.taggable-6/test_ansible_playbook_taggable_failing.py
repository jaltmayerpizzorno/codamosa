# Automatically generated by Pynguin.
import ansible.playbook.taggable as module_0

def test_case_0():
    try:
        str_0 = "'l{U'r}u}:ja`Na]J\x0cFw"
        taggable_0 = module_0.Taggable()
        dict_0 = {}
        taggable_1 = module_0.Taggable()
        taggable_2 = module_0.Taggable()
        var_0 = taggable_2.evaluate_tags(str_0, dict_0, dict_0)
    except BaseException:
        pass