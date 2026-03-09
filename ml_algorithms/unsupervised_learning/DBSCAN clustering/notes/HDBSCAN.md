# HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)

## 1. Intuitive Explanation

**DBSCAN** groups points by checking if there are enough neighbors within a fixed distance **(ε)**.

The main limitation:

> A single global **ε** cannot work well if clusters have **different densities**.

### Example

Imagine two clusters:

- **Cluster A** → very dense  
- **Cluster B** → more spread out  

Problems with DBSCAN:

- If **ε is small** → Cluster B breaks apart  
- If **ε is large** → Cluster A merges with nearby clusters  

So DBSCAN struggles when clusters have **varying densities**.

---

### HDBSCAN Solution

Instead of choosing **one ε value**, HDBSCAN:

- Examines clustering across **many density levels**
- Builds a **hierarchical tree of clusters**
- Selects the **most stable clusters**

So HDBSCAN combines ideas from:

- **DBSCAN** → density-based clustering  
- **Hierarchical clustering** → tree structure of clusters  

---

## 2. Formal Definition

**HDBSCAN** is a density-based clustering algorithm that:

- Extends DBSCAN
- Builds a **hierarchy of clusters across varying density thresholds**
- Extracts the **most stable clusters** from this hierarchy

---

## 3. Mathematical Foundation

HDBSCAN modifies DBSCAN using several key concepts.

---

### 1. Core Distance

Instead of using only ε, HDBSCAN computes a **core distance** for each point.

Core distance represents:

> The distance required to reach the **minimum number of neighbors**.

This measures **local density around a point**.

---

### 2. Mutual Reachability Distance

HDBSCAN introduces a modified distance metric called:

> **Mutual Reachability Distance**

This helps stabilize clustering by preventing **very dense points from dominating cluster formation**.

---

### 3. Minimum Spanning Tree (MST)

Using the mutual reachability distances, HDBSCAN constructs a:

> **Minimum Spanning Tree (MST)**

This connects all points while minimizing total distance.

Clusters are then formed by **removing edges from the tree**.

---

### 4. Cluster Stability

HDBSCAN evaluates clusters based on **stability across density levels**.

- Clusters that persist across many density thresholds → **stable clusters**
- Unstable clusters disappear

Stable clusters are selected as **final clusters**.

---

## 4. Algorithmic Process

1. Compute **core distance** for each point
2. Compute **mutual reachability distances**
3. Construct a **minimum spanning tree**
4. Build a **hierarchical clustering tree**
5. Condense the cluster hierarchy
6. Select clusters based on **cluster stability**

Points that never belong to stable clusters are labeled **noise**.

---

## 5. Assumptions

HDBSCAN assumes:

- Clusters correspond to **dense regions**
- Clusters may have **different densities**
- A **density hierarchy** exists in the data

---

## 6. Advantages and Strengths

### 1. Handles Clusters with Different Densities

This is the **biggest improvement over DBSCAN**.

---

### 2. No Need to Choose ε

Only requires specifying:

- **Minimum cluster size**

---

### 3. Automatically Detects Noise

Like DBSCAN, outliers are naturally identified.

---

### 4. Detects Complex Cluster Shapes

Works well for:

- Spirals
- Curved clusters
- Irregular cluster shapes

---

### 5. Produces Cluster Membership Probabilities

HDBSCAN can estimate:

> How strongly a point belongs to a cluster.

---

## 7. Limitations and Weaknesses

### 1. More Computationally Expensive

More complex than DBSCAN.

---

### 2. Harder to Interpret Parameters

Understanding parameter effects can be challenging.

---

### 3. Not Ideal for High-Dimensional Data

Distance metrics become less meaningful in high dimensions.

---

## 8. When to Use HDBSCAN

Use HDBSCAN when:

- Clusters have **different densities**
- Dataset contains **noise**
- Cluster shapes are **irregular**
- Number of clusters is **unknown**


---

## 9. When NOT to Use HDBSCAN

Avoid HDBSCAN when:

- Clusters are **simple spherical shapes** → K-Means is faster
- Dataset is **extremely large**
- Data has **very high dimensionality**

---

## 10. Summary (Teaching Version)

**HDBSCAN** is an extension of DBSCAN that performs **density-based clustering across multiple density levels**.

It:

- Builds a **hierarchy of clusters**
- Uses **mutual reachability distances**
- Extracts the **most stable clusters**

### Key Advantages

- Handles **varying cluster densities**
- Detects **complex cluster shapes**
- Automatically identifies **noise**

Unlike DBSCAN, HDBSCAN does **not require specifying the neighborhood radius (ε)**.

---