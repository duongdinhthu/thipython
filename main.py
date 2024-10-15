from controller.mainController import MainController  # Import controller tổng hợp
from entity.patients import Patient
from entity.doctors import Doctor
from entity.appointments import Appointment

def print_menu():
    print("----- MENU -----")
    print("1. Manage Patients")
    print("2. Manage Doctors")
    print("3. Manage Appointments")
    print("4. Exit")

def print_crud_menu():
    print("\nChoose an action:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Back to main menu")

def get_input_for_patient():
    full_name = input("Enter patient full name: ")
    date_of_birth = input("Enter patient date of birth (YYYY-MM-DD): ")
    gender = input("Enter patient gender (M/F): ")
    address = input("Enter patient address: ")
    phone_number = input("Enter patient phone number: ")
    email = input("Enter patient email: ")
    return Patient(full_name=full_name, date_of_birth=date_of_birth, gender=gender, 
                   address=address, phone_number=phone_number, email=email)

def get_input_for_doctor():
    full_name = input("Enter doctor full name: ")
    specialization = input("Enter doctor specialization: ")
    phone_number = input("Enter doctor phone number: ")
    email = input("Enter doctor email: ")
    years_of_experience = input("Enter doctor years of experience: ")
    return Doctor(full_name=full_name, specialization=specialization, 
                  phone_number=phone_number, email=email, 
                  years_of_experience=years_of_experience)

def get_input_for_appointment():
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    reason = input("Enter appointment reason: ")
    status = input("Enter appointment status: ")
    return Appointment(patient_id=patient_id, doctor_id=doctor_id, 
                       appointment_date=appointment_date, reason=reason, 
                       status=status)

def main():
    controller = MainController()  # Khởi tạo controller tổng hợp
    while True:
        print_menu()
        choice = input("Select an entity to manage: ")

        if choice == '4':
            print("Exiting...")
            break

        if choice == '1':  # Manage Patients
            while True:
                print_crud_menu()
                crud_choice = input("Choose an action for Patients: ")

                if crud_choice == '1':  # Create
                    patient = get_input_for_patient()
                    controller.create(Patient, patient)
                    print(f"Patient {patient.full_name} added successfully!")
                elif crud_choice == '2':  # Read
                    patients = controller.get_all(Patient)
                    print("All Patients:", patients)
                elif crud_choice == '3':  # Update
                    patient_id = input("Enter the patient ID to update: ")
                    fields_to_update = input("Enter fields to update (as dictionary): ")
                    controller.update(Patient, patient_id, fields_to_update)
                elif crud_choice == '4':  # Delete
                    patient_id = input("Enter the patient ID to delete: ")
                    controller.delete(Patient, patient_id)
                elif crud_choice == '5':  # Back to main menu
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '2':  # Manage Doctors
            while True:
                print_crud_menu()
                crud_choice = input("Choose an action for Doctors: ")

                if crud_choice == '1':  # Create
                    doctor = get_input_for_doctor()
                    controller.create(Doctor, doctor)
                    print(f"Doctor {doctor.full_name} added successfully!")
                elif crud_choice == '2':  # Read
                    doctors = controller.get_all(Doctor)
                    print("All Doctors:", doctors)
                elif crud_choice == '3':  # Update
                    doctor_id = input("Enter the doctor ID to update: ")
                    fields_to_update = input("Enter fields to update (as dictionary): ")
                    controller.update(Doctor, doctor_id, fields_to_update)
                elif crud_choice == '4':  # Delete
                    doctor_id = input("Enter the doctor ID to delete: ")
                    controller.delete(Doctor, doctor_id)
                elif crud_choice == '5':  # Back to main menu
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '3':  # Manage Appointments
            while True:
                print_crud_menu()
                crud_choice = input("Choose an action for Appointments: ")

                if crud_choice == '1':  # Create
                    appointment = get_input_for_appointment()
                    controller.create(Appointment, appointment)
                    print(f"Appointment for patient ID {appointment.patient_id} added successfully!")
                elif crud_choice == '2':  # Read
                    appointments = controller.get_all(Appointment)
                    print("All Appointments:", appointments)
                elif crud_choice == '3':  # Update
                    appointment_id = input("Enter the appointment ID to update: ")
                    fields_to_update = input("Enter fields to update (as dictionary): ")
                    controller.update(Appointment, appointment_id, fields_to_update)
                elif crud_choice == '4':  # Delete
                    appointment_id = input("Enter the appointment ID to delete: ")
                    controller.delete(Appointment, appointment_id)
                elif crud_choice == '5':  # Back to main menu
                    break
                else:
                    print("Invalid choice, please try again.")

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
