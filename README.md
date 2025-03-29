# fraud-detection-app
# 🚀 Fraud Detection App
## 📌 Overview
This project is a Fraud Detection App that identifies fraudulent transactions using Machine Learning. The app takes user inputs, processes the data, and predicts whether a transaction is fraudulent. It is built using Python, Scikit-Learn, XGBoost, and Streamlit for deployment.

## 📊 Features
✅ Data Preprocessing – Handling missing values, encoding categorical variables, and scaling numerical features
✅ Machine Learning Model – Trained using Logistic Regression, Decision Trees, and XGBoost
✅ Model Evaluation – Optimized using precision, recall, and F1-score
✅ Deployment – Deployed using Streamlit with a simple UI

## 🛠 Technologies Used
Python (pandas, numpy, scikit-learn, joblib)

Machine Learning Models (Logistic Regression, Decision Tree, XGBoost)

Streamlit (For deployment & UI)

Git & GitHub (Version control)

## 📂 Project Structure
bash
Copy
Edit
fraud-detection-app/
│── fraud_env/                # Virtual environment (ignored in GitHub)  
│── data/                     # Dataset folder  
│── models/                   # Contains trained ML models (Pickle files)  
│── app.py                     # Main application script  
│── requirements.txt          # Dependencies  
│── README.md                 # Project documentation  
## ⚡ Installation & Usage
Step 1️⃣: Clone the Repository
git clone https://github.com/your-username/fraud-detection-app.git
cd fraud-detection-app
Step 2️⃣: Create & Activate Virtual Environment
python -m venv fraud_env  
fraud_env\Scripts\activate  
Step 3️⃣: Install Dependencies
pip install -r requirements.txt  
Step 4️⃣: Run the App
streamlit run app.py  
🚀 Deployment
The app is successfully deployed on Streamlit Cloud. You can access it here:
🔗 Live App: [https://fraud-detection-app-chcy8vvjodxs4ybszma8vr.streamlit.app/]

📌 Acknowledgments
A huge thanks to Scikit-Learn, XGBoost, and Streamlit for providing such amazing tools for data science and deployment.
