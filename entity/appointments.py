from entity.entity import Entity

class Appointment(Entity):
    def __init__(self, id=None, patient_id=None, doctor_id=None, appointment_date=None, reason=None, status=None):
        super().__init__(id)  # Gọi constructor của lớp cha Entity
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason
        self.status = status
