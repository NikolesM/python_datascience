#entorno virtual con venv y pip 
# 1. Crear entorno virtual (desde la raíz de tu proyecto)
py -m venv venv

# 2. Activar entorno virtual (Windows)
.\venv\Scripts\activate

# 3. Instalar las dependencias NECESARIAS (ej: Flask, pandas, etc)
pip install flask pandas numpy  # Tus paquetes aquí

# 4. Generar requirements.txt (SOLO con los paquetes instalados)
pip freeze > requirements.txt

# 5. Desactivar entorno (opcional)
deactivate
-----------------------------------------------------------------------------------------------------------
#si se va a ejecturar desde otra maquina
# 1. Activar entorno
.\venv\Scripts\activate

# 2. Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# 3. Ejecutar tu aplicación
python main.py


# Utiliza las funciones según tus necesidades
----------------------------------------------------------------------------------------------------------------
#comandos git
'''
git clone <URL_del_repositorio>
git clone git clone https://github.com/NikolesM/python_datascience.git
cd "project"
git init
git remote add origin linkssh
git add . or git add archivo1.js
git commit -m "fix, build, add, etc"
git push -u origin main
'''