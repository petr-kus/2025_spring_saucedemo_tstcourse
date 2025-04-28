import logging
import os
from datetime import datetime

def setup_logging(script_name="test", log_folder="test_Reset_App_Store_u9/Pytest/Utils/Logs"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"{script_name.replace('.py', '')}_{timestamp}.log"
    full_path = os.path.join(log_folder, log_filename)

    os.makedirs(log_folder, exist_ok=True)

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

def assert_and_log(condition, message, logger):
    """
    Provede assert a v případě selhání zaloguje chybu.
    
    :param condition: Podmínka, která by měla být True.
    :param message: Zpráva, která se objeví při selhání asserce.
    :param logger: Logger instance, do které se má logovat.
    """
    try:
        assert condition, message
    except AssertionError as e:
        logger.error(str(e))
        raise