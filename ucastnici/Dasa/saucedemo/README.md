# SauceDemo Test Automation

Tento projekt obsahuje automatizované testy pro webovou aplikaci SauceDemo (https://www.saucedemo.com/).

## Požadavky

- Python 3.8 nebo novější
- Chrome browser
- pip (Python package manager)

## Instalace

1. Vytvořte virtuální prostředí:
```bash
python -m venv venv
```

2. Aktivujte virtuální prostředí:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Nainstalujte závislosti:
```bash
pip install -r requirements.txt
```

## Spuštění testů

### Spuštění všech testů s HTML reportem:
```bash
pytest tests/test_saucedemo.py --html=report.html
```

### Spuštění testů s Allure reportem:
```bash
pytest tests/test_saucedemo.py --alluredir=./allure-results
allure serve ./allure-results
```

## Struktura projektu

```
saucedemo/
├── tests/
│   └── test_saucedemo.py
├── logs/
│   └── test_*.log
├── requirements.txt
└── README.md
```

## Testovací scénáře

1. Úspěšné přihlášení
2. Přidání produktu do košíku
3. Odebrání produktu z košíku
4. Řazení produktů podle ceny

## Logování

Všechny testy jsou logovány do souborů v adresáři `logs/`. Každý test vytváří nový log soubor s časovým razítkem. 