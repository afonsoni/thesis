"""
Utility for loading and accessing configuration settings from config.yaml
"""
import os
import yaml
from typing import Any, Dict, Optional

# Default config path (relative to the project root)
DEFAULT_CONFIG_PATH = "config/config.yaml"


class ConfigLoader:
    """
    Class for loading and accessing configuration settings
    """

    _instance = None
    _config = None

    def __new__(cls, config_path: Optional[str] = None):
        """
        Singleton pattern to ensure only one instance of ConfigLoader exists
        """
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config(config_path)
        return cls._instance

    def _load_config(self, config_path: Optional[str] = None):
        """
        Load configuration from the YAML file
        
        Args:
            config_path: Path to the config file (optional)
        """
        if config_path is None:
            # Get the absolute path to the config file
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            config_path = os.path.join(project_root, DEFAULT_CONFIG_PATH)
        
        try:
            with open(config_path, 'r') as config_file:
                self._config = yaml.safe_load(config_file)
            print(f"Configuration loaded from {config_path}")
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            self._config = {}
        except yaml.YAMLError as e:
            print(f"Error parsing config file: {e}")
            self._config = {}

    def get(self, path: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation path
        
        Args:
            path: Path to the configuration value (e.g., "milvus.host")
            default: Default value to return if the path doesn't exist
            
        Returns:
            The configuration value or the default value if not found
        """
        if self._config is None:
            return default
        
        # Split the path into parts
        parts = path.split('.')
        value = self._config
        
        # Navigate through the config dictionary
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        
        return value

    def get_dict(self, path: str = "", default: Dict = None) -> Dict:
        """
        Get a dictionary of configuration values
        
        Args:
            path: Path to the configuration section (e.g., "milvus")
            default: Default dictionary to return if the path doesn't exist
            
        Returns:
            Dictionary of configuration values or the default if not found
        """
        if default is None:
            default = {}
            
        value = self.get(path, default)
        if not isinstance(value, dict):
            return default
        return value

    def reload(self, config_path: Optional[str] = None):
        """
        Reload the configuration from the file
        
        Args:
            config_path: Path to the config file (optional)
        """
        self._load_config(config_path)


# Create a default instance for easy import
config = ConfigLoader()


if __name__ == "__main__":
    # Example usage
    print("Milvus Host:", config.get("milvus.host"))
    print("Embedding Model:", config.get("embeddings.model"))
    print("LLM Config:", config.get_dict("llm"))