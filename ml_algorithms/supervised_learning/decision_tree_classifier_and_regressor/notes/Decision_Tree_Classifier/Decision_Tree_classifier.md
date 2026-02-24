# Decision Tree Classifier

## 1. Intuitive Explanation

A **Decision Tree** is a flowchart-like model that makes decisions by asking a sequence of questions.

It mimics human decision-making:

> “Is the email from a known sender?”  
> → Yes → “Does it contain suspicious links?”  
> → No → **Not spam**

Each question **splits the data into smaller and more homogeneous groups**.

### Goal

At every step, select the feature and threshold that **best separates the classes**.

### Tree Structure

- Starts with the full dataset at the **root**
- Splits using the **most informative feature**
- Continues splitting recursively
- Ends at **leaf nodes**, where most samples belong to a single class

It is called a *tree* because it grows downward with branches.

---

## 2. Formal Definition

A **Decision Tree Classifier** is a **non-parametric supervised learning algorithm** that:

- Recursively partitions the feature space into **disjoint regions**
- Selects feature–threshold splits that **maximize class purity**

The predicted class for a sample is the **majority class of the leaf node** in which the sample falls.

---

## 3. Mathematical Foundation

### 3.1 Core Idea: Measuring Impurity

At each node, the algorithm selects the split that produces the **purest child nodes**.

#### (a) Gini Impurity

\[
Gini = 1 - \sum_{i=1}^{C} p_i^2
\]

Where:

- \( p_i \) = proportion of class *i* in the node
- \( C \) = number of classes

**Properties:**

- Pure node → Gini = 0
- Mixed classes → Gini increases
- Represents probability of misclassification

---

#### (b) Entropy

\[
H = - \sum_{i=1}^{C} p_i \log_2(p_i)
\]

**Properties:**

- From **Information Theory**
- Measures **uncertainty**
- Minimum when node is pure

---

### 3.2 Information Gain

\[
IG = H(parent) - \sum_{k} \frac{N_k}{N} H(child_k)
\]

Where:

- \( N \) = number of samples in parent
- \( N_k \) = number of samples in child node

**Interpretation:**

- Measures how much uncertainty is reduced after a split
- The algorithm:
  - **Maximizes Information Gain**
  - or **Minimizes Gini Impurity**

---

## 4. Algorithmic Process

### Training Phase

1. Start with the full dataset at the root
2. For each feature:
   - Try all possible split points
   - Compute impurity for each split
3. Select the split with the **best impurity reduction**
4. Divide the dataset into child nodes
5. Repeat recursively for each child

### Stopping Criteria

- Node becomes pure
- Maximum depth reached
- Minimum samples per node reached

---

### Prediction Phase

For a new sample:

1. Start at the root
2. Follow the decision rules
3. Reach a leaf node
4. Output the **majority class**

---

## 5. Assumptions

Decision Trees are **non-parametric**, so they make very few assumptions:

### No Assumption About

- Linearity
- Normal distribution
- Feature scaling

### Implicit Assumptions

- Training data is representative
- Greedy splitting leads to a good structure

---

## 6. Advantages and Strengths

1. **Highly interpretable**
   - Every decision can be visualized and explained

2. **Works with**
   - Numerical data
   - Categorical data
   - Non-linear relationships

3. **No feature scaling required**

4. **Automatic feature selection**
   - Important features appear near the top

5. **Captures feature interactions**


---

## 7. Limitations and Weaknesses

1. **Overfitting (major issue)**
- Deep trees memorize training data
- Leaves become overly specific

2. **High variance**
- Small data changes → completely different tree

3. **Greedy algorithm**
- Finds locally optimal splits, not globally optimal ones

4. **Bias toward features with many unique values**
- Example: ID column

---

## 8. When NOT to Use Decision Trees

Avoid using a single Decision Tree when:

- High predictive accuracy is required  
→ Prefer **Random Forest** or **XGBoost**

- Dataset is very small  
→ High risk of overfitting

- Smooth decision boundaries are needed

- Data is very high-dimensional and sparse  
→ Example: TF-IDF text features

---

## 9. Summary (Teaching Version)

A **Decision Tree** is a supervised learning algorithm that:

- Recursively splits data based on the feature that gives the **maximum impurity reduction**  
(using **Gini** or **Entropy**)
- Produces increasingly **homogeneous nodes**
- Makes predictions using the **majority class in a leaf node**

### Key Characteristics

- Highly interpretable
- Handles non-linear relationships
- Requires minimal preprocessing

### Main Drawbacks

- Prone to overfitting
- High variance
- Greedy optimization

---
