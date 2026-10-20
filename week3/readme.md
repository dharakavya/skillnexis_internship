Project Overview
This project implements an unsupervised machine learning approach to group Iris flowers based on their physical measurements using the K-Means clustering algorithm. Principal Component Analysis (PCA) is applied to reduce the dimensionality of the dataset and visualize the resulting clusters in two dimensions.

The project also compares the predicted clusters with the actual Iris species to understand how effectively the algorithm groups similar flower.

Objectives
- Understand and implement unsupervised machine learning.
- Apply K-Means clustering with three clusters.
- Perform feature standardization before clustering.
- Apply PCA to reduce the number of dimensions from four to two.
- Visualize the clustering results using scatter plots.
- Compare predicted clusters with actual flower species.
- Evaluate clustering performance using the Silhouette Score and Inertia.
Dataset
Dataset Name: Iris Species Dataset

Source: Kaggle – Iris Species Dataset

The dataset contains 150 flower samples belonging to three Iris species.
Features Used
Feature	Description
SepalLengthCm	Length of the sepal in centimetres
SepalWidthCm	Width of the sepal in centimetres
PetalLengthCm	Length of the petal in centimetres
PetalWidthCm	Width of the petal in centimetres


Target Labels for Evaluation
The dataset contains three species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica
The Species column is not used to train the K-Means model. It is used only to compare the predicted clusters with the actual species.
Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
Machine Learning Workflow
1. Data Loading and Exploration
The Iris dataset is loaded using Pandas. The dataset structure, column names, missing values, and species distribution are examined before applying machine learning.
2. Feature Selection
Four numerical features are selected for clustering:
- Sepal length
- Sepal width
- Petal length
- Petal width
The Id column is excluded because it is an identifier rather than a meaningful flower measurement.

The Species column is excluded from model training to maintain the unsupervised learning approach.
3. Feature Standardization
StandardScaler is used to standardize the numerical features before applying K-Means.

Standardization helps prevent features with larger numerical scales from dominating the distance calculations.
4. K-Means Clustering
The K-Means algorithm is applied with the following configuration:
- Number of clusters: 3
- Random state: 42
- Number of initializations: 10
The algorithm groups flowers based on similarities in their standardized measurements and assigns each flower a predicted cluster ID.
5. PCA Dimensionality Reduction
Principal Component Analysis (PCA) is used to transform the four standardized features into two principal components.

This reduces the dataset from four dimensions to two dimensions while retaining as much variance as possible.

The reduced dataset is used to visualize the clusters in a two-dimensional scatter plot.
6. Cluster Visualization
Scatter plots are created to visualize the predicted clusters and compare them with the actual Iris species.

These visualizations help illustrate the separation between the groups and identify areas where the species overlap.
7. Model Evaluation
The clustering results are evaluated using the following metrics:

Silhouette Score

Measures how well samples fit within their assigned clusters compared with other clusters. Its values range from -1 to +1, with higher values generally indicating better-separated clusters.

Inertia

Measures the sum of squared distances between samples and their assigned cluster centres. Lower values indicate tighter clusters for the same dataset and number of clusters, although inertia generally decreases as the number of clusters increases.
Results
The K-Means model was trained using all 150 samples and generated three clusters.
Evaluation Metrics
Metric	Result
Total samples	150
Number of features used	4
Number of clusters	3
Silhouette Score	0.459
Inertia	140.9658


Actual Species vs Predicted Clusters
The following table shows the clustering results obtained during the experiment.
Actual Species	Cluster 0	Cluster 1	Cluster 2
Iris-setosa	0	50	0
Iris-versicolor	39	0	11
Iris-virginica	14	0	36


Interpretation
- All 50 Iris-setosa samples were assigned to Cluster 1.
- Of the Iris-versicolor samples, 39 were assigned to Cluster 0 and 11 to Cluster 2.
- Of the Iris-virginica samples, 14 were assigned to Cluster 0 and 36 to Cluster 2.
The results show that Iris-setosa was clearly separated from the other species. Some Iris-versicolor and Iris-virginica samples were grouped together because their measurements have overlapping characteristics.

The Silhouette Score of 0.459 indicates moderate cluster separation, suggesting that the model identified meaningful groupings while some overlap remained.


The following Python libraries are required:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
These dependencies can be installed using the requirements.txt file.
Key Learnings
Through this project, I gained practical experience in:
- Understanding unsupervised machine learning.
- Implementing K-Means clustering using Scikit-learn.
- Preparing numerical data for distance-based algorithms.
- Applying feature standardization.
- Understanding PCA and dimensionality reduction.
- Visualizing multidimensional data in two dimensions.
- Comparing predicted clusters with known labels.
- Evaluating clustering quality using the Silhouette Score and Inertia.
Conclusion
This project demonstrates the application of K-Means clustering and PCA to the Iris dataset.

K-Means successfully grouped the 150 flower samples into three clusters based on their physical measurements. PCA reduced the four original features to two principal components, enabling two-dimensional visualization of the clustering results.

The comparison between predicted clusters and actual species showed clear separation of Iris-setosa, while some overlap remained between Iris-versicolor and Iris-virginica.

Overall, this project provided practical experience with unsupervised machine learning, dimensionality reduction, data visualization, and clustering evaluation.