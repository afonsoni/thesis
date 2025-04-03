import subprocess
import sys

def check_and_install_dependencies():
    dependencies = ["marker-pdf"]

    for dependency in dependencies:
        try:
            # Check if the dependency is available
            subprocess.run([dependency, "--help"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        except FileNotFoundError:
            print(f"Dependency '{dependency}' is not installed. Attempting to install...")
            if dependency == "marker-pdf":
                # Example installation command for marker-pdf
                subprocess.run([sys.executable, "-m", "pip", "install", "marker-pdf"], check=True)
                print(f"'{dependency}' has been installed.")
            else:
                print(f"Unable to install '{dependency}'. Please install it manually.")

if __name__ == "__main__":
    check_and_install_dependencies()
