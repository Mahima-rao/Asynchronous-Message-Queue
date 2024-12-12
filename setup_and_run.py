import subprocess
import os
import sys

def install_dependencies():
    """Install necessary dependencies."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_services():
    """Run both Service A and Service B."""
    service_a_command = ["uvicorn", "service_a.main:app", "--reload", "--port", "8000"]
    service_b_command = ["uvicorn", "service_b.main:app", "--reload", "--port", "8001"]
    
    # Run Service A and Service B concurrently
    subprocess.Popen(service_a_command)
    subprocess.Popen(service_b_command)

if __name__ == "__main__":
    if not os.path.exists("requirements.txt"):
        print("requirements.txt is missing. Please create it.")
    else:
        install_dependencies()
        run_services()
