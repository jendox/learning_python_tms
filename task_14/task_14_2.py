class MyIterator:
    def __init__(self, m_list):
        self.m_list = m_list
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.counter < len(self.m_list):
            return self.m_list[self.counter]**2
        else:
            raise StopIteration


m_iter = MyIterator([1,22,13,4,52,6,79,81,9,10,123,12,320,4,565,78])
for i in m_iter:
    print(i)