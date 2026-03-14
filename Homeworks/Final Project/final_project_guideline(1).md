# Final Project (Machine Learning)

## Choose ONE Track Only

You must choose **ONE** of the following project tracks:

1. Track A: Regression Project (Linear Regression)
2. Track B: Classification Project (Logistic Regression)
3. Track C: Tree-Based Project (Decision Tree / Random Forest)

Each track includes full ML pipeline + deployment.

---

# TRACK A — Regression Project

## Topic: Salary Prediction System

### Objective

Build a machine learning system that predicts a **continuous value** (e.g., monthly income or house price).

---

## 1) Intro ML – Problem Definition

- Define regression problem clearly.
- Target variable must be numeric.
- Choose evaluation metrics:
  - MAE (optional)
  - RMSE (required)
- Split data into train/test (e.g., 80/20).
- Create baseline model (predict mean value).

---

## 2) Data & EDA

- Explore dataset
- Handle missing values
- Visualize distributions
- Check correlations
- Avoid data leakage

Deliverable: `01_eda.ipynb`

---

## 3) Preprocessing

- Handle missing values
- Encode categorical variables (OneHotEncoding)
- Scale numeric features (StandardScaler), (optional)
- Build pipeline using ColumnTransformer, (optional)

Save preprocessor as:
`models/preprocessor.pkl`

---

## 4) Model Implementation (Regression Only)

You must implement:

1. Linear Regression (Required)
2. Compare with ONE of:
   - Decision Tree Regressor
   - Random Forest Regressor

Evaluate using:

- MAE
- RMSE

Select best model.

Save:
`models/reg_model.pkl`

---

## 5) Deployment (Flask/FastApi/Streamlit)

Create web app:

- Input form (features)
- Predict numeric output
- Show predicted value clearly

OR

Create Api request:

- GET / → show form
- POST /predict → show prediction

---

## 6) Report Requirements

Include:

- Problem statement
- Dataset description
- Model comparison table
- Interpretation (coefficients or feature importance)
- Screenshot of working app

---

# TRACK B — Classification Project

## Topic: Employee Attrition Prediction

### Objective

Predict a **binary outcome** (Yes/No, 0/1).

---

## 1) Intro ML – Problem Definition

- Define classification problem.
- Target must be binary.
- Metrics required:
  - Accuracy
  - F1-score
  - Confusion Matrix
- Use stratified train/test split.

---

## 2) Data & EDA

- Analyze class distribution
- Check imbalance
- Visualize features vs target
- Handle missing values

Deliverable: `01_eda.ipynb`

---

## 3) Preprocessing

- Encode categorical variables
- Scale numeric features
- Handle imbalance (optional):
  - class_weight="balanced"

Save:
`models/preprocessor.pkl`

---

## 4) Model Implementation (Classification Only)

You must implement:

1. Logistic Regression (Required)
2. Compare with ONE of:
   - Decision Tree Classifier
   - Random Forest Classifier

Evaluate using:

- Accuracy
- F1-score
- Confusion matrix

Select best model.

Save:
`models/clf_model.pkl`

---

## 5) Deployment (Flask)

Create web app:

- Survey-style input form
- Output:
  - Predicted label (Yes/No)
  - Probability score

Example output:
"Attrition Risk: 0.73 (High)"

---

## 6) Report Requirements

Include:

- Dataset description
- Class distribution
- Model comparison table
- Confusion matrix
- Feature importance or coefficients
- App screenshots

---

# TRACK C — Tree-Based Project

## Topic: Decision Tree / Random Forest System

### Objective

Build a project using **Decision Tree and Random Forest as primary models**.

You may choose:

- Regression problem
  OR
- Classification problem

But ONLY use tree-based models.

---

## 1) Intro ML – Problem Definition

- Clearly define regression OR classification.
- Choose proper evaluation metrics:
  - Regression → MAE
  - Classification → Accuracy + F1

---

## 2) Data & EDA

- Explore dataset
- Analyze feature importance potential
- Clean missing data

Deliverable: `01_eda.ipynb`

---

## 3) Model Implementation

You must implement:

1. Decision Tree
2. Random Forest

Tune at least:

- max_depth
- n_estimators (for RF)

Compare performance.

---

## 4) Interpretation (Important)

- Show feature importance chart
- Explain top 3 important features
- **Discuss overfitting (compare train vs test score)**

---

## 5) Deployment (Python Flask/FastApi)

- Input form / Input Json Data
- Prediction result
- Clean UI/API HTTP request
- Proper error handling

---

# Common Requirements (All Tracks)

## Folder Structure

```
final_project/
  data/
  notebooks/
  src/
  app/
  models/
  REPORT.pdf
  requirements.txt
```

## REPORT(PDF) Must Include

- Problem statement
- Data description
- Preprocessing explanation
- Model comparison
- Final model choice
- Deployment explanation
- How to run/setup project

## Engineering Quality (Required)

Add at least 2:

- Input validation
- Logging predictions
- API endpoint returning JSON
- Basic unit tests
- Clean code structure

---

# Grading Rubric

- Problem definition (10%)
- Data understanding & EDA (20%)
- Model implementation (25%)
- Evaluation & interpretation (20%)
- Deployment (20%)
- Code quality & structure (5%)

---

# Important Rules

1. You must choose ONE track only.
1. Do not mix regression and classification in same project.
1. Use proper evaluation metrics for your chosen task.
1. Avoid data leakage.
1. **Preprocessing must be reusable in deployment.**

---

# Bonus (Optional)

- Cross-validation
- Hyperparameter tuning
- Docker deployment
- Online hosting
