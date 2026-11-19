class Student():
    def __init__(self, fname="", lname="", id=0, energy_level=10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return("lname:", id)

    def greeting(self):
        print(f"Hello! I'm {self.fname} {self.lname}.")

    def take_exam(self):
        self.energy_level -= 1

    def get_energy_level(self):
        return self.energy_level