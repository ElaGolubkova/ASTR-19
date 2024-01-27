class Animal:
    def __init__(self, name, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Description of a {self.name}:")
        print(f"Arm Length: {self.arm_length} inches")
        print(f"Leg Length: {self.leg_length} inches")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")

wolf = Animal("wolf",15.0, 15.0, 2, True, True)

wolf.describe()

