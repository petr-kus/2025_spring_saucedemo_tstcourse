python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate.ps1
pip install -r \ucastnici\jainatom\requirements.txt
pip freeze > \ucastnici\jainatom\requirements.txt

#Lekotr note: zde byh ocekaval relativni cesty misto absolutnich!? Ke vsemu jsou tam mezery a cesty nejsou v uvozovkach...
# takze jen: pip install -r requirements.txt