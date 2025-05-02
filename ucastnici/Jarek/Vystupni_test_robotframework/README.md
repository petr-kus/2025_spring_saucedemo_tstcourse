# 🧪 Automatizované testy – Robot Framework + SeleniumLibrary

Tento projekt obsahuje sadu testů napsanou v [Robot Frameworku](https://robotframework.org/) s využitím knihovny [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/). Cílem je demonstrovat čistou strukturu testů ve stylu Page Object Model.

---

## 📁 Struktura projektu

```
.
├── tests/              # Testovací scénáře
├── pages/              # Definice jednotlivých stránek (Page Objects)
├── variables/          # Globální proměnné (např. URL, uživatelé)
├── reports/            # Výstupní složka s výsledky testů
├── requirements.txt    # Seznam všech závislostí pro instalaci
└── arguments.txt       # Parametry pro spuštění testů
```

---

## ✅ Požadavky

- Python 3.8+
- Chrome nebo Firefox
- WebDriver v PATH (chromedriver/geckodriver)
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

Níže jsou přehledné varianty, jak spustit testování:

### 1) Spuštění všech testů ve složce `tests/`
```bash
robot --argumentfile arguments.txt tests/
```

### 2) Spuštění konkrétního souboru
```bash
robot reports --argumentfile arguments.txt tests/login_tests.robot
```

### 3) Spuštění jednoho testu v souboru
```bash
robot  --argumentfile arguments.txt --test "Název testu" tests/login_tests.robot
```

> **Tip:** Parametr `--outputdir` určuje, kam se uloží `report.html`, `log.html` a `output.xml`.

---

## 📄 Výstupy

Po každém spuštění testů se vygenerují soubory v adresáři `reports/`:

- `report.html` – souhrnný report
- `log.html` – podrobný log kroků
- `output.xml` – strojově čitelný výstup

---

## 📚 Doporučené zdroje

- [Oficiální dokumentace Robot Framework](https://robotframework.org/)  
- [SeleniumLibrary Keywords](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)  
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
