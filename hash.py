class h_table:
    def __init__(self):
        self.table=[[]]*20

    def insert(self, index, val):
        k=h_func(index)
        self.table[k].append((table,val)) #inside, should be read as tuple

    def h_func(index):
        return index%20

    def retrieve(input):
        for k in table[input%20]:
            if k[0]==input
            return k[1]
