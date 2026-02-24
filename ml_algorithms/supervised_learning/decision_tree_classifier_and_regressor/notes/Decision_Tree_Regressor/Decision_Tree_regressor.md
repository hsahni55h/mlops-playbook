# Decision Tree Regressor

## 1. Intuitive Explanation

A **Decision Tree Regressor** predicts **continuous values** by:

- Repeatedly splitting the dataset into smaller regions
- Assigning a **constant prediction** to each region


Instead of predicting a class label, the model predicts the **average target value** within a region.

### Key Intuition

- The feature space is divided into **rectangular regions (boxes)**
- Each region outputs a **constant value**
- The final model represents a **piecewise constant function**

---

## 2. Formal Definition

A **Decision Tree Regressor** is a **non-parametric supervised learning algorithm** that:

- Recursively partitions the feature space into **disjoint regions**
- Minimizes the **variance (or squared error)** of the target variable within each region

The prediction for a sample is the **mean target value of the training samples in the corresponding leaf node**.

---

## 3. Mathematical Foundation

### 3.1 Objective

At each split, the goal is to **reduce prediction error**.

For regression:

> Impurity = **Variance**

---

### 3.2 Mean Squared Error (MSE)

For a node with **N samples**:

\[
MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \bar{y})^2
\]

Where:

- \( y_i \) = actual target value
- \( \bar{y} \) = mean target value in that node

---

### 3.3 Why the Mean is Used as Prediction

The mean minimizes the squared error:

\[
\arg\min_c \sum (y_i - c)^2 = \bar{y}
\]

This is why **each leaf outputs the average value**.

---

### 3.4 Split Criterion

We select the split that minimizes the **weighted MSE after splitting**:

\[
\text{Weighted MSE} =
\frac{N_L}{N} MSE_L +
\frac{N_R}{N} MSE_R
\]

Where:

- \( N_L, N_R \) = samples in left and right nodes
- \( MSE_L, MSE_R \) = errors of child nodes

### Optimization Goal

Maximize:

> **Reduction in variance**

---

## 4. Algorithmic Process

### Training Phase

1. Start with all data at the root
2. For each feature:
   - Try all possible split points
3. For each split:
   - Divide data into left and right
   - Compute **weighted MSE**
4. Select the split with the **lowest error**
5. Repeat recursively

### Stopping Criteria

- Maximum depth reached
- Minimum samples per leaf reached
- No further error reduction

---

### Prediction Phase

For a new input:

1. Follow the decision rules from the root
2. Reach a leaf node
3. Output the **mean target value of that leaf**

---

## 5. Assumptions

### No Assumptions About

- Linearity
- Normal distribution
- Feature scaling

### Implicit Assumptions

- Greedy local optimization leads to a good structure
- The function can be approximated using **piecewise constant regions**

---

## 6. Advantages and Strengths

### 1. Captures Non-Linear Relationships

No need for polynomial feature engineering.

### 2. No Feature Scaling Required

Works directly with raw feature values.

### 3. Handles Feature Interactions Automatically


### 4. More Robust to Outliers (vs Linear Regression)

Because:

- Splits are based on **variance reduction**
- Not a global fit

### 5. Interpretable

Decision rules can be visualized and explained.

---

## 7. Limitations and Weaknesses

### 1. Piecewise Constant Predictions

The output is a:

> Step function, not a smooth curve

#### Implications

- Cannot model smooth transitions
- Cannot extrapolate

Example:

If max training target = 500  
→ The model will **never predict 600**

---

### 2. Overfitting

Deep trees memorize noise in the training data.

---

### 3. High Variance

Small data changes → completely different tree.

---

### 4. Poor for Linear Relationships

A tree approximates a straight line using many steps, while:

> Linear Regression fits it directly.

---

## 8. When NOT to Use Decision Tree Regressor

Avoid when:

- Smooth predictions are required
- Extrapolation beyond training range is needed
- The relationship is truly linear
- Dataset is very small

### Better Alternatives

- **Linear Regression** → for linear relationships
- **Random Forest / Gradient Boosting** → for higher accuracy

---

## 9. Summary (Teaching Version)

A **Decision Tree Regressor**:

- Recursively splits the dataset into regions that **minimize target variance**
- Predicts the **mean value** of the samples in each leaf

### Key Characteristics

- Models non-linear relationships
- Captures feature interactions
- Requires minimal preprocessing
- Highly interpretable

### Main Drawbacks

- Produces **piecewise constant predictions**
- Cannot extrapolate beyond training data
- Prone to overfitting
- High variance

---

