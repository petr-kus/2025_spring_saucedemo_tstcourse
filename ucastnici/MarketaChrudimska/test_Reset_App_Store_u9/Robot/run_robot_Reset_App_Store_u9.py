import time
import os

'''
spouští se příkazem v terminálu 'python run_robot_Reset_App_Store_u9.py' ve složce Robot
'''

current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

# Vytvoření příkazového řádku pro spuštění testu Robot Frameworku
command = f"robot --output Logs/output_test_Reset_App_Store_u9_{current_time}.xml --log Logs/log_test_Reset_App_Store_u9_{current_time}.html --report Logs/report_test_Reset_App_Store_u9_{current_time}.html robot_Reset_App_Store_u9.robot"

# Spuštění příkazu
os.system(command)

