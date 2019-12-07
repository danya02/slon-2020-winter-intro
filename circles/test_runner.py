import gen
import detect
import sys
import io
import math
import time

def test_single():
    outstream = sys.stdout
    fakeout = io.StringIO()
    sys.stdout = fakeout
    truex, truey,path = gen.gen_testcase()
    sys.stdout = outstream
    print('True answer:',truex,truey)
    sys.stdout = fakeout
    testa = detect.detect(path)
    sys.stdout = outstream
    if testa is not None:
        testx, testy = testa
        print('Algo\'s answer:',testx,testy)
        print('Deltas:',testx-truex, testy-truey)
        dist = math.hypot(testx-truex, testy-truey)
        print('Distance:',dist)
        return dist
    else:
        print('The algo says there are no circles!')
        return None

def get_test_score(iterations=float('inf'), key_func=lambda avg_error, failure_rate, avg_time: avg_error/(1-failure_rate)):
    tests = 1
    ts = time.time()
    sumdists = test_single()
    t = time.time()-ts
    errors=0

    while tests<iterations:
        print('Average error (out of {} tests, with {} ({}) fails): {}'.format(tests, errors, errors/tests, sumdists/tests))
        print('Average time:', t/tests)
        score = key_func(sumdists/tests, errors/tests, t/tests)
        print('Current score:', score)
        print('====')
        ts = time.time()
        d = test_single()
        if d is None:
            errors+=1
        else:
            sumdists+=d
        t += time.time()-ts
        tests+=1
    return key_func(sumdists/tests, errors/tests, t/tests)

if __name__=='__main__':
    get_test_score()
