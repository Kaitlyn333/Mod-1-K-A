import csv

class Patient:

    all_patients = []

    def __init__(self, donor_ID: str, sex: str, age: int, status: str, brain_weight: int, ABeta42: float, pTAU: float):
        self.donor_ID = donor_ID
        self.sex = sex
        self.age = age
        self.status = status
        self.brain_weight = brain_weight
        self.ABeta42 = ABeta42
        self.pTAU = pTAU
        Patient.all_patients.append(self)

    def __repr__(self):  
        return f"{self.donor_ID}: ({self.sex} | {self.age} | {self.status} | {self.brain_weight} | {self.ABeta42} | {self.pTAU})"

    @classmethod 
    def instantiate_from_csv(cls, filename: str):

        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
        
        
            for row in rows_of_patients:
                Patient( 
                    donor_ID = row['Donor ID'],
                    sex = row['Sex'],
                    age = int(row['Age at Death']),
                    status = row['Cognitive Status'],
                    brain_weight = int(row['Fresh Brain Weight']) if row['Fresh Brain Weight'] != "Unavailable" else "Unavailable",
                    ABeta42 = float(row['ABeta42 pg/ug']),
                    pTAU = float(row['pTAU pg/ug'])
                    )
                                                        
    def get_age(self):
        return self.age

    @classmethod
    def filter(cls, list, donor_ID: str = "any", sex: str = "any", age: int = "any", status: str = "any", brain_weight: int = "any", ABeta42: float = "any", pTAU: float = "any"):
            all_patients = list
            remove_list = []
            attr_list = (
                        donor_ID,
                        sex,
                        age,
                        status,
                        brain_weight,
                        ABeta42,
                        pTAU
                        )
            attr_name = (
                        "donor_ID",
                        "sex",
                        "age",
                        "status",
                        "brain_weight",
                        "ABeta42",
                        "pTAU"
                        )
            for attr in range(len(attr_list)):
                if attr_list[attr] != "any":
                    for patient in all_patients:
                        if getattr(patient,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(patient)
                    all_patients = [patient for patient in all_patients if patient not in remove_list]
                    remove_list.clear()

            return all_patients
