import pytest
import glob
import os
from datetime import datetime

def pytest_configure(config):
    if config.args:
        test_file = os.path.basename(config.args[0])
        test_name = os.path.splitext(test_file)[0]

        reports_folder = "test_Reset_App_Store_u9/Pytest/Reports"
        os.makedirs(reports_folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_name = f"{test_name}_{timestamp}.html"
        report_path = os.path.join(reports_folder, report_name)

        config.option.htmlpath = report_path

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    logs_path = "Utils/logs"
    list_of_logs = sorted(glob.glob(os.path.join(logs_path, "*.log")), reverse=True)
    latest_log = list_of_logs[0] if list_of_logs else None

    if latest_log:
        relative_path = os.path.relpath(latest_log, start=".")
        link = f"<a href='{relative_path}' target='_blank'>Zobrazit log ({os.path.basename(latest_log)})</a>"
        prefix.extend([f"<div>{link}</div>"])