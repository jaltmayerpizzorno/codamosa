# Automatically generated by Pynguin.
import tqdm.rich as module_0
import tqdm.std as module_1

def test_case_0():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_1():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_2():
    try:
        rate_column_0 = module_0.RateColumn()
        rate_column_1 = module_0.RateColumn()
        set_0 = {rate_column_0, rate_column_1}
        var_0 = rate_column_0.render(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        rate_column_0 = module_0.RateColumn(bool_0)
        dict_0 = {}
        tqdm_rich_0 = module_0.tqdm_rich(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.trrange()
    except BaseException:
        pass

def test_case_5():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1001
        str_0 = 'test'
        bool_0 = True
        tqdm_0 = module_1.tqdm(str_0, int_0, bool_0)
        var_0 = tqdm_0.close()
    except BaseException:
        pass