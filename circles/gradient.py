import test_runner
import settings
import threading
import multiprocessing
import time
import json

def get_score_at(p1,p2):
    sp1,sp2 = settings.param1, settings.param2
    settings.param1, settings.param2 = p1,p2
    v = test_runner.get_test_score(1)
    settings.param1, settings.param2 = sp1, sp2
    return v

def save_params():
    with open('settings.py','w') as o:
        print('param1 = {}\nparam2 = {}'.format(settings.param1, settings.param2), file=o)

class DeferredComputationProcess:
    cached_values = {}
    def __init__(self, param1, param2):
        try:
            DeferredComputationProcess.cached_values = json.load(open('score_cache.json'))
        except:
            pass
        self.param1 = param1
        self.param2 = param2
        if str((self.param1, self.param2)) in DeferredComputationProcess.cached_values:
            self.value = DeferredComputationProcess.cached_values[str((self.param1, self.param2))]
        else:
            self.value = None

    def start_work(self):
        if self.value is None:
            my_pipe, his_pipe = multiprocessing.Pipe()
            self.pipe = my_pipe
            self.proc = multiprocessing.Process(target=self.work, args=(self.param1, self.param2, his_pipe))
            self.proc.start()
            thread = threading.Thread(target=self.wait_until_ready)
            thread.start()
    
    @staticmethod
    def work(p1,p2,pipe):
        v=get_score_at(p1, p2)
        pipe.send(str(v))

    def wait_until_ready(self):
        self.proc.join()
        v = float(self.pipe.recv())
        self.value = v
        DeferredComputationProcess.cached_values.update({str((self.param1, self.param2)):v})
        json.dump(DeferredComputationProcess.cached_values, open('score_cache.json', 'w'))

    @property
    def ready(self):
        return self.value is not None
    
    @property
    def result(self):
        return self.value

def compute_gradient():
    current_value = DeferredComputationProcess(settings.param1, settings.param2)
    current_value.start_work()
    step_value = 1
    neighbor_values = []
    for i in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        p1,p2 = settings.param1, settings.param2
        p1+=i[0]
        p2+=i[1]
        neighbor_values.append(DeferredComputationProcess(p1,p2))
        neighbor_values[-1].start_work()
    for i in [current_value]+neighbor_values:
        while not i.ready:
            time.sleep(0.1)
    # TODO: compute proportional gradient; this just returns minimum direction

    mindir = min(neighbor_values, key=lambda x: x.result)
    return mindir.param1-settings.param1, mindir.param2-settings.param2, current_value.result

def gradient_descent():
    while 1:
        p1d, p2d, score = compute_gradient()
        settings.param1+=int(p1d)
        settings.param2+=int(p2d)
        print(settings.param1, settings.param2, score)
        save_params()
if __name__ == '__main__':
    gradient_descent()
