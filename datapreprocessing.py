import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("C:\learnathon\dataset.csv")

# Drop irrelevant columns
df = df.drop(columns=['Name', 'Doctor', 'Room Number'])

# Convert date columns
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

# Feature engineering: Length of stay
df['Length of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days
df = df.drop(columns=['Date of Admission', 'Discharge Date'])

# List of categorical columns to encode
categorical_cols = ['Gender', 'Blood Type', 'Medical Condition', 'Hospital',
                    'Insurance Provider', 'Admission Type', 'Medication', 'Test Results']

# Label Encoding (or you can use OneHotEncoder later)
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # store for inverse transform if needed

# Final check
df.info()
df.head()
