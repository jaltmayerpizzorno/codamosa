# Automatically generated by Pynguin.
import thefuck.rules.lein_not_task as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "\n    :namespaces [:dependencies, :help, :hooks, :install, :lectures, :monad, :profile, :repl-options, :repl, :shell, :show, :test, :trace, :uberjar, :update, :vcs, :version, :with-profile]\n    lein: 'migrattion' is not a task. See 'lein help'\n    Did you mean this? migration\n    "
    str_1 = ''
    var_0 = ()
    str_2 = 'script'
    str_3 = 'output'
    str_4 = 'lein migrattion'
    str_5 = {str_2: str_4, str_3: str_0}
    var_1 = type(str_1, var_0, str_5)
    var_2 = module_0.get_new_command(var_1)