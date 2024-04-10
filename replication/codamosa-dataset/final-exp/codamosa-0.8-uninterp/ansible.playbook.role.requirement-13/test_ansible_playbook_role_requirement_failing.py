# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    try:
        bool_0 = False
        role_requirement_0 = module_0.RoleRequirement()
        float_0 = -1295.0
        dict_0 = {float_0: role_requirement_0, float_0: bool_0}
        var_0 = role_requirement_0.role_yaml_parse(dict_0)
        var_1 = role_requirement_0.scm_archive_role(role_requirement_0)
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
        bool_0 = False
        set_0 = {bool_0}
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1294
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = '8 8tdn4q3=@+'
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        var_1 = role_requirement_0.repo_url_to_role_name(str_0)
        var_2 = role_requirement_0.scm_archive_role(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'git+https://github.com/coveooss/ansible-coveo.git,1.0.3,coveo.ansible'
        set_0 = set()
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.repo_url_to_role_name(str_0)
        role_requirement_1 = module_0.RoleRequirement()
        var_1 = role_requirement_1.role_yaml_parse(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'role'
        var_0 = dict(name=str_0, src=str_0, scm=str_0, version=str_0)
        str_1 = 'role1,v1'
        role_requirement_0 = module_0.RoleRequirement()
        str_2 = {str_0: str_1}
        var_1 = dict(name=str_2, src=var_0, scm=var_0, version=str_0)
        var_2 = role_requirement_0.role_yaml_parse(str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n# Obtain the stats of /etc/foo.conf, and check that the file still belongs\n# to \'root\'. Fail otherwise.\n- name: Get stats of a file\n  ansible.builtin.stat:\n    path: /etc/foo.conf\n  register: st\n- name: Fail if the file does not belong to \'root\'\n  ansible.builtin.fail:\n    msg: "Whoops! file ownership has changed"\n  when: st.stat.pw_name != \'root\'\n\n# Determine if a path exists and is a symlink. Note that if the path does\n# not exist, and we test sym.stat.islnk, it will fail with an error. So\n# therefore, we must test whether it is defined.\n# Run this to understand the structure, the skipped ones do not pass the\n# check performed by \'when\'\n- name: Get stats of the FS object\n  ansible.builtin.stat:\n    path: /path/to/something\n  register: sym\n\n- name: Print a debug message\n  ansible.builtin.debug:\n    msg: "islnk isn\'t defined (path doesn\'t exist)"\n  when: sym.stat.islnk is not defined\n\n- name: Print a debug message\n  ansible.builtin.debug:\n    msg: "islnk is defined (path must exist)"\n  when: sym.stat.islnk is defined\n\n- name: Print a debug message\n  ansible.builtin.debug:\n    msg: "Path exists and is a symlink"\n  when: sym.stat.islnk is defined and sym.stat.islnk\n\n- name: Print a debug message\n  ansible.builtin.debug:\n    msg: "Path exists and isn\'t a symlink"\n  when: sym.stat.islnk is defined and sym.stat.islnk == False\n\n\n# Determine if a path exists and is a directory.  Note that we need to test\n# both that p.stat.isdir actually exists, and also that it\'s set to true.\n- name: Get stats of the FS object\n  ansible.builtin.stat:\n    path: /path/to/something\n  register: p\n- name: Print a debug message\n  ansible.builtin.debug:\n    msg: "Path exists and is a directory"\n  when: p.stat.isdir is defined and p.stat.isdir\n\n- name: Don not do checksum\n  ansible.builtin.stat:\n    path: /path/to/myhugefile\n    get_checksum: no\n\n- name: Use sha256 to calculate checksum\n  ansible.builtin.stat:\n    path: /path/to/something\n    checksum_algorithm: sha256\n'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
    except BaseException:
        pass