# 🏠 House Price Prediction App

A Machine Learning based web application that predicts house prices based on location, total square feet area, number of bathrooms, and BHK configuration.

## 🚀 Live Demo

🌐 Live App: https://house-price-prediction-app-2p1b.onrender.com

## 📂 GitHub Repository

🔗 Repository: https://github.com/utkarsh4863/House-price-prediction-app

---

## 📌 Project Overview

This project uses a Bengaluru housing dataset and applies Machine Learning techniques to predict house prices. The application allows users to enter house details and receive an estimated price instantly through a Flask web interface.

---

## ✨ Features

- Predict house prices instantly
- Location dropdown with multiple areas
- Responsive Bootstrap UI
- Data preprocessing and cleaning
- Outlier detection and removal
- One-hot encoding for categorical features
- Linear Regression model training
- Flask backend integration
- Deployed online using Render

---

## 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Flask
- Pickle
- JSON

### Frontend
- HTML
- Bootstrap

### Deployment
- GitHub
- Render

---

## 📊 Machine Learning Workflow

### Data Cleaning
- Removed unnecessary columns
- Handled missing values
- Converted `size` into `BHK`
- Converted `total_sqft` values into numeric format

### Feature Engineering
- Created BHK feature
- Grouped low-frequency locations into `other`

### Outlier Removal
- Price per square feet outliers
- BHK-based outliers
- Bathroom outliers

### Model Training
- Linear Regression
- Cross-validation
- Model evaluation

---

## 📁 Project Structure

```text
House-price-prediction-app/
│
├── app.py
├── house_price_model.pkl
├── columns.json
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
│
├── templates/
│     └── index.html
│
├── Data/
│     └── bengaluru_house_prices.csv
│
└── House_Price_Prediction.ipynb
```

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/utkarsh4863/House-price-prediction-app.git
```

Move into project directory:

```bash
cd House-price-prediction-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

- Home Page
- Prediction Result
- User Input Form

---

## 🎯 Future Improvements

- Add charts and analytics
- Improve UI design
- Add price trends visualization
- Add map integration
- Add user authentication

---

## 👨‍💻 Author

**Utkarsh Kashyap**

LinkedIn: Add your LinkedIn profile here  
GitHub: https://github.com/utkarsh4863

---

⭐ If you found this project useful, consider giving it a star.
