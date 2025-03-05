import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv("iris.data.txt", delimiter=",", header=None)
#setting class names provided in project description
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df.columns = column_names
#dropping NA values
df.dropna(inplace=True)
scaler = StandardScaler()
#Adding standardized values to new columns
df[['sepal_length_t', 'sepal_width_t', 'petal_length_t', 'petal_width_t']] = scaler.fit_transform(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
#dropping class column since not used in k-means algorithm
X = df[['sepal_length_t', 'sepal_width_t', 'petal_length_t', 'petal_width_t']]

#FINDING OPTIMAL K
wcss = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

""" plt.figure(figsize=(8,5))
plt.plot(range(1, 10), wcss)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.title("Elbow Method to Find Optimal k")
plt.xticks(range(1, 10))
plt.grid()
plt.show() """

#APPLYING K MEANS Clustering
kmeans =  KMeans(n_clusters=3)
kmeans.fit(X)
df['kmeans_3'] = kmeans.labels_
#save as csv to check accuracy of clusters
df.to_csv("iris_result.csv", index=False)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
clusters = kmeans.fit_predict(X_pca)
plt.figure(figsize=(8,5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', edgecolors='k', alpha=0.7)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering (PCA Reduced to 2D)")
plt.show()


plt.figure(figsize=(10, 5))

# Create the dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))

plt.title("Dendrogram for Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

hc = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage="ward")
clusters = hc.fit_predict(X)