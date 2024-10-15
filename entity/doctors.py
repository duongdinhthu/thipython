from entity.entity import Entity

class Doctor(Entity):
    def __init__(self, id=None, full_name=None, specialization=None, phone_number=None, email=None, years_of_experience=None):
        super().__init__(id)  # Gọi constructor của lớp cha Entity
        self.full_name = full_name
        self.specialization = specialization
        self.phone_number = phone_number
        self.email = email
        self.years_of_experience = years_of_experience
