# SauceDemo Robot Framework Tests

Tento projekt obsahuje automatizované testy pro webovou aplikaci SauceDemo vytvořené pomocí Robot Frameworku.

## Požadavky

- Python 3.7 nebo novější
- Chrome WebDriver

## Instalace

1. Nainstalujte požadavky:
```bash
pip install -r requirements.txt
```

2. Ujistěte se, že máte nainstalovaný Chrome WebDriver a je v PATH.

## Spuštění testů

Pro spuštění všech testů použijte příkaz:
```bash
robot Test_RobrotFramework.robot
```

Pro spuštění s reportem:
```bash
robot --outputdir reports Test_RobrotFramework.robot
```

## Struktura projektu

- `Test_RobrotFramework.robot` - hlavní testovací soubor
- `resources/keywords.robot` - klíčová slova a proměnné
- `requirements.txt` - seznam požadavků
- `reports/` - složka s reporty (vytvoří se po spuštění testů) 