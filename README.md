**Predict Hospital Readmission Risk for Patients with Chronic Conditions**





**🧠 Overview**
This project aims to predict the risk of hospital readmission among patients suffering from chronic diseases such as diabetes, hypertension, and heart disease. Hospital readmissions are a critical healthcare concern, both financially and in terms of patient outcomes. Using machine learning, we can identify high-risk patients early and enable healthcare providers to take timely interventions.




**🎯 Objective**
To build and evaluate a machine learning model that predicts whether a patient with a chronic condition is likely to be readmitted to the hospital, based on their clinical and administrative data.





**📁 Dataset**
• Source: Custom dataset (dataset.csv)
• Location: C:/learnathon/dataset.csv





**• Features include:**
  - Demographics (age, gender)
  - Clinical details (diagnoses, conditions)
  - Hospital stay duration
  - Financial info (billing amount)
  - Previous admission details




    
**⚙️ Technologies Used**
• Python
• Pandas, NumPy
• Scikit-learn
• Matplotlib, Seaborn (for visualizations)
• Jupyter Notebook


**🔄 Data Preprocessing**
• Dropped irrelevant columns like Patient_ID
• Converted date columns to calculate Length of Stay
• Label encoding of categorical features
• Standardization of numerical features
• Split data into train/test sets




**🤖 Model Used**
• Logistic Regression (main model)
• Compared with:
  - Decision Tree
  - Random Forest
  - SVM
  - KNN



    
**🧪 Model Output**
🔹 Prediction of Readmission Risk for one sample: 80.61%
📊 Evaluation Metrics
🔹 Accuracy:  93.45%
🔹 Precision: 95.50%
🔹 Recall:    96.41%
🔹 F1 Score:  95.95%
🔹 ROC AUC:   98.12%




**🔭 Future Work**
• Deploy as a web app using Flask
• Add visual dashboards for hospital teams
• Integrate with real-time hospital databases

