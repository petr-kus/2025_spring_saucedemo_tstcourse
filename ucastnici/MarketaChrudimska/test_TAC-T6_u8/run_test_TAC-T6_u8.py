import os

def main():
    print(f"Spouštím testy...\nHTML report se uloží do složky Reports\nLog soubor se uloží do složky Utils/Logs\n")
    
    cmd = "pytest -s test_TAC-T6_u8/test_TAC-T6_u8.py --html= --self-contained-html"
    os.system(cmd)

if __name__ == "__main__":
    main()