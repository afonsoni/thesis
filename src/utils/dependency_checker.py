import subprocess
import sys
import importlib.util

def check_and_install_dependencies():
    # Define dependencies with their pip package names (if different from import name)

    # Check config.yaml dependencies
    dependencies = {
        "psycopg2": "psycopg2",
        "sentence-transformers": "sentence-transformers",
        "markdown": "markdown",
    }

    for name, pip_package in dependencies.items():
        is_python_package = name in ["pymilvus", "sentence-transformers", "markdown"]
        
        if is_installed(name, is_python_package):
            print(f"'{name}' is already installed.")
        else:
            print(f"Dependency '{name}' is not installed. Attempting to install...")
            install_dependency(name, pip_package)

def is_installed(name, is_python_package):
    """Check if a dependency is installed."""
    try:
        if is_python_package:
            if name == "sentence-transformers":
                # Special case for sentence-transformers
                import_name = "sentence_transformers"
            else:
                import_name = name
                
            # Check if module can be imported
            if importlib.util.find_spec(import_name) is None:
                return False
        else:
            # For command line tools, check if they're available
            subprocess.run([name, "--help"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        return True
    except (ImportError, ModuleNotFoundError, subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_dependency(name, pip_package):
    """Install a dependency using pip."""
    try:
        # Use upgrade flag for certain packages
        if name in ["pymilvus", "sentence-transformers"]:
            subprocess.run([sys.executable, "-m", "pip", "install", "-U", pip_package], check=True)
        else:
            subprocess.run([sys.executable, "-m", "pip", "install", pip_package], check=True)
        
        print(f"'{name}' has been installed.")
    except subprocess.CalledProcessError:
        print(f"Unable to install '{name}'. Please install it manually.")

if __name__ == "__main__":
    check_and_install_dependencies()
