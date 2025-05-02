# 🧪 Test Project – PyTest + Selenium

Tento projekt obsahuje testy ve stylu PyTest s využitím Selenium WebDriveru.

---

## 📁 Struktura projektu

```
test_project/
├── test.py # Hlavní testovací skript
├── install_dependencies.ps1 # Skript pro instalaci závislostí (Windows)
├── requirements.txt # Seznam Python závislostí
├── conftest.py # Definice fixture (např. driver)
└── web_saucedemo/ # Page Objects a pomocné moduly
├── InventoryAddCart.py # Page Object pro přidávání/odebírání produktů
├── LoginPage.py # Page Object pro přihlášení
├── Logout.py # Page Object pro odhlášení
└── Menu.py # Page Object pro menu
```

---

## ✅ Požadavky

- Python 3.8+
- Selenium WebDriver (ChromeDriver / GeckoDriver) v PATH
- Prohlížeč Chrome nebo Firefox
- Virtuální prostředí (doporučeno)

---

## 🔧 Instalace prostředí

jednoduchá instalace

```bash
install_dependencies.ps1
```

nebo složitější

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Spuštění testů

Testy spustíš pomocí příkazu:

```bash
pytest -html=report.html test.py
```



## 📄 Výstupy

Po spuštění pytestu uvidíš report v konzoli. Pro generování HTML reportu:

```bash
pytest --html=report.html
```

---

## 📚 Doporučené zdroje

- [Oficiální dokumentace pytest](https://docs.pytest.org/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [pytest-html plugin](https://pytest-html.readthedocs.io/)