import logging
import os
from datetime import datetime

def setup_logging(script_name="test", log_folder="test_TAC-T6_u8/Utils/Logs"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"{script_name.replace('.py', '')}_{timestamp}.log"
    full_path = os.path.join(log_folder, log_filename)

    os.makedirs(log_folder, exist_ok=True)

    # Force=True přepíše konfiguraci i když už logger byl nastavený
    logging.basicConfig(
        filename=full_path,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True
    )

    print(f"✅ Logger nastaven: {full_path}")
    logging.info("✅ Logování výsledků inicializováno.")

    return full_path