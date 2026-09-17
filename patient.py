# Define the Patient class
class Patient:

    # Initialize a Patient object with information from the CSV file
    def __init__(self, donor_id: str, age: float, sex: str, education: str,
                 years_education: float, cognitive_status: str, thal: str,
                 abeta40: float, abeta42: float, tau: float):

        self.donor_id = donor_id
        self.age = age
        self.sex = sex
        self.education = education
        self.years_education = years_education
        self.cognitive_status = cognitive_status
        self.thal = thal
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.tau = tau

    # Define how a Patient object is displayed when it is printed
    def __repr__(self):
        return f"{self.donor_id}: ({self.age} | {self.sex} | {self.cognitive_status} | {self.thal})"

    # Filter patients based on sex and cognitive status and print the matches
    @classmethod
    def filter_patients(cls, patients, sex, cognitive_status):
        for patient in patients:
            if patient.sex == sex and patient.cognitive_status == cognitive_status:
                print(patient)