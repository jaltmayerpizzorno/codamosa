# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        str_0 = 'toto'
        var_0 = module_0.do_vault(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        filter_module_0 = module_0.FilterModule()
        float_0 = 248.825
        filter_module_1 = module_0.FilterModule()
        str_0 = '8\\wj-Hgn,'
        var_0 = filter_module_0.filters()
        var_1 = filter_module_1.filters()
        dict_0 = {str_0: float_0}
        bytes_0 = b'\xc6x\xb5e\x01'
        var_2 = module_0.do_vault(float_0, filter_module_1, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "\n---\nauthor: Ansible Core Team (@ansible)\nmodule: include_tasks\nshort_description: Dynamically include a task list\ndescription:\n  - Includes a file with a list of tasks to be executed in the current playbook.\nversion_added: '2.4'\noptions:\n  file:\n    description:\n      - The name of the imported file is specified directly without any other option.\n      - Unlike M(ansible.builtin.import_tasks), most keywords, including loop, with_items, and conditionals, apply to this statement.\n      - The do until loop is not supported on M(ansible.builtin.include_tasks).\n    type: str\n    version_added: '2.7'\n  apply:\n    description:\n      - Accepts a hash of task keywords (e.g. C(tags), C(become)) that will be applied to the tasks within the include.\n    type: str\n    version_added: '2.7'\n  free-form:\n    description:\n      - |\n        Supplying a file name via free-form C(- include_tasks: file.yml) of a file to be included is the equivalent\n        of specifying an argument of I(file).\nextends_documentation_fragment:\n    - action_common_attributes\n    - action_common_attributes.conn\n    - action_common_attributes.flow\n    - action_core\n    - action_core.include\nattributes:\n    check_mode:\n        support: none\n    diff_mode:\n        support: none\nseealso:\n- module: ansible.builtin.import_playbook\n- module: ansible.builtin.import_role\n- module: ansible.builtin.import_tasks\n- module: ansible.builtin.include_role\n- ref: playbooks_reuse_includes\n  description: More information related to including and importing playbooks, roles and tasks.\n"
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        bool_0 = False
        str_1 = 'rpc.'
        var_1 = module_0.do_vault(bool_0, str_1, str_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256\n353066356464623132353036356437363364396561356464613435316430343431663337663035\n363734623134313739376236313765653966643632666361623066376365393763303730663435\n656331366366353864626332612a1b5d5f566f5b5c5d5b5d5c5f5d5d5d5f5e5f5d5e566f'
        var_0 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xa4\x16\xbe/9\xcd\xcc6\xf4\xb1\xff%\xb8\x96\x16\x80\xdf'
        float_0 = -2315.6
        var_0 = module_0.do_unvault(bytes_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        complex_0 = None
        bytes_0 = b'{\x17\xc1\xc9\xe9'
        var_0 = module_0.do_unvault(complex_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256;foo\n61646d696e626f756e64\n'
        ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(str_0)
        var_0 = module_0.do_unvault(ansible_vault_encrypted_unicode_0, str_0)
    except BaseException:
        pass