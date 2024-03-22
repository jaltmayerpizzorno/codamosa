# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    try:
        float_0 = 1590.4
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.repo_url_to_role_name(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(role_requirement_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        bool_0 = False
        tuple_0 = None
        tuple_1 = (tuple_0,)
        role_requirement_1 = module_0.RoleRequirement()
        var_0 = role_requirement_1.scm_archive_role(bool_0, tuple_1)
    except BaseException:
        pass

def test_case_3():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = ' displays information on modules installed in Ansible libraries.\n        It displays a terse listing of plugins and their short descriptions,\n        provides a printout of their DOCUMENTATION strings,\n        and it can create a short "snippet" which can be pasted into a playbook.  '
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        var_1 = role_requirement_0.repo_url_to_role_name(role_requirement_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n---\nauthor: Ansible Core Team (@ansible)\nmodule: import_tasks\nshort_description: Import a task list\ndescription:\n  - Imports a list of tasks to be added to the current playbook for subsequent execution.\nversion_added: "2.4"\noptions:\n  free-form:\n    description:\n      - The name of the imported file is specified directly without any other option.\n      - Most keywords, including loops and conditionals, only applied to the imported tasks, not to this statement itself.\n      - If you need any of those to apply, use M(ansible.builtin.include_tasks) instead.\nextends_documentation_fragment:\n    - action_common_attributes\n    - action_common_attributes.conn\n    - action_common_attributes.flow\n    - action_core\n    - action_core.import\nattributes:\n    check_mode:\n      support: none\n    diff_mode:\n      support: none\nnotes:\n  - This is a core feature of Ansible, rather than a module, and cannot be overridden like a module\nseealso:\n- module: ansible.builtin.import_playbook\n- module: ansible.builtin.import_role\n- module: ansible.builtin.include_role\n- module: ansible.builtin.include_tasks\n- ref: playbooks_reuse_includes\n  description: More information related to including and importing playbooks, roles and tasks.\n'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = '\n    name: runas\n    short_description: Run As user\n    description:\n        - This become plugins allows your remote/login user to execute commands as another user via the windows runas facility.\n    author: ansible (@core)\n    version_added: "2.8"\n    options:\n        become_user:\n            description: User you \'become\' to execute the task\n            ini:\n              - section: privilege_escalation\n                key: become_user\n              - section: runas_become_plugin\n                key: user\n            vars:\n              - name: ansible_become_user\n              - name: ansible_runas_user\n            env:\n              - name: ANSIBLE_BECOME_USER\n              - name: ANSIBLE_RUNAS_USER\n            required: True\n        become_flags:\n            description: Options to pass to runas, a space delimited list of k=v pairs\n            default: \'\'\n            ini:\n              - section: privilege_escalation\n                key: become_flags\n              - section: runas_become_plugin\n                key: flags\n            vars:\n              - name: ansible_become_flags\n              - name: ansible_runas_flags\n            env:\n              - name: ANSIBLE_BECOME_FLAGS\n              - name: ANSIBLE_RUNAS_FLAGS\n        become_pass:\n            description: password\n            ini:\n              - section: runas_become_plugin\n                key: password\n            vars:\n              - name: ansible_become_password\n              - name: ansible_become_pass\n              - name: ansible_runas_pass\n            env:\n              - name: ANSIBLE_BECOME_PASS\n              - name: ANSIBLE_RUNAS_PASS\n    notes:\n        - runas is really implemented in the powershell module handler and as such can only be used with winrm connections.\n        - This plugin ignores the \'become_exe\' setting as it uses an API and not an executable.\n        - The Secondary Logon service (seclogon) must be running to use runas\n'
        role_requirement_1 = module_0.RoleRequirement()
        var_0 = role_requirement_1.repo_url_to_role_name(str_0)
        role_requirement_2 = module_0.RoleRequirement()
        float_0 = 60.0
        var_1 = role_requirement_2.role_yaml_parse(float_0)
    except BaseException:
        pass