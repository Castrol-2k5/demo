"""OOP trong Python"""
class Bird:
    def intro(self):
        print("This is  bird ")
    def flight(self):
        print("Flying method")
class Eagle(Bird):
    def flight(self):
        print("Eagle Flying")
class Hawks(Bird):
    def flight(self):
        print("Hawks Flying")
obj_bird = Bird()
obj_eag = Eagle()
obj_haw = Hawks()
obj_bird.intro()
obj_bird.flight()
obj_eag.intro()
obj_eag.flight()
obj_haw.intro()
obj_haw.flight()