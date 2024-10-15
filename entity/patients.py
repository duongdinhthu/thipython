from entity.entity import Entity

class Patient(Entity):
    def __init__(self, id=None, full_name=None, date_of_birth=None, gender=None, address=None, phone_number=None, email=None):
        super().__init__(id)  # Call the parent constructor from Entity class
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
