import random
import time

class FaultInjector:
    def __init__(self, drop_rate=0.1, modify_rate=0, delay_rate=0.1, delay_time=1.0, corruption_rate=0.1, reordering_rate=0.1):
        self.drop_rate = drop_rate
        self.modify_rate = modify_rate
        self.delay_rate = delay_rate
        self.delay_time = delay_time
        self.corruption_rate = corruption_rate
        self.reordering_rate = reordering_rate
        random.seed(time.time())

    def inject_faults(self, data):
        if random.random() < self.drop_rate:
            return None
        if random.random() < self.modify_rate:
            return None
        if random.random() < self.delay_rate:
            return self.inject_delay(data, self.delay_time)
        if random.random() < self.corruption_rate:
            return self.inject_corruption(data)
        if random.random() < self.reordering_rate:
            return self.inject_reordering(data)
        return data
    
    def inject_delay(self, data, delay_time=1.0):
        time.sleep(delay_time)
        return data

    def inject_corruption(self, data):
        if isinstance(data, str):
            corrupted_data = list(data)
            index = random.randint(0, len(corrupted_data) - 1)
            corrupted_data[index] = chr(random.randint(32, 126))
            return ''.join(corrupted_data)
        return data

    def inject_reordering(self, data_list):
        if len(data_list) > 1:
            index1, index2 = random.sample(range(len(data_list)), 2)
            data_list[index1], data_list[index2] = data_list[index2], data_list[index1]
        return data_list