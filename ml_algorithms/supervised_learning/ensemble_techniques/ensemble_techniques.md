# Ensemble Techniques

## What are Ensemble Techniques?

Ensemble techniques are machine learning methods where multiple models are combined to solve the same problem, 
with the goal of achieving better performance than any single model.

## Why Do Ensembles Work?

Different models make different mistakes. Combining them helps to:

- Reduce overfitting  
- Improve generalization  
- Increase stability and accuracy  

**Core idea:**  
Many weak or moderately strong models together can outperform one strong model.

---

## Types of Ensemble Techniques

There are two major categories:

1. **Bagging (Bootstrap Aggregating)**  
2. **Boosting**

---

## 1. Bagging (Bootstrap Aggregating)

### Core Idea of Bagging

Bagging focuses on reducing **variance** by training multiple models independently and in parallel on different subsets of the training data.

### How Bagging Works (Step-by-Step)

1. Start with a training dataset  
2. Create multiple random subsets of the data  
   - Sampling is done **with replacement** (bootstrap sampling)  
3. Train a base learner on each subset  

Example base learners:

- M1 = Decision Tree  
- M2 = Logistic Regression  
- M3 = Decision Tree  
- M4 = Any other ML model  

The base learners can be:
- The same algorithm (most common), or  
- Different algorithms  

Each model learns **independently**.

### Prediction Phase

- Each model gives its own prediction  
- Predictions are combined to produce the final output  

### How Predictions Are Combined

**Classification (Binary or Multiclass):**
- Majority Voting  
- The class predicted by most models is selected  

**Regression:**
- Average of predictions from all models  

### Key Characteristics of Bagging

- Models are trained in parallel  
- Each model sees a different version of the data  
- Reduces overfitting, especially for high-variance models  
- Works best with unstable models (e.g., Decision Trees)  

### Example of Bagging

**Random Forest**

- Uses multiple Decision Trees  
- Applies bootstrap sampling  
- Uses random feature selection  
- One of the most popular and powerful ensemble models  

### When to Use Bagging

- When your model is overfitting  
- When variance is high  
- When you have sufficient data  
- Especially effective with Decision Trees  

---

## 2. Boosting

### Core Idea of Boosting

Boosting focuses on reducing **bias** by training models **sequentially**, where each new model learns from the mistakes of the previous ones.

**Key intuition:**  
Later models focus more on difficult or misclassified data points.

### Weak Learners → Strong Learner

- Boosting starts with weak learners  
- Weak learners perform only slightly better than random guessing  
- These weak learners are combined to form a strong learner  

### How Boosting Works (Step-by-Step)

1. Train the first model (M1) on the dataset  
2. M1 makes predictions and some errors  
3. Increase importance (weight) of misclassified samples  
4. Train the next model (M2) focusing more on difficult samples  
5. Repeat the process: M1 - M2 - M3 - ...  Mn
6. Final prediction is made by combining all models  

### Important Characteristics of Boosting

- Models are trained sequentially  
- Each model tries to correct the mistakes of the previous ones  
- More sensitive to:
- Noise  
- Outliers  
- Generally achieves higher accuracy than bagging (if tuned well)  

---

## Types of Boosting Algorithms

### 1. AdaBoost (Adaptive Boosting)

- Adjusts weights of misclassified samples  
- Simple and effective  
- Sensitive to noisy data  

### 2. Gradient Boosting

- Uses gradient descent to minimize loss  
- Each model learns the residual errors of the previous model  
- More flexible than AdaBoost  

### 3. XGBoost (Extreme Gradient Boosting)

- Optimized and regularized version of Gradient Boosting  
- Very fast and powerful  
- Widely used in:
- Kaggle competitions  
- Industry ML systems  

---

## How Predictions Are Combined in Boosting

**Classification:**
- Weighted voting (not simple majority)  
- Stronger models have more influence  

**Regression:**
- Weighted sum or average of predictions  

---

## When to Use Boosting

- When your model is underfitting  
- When bias is high  
- When you want high accuracy  
- When data quality is reasonably good  

