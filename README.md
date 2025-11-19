# 📦 **AI-Driven Discount Recommendation System**  
### Intelligent User Behavior Analysis for WooCommerce  

## 📘 **Project Description**  
This project is a machine learning–powered discount recommendation system designed for **WooCommerce-based WordPress websites**.  
It collects user activity, analyzes behavioral patterns (views, cart events, purchases), and uses a **Random Forest model** to determine which products should receive discounts to increase sales.

The architecture follows the **MVC design pattern**, uses **clean OOP principles**, and is organized in a **multi-file, production-level codebase**.

---

## ✨ **Features**

### 🔹 **Core System**
- Full **MVC architecture** (Models, Views, Controllers, Config)
- Clean, modular, fully **object-oriented** structure
- Complete **MySQL integration** (`database.py` + `repository.py`)
- Centralized configuration management (`settings.py`)

### 🔹 **Data Layer**
- Models for **Users**, **Products**, **Events**, **Discounts**
- Repository pattern for clean database access
- Ready SQL schema (`schema.sql`)

### 🔹 **Machine Learning Layer**
- Advanced **Random Forest** model
- Preprocessing (encoding, scaling, feature engineering)
- Training pipeline with cross-validation
- Model persistence using **pickle/joblib**
- Predicts which product should receive a discount
- Fully isolated ML module (`ml_model.py`)

### 🔹 **Controllers**
- Controllers for user, product, event, and ML operations
- Layered request handling

### 🔹 **Views**
- API response formatter
- Dashboard-style output view
- CLI-friendly preview of ML insights

### 🔹 **Main App**
- Integrated entry point (`main.py`)
- Demonstrates DB access, preprocessing, ML training & prediction

---

## 🛠 **Requirements**

Before installing, make sure you have:

- **Python 3.10+**
- **MySQL 8+**
- **pip** (latest recommended)

Python libraries required:
- `mysql-connector-python`
- `scikit-learn`
- `pandas`
- `numpy`
- `joblib`

Additional Requirement:
- A **WordPress + WooCommerce** website where the data is collected

---

## 🚀 **Installation & Usage**

### **1. Clone the Project**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### **2. Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure Database**
Edit the configuration file:

```
/config/settings.py
```

Set database settings:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_NAME = "discount_ai"
```

### **5. Generate Database Tables**
Import SQL schema into MySQL:

```bash
mysql -u root -p discount_ai < sql/schema.sql
```

### **6. Run the Application**
```bash
python main.py
```

This will:

- Connect to MySQL  
- Fetch users, products, and events  
- Prepare ML dataset  
- Train the Random Forest model  
- Recommend products for discount  
- Display dashboard results  

---

## 🖼 **Screenshots**

### 📊 System Architecture (MVC)
```
project/
│── main.py
│── /models
│── /controllers
│── /views
│── /config
│── /sql
```

### 🧠 Machine Learning Prediction (Example Output)
```
Recommended products for discount:
- Product 14 (High interest)
- Product 22 (Abandoned carts)
```

### 📋 Dashboard Output Example
```
=== Dashboard Summary ===
Total Users: 3251
Total Products: 412
Top Event: product_view
Most Popular Product: AirPods Pro
```

---

## 🤝 **Contributing**

Contributions are welcome!

### How to contribute:
1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push and open a Pull Request  
