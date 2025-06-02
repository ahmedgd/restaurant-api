<<<<<<< HEAD
## 🍽️ مشروع REST API لمطعم باستخدام FastAPI

### ✍️ تم بواسطة: [م. أحمد جمال](https://www.linkedin.com/in/ahmed-gamal-dev/)

🔗 حساب GitHub: [ahmedgd](https://github.com/ahmedgd)

---

### 📌 وصف المشروع

هذا المشروع هو نظام RESTful API بسيط مخصص لإدارة مطعم. باستخدام هذا الـ API، يمكن تسجيل المستخدمين، تسجيل الدخول باستخدام JWT، بالإضافة إلى إدارة قائمة الطعام (إضافة وعرض الوجبات).

يهدف المشروع إلى توفير بنية قوية لتطبيقات الويب التي تحتاج إلى مصادقة وتفاعل مع بيانات عبر HTTP بطريقة آمنة ومنظمة.

---

### 🛠️ التقنيات المستخدمة

* **FastAPI** – لبناء API سريع وعصري.
* **SQLite** – قاعدة بيانات بسيطة ومناسبة للتطبيقات الصغيرة.
* **SQLAlchemy** – ORM للتعامل مع قاعدة البيانات بشكل ديناميكي.
* **Pydantic** – للتحقق من صحة البيانات والنمذجة.
* **Passlib + Bcrypt** – لتأمين كلمات المرور.
* **JWT (JSON Web Token)** – للمصادقة وتأمين الوصول للبيانات.

---

### 🧩 الوظائف الأساسية للنظام

#### 🔐 المصادقة:

* `POST /auth/register` – تسجيل مستخدم جديد.
* `POST /auth/login` – تسجيل الدخول واستلام توكن JWT.

#### 🍽️ إدارة قائمة الطعام:

* `GET /meals/` – عرض جميع الوجبات (يتطلب التوكن).
* `POST /meals/` – إضافة وجبة جديدة (يتطلب التوكن).

---

### 🚀 طريقة التشغيل المحلي

1. **استنساخ المشروع:**

```bash
git clone https://github.com/ahmedgd/restaurant-api.git
cd restaurant-api
```

2. **تفعيل البيئة الافتراضية (اختياري ولكن موصى به):**

```bash
python -m venv venv
venv\Scripts\activate  # على Windows
```

3. **تثبيت المتطلبات:**

```bash
pip install -r requirements.txt
```

4. **تشغيل التطبيق:**

```bash
uvicorn app.main:app --reload
```

5. **الوصول إلى الوثائق التفاعلية (Swagger UI):**
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🔐 المصادقة واستخدام JWT

* بعد تسجيل الدخول من خلال `POST /auth/login` ستحصل على توكن JWT.
* لإرسال طلب محمي مثل `POST /meals` يجب إضافة التوكن في الهيدر:

```http
Authorization: Bearer <access_token>
```

---

### 🧪 أمثلة باستخدام Curl

#### ✅ تسجيل مستخدم:

```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "ali", "password": "123123"}'
```

#### ✅ تسجيل الدخول:

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "ali", "password": "123123"}'
```

---

### 🗄️ قاعدة البيانات

يتم إنشاء قاعدة البيانات تلقائيًا باستخدام SQLite داخل ملف `restaurant.db`. يمكنك استعراضها باستخدام أداة [DB Browser for SQLite](https://sqlitebrowser.org/).

---

### 💡 ملاحظات مهمة

* المشروع للتعلم والتجربة، لا يُستخدم في الإنتاج بدون تحسينات أمنية.
* تأكد من تغيير `SECRET_KEY` في `auth_utils.py` في حالة الاستخدام الحقيقي.
* يمكن توسيع المشروع لاحقًا بإضافة صلاحيات للمستخدمين ولوحة تحكم Admin وربط مع واجهات أمامية مثل React أو Vue.

---

### 📬 للتواصل

إذا كان لديك أي استفسار أو اقتراح:

* 💼 [LinkedIn – أحمد جمال](https://www.linkedin.com/in/ahmed-gamal-dev/)
* 💻 [GitHub – ahmedgd](https://github.com/ahmedgd)

---

بالتوفيق للجميع ❤️
=======
# restaurant-api
A simple restaurant API built with FastAPI and SQLite. Includes user registration, login (JWT), and meal management.
>>>>>>> 7abd2d4ecb2d331aee8b85295c4eceb76905b91f
