restaurant-api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       ├── auth.py
│       └── orders.py
│
├── requirements.txt
└── README.md


uvicorn app.main:app --reload
http://127.0.0.1:8000/docs


###database view
https://sqlitebrowser.org/dl/