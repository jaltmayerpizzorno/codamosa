# Automatically generated by Pynguin.
import tqdm.rich as module_0
import rich.progress as module_1
import typing as module_2

def test_case_0():
    pass

def test_case_1():
    rate_column_0 = module_0.RateColumn()

def test_case_2():
    dict_0 = {}
    str_0 = '+'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = True
    progress_0 = module_1.Progress(*list_0, transient=bool_0, disable=bool_0)
    var_0 = progress_0.add_task(str_0, bool_0, **dict_0)
    float_0 = 2099.0
    int_0 = -406
    task_0 = module_1.Task(var_0, str_0, float_0, float_0, int_0, float_0, str_0)
    fraction_column_0 = module_0.FractionColumn()
    var_1 = fraction_column_0.render(task_0)

def test_case_3():
    str_0 = '}\tV\\k;.'
    bool_0 = False
    progress_0 = module_1.Progress(auto_refresh=bool_0)
    var_0 = progress_0.add_task(str_0)
    none_type_0 = None
    float_0 = -584.9187
    int_0 = 1081
    text_i_o_0 = module_2.TextIO()
    var_1 = text_i_o_0.readline(int_0)
    list_0 = [var_1]
    task_0 = module_1.Task(var_0, str_0, none_type_0, float_0, list_0, bool_0)
    rate_column_0 = module_0.RateColumn()
    var_2 = rate_column_0.render(task_0)
    bool_1 = True
    float_1 = 0.5
    bool_2 = True
    progress_1 = module_1.Progress(auto_refresh=bool_1, speed_estimate_period=float_1, redirect_stdout=bool_2)