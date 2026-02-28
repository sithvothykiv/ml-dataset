# Final Project (Machine Learning): **“Smart HR Dashboard”**

Build an end-to-end ML mini-product that:

1) predicts a **continuous target** (Regression)
2) predicts a **binary outcome** (Classification)
3) compares **Linear / Logistic** with **Decision Tree / Random Forest**
4) is **deployed as a small web app** (Flask or any Python web framework) that includes a **survey-style form** for predictions.

---

## 0) How this project matches the course syllabus

- **1. Intro ML** → problem framing, data types, train/valid/test, metrics, leakage, baseline
- **2. Regression (Linear)** → predict a numeric value (e.g., salary estimate)
- **3. Classification (Logistic)** → predict a yes/no outcome (e.g., employee attrition)
- **4. Deployment + survey prediction** → build a web form to input features and return predictions
- **5. Decision Tree + Random Forest** → compare models and interpret feature importance

---

## 1) Project idea & real-world story

**Scenario:** A company wants a simple “HR dashboard” that can:

- **Estimate monthly income** from employee information (**Regression**)
- **Predict whether an employee is likely to leave** (**Classification**)

The dashboard is used by HR staff to fill a short survey form and get instant predictions.

---

## 2) Recommended dataset (choose one)

Pick **ONE** dataset option:

### Option A (recommended): Public HR dataset

Use a common HR dataset with columns like:

- Age, Gender, Department, JobRole, YearsAtCompany, Education, JobSatisfaction, OverTime, etc.
- Targets (examples):
  - **Attrition**: Yes/No (classification)
  - **MonthlyIncome**: numeric (regression)

> You can find similar datasets on Kaggle/UCI. If you cannot access public datasets, use Option B.

### Option B: Create your own small dataset (synthetic)

Generate a CSV (300–3000 rows) using Python with realistic ranges.

- Create a numeric target (e.g., monthly_income)
- Create a binary target (e.g., attrition) based on a rule + randomness

**Minimum columns (example):**

- age, years_at_company, overtime (0/1), job_satisfaction (1–5), dept (category), education_level (1–5)
- monthly_income (float)  ← regression target
- attrition (0/1)         ← classification target

---

## 3) Project deliverables (what you must submit)

Your submission must include:

### A) Code repository / folder structure

```
final_project/
  data/
    raw.csv
    processed.csv
  notebooks/
    01_eda.ipynb
    02_models.ipynb
  src/
    preprocess.py
    train_regression.py
    train_classification.py
    evaluate.py
    utils.py
  app/
    app.py
    templates/
      index.html
      result.html
    static/
      style.css
  models/
    reg_model.pkl
    clf_model.pkl
    preprocessor.pkl
  README.md
  REPORT.md
  requirements.txt
```

### B) REPORT.md (short report)

Include:

- Problem statement
- Dataset description
- Preprocessing steps
- Models + evaluation results
- Comparison and final model choice
- Deployment screenshots (or description)
- How to run

### C) Deployed prediction app

- A web page with input fields (“survey form”)
- A result page showing predictions
- Clear validation and user-friendly messages

---

## 4) Step-by-step guideline

### Step 1 — Define the ML tasks (Intro ML)

1. Write the two tasks:
   - Regression: predict **monthly_income**
   - Classification: predict **attrition** (the process of reducing something's strength or effectiveness)
2. Decide the success metrics:
   - Regression: MAE (and/or RMSE), R² (optional)
   - Classification: Accuracy + F1-score (and confusion matrix)
3. Split data:
   - Train / validation / test (e.g., 70/15/15 or 80/20 with CV)
4. Create a **baseline**:
   - Regression baseline: predict mean income
   - Classification baseline: predict majority class

Output: a short section in `REPORT.md` describing tasks + metrics + splits.

---

### Step 2 — Load and explore the data (EDA)

1. Load CSV
2. Inspect:
   - data shape, dtypes, missing values
   - target distributions (income histogram; attrition ratio)
3. Visualize:
   - correlations for numeric columns
   - attrition vs overtime / satisfaction / years_at_company (bar charts)
4. Identify:
   - columns to drop (IDs, constant columns)
   - potential leakage (columns that directly reveal target)

Output: `notebooks/01_eda.ipynb` with charts and key notes.

---

### Step 3 — Preprocess data (clean + encode)

1. Handle missing values:
   - Numeric: median
   - Categorical: most frequent (or “Unknown”)
2. Encode categorical features:
   - One-hot encoding recommended
3. Scale numeric (for linear/logistic):
   - StandardScaler recommended
4. Keep preprocessing consistent:
   - Use a single `ColumnTransformer` pipeline
   - Save the fitted preprocessor to `models/preprocessor.pkl`

Output: `src/preprocess.py` and saved preprocessor.

---

### Step 4 — Train Regression models

Train and compare:

1) **Linear Regression**
2) **Decision Tree Regressor**
3) **Random Forest Regressor**

**Required:**

- Use the same train/val split
- Tune at least 1–2 hyperparameters for tree/RF (e.g., max_depth, n_estimators)
- Evaluate with MAE (and RMSE optional)

Output:

- `models/reg_model.pkl`
- Table in `REPORT.md` with regression metrics

---

### Step 5 — Train Classification models

Train and compare:

1) **Logistic Regression**
2) **Decision Tree Classifier**
3) **Random Forest Classifier**

**Required:**

- Use metrics: Accuracy + F1-score
- Show confusion matrix
- Handle class imbalance if needed:
  - try `class_weight="balanced"` for logistic/RF, or use stratified split

Output:

- `models/clf_model.pkl`
- Table in `REPORT.md` with classification metrics + confusion matrix

---

### Step 6 — Model selection + interpretation

1. Pick the best regression model and the best classification model
2. Explain *why* (metrics + simplicity + overfitting risk)
3. Interpret:
   - Linear/Logistic: coefficients (top positive/negative features)
   - Tree/RF: feature importance
4. Add at least 2 insights:
   - Example: overtime increases attrition risk
   - Example: years_at_company correlates with income

Output: interpretation section in `REPORT.md`.

---

### Step 7 — Save models for deployment

1. Save:
   - preprocessor (pipeline)
   - best regression model
   - best classification model
2. Ensure inference uses the **same feature order** as training
3. Provide a small inference test script:
   - Load models and run prediction on 1 example row

Output: `src/utils.py` (load/save helpers) + `src/evaluate.py` or `src/inference_test.py`.

---

### Step 8 — Build the web app (Flask)

**Minimum requirements:**

- `GET /` shows form with input fields (survey)
- `POST /predict` processes form → runs preprocessing → runs both models → shows results

**Recommended UI fields (example):**

- age (number)
- years_at_company (number)
- overtime (yes/no)
- job_satisfaction (1–5)
- education_level (1–5)
- department (dropdown)

**Outputs:**

- Predicted monthly income (regression output)
- Attrition probability and label (classification output)
  - Example: “Attrition risk: 0.73 (High)”

Output: `app/app.py` + templates.

---

### Step 9 — Add practical engineering touches

Add at least **3** of the following:

- Input validation (range checks, required fields)
- Friendly error pages/messages
- Logging predictions to a CSV file
- Simple API endpoint returning JSON (`/api/predict`)
- Unit tests for preprocessing or inference
- Dockerfile (optional)

Output: show changes in repo and mention in `REPORT.md`.

---

### Step 10 — Final check & submission

Your final submission must include:

- `REPORT.md` with results and screenshots
- Reproducible environment:
  - `requirements.txt` 
- How to run:
  - training scripts
  - app locally

**Suggested run commands:**

- Train:
  - `python src/train_regression.py`
  - `python src/train_classification.py`
- Run app:
  - `python app/app.py`

---

## 5) Grading rubric (simple)

- **Data & EDA (15%)**: clear understanding, good charts, leakage check
- **Preprocessing (15%)**: correct handling of missing + encoding, reusable pipeline
- **Regression models (15%)**: linear + tree/RF + metrics table
- **Classification models (20%)**: logistic + tree/RF + metrics + confusion matrix
- **Comparison & interpretation (15%)**: explains trade-offs, shows insights
- **Deployment (20%)**: working survey form + predictions + clear instructions

---

## 6) Tips to avoid common mistakes

- Don’t fit preprocessing on the full dataset (avoid leakage). Fit on train only.
- Keep the same preprocessing pipeline for training and inference.
- For categorical columns, ensure your app uses allowed values (dropdowns).
- Use stratified splits for classification.
- Save and load models using the same library versions (pin in requirements).

---

## 7) Optional extensions (bonus)

- Add model monitoring: save each prediction with timestamp
- Add a “confidence explanation” section: top 3 important features
- Add cross-validation and hyperparameter search (GridSearchCV)
- Deploy to a free hosting platform (if available) and include link in report
