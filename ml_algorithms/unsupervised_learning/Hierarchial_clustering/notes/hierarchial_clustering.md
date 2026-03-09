# Hierarchical Clustering

## 1. Intuitive Explanation

**Hierarchical Clustering** builds a **hierarchy (tree) of clusters**.

Unlike K-Means, which directly creates **K clusters**, hierarchical clustering forms clusters **step by step**.

There are two main approaches:

### Agglomerative Clustering (Bottom-Up)

Start with:

- Every data point as its **own cluster**

Then repeatedly:

- Merge the **two most similar clusters**

Eventually:

- All points merge into **one large cluster**

This is the **most commonly used approach**.

---

### Divisive Clustering (Top-Down)

Start with:

- All points in **one cluster**

Then repeatedly:

- Split clusters into **smaller clusters**

This method is less commonly used because it is computationally more expensive.

---

### Example

Imagine clustering animals based on:

- Weight
- Height
- Habitat

Possible merging process:

- Cat and Dog merge  
- Lion joins them  
- Tiger joins  
- Fish and Shark merge separately  

This gradually forms a **hierarchical structure of clusters**.

---

## 2. Formal Definition

Hierarchical clustering is an **unsupervised learning method** that builds a hierarchy of clusters by **iteratively merging or splitting clusters** based on a distance or similarity metric.

The result is represented using a **dendrogram**, a tree-like diagram showing the relationships between clusters.

---

## 3. Mathematical Foundation

Hierarchical clustering relies on two types of distances:

### Distance Between Data Points

Common metrics include:

- **Euclidean Distance**
- **Manhattan Distance**
- **Cosine Distance**

These measure how similar or different individual data points are.

---

### Distance Between Clusters (Linkage Criteria)

To determine which clusters to merge, we define a **linkage method**.

#### 1. Single Linkage

Distance between the **closest points** of two clusters.

**Effect:**

- Can create **long chain-like clusters**

---

#### 2. Complete Linkage

Distance between the **farthest points** of two clusters.

**Effect:**

- Produces **compact clusters**

---

#### 3. Average Linkage

Average distance between **all pairs of points** in two clusters.

**Effect:**

- Produces **balanced clusters**

---

#### 4. Ward Linkage

Merges clusters that **minimize the increase in variance**.

**Effect:**

- Often produces **high-quality clusters**

---

## 4. Algorithmic Process

### Agglomerative Hierarchical Clustering

1. Start with **each data point as its own cluster**
2. Compute distances between all clusters
3. Merge the **two closest clusters**
4. Update the distance matrix
5. Repeat until **only one cluster remains**

The merging process creates a **cluster hierarchy**.

---

## 5. Assumptions

Hierarchical clustering assumes:

- Similarity between data points can be measured using **distance**
- Data contains **meaningful cluster structure**
- Relationships between clusters can form a **hierarchy**

---

## 6. Advantages and Strengths

### 1. No Need to Specify Number of Clusters Initially

You can decide the number of clusters **later** by cutting the dendrogram.

---

### 2. Produces Hierarchical Structure

Useful for understanding **relationships between clusters**.

---

### 3. Works Well for Small Datasets

Provides detailed clustering insights.

---

### 4. Flexible Distance Metrics

Supports multiple similarity measures.

---

### 5. Dendrogram Visualization

Helps interpret clusters visually.

---

## 7. Limitations and Weaknesses

### 1. Computationally Expensive

Complexity grows quickly as dataset size increases.

---

### 2. Not Scalable to Large Datasets

Typically used for **small to medium datasets**.

---

### 3. Greedy Clustering

Once clusters merge:

- They **cannot be undone**

---

### 4. Sensitive to Noise and Outliers

Outliers can distort cluster formation.

---

## 8. When to Use Hierarchical Clustering

Use hierarchical clustering when:

- Dataset is **small or medium-sized**
- You need an **interpretable cluster hierarchy**
- The **number of clusters is unknown**
- Understanding **relationships between clusters** is important

---

## 9. When NOT to Use It

Avoid hierarchical clustering when:

- Dataset is **very large**
- Fast clustering is required
- Clusters are **clearly spherical** (K-Means performs better)

---

## 10. Summary (Teaching Version)

Hierarchical clustering is an **unsupervised learning method** that builds a **tree-like hierarchy of clusters** by iteratively merging or splitting clusters based on distance measures.

The final structure is represented by a **dendrogram**, which allows the number of clusters to be selected **after the clustering process**.

It provides **high interpretability and cluster relationships**, but is **computationally expensive for large datasets**.