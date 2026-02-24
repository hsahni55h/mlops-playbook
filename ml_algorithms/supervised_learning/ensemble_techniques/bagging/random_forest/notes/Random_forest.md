# Random Forest Algorithm

## 1. Intuitive Explanation

A single decision tree:

- Learns very detailed rules
- Overfits easily
- Is highly sensitive to small changes in data

### How Random Forest Solves This

Random Forest:

- Builds **many decision trees**
- Trains each on **slightly different data**
- Combines their predictions

### Analogy

If you ask:

- One expert → they may be wrong  
- 100 independent experts → the majority decision is usually reliable  

### Key Idea

Each tree:

- Is trained on a **different dataset**
- Sees a **different subset of features**

This makes the trees **decorrelated**.

### Final Prediction

| Task           | Aggregation Method |
|---------------|--------------------|
Classification  | Majority vote      |
Regression      | Average            |

➡ This dramatically **reduces variance**.

---

## 2. Formal Definition

**Random Forest** is an ensemble learning method that:

- Constructs multiple decision trees using:
  - Bootstrap sampling
  - Random feature selection
- Outputs the **aggregated prediction** of the individual trees.

---

## 3. Mathematical Foundation

Random Forest is based on:

### 3.1 Bagging (Bootstrap Aggregating)

Given a dataset \( D \), we create \( B \) new datasets:

\[
D_1, D_2, D_3, \dots, D_B
\]

by **sampling with replacement**.

Each tree is trained on one bootstrap dataset.

#### Why Bagging Works

If models are independent:

\[
Var(\text{average}) = \frac{1}{B} Var(\text{tree})
\]

So:

> Increasing the number of trees → decreases variance

---

### 3.2 Random Feature Selection

At each split:

Instead of using all features, we use:

\[
m \ll p
\]

Where:

- \( p \) = total number of features
- \( m \) = randomly selected subset of features

#### Why?

To:

- Reduce correlation between trees
- Improve variance reduction when averaging

Highly correlated trees → averaging gives little benefit.

---

### 3.3 Final Prediction

#### Regression

\[
\hat{y} = \frac{1}{B} \sum_{b=1}^{B} T_b(x)
\]

#### Classification

\[
\hat{y} = \text{majority vote}
\]

---

## 4. Algorithmic Process

### Training Phase

For \( b = 1 \) to \( B \):

1. Draw a **bootstrap sample** from the training data
2. Train a decision tree:
   - At each split:
     - Randomly select \( m \) features
     - Choose the best split among them
3. Grow the tree (usually **deep and unpruned**)

---

### Prediction Phase

For a new sample:

1. Pass the sample through all trees
2. Collect predictions
3. Aggregate:

   - Mean → regression  
   - Majority vote → classification  

---

## 5. Assumptions

Random Forest assumes:

- Individual trees have **low bias**
- Variance can be reduced by averaging
- Errors between trees are **not perfectly correlated**

### It Does NOT Assume

- Linearity
- Normal distribution
- Feature scaling

---

## 6. Advantages and Strengths

### 1. Massive Reduction in Overfitting

Compared to a single decision tree.

### 2. High Accuracy Out-of-the-Box

Works well with minimal tuning.

### 3. Handles

- Non-linear relationships
- Feature interactions
- Mixed data types

### 4. Built-in Feature Importance

Very useful for real-world applications.

### 5. Robust To

- Noise
- Outliers

### 6. Works Well for High-Dimensional Data

---

## 7. Limitations and Weaknesses

### 1. Less Interpretable

You cannot visualize hundreds of trees.

### 2. Computationally Expensive

- Slower training
- Slower inference compared to a single tree

### 3. Large Memory Usage

Stores many trees.

### 4. Cannot Extrapolate (Regression)

Same limitation as decision trees.

### 5. Bias Toward Features with Many Categories

Inherits this from decision trees.

---

## 8. When NOT to Use Random Forest

Avoid when:

- Interpretability is critical
- Real-time, low-latency prediction is required
- Dataset is very small
- Extrapolation is required in regression

### Better Alternatives

| Requirement              | Better Choice          |
|--------------------------|------------------------|
High interpretability      | Linear models          |
Maximum predictive accuracy| Gradient Boosting      |
Unstructured data          | Neural networks        |

---

## 9. Summary (Teaching Version)

**Random Forest** is an ensemble learning algorithm that:

- Builds multiple decision trees using:
  - Bootstrap samples
  - Random subsets of features
- Produces predictions by:
  - Averaging (regression)
  - Majority voting (classification)

### Key Benefits

- Strong variance reduction
- Excellent generalization
- High accuracy on tabular data
- Minimal preprocessing required

### Trade-offs

- Reduced interpretability
- Higher computational and memory cost

---