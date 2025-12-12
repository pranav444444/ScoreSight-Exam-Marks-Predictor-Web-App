
# 📘 **ScoreSight — Student Exam Predictor**

### *A Machine Learning Web App for Predicting Student Exam Performance*

ScoreSight is a predictive analytics system designed to estimate a student’s exam score based on factors such as study habits, attendance, mental health rating, sleep duration, and part-time work status.
The project demonstrates a complete end-to-end ML workflow including:

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Model training & evaluation
* Hyperparameter tuning
* Model selection
* Streamlit web deployment

This project was created as part of an academic learning initiative in machine learning and predictive modeling.

---

# 📂 **Project Structure**

```
ScoreSight/
│
├── app.py                    # Streamlit web app
├── best_model.pkl            # Saved Linear Regression model
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
│
├── data/
│   └── student_habits_performance.csv   # Original dataset (if included)
│
├── notebooks/
│   └── marks_predictive_analytics.ipynb # Full EDA + model training notebook
│
└── assets/
    └── model_scores.docx     # Model reports (optional)
```

---

# 📊 **1. Dataset Overview**

The dataset consists of student behavioral and academic features:

| Feature Name              | Description                            |
| ------------------------- | -------------------------------------- |
| **study_hours_per_day**   | Average hours studied per day          |
| **attendance_percentage** | Class attendance (%)                   |
| **mental_health_rating**  | Self-reported mental well-being (1–10) |
| **sleep_hours**           | Daily sleep duration                   |
| **part_time_job**         | 1 = Yes, 0 = No                        |
| **exam_score**            | Target variable                        |

---

# 🧹 **2. Data Preprocessing Summary**

Performed cleaning and preparation steps:

* Missing value handling
* Converting categorical variables (`Part-time Job`) to numeric
* Outlier analysis
* Feature scaling (for some models)
* Train-test split (80–20)

---

# 🤖 **3. Model Training & Results**

We tested multiple models:

| Model                          | Test R²    | Test RMSE |
| ------------------------------ | ---------- | --------- |
| **Linear Regression**          | **0.7908** | **7.324** |
| Support Vector Regressor (SVR) | 0.766      | 7.744     |
| Random Forest Regressor        | 0.761      | 7.822     |
| Decision Tree Regressor        | 0.702      | 8.740     |

🎯 **Selected Model → Linear Regression**
Reason:

* Highest generalization accuracy
* Lowest RMSE among all tested models
* Simple, interpretable, robust for small datasets

---

# 📈 **Model Interpretation**

### ✔️ **R² Score: 0.79**

The model explains **79% of the variability** in student exam results.

### ✔️ **RMSE: ~7.3 marks**

Typical error range: ±7 marks — acceptable for educational use.

### ✔️ **Generalization gap (Train vs Test)**

* Train R² ≈ 0.818
* Test R² ≈ 0.790
* Very small gap → **no overfitting**, model generalizes well.

---

# 🧠 **Key Insights From Analysis**

* Students studying **more hours** and maintaining **higher attendance** tend to score better.
* Better **mental health rating** improves performance.
* Optimal sleep (~7–8 hours) improves scores.
* Students with **part-time jobs** show slightly lower predicted scores (due to reduced study time).

---

# 🌐 **4. Streamlit Web Application**

A fully interactive web app built using Streamlit allows users to:

✔️ Adjust sliders (study hours, attendance, sleep, etc.)
✔️ View real-time predicted exam marks
✔️ Experience a clean and modern UI

### **To run locally:**

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  **Run the app**
OPen app.py in terminal and run this command "streamlit run app.py"


🎉 Your app will open automatically in your browser.

Note: Deployment (Streamlit Cloud/Render) is optional. Local execution works perfectly.

# 📦 **requirements.txt**

```
streamlit
numpy
pandas
scikit-learn
joblib
plotly
```

---

# 🔮 **Future Improvements**

* Add visual analytics dashboard
* Add confidence intervals for predictions
* Train additional models (Gradient Boosting, XGBoost, CatBoost)
* Introduce feature engineering (interaction terms)
* Deploy on cloud + load-balanced infra
* Add login system for personalized analytics

---

# 📝 **Author**

**Pranav Patel**
Aspiring Data Analyst → transitioning to Data Science
Skilled in Python, ML, SQL, Power BI, Streamlit
GitHub: [https://github.com/pranav444444](https://github.com/pranav444444)

---

# ⭐ If you use this project, please star the repo!

---


