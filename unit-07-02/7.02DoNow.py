class Pet:
  def __init__(self, name):
    self.name = name

my_pet = Pet('Peter')
print(my_pet.name)

class PrintTest:
    """demo"""
    def __init__(self):
        print('Did i get here?')

my_print = PrintTest()