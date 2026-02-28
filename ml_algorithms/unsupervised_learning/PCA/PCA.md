# Core Terms for PCA (Principal Component Analysis)

## 1. Variance

### Intuitive
Variance tells us **how spread out a feature is**.

- Values very similar → **Low variance**
- Values very different → **High variance**

In PCA:

> **High variance = more information**

### Formal
Variance is a measure of how much the values of a variable deviate from their mean.  
It quantifies the **dispersion of data**.

---

## 2. Covariance

### Intuitive

Covariance tells us **whether two features change together**.

- Both increase together → **Positive covariance**
- One increases while the other decreases → **Negative covariance**
- No consistent relationship → **Near zero covariance**

---

### Real-World Examples

**Positive Covariance**

- Temperature ↑ → Ice cream sales ↑  
  → They move together

**Negative Covariance**

- Speed of car ↑ → Time to reach destination ↓  
  → Opposite movement

**Near-Zero Covariance**

- Shoe size and exam score  
  → No meaningful relationship

---

### ML Example

In a housing dataset:

- House size
- Number of rooms

These usually increase together → **positive covariance**

This indicates:

> They contain **overlapping information**

---

### What to Remember

- Covariance gives **direction**, not strength
- Value depends on **scale** → hard to compare across feature pairs
- Used to build the **covariance matrix in PCA**

---

### Pitfall

A large covariance **does not always mean a strong relationship**  
→ It may simply be due to large feature values.

This is why we use **correlation**.

---

## 3. Correlation

### Intuitive

Correlation tells us:

> **Direction + strength of a relationship**

It is **scale-free**, so it is easy to interpret.

---

### Real-World Examples

**Strong Positive Correlation**

- Height and weight (adults)

**Strong Negative Correlation**

- Price of a product and its demand (in many cases)

**Near-Zero Correlation**

- Roll number and intelligence

---

### ML Example

In a salary prediction dataset:

Features:

- Years of experience
- Salary

These typically show **high positive correlation**.

So:

> One can help predict the other.

---

### Why It Matters in ML

High correlation between features leads to:

- Redundant information
- Unstable linear model coefficients
- Slower training

**PCA solves this by creating:**

> Uncorrelated components

---

### What to Remember

- Correlation ∈ **[-1, 1]**
- Unit-free (scale independent)
- Measures **linear relationship only**

---

### Pitfall

**Zero correlation ≠ independence**

Example:

A perfect **U-shaped relationship**  
→ Correlation ≈ 0  
→ But variables are clearly dependent.

---

## 4. Multicollinearity

### Intuitive

Multicollinearity occurs when:

> One feature contains the same information as another.

The model becomes **confused about which feature to trust**.

---

### Real-World Examples

**Salary Dataset**

- Monthly salary
- Annual salary  
→ Identical information

**Health Dataset**

- Weight
- BMI
- Obesity index  
→ Strongly dependent

**Education Dataset**

- Total study time per week
- Study time per day  
→ Linearly related

---

### ML Example — House Price Prediction

Features:

- House size (sq ft)
- Number of rooms
- Number of bedrooms

These are **highly correlated**.

#### Effect in Linear Regression

- Coefficients become unstable
- Signs may flip
- Model becomes hard to interpret

---

## 4. Why Multicollinearity is a Problem

### 1. Unstable Coefficients

Small change in data → huge change in coefficients.

### 2. Misleading Feature Importance

Important features may appear:

- Statistically insignificant

### 3. High Model Variance

---

## 5. How to Detect Multicollinearity

Key methods to remember:

- **Correlation matrix**
- **Variance Inflation Factor (VIF)** 

---

## 6. How to Fix Multicollinearity

Common solutions:

- Remove one of the correlated features
- Apply **PCA**
- Use **regularization**:
  - Ridge
  - Lasso

---

## 7. Model Sensitivity

### Major Issue For

- Linear regression
- Logistic regression
- Other linear models

### Not a Serious Issue For

Tree-based models:

- Random Forest
- XGBoost

These models are **largely unaffected**.

---

## 8. Quick Summary

| Concept | Key Role | Important Note |
|--------|----------|----------------|
Covariance | Direction of joint movement | Scale-dependent |
Correlation | Direction + strength | Scale-free, bounded [-1, 1] |
Multicollinearity | Redundant features | Harms linear models |

---

## 5. Dimensionality

### Intuitive
Dimensionality = **number of features**.

High dimensional data:

- Hard to visualize
- Slower to train
- Often contains redundancy

### Formal
Dimensionality refers to the **number of variables used to represent each data point** in a dataset.

---

## 6. Projection

### Intuitive
Projection means:

> Expressing high-dimensional data using fewer dimensions.

Example:

The **shadow of a 3D object on a 2D wall**.

### Formal
Projection is the transformation of data from a **higher-dimensional space onto a lower-dimensional subspace**.

---

## 7. Orthogonal Directions

### Intuitive
Orthogonal directions are:

> Completely independent directions.

In PCA:

- New features **do not overlap in information**
- They are **uncorrelated**

### Formal
Orthogonal directions are **mutually perpendicular axes** that are:

- Linearly independent
- Uncorrelated

---

## 8. Eigenvectors

### Intuitive
Eigenvectors represent:

> The most important directions in the data

They show where the data:

> **spreads the most**

### Formal
Eigenvectors are special directions associated with a transformation where the vector:

- Changes only in scale
- Does **not change direction**

In PCA, they define the **principal components**.

---

## 9. Eigenvalues

### Intuitive
Eigenvalues tell us:

> How important each eigenvector is.

- Large eigenvalue → more information
- Small eigenvalue → less information

### Formal
Eigenvalues represent the **amount of variance captured** along their corresponding eigenvectors.

---

## 10. SVD (Singular Value Decomposition)

### Intuitive
SVD breaks a dataset into:

- Important directions
- Importance of each direction

It is:

> How PCA is actually computed in practice.

### Formal
SVD is a **matrix factorization technique** that decomposes a data matrix into:

- Orthogonal components (directions of maximum variance)
- Their corresponding strengths

---

## 11. Explained Variance

### Intuitive
Explained variance tells us:

> How much information we retain after dimensionality reduction.

Example:

- **95% explained variance → most of the structure is preserved**

### Formal
Explained variance is the **proportion of the total variance in the dataset** captured by a principal component.

---

## Summary Table

| Term | Key Meaning | Role in PCA |
|------|-------------|-------------|
Variance | Spread of a feature | Defines information content |
Covariance | Joint variation | Captures relationships |
Correlation | Standardized covariance | Scale-independent relationship |
Multicollinearity | Redundant features | PCA removes it |
Dimensionality | Number of features | PCA reduces it |
Projection | Mapping to lower dimension | Core PCA operation |
Orthogonal directions | Independent axes | Ensures uncorrelated components |
Eigenvectors | Principal directions | Define new feature space |
Eigenvalues | Importance of each direction | Rank components |
SVD | Matrix decomposition method | Efficient PCA computation |
Explained variance | Information retained | Component selection metric |

---

# Principal Component Analysis (PCA)

## 1. Intuitive Explanation

**Principal Component Analysis (PCA)** creates a new set of features that:

- Retain **maximum information**
- Remove **redundancy**
- Reduce **dimensionality**

It works by **rotating the coordinate system** of the data:

- First axis → direction of **maximum spread (variance)**
- Second axis → next highest spread (perpendicular to the first)
- And so on...

Then we **keep only the most important axes**.

> PCA = **Smart compression of data**

---

## 2. Formal Definition

PCA is a **linear transformation technique** that:

- Converts a dataset into a new coordinate system
- The new axes correspond to **directions of maximum variance**
- Components are **ordered by importance**
- Dimensionality is reduced by selecting the **top principal components**

---

## 3. Mathematical Foundation (Conceptual)

### Core Objective

Find:

> The direction where the data varies the most.

Why?

> **Maximum variance = Maximum information**

### Process

1. Find the first direction of maximum variance
2. Find the next direction:
   - Perpendicular to the first
   - With the highest remaining variance

This creates:

> A new coordinate system with **uncorrelated axes**

---

## 4. Algorithmic Process

1. **Standardize the data**
2. **Center the data around the mean**
3. **Find directions of maximum variance**
4. **Rank them by importance**
5. **Select the top components**
6. **Project the data onto them**

---

## 5. Assumptions

PCA assumes:

- High variance directions contain important structure
- Relationships between features are **linear**
- Mean and variance capture the essential data structure

---

## 6. Advantages and Strengths

- Reduces dimensionality
- Removes multicollinearity
- Speeds up machine learning training
- Reduces noise
- Enables visualization (2D / 3D)
- Performs feature extraction

---

## 7. Limitations and Weaknesses

- Linear method (cannot capture complex non-linear structure)
- Components are hard to interpret
- Sensitive to feature scaling
- Maximum variance ≠ maximum predictive power

---

## 8. When to Use PCA

Use PCA when:

- You have **many correlated features**
- As a **preprocessing step for ML**
- For **data visualization**
- For **data compression**
- For **noise reduction**

---

## 9. When NOT to Use PCA

Avoid PCA when:

- Interpretability is critical
- Number of features is already small
- Relationships are strongly **non-linear**

---

## 10. Summary (Teaching Version)

**PCA** is a dimensionality reduction technique that:

- Transforms correlated features into a new set of **uncorrelated components**
- Orders them by the **amount of variance they capture**
- Keeps only the most important components

This allows:

> Efficient data compression while preserving the maximum possible information.

---