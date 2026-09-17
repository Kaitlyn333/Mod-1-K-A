from patients import Patient       
import csv                          
import matplotlib.pyplot as plt     
from scipy import stats             
import numpy as np                  
import statistics                   


# Load all patient records from the CSV file into Patient.all_patients
Patient.instantiate_from_csv("/Users/alenabhilash/Desktop/CompBME/Module 0/Mod-1-K-A/Metadata and Protein Data for Module 1.csv")


# Sort the patients list in-place by their age (uses get_age as the sort key)
Patient.all_patients.sort(key=Patient.get_age)

# Holds brain weights of male patients
male_bw = []     
# Holds brain weights of female patients
female_bw = []   


# Loop over every Male patient and collect their brain weight
for Patient in Patient.filter(Patient.all_patients, sex="Male"):
    male_bw.append(Patient.brain_weight)


# Loop over every Female patient and collect their brain weight
for Patient in Patient.filter(Patient.all_patients, sex="Female"):
    female_bw.append(Patient.brain_weight)


# Drop any "Unavailable" entries so they don't break the math below (not necessary for male_bw)
female_bw.remove("Unavailable")


# Compute the mean brain weight for each sex
x_male_bar = (statistics.mean(male_bw))
x_female_bar = (statistics.mean(female_bw))


# Compute the standard deviation of brain weight for each sex
bw_male_stdev = (statistics.stdev(male_bw))
bw_female_stdev = (statistics.stdev(female_bw))


# Print the computed stats
print(f'x_male_bar = {x_male_bar}, age_dementia_stdev {bw_male_stdev}')
print(f'x_female_bar = {x_female_bar}, bw_femalestdev {bw_female_stdev}')


# Data for the bar chart: one bar per sex with error bars
sex_cols = ['Male', 'Female']
mean_sex = [x_male_bar, x_female_bar]
stdev_sex = [bw_male_stdev, bw_female_stdev]
yerr = [stdev_sex, stdev_sex]


# Create and show the bar chart
plt.bar(sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("How Biological Sex Affects Brain Weight")
plt.xlabel("Biological Sex")
plt.ylabel("Brain Weight")
plt.show()

# Holds ABeta42 levels for every patient
ABeta42 = []   
# Hold pTAU levels for every patient
pTAU = []      


# Collect ABeta42 measurement from each patient
for Patient in Patient.all_patients:
    ABeta42.append(Patient.ABeta42)


# Collect pTAU measurement from each patient
for Patient in Patient.all_patients:
    pTAU.append(Patient.pTAU)

# Independent variable
X = [ABeta42]  
# Dependent variable
Y = [pTAU]  


# Scatter plot of ABeta42 vs pTAU
plt.scatter(X, Y, color='blue')
plt.xlabel('Amyloid-Beta 42 (pg/ug)')
plt.ylabel('pTAU (pg/ug)')
plt.title('Scatter Plot of ABeta42 levels vs pTAU levels (pg/ug)')
plt.show()