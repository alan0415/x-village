class Ball:
    def set_radius(self,radius_arg):
        self.radius = radius_arg
    def calculate_volume(self):
        volume = 4/3 * 3.14 * (self.radius*self.radius*self.radius)
        return volume
    def calculate_surface_area(self):
        self.surface_area = 4 * 3.14 * (self.radius*self.radius)
x = Ball()
x.set_radius(5)
print(x.radius)
x_volume = x.calculate_volume()
print('x_volume: ',x_volume)