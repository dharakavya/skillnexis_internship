Bank Loan Approval Prediction Using Machine Learning
📌 Project Overview
The Bank Loan Approval Prediction project is a machine learning application that predicts whether a loan application is likely to be approved or rejected based on applicant details, financial information, credit history, and property area.

The project uses supervised machine learning classification algorithms to learn patterns from historical loan application data. It compares multiple models and integrates the selected model into a web application built with Streamlit.

This project demonstrates a complete machine learning workflow, including data preprocessing, exploratory analysis, model training, evaluation, and deployment through an interactive interface.
🎯 Objectives
- Analyze and preprocess a real-world loan application dataset.
- Handle missing values in numerical and categorical features.
- Convert categorical variables into machine-readable features.
- Train and compare machine learning classification models.
- Evaluate model performance using classification metrics.
- Develop an interactive web application for loan status prediction.
- Present predictions in a user-friendly interface.
📊 Dataset Information
Dataset: Loan Prediction Dataset

Source: Kaggle – Loan Prediction Dataset

The dataset contains information about loan applicants and their loan approval status.
- Total records: 614
- Original columns: 13
- Columns after removing Loan_ID: 12
- Input features: 11
- Target variable: Loan_Status
Features Used
Feature	Description
Gender	Gender of the applicant
Married	Marital status
Dependents	Number of dependents
Education	Applicant's education level
Self_Employed	Whether the applicant is self-employed
ApplicantIncome	Applicant's income
CoapplicantIncome	Coapplicant's income
LoanAmount	Requested loan amount
Loan_Amount_Term	Loan term in months
Credit_History	Credit history indicator
Property_Area	Urban, semiurban, or rural area


Target Variable
The target variable is Loan_Status.
- Y — Loan approved
- N — Loan rejected
The original dataset contains 422 approved applications and 192 rejected applications.
🛠️ Technologies Used
- Programming Language: Python
- Data Manipulation: Pandas, NumPy
- Machine Learning: Scikit-learn
- Data Visualization: Matplotlib, Seaborn
- Model Persistence: Joblib
- Web Application: Streamlit
- Development Environment: Jupyter Notebook / VS Code
- Dataset Source: Kaggle
🔄 Project Workflow
1. Data Collection
The loan prediction dataset was obtained from Kaggle.
2. Data Preprocessing
The dataset was prepared for machine learning by:
- Checking missing values.
- Checking duplicate records.
- Removing the Loan_ID column because it is an identifier rather than a meaningful predictive feature.
- Separating the input features and target variable.
- Identifying numerical and categorical columns.
- Handling missing numerical values using median imputation.
- Handling missing categorical values using most-frequent imputation.
- Encoding categorical variables using One-Hot Encoding.
A preprocessing pipeline was created to apply these transformations consistently during training and prediction.
3. Train-Test Split
The dataset was divided into training and testing sets.
- Training set: 80%
- Testing set: 20%
- Random state: 42
- Stratification: Applied to preserve the target class proportions.
The resulting dataset contained 491 training records and 123 testing records.
4. Model Training
Two classification algorithms were trained and evaluated.

Random Forest Classifier

Random Forest combines predictions from multiple decision trees to perform classification.

Logistic Regression

Logistic Regression estimates the likelihood of a categorical outcome and is commonly used for binary classification problems.

Both models were trained using preprocessing pipelines to handle missing values and categorical features.
5. Model Evaluation
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
These metrics provide different perspectives on classification performance.
6. Model Selection
The following results were obtained on the same test split.
Model	Accuracy	Precision	Recall	F1-Score
Random Forest	82.11%	83.87%	91.76%	87.64%
Logistic Regression	82.93%	87.21%	88.24%	87.72%


Logistic Regression was selected for the initial web application because it achieved slightly higher accuracy, precision, and F1-score on this particular test split.

Random Forest achieved higher recall for approved applications. The results do not establish that either model will perform better on every dataset.
7. Model Saving
The trained Logistic Regression pipeline was saved using Joblib.

The saved file is:

loan_approval_model.pkl

Saving the complete pipeline allows the application to reuse the fitted preprocessing steps and trained classifier without retraining the model each time.
8. Web Application Development
A web interface was developed using Streamlit.

Users can enter applicant details through an interactive form and obtain a prediction from the trained model.

The application includes:
- Applicant information inputs.
- Financial information inputs.
- Credit history selection.
- Property area selection.
- Loan approval prediction.
- Model-estimated approval probability, when available.
- A summary of the submitted application details.
The application is intended for educational demonstration, not for making actual lending decisions.
📈 Model Performance
The selected Logistic Regression model achieved the following results on the held-out test dataset:
Evaluation Metric	Score
Accuracy	82.93%
Precision	87.21%
Recall	88.24%
F1-Score	87.72%


Interpretation:
- Accuracy: The proportion of all test predictions that were correct.
- Precision: Of the applications predicted as approved, the proportion that were actually approved.
- Recall: Of the applications that were actually approved, the proportion correctly identified by the model.
- F1-score: The harmonic mean of precision and recall.
These scores describe performance on one test split. They do not guarantee similar results on new applications.
📁 Project Structure
Bank_Loan_Approval_Prediction/
│
├── app.py
├── loan_approval_model.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
    └── loan_approval_prediction.ipynb