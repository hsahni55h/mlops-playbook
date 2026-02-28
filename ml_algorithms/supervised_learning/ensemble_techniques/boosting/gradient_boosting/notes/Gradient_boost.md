# Gradient Boosting

## 1. Intuitive Explanation

Gradient Boosting builds models **sequentially**, similar to AdaBoost.

However, instead of changing the **weights of data points**, it:

> Trains each new model to predict the **errors (residuals)** made by the previous model.

### Learning Process

1. Make an initial prediction  
2. Measure how wrong it is  
3. Train a new model to correct that mistake  
4. Repeat  

So the model improves **stage by stage**, always moving toward the correct solution.

### Analogy

Reaching a destination in dense fog:

- First step → rough direction  
- Check the error  
- Adjust direction  
- Repeat  

This is equivalent to:

> **Gradient descent in function space**

---

## 2. Formal Definition

**Gradient Boosting** is an additive ensemble method that:

- Builds the model in a **stage-wise manner**
- Sequentially fits new learners to the **negative gradient of a loss function**
- Minimizes the overall prediction error

---

## 3. Mathematical Foundation

We want to learn a function:

\[
F(x)
\]

that minimizes a loss:

\[
L(y, F(x))
\]

---

### 3.1 Additive Model

\[
F_M(x) = \sum_{m=1}^{M} \gamma_m h_m(x)
\]

Where:

- \( h_m(x) \) = weak learner (typically a shallow decision tree)
- \( \gamma_m \) = step size (model weight)

---

### 3.2 Key Idea: Fit Residuals Using Gradients

At iteration \( m \), compute:

\[
r_i = - \left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]
\]

These are called:

> **Pseudo-residuals**

Then:

- Train a weak learner to predict \( r_i \)

---

### Why This Works

Model update:

\[
F_m(x) = F_{m-1}(x) + \eta h_m(x)
\]

This is:

> Gradient descent in function space

Instead of updating parameters → we **add a new function**.

---

## 4. Algorithmic Process

### Step 1 — Initialize Model

\[
F_0(x) = \arg\min_c \sum L(y_i, c)
\]

For:

- **MSE** → mean of the target

---

### Step 2 — For m = 1 to M

1. Compute residuals:

\[
r_i = - \frac{\partial L}{\partial F(x_i)}
\]

2. Train weak learner to predict \( r_i \)

3. Compute optimal step size:

\[
\gamma_m =
\arg\min_\gamma
\sum L\left(y_i, F_{m-1}(x_i) + \gamma h_m(x_i)\right)
\]

4. Update model:

\[
F_m(x) =
F_{m-1}(x)
+
\eta \gamma_m h_m(x)
\]

Where:

- \( \eta \) = learning rate

---

## 5. Assumptions

Gradient Boosting assumes:

- Weak learners can approximate residuals
- Loss function is differentiable
- Data is not extremely noisy

---

## 6. Advantages and Strengths

### 1. Extremely High Predictive Accuracy

Often the **best-performing algorithm for tabular data**.

### 2. Works with Any Differentiable Loss Function

Examples:

- MSE
- MAE
- Log loss
- Huber loss
- Quantile loss

### 3. Captures

- Non-linear relationships
- Feature interactions

### 4. Built-in Regularization

Through:

- Learning rate
- Tree depth
- Subsampling

### 5. Robust to Overfitting (With Proper Tuning)

---

## 7. Limitations and Weaknesses

### 1. Sequential Training → Slow

Cannot be parallelized like Random Forest.

### 2. Hyperparameter Sensitive

Requires careful tuning.

### 3. Can Overfit If

- Too many trees
- Trees too deep
- Learning rate too high

### 4. Sensitive to Noisy Data

Less than AdaBoost, but still affected.

---

## 8. When NOT to Use Gradient Boosting

Avoid when:

- Very fast training is required
- Dataset is very small
- Real-time training is needed

### Better Alternatives

| Scenario | Preferred Model |
|----------|-----------------|
Fast and robust | Random Forest |
Small dataset | Linear models |

---

## 9. Summary (Teaching Version)

**Gradient Boosting** is an additive ensemble method that:

- Builds a strong model by sequentially training weak learners
- Each learner predicts the **negative gradient (residual errors)** of the loss function
- Updates the model in the direction that **minimizes the loss**

### Key Insight

> It is equivalent to **gradient descent in function space**.

### Key Strengths

- Very high predictive accuracy
- Supports multiple loss functions
- Handles complex non-linear relationships

### Key Trade-offs

- Computationally slower due to sequential training
- Requires careful hyperparameter tuning

---