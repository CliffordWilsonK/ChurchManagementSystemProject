# Church Management Web App

## 📌 Project Overview
This is a **Church Management Web App** built with **Django**. It helps churches track **weekly offerings, tithes, seeds, and ongoing projects**, displaying the data in a dashboard. It also allows **member registration** and gives access to authorized users (**admin, pastor, and treasurer**)
## 🚀 Features
- **Dashboard**: View total offerings, tithes, seeds, and projects.
- **Member Management**: Add, edit, and view church members.
- **Financial Tracking**: Log weekly offerings, tithes, and seeds.
- **Admin Panel**: Manage users and data through Django Admin.

## 🛠️ Technologies Used
- **Backend**: Django
- **Database**: SQLite (for development)
- **Frontend**: HTML
- **Deployment**: Render (Free Tier)

---
## 🏗️ Installation and Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/church-management.git
cd church-management
```

### 2️⃣ **Create and Activate a Virtual Environment**
```bash
# Windows
type nul > .env  # Create an .env file
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Edit the `.env` file and add:
```bash
SECRET_KEY='your-secret-key'
DEBUG=True  # Change to False in production
ALLOWED_HOSTS=127.0.0.1,localhost,your-app-name.onrender.com
DATABASE_URL=sqlite:///db.sqlite3  # Change to PostgreSQL in production
```

### 5️⃣ **Run Migrations and Collect Static Files**
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6️⃣ **Create a Superuser (Admin Account)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin username and password.

### 7️⃣ **Run the Development Server**
```bash
python manage.py runserver
```
Now, visit **http://127.0.0.1:8000/** in your browser.

---
## 🚀 Deployment on Render (Free Tier)

### **1️⃣ Push Your Code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### **2️⃣ Deploy on Render**
- Sign in at [Render.com](https://render.com)
- Click **New Web Service** → **Deploy from GitHub**
- Select your **Django project repository**
- Set **Build Command:**
  ```bash
  pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
  ```
- Set **Start Command:**
  ```bash
  gunicorn church_management.wsgi:application --bind 0.0.0.0:10000
  ```
- Add environment variables in **Render → Environment Variables**:
  ```bash
  DJANGO_ALLOWED_HOSTS=your-app-name.onrender.com
  PORT=10000
  ```
- Click **Deploy**

### **3️⃣ Access Your Live App**
Visit:
```bash
https://your-app-name.onrender.com.onrender.com
```


---
## 📧 Contact
For any questions, reach out to **cliffordwilsonk@gmail.com**


