# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0

def test_case_0():
    try:
        complex_0 = None
        bool_0 = False
        bytes_0 = b'-\x0c\x08\xc0'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load(complex_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 's qr7,,.fTR\x0b&O/-'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '\n---\nmodule: setup\nversion_added: historical\nshort_description: Gathers facts about remote hosts\noptions:\n    gather_subset:\n        version_added: "2.1"\n        description:\n            - "If supplied, restrict the additional facts collected to the given subset.\n              Possible values: C(all), C(min), C(hardware), C(network), C(virtual), C(ohai), and\n              C(facter). Can specify a list of values to specify a larger subset.\n              Values can also be used with an initial C(!) to specify that\n              that specific subset should not be collected.  For instance:\n              C(!hardware,!network,!virtual,!ohai,!facter). If C(!all) is specified\n              then only the min subset is collected. To avoid collecting even the\n              min subset, specify C(!all,!min). To collect only specific facts,\n              use C(!all,!min), and specify the particular fact subsets.\n              Use the filter parameter if you do not want to display some collected\n              facts."\n        type: list\n        elements: str\n        default: "all"\n    gather_timeout:\n        version_added: "2.2"\n        description:\n            - Set the default timeout in seconds for individual fact gathering.\n        type: int\n        default: 10\n    filter:\n        version_added: "1.1"\n        description:\n            - If supplied, only return facts that match one of the shell-style\n              (fnmatch) pattern. An empty list basically means \'no filter\'.\n              As of Ansible 2.11, the type has changed from string to list\n              and the default has became an empty list. A simple string is\n              still accepted and works as a single pattern. The behaviour\n              prior to Ansible 2.11 remains.\n        type: list\n        elements: str\n        default: []\n    fact_path:\n        version_added: "1.3"\n        description:\n            - Path used for local ansible facts (C(*.fact)) - files in this dir\n              will be run (if executable) and their results be added to C(ansible_local) facts.\n              If a file is not executable it is read instead.\n              File/results format can be JSON or INI-format. The default C(fact_path) can be\n              specified in C(ansible.cfg) for when setup is automatically called as part of\n              C(gather_facts).\n              NOTE - For windows clients, the results will be added to a variable named after the\n              local file (without extension suffix), rather than C(ansible_local).\n            - Since Ansible 2.1, Windows hosts can use C(fact_path). Make sure that this path\n              exists on the target host. Files in this path MUST be PowerShell scripts C(.ps1)\n              which outputs an object. This object will be formatted by Ansible as json so the\n              script should be outputting a raw hashtable, array, or other primitive object.\n        type: path\n        default: /etc/ansible/facts.d\ndescription:\n    - This module is automatically called by playbooks to gather useful\n      variables about remote hosts that can be used in playbooks. It can also be\n      executed directly by C(/usr/bin/ansible) to check what variables are\n      available to a host. Ansible provides many I(facts) about the system,\n      automatically.\n    - This module is also supported for Windows targets.\nextends_documentation_fragment:\n  -  action_common_attributes\n  -  action_common_attributes.facts\nattributes:\n    check_mode:\n        support: full\n    diff_mode:\n        support: none\n    facts:\n        support: full\n    platform:\n        platforms: posix, windows\nnotes:\n    - More ansible facts will be added with successive releases. If I(facter) or\n      I(ohai) are installed, variables from these programs will also be snapshotted\n      into the JSON file for usage in templating. These variables are prefixed\n      with C(facter_) and C(ohai_) so it\'s easy to tell their source. All variables are\n      bubbled up to the caller. Using the ansible facts and choosing to not\n      install I(facter) and I(ohai) means you can avoid Ruby-dependencies on your\n      remote systems. (See also M(community.general.facter) and M(community.general.ohai).)\n    - The filter option filters only the first level subkey below ansible_facts.\n    - If the target host is Windows, you will not currently have the ability to use\n      C(filter) as this is provided by a simpler implementation of the module.\n    - This module should be run with elevated privileges on BSD systems to gather facts like ansible_product_version.\n    - For more information about delegated facts,\n      please check U(https://docs.ansible.com/ansible/latest/user_guide/playbooks_delegation.html#delegating-facts).\nauthor:\n    - "Ansible Core Team"\n    - "Michael DeHaan"\n'
        var_0 = data_loader_0.set_vault_secrets(str_0)
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.is_executable(data_loader_0)
    except BaseException:
        pass

def test_case_3():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = "Skipped '%s' path due to this access issue: %s\n"
        var_0 = data_loader_0.is_executable(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'U>u?9xr'
        set_0 = {data_loader_0, data_loader_0}
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, set_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 1687.28
        set_0 = {float_0, float_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative(float_0, set_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'PjV=b'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'Ye\xb8'
        bool_0 = True
        str_0 = 'Can not load RPM file'
        tuple_0 = (bytes_0, bool_0, str_0)
        bool_1 = False
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(tuple_0, bool_1)
    except BaseException:
        pass

def test_case_8():
    try:
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'$\x8eN\x1eJ\x91\xe8\xb47\x80\x15'
        var_0 = data_loader_0.path_exists(bytes_0)
        bool_0 = False
        var_1 = data_loader_0.find_vars_files(bool_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        list_0 = [str_0, str_0, str_0]
        tuple_0 = (list_0, str_0)
        bool_0 = False
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, tuple_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        data_loader_0 = module_0.DataLoader()
        bool_0 = False
        var_0 = data_loader_0.get_real_file(bool_0, data_loader_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = ()
        int_0 = -1268
        float_0 = -1169.81
        tuple_1 = (tuple_0, int_0, float_0)
        str_0 = 'V\n-Gl\'|.h?#"K\x0cqm\r;6'
        data_loader_0 = None
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.path_dwim_relative_stack(tuple_1, str_0, data_loader_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        set_0 = {str_0, str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(set_0)
        list_0 = [str_0, str_0, str_0]
        int_0 = None
        var_1 = data_loader_0.set_basedir(int_0)
        var_2 = data_loader_0.cleanup_tmp_file(set_0)
        data_loader_1 = module_0.DataLoader()
        var_3 = data_loader_1.cleanup_all_tmp_files()
        str_1 = ')!\x0c0eW[P:*C'
        str_2 = ']&)\r lE7>1YK3f:%3/5\x0b'
        var_4 = data_loader_1.path_dwim_relative_stack(str_0, str_1, str_2, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'P+/.1'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.find_vars_files(str_0, str_0)
        dict_0 = {}
        var_1 = data_loader_0.load_from_file(dict_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        list_0 = [str_0, str_0, str_0]
        data_loader_0 = module_0.DataLoader()
        str_1 = ']&)\r lE7>1YK3f:%3/5\x0b'
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_1, str_1, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(data_loader_0)
        str_0 = '~'
        var_1 = data_loader_0.is_file(str_0)
        var_2 = data_loader_0.cleanup_all_tmp_files()
        int_0 = 15
        var_3 = data_loader_0.set_basedir(data_loader_0)
        var_4 = data_loader_0.set_basedir(int_0)
        var_5 = data_loader_0.is_file(str_0)
        data_loader_1 = module_0.DataLoader()
        var_6 = data_loader_1.get_real_file(data_loader_0, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(data_loader_0)
        str_0 = '-&%pXf"q\'1b\rQl?,(;'
        var_1 = data_loader_0.cleanup_all_tmp_files()
        str_1 = 'Ie9*Tpi'
        float_0 = -6404.818373265785
        var_2 = data_loader_0.path_dwim_relative(str_1, str_1, float_0)
        int_0 = 15
        var_3 = data_loader_0.cleanup_all_tmp_files()
        var_4 = data_loader_0.set_basedir(int_0)
        var_5 = data_loader_0.is_directory(str_0)
        var_6 = data_loader_0.is_file(str_0)
        str_2 = 't*Gi[\x0c:M!f6'
        bytes_0 = b''
        var_7 = data_loader_0.cleanup_all_tmp_files()
        str_3 = ''
        var_8 = data_loader_0.path_dwim_relative_stack(str_2, bytes_0, str_3)
    except BaseException:
        pass

def test_case_17():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'H9H7&d2G!l4X`mfM.oUS'
        set_0 = {str_0, str_0, str_0}
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.is_file(set_0)
        str_1 = '8w9]~,'
        var_1 = data_loader_1.cleanup_all_tmp_files()
        var_2 = data_loader_1.cleanup_tmp_file(set_0)
        list_0 = [str_0, var_0]
        tuple_0 = (list_0, str_0)
        data_loader_2 = module_0.DataLoader()
        data_loader_3 = module_0.DataLoader()
        str_2 = '1VUHKIsb|"(oRi+.GX\rs'
        var_3 = data_loader_1.find_vars_files(str_1, str_2, str_2)
        data_loader_4 = module_0.DataLoader()
        var_4 = data_loader_4.set_basedir(set_0)
        data_loader_5 = module_0.DataLoader()
        var_5 = data_loader_4.get_real_file(set_0, tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ''
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        set_0 = {str_0, str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(set_0)
        var_1 = data_loader_0.cleanup_all_tmp_files()
        list_0 = [str_0, str_0, str_0]
        float_0 = 1062.6
        var_2 = data_loader_0.set_vault_secrets(float_0)
        var_3 = data_loader_0.cleanup_tmp_file(set_0)
        data_loader_1 = module_0.DataLoader()
        str_1 = '//{'
        var_4 = data_loader_1.path_dwim_relative_stack(str_0, str_1, str_1, list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        set_0 = {str_0, str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(set_0)
        var_1 = data_loader_0.path_exists(set_0)
        list_0 = [str_0, str_0, str_0]
        str_1 = '`/Nd0+#~~Pv>(^54r\x0c'
        str_2 = ''
        tuple_0 = ()
        var_2 = data_loader_0.path_dwim_relative(str_1, str_2, tuple_0, str_1)
        var_3 = data_loader_0.cleanup_tmp_file(set_0)
        var_4 = data_loader_0.cleanup_all_tmp_files()
        str_3 = "l':&"
        var_5 = data_loader_0.path_dwim_relative_stack(str_0, str_1, str_3, list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'H9H7&d2Gal4X`mfM.oUS'
        set_0 = {str_0, str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(set_0)
        str_1 = '8w9]~,'
        dict_0 = {str_1: str_1}
        var_1 = data_loader_0.path_dwim_relative(str_1, str_1, dict_0, dict_0)
        var_2 = data_loader_0.cleanup_all_tmp_files()
        data_loader_1 = module_0.DataLoader()
        data_loader_2 = module_0.DataLoader()
        data_loader_3 = module_0.DataLoader()
        bytes_0 = b'7\x00\xa9'
        data_loader_4 = module_0.DataLoader()
        var_3 = data_loader_4.cleanup_tmp_file(bytes_0)
        str_2 = "6'$,[}=-"
        str_3 = '~k\\I'
        var_4 = data_loader_0.path_dwim_relative(str_2, data_loader_0, str_3)
        data_loader_5 = module_0.DataLoader()
        var_5 = data_loader_4.set_basedir(bytes_0)
        data_loader_6 = module_0.DataLoader()
        str_4 = 'sD;z|"`Y*YJ/atjm@'
        var_6 = data_loader_2.get_real_file(str_4)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '!Bn(op 2>$L|'
        set_0 = {str_0, str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_file(set_0)
        str_1 = 'Failed to perform archive operation'
        str_2 = '8w9]~,'
        dict_0 = {str_2: str_1}
        var_1 = data_loader_0.path_dwim_relative(str_1, str_2, dict_0, dict_0)
        var_2 = data_loader_0.cleanup_all_tmp_files()
        str_3 = '#'
        str_4 = 'qR.Wj\nq1\r\ti&uV91'
        data_loader_1 = module_0.DataLoader()
        var_3 = data_loader_1.cleanup_all_tmp_files()
        bytes_0 = b''
        var_4 = data_loader_0.path_dwim_relative(str_3, str_4, bytes_0)
        data_loader_2 = module_0.DataLoader()
        data_loader_3 = module_0.DataLoader()
        bool_0 = None
        var_5 = data_loader_0.cleanup_tmp_file(bool_0)
        bytes_1 = b''
        int_0 = 15
        var_6 = data_loader_1.load_from_file(bytes_1, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '//'
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass