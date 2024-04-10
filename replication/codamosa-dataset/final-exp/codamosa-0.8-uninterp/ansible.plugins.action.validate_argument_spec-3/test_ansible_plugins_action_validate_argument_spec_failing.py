# Automatically generated by Pynguin.
import ansible.plugins.action.validate_argument_spec as module_0

def test_case_0():
    try:
        float_0 = 762.81319
        list_0 = [float_0, float_0]
        str_0 = '/sys/block/'
        tuple_0 = (str_0,)
        dict_0 = {}
        float_1 = 2735.03891
        bool_0 = False
        action_module_0 = module_0.ActionModule(float_1, bool_0, list_0, tuple_0, tuple_0, tuple_0)
        var_0 = action_module_0.get_args_from_task_vars(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '*ZdTcWRthrA8]e'
        bytes_0 = b'\xd2\x84\xfd\xd8\xe9\xd8\xbd\xfd\xaa'
        set_0 = {str_0, bytes_0, bytes_0}
        list_0 = []
        action_module_0 = module_0.ActionModule(str_0, bytes_0, str_0, set_0, list_0, set_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        dict_0 = {}
        float_0 = -598.951948
        str_1 = 'mXnv/[wLSJJ+jr{\x0b'
        str_2 = '<$xj'
        set_0 = {float_0, float_0, str_2, str_2}
        bool_0 = False
        bytes_0 = b'\xf1\xfd\xbcE\xf8\xed\xb4;$\x8c\x9c\xa2\x17\xa7y\xff\xb6'
        int_0 = -3182
        bytes_1 = b'\xe0\xb0h\xbf\xeaY$\xc6\xe7\xeb+\xed\x01\xd2l'
        tuple_0 = (int_0, bytes_1, float_0, set_0)
        str_3 = '\nmodule: reboot\nshort_description: Reboot a machine\nnotes:\n  - C(PATH) is ignored on the remote node when searching for the C(shutdown) command. Use C(search_paths)\n    to specify locations to search if the default paths do not work.\ndescription:\n    - Reboot a machine, wait for it to go down, come back up, and respond to commands.\n    - For Windows targets, use the M(ansible.windows.win_reboot) module instead.\nversion_added: "2.7"\noptions:\n  pre_reboot_delay:\n    description:\n      - Seconds to wait before reboot. Passed as a parameter to the reboot command.\n      - On Linux, macOS and OpenBSD, this is converted to minutes and rounded down. If less than 60, it will be set to 0.\n      - On Solaris and FreeBSD, this will be seconds.\n    type: int\n    default: 0\n  post_reboot_delay:\n    description:\n      - Seconds to wait after the reboot command was successful before attempting to validate the system rebooted successfully.\n      - This is useful if you want wait for something to settle despite your connection already working.\n    type: int\n    default: 0\n  reboot_timeout:\n    description:\n      - Maximum seconds to wait for machine to reboot and respond to a test command.\n      - This timeout is evaluated separately for both reboot verification and test command success so the\n        maximum execution time for the module is twice this amount.\n    type: int\n    default: 600\n  connect_timeout:\n    description:\n      - Maximum seconds to wait for a successful connection to the managed hosts before trying again.\n      - If unspecified, the default setting for the underlying connection plugin is used.\n    type: int\n  test_command:\n    description:\n      - Command to run on the rebooted host and expect success from to determine the machine is ready for\n        further tasks.\n    type: str\n    default: whoami\n  msg:\n    description:\n      - Message to display to users before reboot.\n    type: str\n    default: Reboot initiated by Ansible\n\n  search_paths:\n    description:\n      - Paths to search on the remote machine for the C(shutdown) command.\n      - I(Only) these paths will be searched for the C(shutdown) command. C(PATH) is ignored in the remote node when searching for the C(shutdown) command.\n    type: list\n    default: [\'/sbin\', \'/bin\', \'/usr/sbin\', \'/usr/bin\', \'/usr/local/sbin\']\n    version_added: \'2.8\'\n\n  boot_time_command:\n    description:\n      - Command to run that returns a unique string indicating the last time the system was booted.\n      - Setting this to a command that has different output each time it is run will cause the task to fail.\n    type: str\n    default: \'cat /proc/sys/kernel/random/boot_id\'\n    version_added: \'2.10\'\n\n  reboot_command:\n    description:\n      - Command to run that reboots the system, including any parameters passed to the command.\n      - Can be an absolute path to the command or just the command name. If an absolute path to the\n        command is not given, C(search_paths) on the target system will be searched to find the absolute path.\n      - This will cause C(pre_reboot_delay), C(post_reboot_delay), and C(msg) to be ignored.\n    type: str\n    default: \'[determined based on target OS]\'\n    version_added: \'2.11\'\nextends_documentation_fragment:\n  -  action_common_attributes\n  -  action_common_attributes.flow\nattributes:\n    action:\n        support: full\n    async:\n        support: none\n    bypass_host_loop:\n        support: none\n    check_mode:\n        support: none\n    diff_mode:\n        support: none\n    platform:\n        platforms: posix\nseealso:\n- module: ansible.windows.win_reboot\nauthor:\n    - Matt Davis (@nitzmahone)\n    - Sam Doran (@samdoran)\n'
        tuple_1 = (tuple_0, bytes_0, set_0, str_3)
        action_module_0 = module_0.ActionModule(float_0, str_1, set_0, bool_0, bytes_0, tuple_1)
        var_0 = action_module_0.run(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        float_0 = 762.81319
        list_0 = [float_0, float_0]
        str_0 = '/sys/block/'
        tuple_1 = (str_0,)
        dict_0 = {tuple_1: float_0, tuple_0: list_0}
        float_1 = 2735.03891
        bool_0 = False
        action_module_0 = module_0.ActionModule(float_1, bool_0, list_0, tuple_0, tuple_0, tuple_0)
        var_0 = action_module_0.get_args_from_task_vars(dict_0, tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -999
        float_0 = 1792.573
        dict_0 = {float_0: int_0, float_0: float_0, float_0: float_0}
        bool_0 = True
        str_0 = 'yhIc=(wtGJOPObUzMN<@'
        dict_1 = {str_0: str_0, bool_0: int_0}
        float_1 = 100.0
        bytes_0 = None
        list_0 = []
        bool_1 = False
        str_1 = 'q%kVS8f~?\x0cKoq1l7:'
        bytes_1 = b'\x17v\x1a\x97\xb3\xe4\xf0m\xfdE\xe4\xd51<d\xe5\xfc\xeb\xb1F'
        action_module_0 = module_0.ActionModule(float_1, str_0, bool_0, bytes_1, bool_1, str_0)
        str_2 = '.M8)]\r\\WHgamr'
        tuple_0 = (bytes_0, action_module_0, str_0)
        tuple_1 = (str_2, tuple_0)
        action_module_1 = module_0.ActionModule(list_0, bool_1, str_1, bool_1, action_module_0, tuple_1)
        action_module_2 = module_0.ActionModule(float_1, int_0, bytes_0, action_module_1, int_0, action_module_1)
        tuple_2 = (float_1, action_module_2)
        action_module_3 = module_0.ActionModule(bool_0, bool_0, str_0, dict_1, tuple_2, str_2)
        var_0 = action_module_3.get_args_from_task_vars(dict_0, dict_0)
    except BaseException:
        pass