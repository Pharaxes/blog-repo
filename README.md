```
├── entorno/            <--- Carpeta del entorno
│ ├── Scripts/
│ │ ├── activate.bat
│ │ ├── deactivate.bat
│ │ └── ...
│ └── ...
├── blog-repo/          <--- Carpeta del Repositorio
│ ├── blog/             <--- Carpeta del proyecto Django
│ │ ├── apps/          <--- Aplicaciones Django
│ │ │ ├── post/
│ │ │ │ ├── __pycache__/      **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── user/
│ │ │ │ ├── __pycache__/      **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/        **Ignorada en el .gitignore**
│ │ │ ├── configurations/      <--- Configuraciones django (opcional)
│ │ │ │ ├── __pycache__/      **Ignorada en el .gitignore**
│ │ │ │ ├── base.py       <--- Configuraciones base
│ │ │ │ ├── local.py        <--- Configuraciones para desarrollo local
│ │ │ │ ├── production.py      <--- Configuraciones para produccion
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/            <--- Archivos multimedia - **Ignorada en el .gitignore**
│ │ │ ├── post/
│ │ │ │ ├── post-default.jpeg
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user-default.png
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/           <--- Archivos estáticos
│ │ │ ├── assets/
│ │ │ │ ├── img/
│ │ │ │ ├── svg/
│ │ │ │ ├── favicon.ico
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ ├── main.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/          <--- Archivos templates
│ │ │ ├── auth/
│ │ │ │ ├── auth-login.html
│ │ │ │ ├── auth-register.html
│ │ │ │ └── ...
│ │ │ ├── errors/
│ │ │ │ ├── not-found.html
│ │ │ │ ├── internal-error.html
│ │ │ │ └── ...
│ │ │ ├── includes/
│ │ │ │ ├── base.html
│ │ │ │ ├── footer.html
│ │ │ │ ├── header.html
│ │ │ │ └── ...
│ │ │ ├── post/
│ │ │ │ ├── post-delete.html
│ │ │ │ ├── post-detail.html
│ │ │ │ ├── post-list.html
│ │ │ │ ├── post-new.html
│ │ │ │ ├── post-update.html
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user-profile.html
│ │ │ │ ├── user-update.html
│ │ │ │ └── ...
│ │ │ ├── index.html
│ │ │ └── ...
│ │ ├── db.sqlite3     <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py
│ │ └── ...
│ ├── .gitignore
│ ├── README.md           <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt    <--- Archivo requeriments.txt - Enlista los paquetes
| └── ...
└── ...
```
