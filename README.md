# 🏥 Medical Insurance Expense Predictor

This project predicts **medical insurance expenses** based on patient details such as age, sex, BMI, smoker status, children, and region.
The model is built with **machine learning** and deployed using **Streamlit** for easy interaction.

---

## 📌 Features

* Data preprocessing with encoding & standardization
* Multiple regression models tested (Linear, Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting, SVR)
* Best model selected for deployment
* Interactive **Streamlit web app** for real-time predictions

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
streamlit
scikit-learn
pandas
numpy
joblib
matplotlib
statsmodels
mlxtend
tensorflow   # (only if using Deep Learning)
```

---

## 🚀 Running the App

1. Clone this repository or copy project files.
2. Make sure you have trained your model and saved the artifacts:

```python
import joblib
joblib.dump(preprocessor, "preprocessor.pkl")
joblib.dump(best_model, "best_model.pkl")
```

3. Run the app:

```bash
streamlit run app.py
```

4. Open the link shown in the terminal (default: `http://localhost:8501`).

---

## 🖥️ App Interface

* Input patient details: age, sex, BMI, children, smoker, region
* Click **Predict Expenses**
* Get estimated **insurance cost in \$**

---

## 📊 Project Workflow

1. **Data Preprocessing** – Handle categorical variables, scaling, encoding
2. **Model Training** – Train 7 models with standardization
3. **Model Evaluation** – Compare R², MAE, RMSE, CV scores
4. **Model Deployment** – Streamlit app for predictions

---

## 📦 Deployment

You can deploy this app on:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Hugging Face Spaces](https://huggingface.co/spaces)
* [Render](https://render.com)

---

## 📝 Example Input & Output

**Input:**

```
Age: 45
Sex: Male
BMI: 29.5
Children: 2
Smoker: Yes
Region: Southeast
```

**Output:**

```
💰 Estimated Medical Expenses: $16,500.75
```

---

Would you like me to also **generate the `requirements.txt` file** for you so deployment is smoother?
