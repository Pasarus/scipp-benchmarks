import scipp as sc

class Scipp:
    """
    Benchmark creating, adding, and, removing from Variables.
    """
    def setup(self):
        self.var1 = sc.array(dims=['x'], values=[1, 2, 3, 4, 5])
        self.var2 = sc.array(dims=['x'], values=[1, 2, 3, 4, 5])

    def time_shallow_copy(self):
        self.var1 = self.var2

    def time_deep_copy(self):
        self.var1.copy()

    def time_variable_inplace_operation(self):
        self.var1 += self.var2

    def time_variable_non_inplace_operation(self):
        self.var1 + self.var2
