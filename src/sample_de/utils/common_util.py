
import locale
import os

class common_util:
    """
    commonUtil is a utility class that provides common functionalities for the application.
    Returns:
        _type_: CommonUtil: A utility class providing common functionalities 
        such as retrieving the system's language locale and determining the chart storage path.
    """
    @staticmethod
    def getLangLocal():
        """
        Get Language Locale: Returns the language code (e.g., 'en' for English, 'fr' for French) based on the system's locale settings. If the locale is not set or is 'C', it defaults to 'en'.
        Returns:
            _type_: Language Code (str): The language code based on the system's locale settings.
        """
        lang_code, _ = locale.getlocale()
        return lang_code.split("_")[0] if (lang_code and lang_code != "C") else "en"

    @staticmethod
    def getChartPath():
        """
        Get Chart Path: Returns the path to the directory where charts are stored. It checks for an environment variable 'VISUALIZATION_PATH' and defaults to 'charts' if not set.
        Returns:
            _type_: Chart Path (str): The path to the directory where charts are stored.
        """
        chartPath = os.getenv("VISUALIZATION_PATH", "charts")
        os.makedirs(chartPath, exist_ok=True)
        return chartPath
    
