# Automatically generated by Pynguin.
import ansible.parsing.yaml.objects as module_0
import ansible.playbook.playbook_include as module_1

def test_case_0():
    pass

def test_case_1():
    ansible_mapping_0 = module_0.AnsibleMapping()
    playbook_include_0 = module_1.PlaybookInclude()
    var_0 = playbook_include_0.preprocess_data(ansible_mapping_0)

def test_case_2():
    str_0 = 'Ib0\x0b'
    int_0 = 1
    var_0 = dict(one=str_0, two=int_0)
    var_1 = dict(import_playbook=str_0, vars=var_0)
    playbook_include_0 = module_1.PlaybookInclude()
    var_2 = playbook_include_0.preprocess_data(var_1)