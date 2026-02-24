# Tree Pruning in Decision Trees (Pre-pruning vs Post-pruning)

## 1. Intuitive Explanation

A fully grown decision tree keeps splitting until:

- Every leaf is pure  
**or**
- Very few samples remain  

This results in:

- A very complex tree  
- Perfect training accuracy  
- Poor test performance → **Overfitting**

### What is Pruning?

**Pruning = Cutting the tree to make it simpler**

A simpler tree:

- Captures the true underlying pattern
- Ignores noise
- Generalizes better

### Two Main Strategies

| Strategy      | Idea                              |
|--------------|------------------------------------|
| Pre-pruning  | Stop the tree from growing early   |
| Post-pruning | Grow the full tree, then trim it   |

---

## 2. Formal Definition

**Tree pruning** is a regularization technique used to:

- Reduce the size of a decision tree
- Remove sections that provide little predictive power
- Improve generalization performance

---

## 3. Mathematical Foundation

### Objective

The real goal is to minimize:

> **Generalization error**

Since this is not directly accessible, we control:

> **Model complexity**

---

### 3.1 Cost Complexity Pruning (CART)

We minimize:

\[
R_\alpha(T) = R(T) + \alpha |T|
\]

Where:

- \( R(T) \) = training error (MSE, Gini, or Entropy)
- \( |T| \) = number of leaf nodes
- \( \alpha \) = complexity penalty

### Why This Works

This is analogous to **L1 / L2 regularization**:

We trade off:

| Large Tree | Small Tree |
|------------|------------|
Low training error | Higher training error |
High complexity penalty | Lower complexity penalty |

The **optimal tree** minimizes the total cost.

---

## 4. Algorithmic Process

---

### 🔹 Pre-pruning (Early Stopping)

#### Core Idea

Stop splitting when the split is **not statistically meaningful**.

#### Common Stopping Conditions

Stop if:

- `max_depth` reached
- Samples in node < `min_samples_split`
- Samples in leaf < `min_samples_leaf`
- Impurity decrease < threshold

#### Steps

1. Start growing the tree
2. Before making a split:
   - Check stopping criteria
3. If condition is met → convert node into a leaf

---

### 🔹 Post-pruning (Cost Complexity Pruning)

#### Core Idea

1. Grow the full tree
2. Remove weak branches

#### Weakest Link Pruning (CART)

For each subtree, compute:

\[
\frac{R(t) - R(T_t)}{|T_t| - 1}
\]

Where:

- \( R(t) \) = error at the node
- \( R(T_t) \) = error of the subtree
- \( |T_t| \) = number of leaves in the subtree

This measures:

> **Error increase per leaf removed**

#### Steps

1. Train a full tree
2. Compute pruning cost for all subtrees
3. Remove the branch with the **smallest increase in error**
4. Repeat → generates a sequence of smaller trees
5. Select the best tree using **cross-validation**

---

## 5. Assumptions

Pruning assumes:

- A smaller tree generalizes better
- Some splits are fitting **noise, not signal**
- Validation performance reflects true performance

---

## 6. Advantages and Strengths

### Pre-pruning

- Faster training
- Less memory usage
- Simple to implement

### Post-pruning

- Better generalization
- Finds optimal tree size
- Not greedy
- Theoretically grounded (cost-complexity objective)

---

## 7. Limitations and Weaknesses

### Pre-pruning

- Can stop too early → **Underfitting**
- Greedy local decision  
  A split that looks bad early may be useful later.

### Post-pruning

- Computationally expensive
- Requires validation / cross-validation

---

## 8. When to Use What

### Use Pre-pruning When

- Dataset is large
- Training time matters
- You need a quick baseline
- In ensemble methods with depth constraints (e.g., Random Forest)

### Use Post-pruning When

- Interpretability is important
- You want the **optimal tree size**
- You are using a **single decision tree**

---

## 9. Summary (Teaching Version)

**Pruning** is a regularization technique used to reduce overfitting in decision trees by controlling their size.

- **Pre-pruning:**  
  Stops tree growth early using constraints such as:
  - Maximum depth
  - Minimum samples per node  
  → Faster but may underfit

- **Post-pruning:**  
  Grows the full tree and then removes weak branches using a **cost-complexity objective** that balances:
  - Training error
  - Model complexity  
  → Better generalization

In practice:

> Pre-pruning is efficient,  
> Post-pruning is more optimal.