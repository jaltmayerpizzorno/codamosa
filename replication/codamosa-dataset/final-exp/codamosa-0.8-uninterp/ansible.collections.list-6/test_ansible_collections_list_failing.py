# Automatically generated by Pynguin.
import ansible.collections.list as module_0

def test_case_0():
    try:
        var_0 = module_0.list_collection_dirs()
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'yE2\x0b3a'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'mynamespace.mycollection1'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n---\nmodule: group_by\nshort_description: Create Ansible groups based on facts\nextends_documentation_fragment:\n  - action_common_attributes\n  - action_common_attributes.conn\n  - action_common_attributes.flow\n  - action_core\ndescription:\n- Use facts to create ad-hoc groups that can be used later in a playbook.\n- This module is also supported for Windows targets.\nversion_added: "0.9"\noptions:\n  key:\n    description:\n    - The variables whose values will be used as groups.\n    type: str\n    required: true\n  parents:\n    description:\n    - The list of the parent groups.\n    type: list\n    default: all\n    version_added: "2.4"\nattributes:\n    action:\n      support: full\n    become:\n      support: none\n    bypass_host_loop:\n      support: full\n    bypass_task_loop:\n      support: none\n    check_mode:\n      details: While this makes no changes to target systems the \'in memory\' inventory will still be altered\n      support: partial\n    core:\n      details: While parts of this action are implemented in core, other parts are still available as normal plugins and can be partially overridden\n      support: partial\n    connection:\n        support: none\n    delegation:\n        support: none\n    diff_mode:\n      support: none\n    platform:\n        platforms: all\nnotes:\n- Spaces in group names are converted to dashes \'-\'.\n- Though this module does not change the remote host,\n  we do provide \'changed\' status as it can be useful\n  for those trying to track inventory changes.\nseealso:\n- module: ansible.builtin.add_host\nauthor:\n- Jeroen Hoekx (@jhoekx)\n'
        var_0 = module_0.list_collection_dirs(str_0, str_0)
        var_1 = list(var_0)
    except BaseException:
        pass