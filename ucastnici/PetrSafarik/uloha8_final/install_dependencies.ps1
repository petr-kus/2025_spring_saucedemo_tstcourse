python -m venv venv
.\venv\Scripts\activate
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
python.exe -m pip install --upgrade pip
pip install -r requirements.txt