from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO - Lektor - podrobne probirana uloha na 7 lekci a v 8 lekci byla i ukazka jak myslenku hlavniho test casu prepsat/napsat lepe. 

def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    #TODO - Lektor - parametrizace otevirane stranky mohla byt vytazena ven jako parametr funkce.
    #TODO - Lektor - klidne zde mohla byt i kontrola spravenho otevreni dane stranky.
    #TODO - Lektor - TIP: driver mohl byt vytvoren jako 'global driver' - a pak jsi si ho nemusela predavat mezi testy jako parametr!
    return driver

def login(driver, username, password):
    #TODO - Lektor - pochvala za parametrizaci uzivatele a hesla!
    try:
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        print("Login successful!")
        #TODO - Lektor - tohle logovani mophlo byt do souboru :-) i do command liny (mohla jsi si na to napsat funkci napr.)
        #TODO - Lektor - PS: skutecne byl successful? (nekontrolujes to jen to predpoklads... !)
        #TODO - Lektor - PS2: co treba vzit i obrazek / screenshot?

    except Exception as e:
        print(f"Login failed: {e}")
        #TODO - Lektor - Kolem {e} mohlo byt  '{e}' kdyby to bylo prazdne at to jde poznat... . (a zase log do souboru...)

def add_items_to_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))
        )
        #TODO - Lektor - toto explicitini cekani zde nema smysl vzhledem k defaultni load strategy, ktere ceka na nacteni stranky (takze to tam uz je kdyz bezi tento kod). 

        button_add_to_cart = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        
        if not button_add_to_cart:
            print("No 'Add to Cart' buttons found!")
            return

        for button in button_add_to_cart:
            button.click()
            print("Item added to cart.")

        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        print(f"Items in cart after adding: {cart_count}")    
        
    except Exception as e:
        print(f"Error adding items to cart: {e}")

     #TODO - Lektor - v techto dvou test casech se celkove bojovalo s cekanim na zmenu cisla v badge (ktere se zmeni naky cas po kliku na button)
     #TODO - Lektor - a kdyz tam nic neni badge zmizi.
     #TODO - Lektor - spravne by se zde muselo by se zde implementovat explicitini cekani na spravnou hodnotu v badge... . (rozebirano na lekci 7 a 8)

def remove_items_from_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))
        )

        button_remove = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        #TODO - Lektor - obecne ... ty cesty bych (By.CLASS_NAME, "btn_inventory") bych si vytahl bokem a ulozil do promenych s handy nazvem... .
        
        if not button_remove:
            print("No 'Remove' buttons found!")
            return

        for button in button_remove:
            button.click()
            print("Item removed from cart.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

    except Exception as e:
        print(f"Error removing items from cart: {e}")

def run_test():
    driver = setup_browser()
    try:
        login(driver, "standard_user", "secret_sauce")
        add_items_to_cart(driver)  
        remove_items_from_cart(driver) 

        #TODO - Lektor - kod nize zde principielne nema co delat, je uz moc slozity na uroven test casu a necitelny... .
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']"))
        )
        assert button.is_displayed(), "Žádné tlačítko 'Add to cart' se nenašlo po odstranění zboží."

    except Exception as e:
        print("Test selhal:", e)

    finally:
        driver.quit()

run_test()