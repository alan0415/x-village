class Map:
    my_map = list()
    def set_map(self, n_arg):
        self.n = n_arg
        for i in range (0, self.n + 1):
            a = list()
            for j in range (0, self.n + 1):
                a[j] = '*'
            self.my_map[i].extend(a)
    def set_pattern(self, p_arg):
        pass
    def display(self):
        j = 0
        for i in range(0, self.n):
            print(self.my_map[j])
            print(' ')
            i += 1
my_map = Map()
my_map.set_map(5)