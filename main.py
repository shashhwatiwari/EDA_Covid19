import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("Covid Data.csv")

p_count = data["PATIENT_TYPE"].count()  # number of patients total in csv file.
print(p_count)

# proportion of patient types.
count_1, count_2 = 0, 0
type_list = data['PATIENT_TYPE'].to_list()
for item in type_list:
    item = int(item)
    if item == 1:
        count_1 += 1
    elif item == 2:
        count_2 += 1

type_1 = float(count_1 / p_count) * 100
type_2 = float(count_2 / p_count) * 100
print(f"Type 1 patients i.e the proportion of patients who were treated at home are {round(type_1, 2)} and the "
      f"proportion of "
      f"patients who were hospitalized were {round(type_2, 2)}")

# Plotting the same on a bar graph to show the contrast visually.
# Counting the number of patients in each treatment type
treatment_counts = data['PATIENT_TYPE'].value_counts()
print(f"The values of 'Treated at home' vs those who were 'Hospitalized' is as follows :- \n{treatment_counts}")

# TREATMENT TYPE CHART
plt.bar(treatment_counts.index, treatment_counts.values)  # .index being a functionality provided by matplotlib

# Adding labels and title
plt.xlabel('Patient Type')
plt.ylabel('Number of Patients')
plt.title('Number of Patients by Treatment Type: At Home or Hospitalized')
plt.show()

# DISTRIBUTION BY AGE
# Extract the age column as a numpy array
ages = data['AGE'].values

# Create a histogram of the age distribution
plt.hist(ages, bins=30, color='green')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Display the plot
plt.show()

# MORTALITY RATE.


def categorize_date(date):
    if date == '9999-99-99':
        return 'Alive'
    else:
        return 'Dead'


# Apply the function to the date column and count the values
counts = data['DATE_DIED'].apply(categorize_date).value_counts()
print(f"The proportion of people who survived the disease are as follows: \n{counts}")

# Create a pie chart of the counts
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')

# Add a title
plt.title('Proportion of Alive and Dead Individuals')

# Display the plot
plt.show()

# Cardiovascular vs death ratio
# Filter the individuals who had cardiovascular issues and died
filtered = data[(data['CARDIOVASCULAR'] == 1) & (data['DATE_DIED'] == '9999-99-99')]

# Group the individuals by cardiovascular status and survival status
groups = filtered.groupby(['CARDIOVASCULAR', 'DATE_DIED'])

# Count the number of individuals in each group
counts = groups.size().unstack()

# Plot a bar chart of the counts
ax = counts.plot(kind='bar', stacked=True)

# Add labels and a title
ax.set_xlabel('Cardiovascular Status')
ax.set_ylabel('Count')
ax.set_title('Counts of Individuals with Cardiovascular Issues who Died')

# Display the plot
plt.show()


# PEOPLE WHO DIED AND HAD CARDIOVASCULAR ISSUES VS WHO DIED AND DIDNT HAVE THEM.

df_died = data[data['DATE_DIED'] != '9999-99-99']

# Count the number of individuals who died with and without cardiovascular issues
died_cardio_count = df_died[df_died['CARDIOVASCULAR'] == 1].shape[0]
died_no_cardio_count = df_died[df_died['CARDIOVASCULAR'] == 2].shape[0]

# Create a pie chart of the died_cardio_count and died_no_cardio_count data
labels = ['Cardiovascular Issues', 'No Cardiovascular Issues']
sizes = [died_cardio_count, died_no_cardio_count]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
ax.set_title('Proportion of Individuals who Died with and without Cardiovascular Issues')

# Display the plot
plt.show()

# FOR TOBACCO USE
df_died = data[data['DATE_DIED'] != '9999-99-99']

# Count the number of individuals who died with and without tobacco issues
died_tobac_count = df_died[df_died['TOBACCO'] == 1].shape[0]
died_no_tobac_count = df_died[df_died['TOBACCO'] == 2].shape[0]

# Create a pie chart of the died_cardio_count and died_no_cardio_count data
labels = ['Had a Tobacco dependence', 'No dependence']
sizes = [died_tobac_count, died_no_tobac_count]

fig2, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
ax.set_title('Proportion of Individuals who Died with and without Tobacco consumption and its dependence.')

# Display the plot
plt.show()

# THOSE WHO DIED AND REQUIRED ICU BEFORE THEY PASSED.
df_died = data[data['DATE_DIED'] != '9999-99-99']

# Count the number of individuals who died with and without icu use.
died_icu_count = df_died[df_died['ICU'] == 2].shape[0]
died_no_icu_count = df_died[df_died['ICU'] == 97].shape[0]

# Create a pie chart of the died_cardio_count and died_no_cardio_count data
labels = ['Needed ICU', 'No ICU needed']
sizes = [died_icu_count, died_no_icu_count]

fig3, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
ax.set_title('Proportion of Individuals who Died with the use of ICU and without.')

# Display the plot
plt.show()

# studying obesity as a factor causing the death of a patient.
df_died = data[data['DATE_DIED'] != '9999-99-99']

# Count the number of individuals who died and were either obese or not.
died_obs_count = df_died[df_died['OBESITY'] == 1].shape[0]
died_no_obs_count = df_died[df_died['OBESITY'] == 2].shape[0]


labels = ['Obese', 'Not Obese']
sizes = [died_icu_count, died_no_icu_count]

fig4, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
ax.set_title('Proportion of Individuals who Died and were Obese vs those who were not.')

# Display the plot
plt.show()






