# 🏠 House Price Prediction Using Linear Regression
House Price Prediction Using Linear Regression
📌 Project Overview
House Price Prediction is a Machine Learning project that predicts house prices based on various property features.

This project implements a Linear Regression model using Python and Scikit-learn to understand the relationship between property characteristics and house prices. The model is trained on a housing dataset and evaluated using the R² score.

The project demonstrates the fundamental steps of a Machine Learning workflow, from data exploration and preprocessing to model training, prediction, evaluation, and visualization.
🎯 Objectives
- Analyze and understand the housing dataset.
- Perform data preprocessing and exploratory data analysis.
- Convert categorical variables into numerical representations.
- Build a Linear Regression model for house price prediction.
- Evaluate model performance using the R² score.
- Visualize actual versus predicted house prices.
📊 Dataset
Dataset: Housing Prices Dataset
Source: Kaggle – Housing Prices Dataset

The dataset contains 545 records and 13 columns, including house prices and property characteristics.
Features
Feature	Description
Price	House price (target variable)
Area	Area of the house
Bedrooms	Number of bedrooms
Bathrooms	Number of bathrooms
Stories	Number of stories
Mainroad	Main road accessibility
Guestroom	Guestroom availability
Basement	Basement availability
Hotwaterheating	Hot-water heating availability
Airconditioning	Air-conditioning availability
Parking	Number of parking spaces
Prefarea	Whether the house is in a preferred area
Furnishingstatus	Furnishing status of the house


Target Variable: price
🛠️ Technologies Used
- Programming Language: Python
- Data Analysis: Pandas, NumPy
- Data Visualization: Matplotlib
- Machine Learning: Scikit-learn
- Development Environment: Jupyter Notebook
⚙️ Methodology
1. Data Loading
Loaded the housing dataset into a Pandas DataFrame for analysis.
2. Exploratory Data Analysis
Examined the dataset structure, data types, descriptive statistics, missing values, duplicate records, and house price distribution.
3. Data Preprocessing
Separated the independent features from the target variable. Converted categorical features into numerical representations using one-hot encoding with pd.get_dummies().
4. Train-Test Split
Divided the dataset into training and testing sets using an 80:20 ratio.
5. Model Training
Trained a Linear Regression model using the training dataset.
6. Price Prediction
Generated house price predictions using the testing dataset.
7. Model Evaluation
Evaluated the model using the R² score to measure how well it explains variations in house prices.
8. Data Visualization
Created an Actual vs Predicted House Prices scatter plot to compare predicted prices with actual prices.
📈 Model Performance
The Linear Regression model achieved the following results:
Evaluation Metric	Score
Training R² Score	0.6859
Testing R² Score	0.6529
Testing R² Percentage	65.29%


Performance Analysis
The model achieved a testing R² score of 0.6529, indicating that it explains approximately 65.29% of the variation in house prices within the test dataset.

The training and testing scores are relatively close, suggesting that severe overfitting is unlikely. However, the model's predictive performance could be improved through additional feature engineering, more informative data, or alternative regression algorithms.

Note: R² measures the variation in the target variable explained by the model. It is not the same as prediction accuracy.
📉 Actual vs Predicted House Prices
The project includes a scatter plot comparing actual house prices against predicted house prices.
- X-axis: Actual house prices.
- Y-axis: Predicted house prices.
- Diagonal reference line: Represents perfect predictions.
- Points near the line: Indicate predictions closer to actual prices.
This visualization helps assess the model's predictive performance and identify differences between actual and predicted values.
📁 Project Structure
- Housing.csv — Dataset used for model development.
- house_price_prediction.ipynb — Jupyter Notebook containing data exploration, preprocessing, model training, prediction, evaluation, and visualization.
- README.md — Project documentation.
🚀 How to Run the Project
1. Clone the repository from GitHub.
2. Install Python and the required libraries.
3. Open the Jupyter Notebook.
4. Ensure the dataset is available at the specified file path.
5. Execute the notebook cells in order to reproduce the results.
Required Libraries
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
🔮 Future Improvements
- Perform additional feature engineering.
- Experiment with nonlinear regression techniques.
- Compare Linear Regression with Decision Tree and Random Forest models.
- Evaluate predictions using MAE and RMSE.
- Apply cross-validation for more reliable model evaluation.
- Investigate additional property features that may influence house prices.
🎓 Key Learnings
Through this project, I gained practical experience in:
- Data exploration and preprocessing.
- Encoding categorical variables.
- Training and testing Machine Learning models.
- Implementing Linear Regression with Scikit-learn.
- Evaluating regression performance using R².
- Visualizing actual and predicted values.
- Documenting a Machine Learning project for GitHub.
📝 Conclusion
This project demonstrates the application of Linear Regression to house price prediction using property characteristics.

The model achieved a testing R² score of 0.6529 and provided practical experience with the end-to-end workflow of a supervised Machine Learning regression task.

The results establish a baseline for further experimentation and model improvement.
