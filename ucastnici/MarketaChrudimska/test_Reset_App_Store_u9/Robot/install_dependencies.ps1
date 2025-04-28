# Vytvoření virtuálního prostředí
python -m venv venv

# Povolení skriptů ve Windows (pouze pro aktuální terminál)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Aktivace virtuálního prostředí
.\venv\Scripts\activate.ps1

# Instalace požadovaných balíčků
pip install robotframework==7.2.2 `
            robotframework-seleniumlibrary==6.7.1 `
            selenium==4.31.0 `
            webdriver-manager==4.0.2 `
            python-dotenv==1.0.1

# Uložení přesných verzí do requirements.txt
pip freeze > requirements.txt
