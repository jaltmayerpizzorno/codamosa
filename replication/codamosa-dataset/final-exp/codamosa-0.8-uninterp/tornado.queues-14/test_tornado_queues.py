# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    queue_iterator_0 = module_0._QueueIterator(var_0)

def test_case_2():
    queue_0 = module_0.Queue()

def test_case_3():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__repr__()

def test_case_4():
    queue_0 = module_0.Queue()
    int_0 = queue_0.qsize()

def test_case_5():
    int_0 = 2
    queue_0 = module_0.Queue(int_0)
    int_1 = 3
    queue_0.put_nowait(int_1)
    int_2 = -13
    queue_0.put_nowait(int_2)
    var_0 = queue_0.get_nowait()
    int_3 = queue_0.qsize()
    bool_0 = queue_0.empty()
    bool_1 = queue_0.full()

def test_case_6():
    var_0 = None
    queue_0 = module_0.Queue()
    queue_0.put_nowait(var_0)

def test_case_7():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()

def test_case_8():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    var_0 = None
    queue_0.put_nowait(var_0)
    var_1 = queue_0.get_nowait()
    queue_0.put_nowait(var_1)

def test_case_9():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    var_0 = None
    queue_0.put_nowait(var_0)
    var_1 = queue_0.__aiter__()
    str_1 = queue_0.__str__()

def test_case_10():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    var_0 = None
    queue_0.put_nowait(var_0)
    var_1 = queue_0.__aiter__()
    var_2 = queue_0.get_nowait()
    int_0 = 1988
    queue_1 = module_0.Queue(int_0)
    queue_1.put_nowait(var_2)

def test_case_11():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    var_0 = None
    queue_0.put_nowait(var_0)
    queue_0.put_nowait(var_0)
    var_1 = queue_0.__aiter__()
    var_2 = queue_0.__aiter__()
    var_3 = queue_0.get_nowait()
    queue_0.task_done()
    queue_1 = module_0.Queue()
    queue_0.put_nowait(var_0)