# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    pass

def test_case_1():
    queue_0 = module_0.Queue()
    var_0 = queue_0.__aiter__()
    str_0 = queue_0.__repr__()

def test_case_2():
    queue_0 = module_0.Queue()

def test_case_3():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()

def test_case_4():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.empty()
    queue_1 = module_0.Queue()
    var_0 = queue_0.__aiter__()
    var_1 = None
    queue_1.put_nowait(var_1)

def test_case_5():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.full()
    lifo_queue_0 = module_0.LifoQueue()

def test_case_6():
    queue_0 = module_0.Queue()
    var_0 = None
    queue_0.put_nowait(var_0)

def test_case_7():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__repr__()

def test_case_8():
    var_0 = None
    queue_0 = module_0.Queue()
    queue_0.put_nowait(var_0)
    queue_0.task_done()
    bool_0 = queue_0.full()
    var_1 = queue_0.get_nowait()

def test_case_9():
    queue_0 = module_0.Queue()
    var_0 = None
    queue_0.put_nowait(var_0)
    str_0 = queue_0.__repr__()

def test_case_10():
    var_0 = None
    int_0 = 3692
    queue_0 = module_0.Queue(int_0)
    queue_0.put_nowait(var_0)
    bool_0 = queue_0.full()
    var_1 = queue_0.get_nowait()

def test_case_11():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    bool_0 = queue_0.empty()
    str_1 = queue_0.__repr__()
    var_0 = queue_0.__aiter__()
    var_1 = None
    queue_0.put_nowait(var_1)
    str_2 = "Mp|%Qq=FH'1o/jiO"
    queue_iterator_0 = module_0._QueueIterator(str_2)
    queue_empty_0 = module_0.QueueEmpty()
    queue_0.put_nowait(var_1)
    queue_0.task_done()
    bool_1 = queue_0.full()
    var_2 = queue_0.get_nowait()