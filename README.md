# 🏥 **Predict Hospital Readmission Risk for Patients with Chronic Conditions**

---

### 👥 **Team ID:** `TEAM(SC2)-09`

#### 👨‍💻 Team Members:
- **Gudla Sindhuja** – `23CSE619` – 23UG010696  
- **Wilson Sahani** – `23ECE059` – 23UG011083  
- **Pitta Saiganesh** – `23CSE640` – 23UG010716  
- **Subhasmita Das** – `23CSE625` – 23UG010701  

---

## 🧠 **Overview**

Hospital readmissions, especially for patients with **chronic illnesses** like **diabetes**, **hypertension**, and **heart disease**, are a major concern for healthcare systems — both in terms of **cost** and **patient health**.  
This project leverages **machine learning** to predict **readmission risks**, helping hospitals take **preventive action** and improve **patient outcomes**.

---

## 🎯 **Objective**

To build and evaluate a **machine learning model** that predicts whether a patient with a **chronic condition** is likely to be **readmitted**, based on their **clinical and administrative data**.

---

## 📁 **Dataset**

- **Source**: Custom dataset (`dataset.csv`)  
- **Local Path**: `C:/learnathon/dataset.csv`

### 🔍 Features Include:
- **Demographics**: Age, Gender  
- **Clinical Details**: Diagnoses, Conditions  
- **Hospital Stay Duration**  
- **Financial Info**: Billing Amount  
- **Previous Admission Details**

---

## ⚙️ **Technologies Used**

- **Python**  
- **Pandas**, **NumPy**  
- **Scikit-learn**  
- **Matplotlib**, **Seaborn** *(for visualizations)*  
- **Jupyter Notebook**

---

## 🔄 **Data Preprocessing**

- Removed irrelevant columns like `Patient_ID`  
- Calculated **Length of Stay** from admission and discharge dates  
- **Label Encoded** categorical variables  
- **Standardized** numerical features  
- Split dataset into **training** and **testing** sets

---

## 🤖 **Modeling**

### ✅ Main Model:
- **Logistic Regression**

### 🔁 Models Compared:
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)

---

## 🧪 **Model Results**

### 📌 Sample Prediction:
- **Readmission Risk**: `80.61%`

### 📊 Evaluation Metrics:
| Metric       | Score     |
|--------------|-----------|
| Accuracy     | 93.45%    |
| Precision    | 95.50%    |
| Recall       | 96.41%    |
| F1 Score     | 95.95%    |
| ROC AUC      | 98.12%    |

---

## 🔭 **Future Enhancements**

- Deploy as a **Flask Web Application**  
- Integrate **real-time hospital dashboards**  
- Connect to **live hospital databases** for production use  

---

## 📌 **Contact**

For questions or collaboration, reach out to any of the team members listed above.
gmail - saiganesh1901@gmail.com
