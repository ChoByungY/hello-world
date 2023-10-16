import simpy
    
def car(env):
    """
    자동차 프로세스
    주차하고 여행을 떠남
    parking과 driving 상태를 스위칭함
    """
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
                # 환경에서 timeout 이벤트를 발생시킴(parking_duration동안 휴면)
        yield env.timeout(parking_duration)
    
        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)
    
env = simpy.Environment()
env.process(car(env))
env.run(until=15)