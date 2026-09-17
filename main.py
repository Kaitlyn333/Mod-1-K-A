# Import pandas to read and work with the patient CSV file
import pandas as pd

# Import matplotlib and numpy to make graphs and calculate statistics
import matplotlib.pyplot as plt
import numpy as np

# Import the Patient class from patient.py
from patient import Patient


# Read the patient data from the CSV file
data = pd.read_csv("Mod 1/Metadata and Protein Data for Module 1.csv")


# Create an empty list to store all of the Patient objects
patients = []


# Create a Patient object for each row in the CSV file
for index, row in data.iterrows():
    patient = Patient(
        row["Donor ID"],
        row["Age at Death"],
        row["Sex"],
        row["Highest level of education"],
        row["Years of education"],
        row["Cognitive Status"],
        row["Thal"],
        row["ABeta40 pg/ug"],
        row["ABeta42 pg/ug"],
        row["tTAU pg/ug"]
    )

    patients.append(patient)


# Sort the patients by age at death and print them
patients.sort(key=lambda patient: patient.age)

for patient in patients:
    print(patient)


# Use the class method to find female patients with dementia
print("Female patients with dementia:")
Patient.filter_patients(patients, "Female", "Dementia")


# Find ABeta42 values for female patients with dementia
female_abeta42 = [
    patient.abeta42
    for patient in patients
    if patient.sex == "Female" and patient.cognitive_status == "Dementia"
]


# Find ABeta42 values for male patients with dementia
male_abeta42 = [
    patient.abeta42
    for patient in patients
    if patient.sex == "Male" and patient.cognitive_status == "Dementia"
]


# Calculate the mean and standard deviation for each group
means = [np.mean(female_abeta42), np.mean(male_abeta42)]
stds = [np.std(female_abeta42), np.std(male_abeta42)]


# Create a bar graph comparing the two groups
plt.bar(["Female", "Male"], means, yerr=stds, capsize=5)

# Add labels and a title to the bar graph
plt.ylabel("ABeta42 (pg/ug)")
plt.xlabel("Sex")
plt.title("Mean ABeta42 Levels by Sex in Patients with Dementia")

# Display the bar graph
plt.show()


# Create lists of age at death and ABeta42 levels for the scatter plot
ages = [patient.age for patient in patients]
abeta42 = [patient.abeta42 for patient in patients]


# Create a scatter plot of age at death versus ABeta42
plt.scatter(ages, abeta42)

# Add labels and a title to the scatter plot
plt.xlabel("Age at Death")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("ABeta42 Levels vs. Age at Death")

# Display the scatter plot
plt.show()