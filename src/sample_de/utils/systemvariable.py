import os
import json
from dotenv import load_dotenv

# 1. अपनी .env फाइल के वेरिएबल्स को लोड करें (यदि कोई हो)
class systemvariablemanager:
    """
    A class to manage system variables.
    """
    _instance = None  # Stores the single instance
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance if it doesn't exist yet
            cls._instance = super().__new__(cls)
            load_dotenv()  # Load environment variables from .env file
        return cls._instance

    def get_env(self, var_name,default: None = None):
        """Fetches the value of an environment variable.

        Args:
            var_name (str): The name of the environment variable.

        Returns:
            str: The value of the environment variable or None if not found.
        """
        return os.getenv(var_name, default)
    
    def get_all_env_variables(self):
        """Fetches all environment variables as a dictionary.

        Returns:
            dict: A dictionary containing all environment variables.
        """
        return json.dumps(dict(os.environ), indent=4)  # Return as formatted JSON string for better readability


if __name__ == "__main__":
    print("--- सभी एनवायरनमेंट वेरिएबल्स (Dictionary) ---")
    envVar = systemvariablemanager()
    all_vars = envVar.get_all_env_variables()    
    # साफ-सुथरे तरीके (Formatted JSON Layout) से प्रिंट करने के लिए:
    print(all_vars)
    print(envVar.get_env("PALETTE", 123))
