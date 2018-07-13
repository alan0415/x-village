class Shape:
    def set_edge(self, edge_arg):
        self.edge = edge_arg
    def display(self):
        i=1
        j=1 
        k=1
        while i <= self.edge:
            while j <= k:
                print("*",end ='')
                j += 1
            i += 1
            k += 1
            j = 1
            print("")
x = Shape()
x.set_edge(6)
#print("edge = ", x.edge)
x.display()