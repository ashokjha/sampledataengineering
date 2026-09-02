import json
from pathlib import Path

class TranslationManager:
    """ A class to manage translations for the application.
    It loads translation files from the 'locales' directory 
    and provides methods to fetch translated text based on the specified language.
    """
    
    _instance = None  # Stores the single instance
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance if it doesn't exist yet
            cls._instance = super().__new__(cls)
            cls.LOCALES_DIR = Path(__file__).resolve().parent.parent / 'locales'
            cls.translations_cache = cls._instance._load_all_translations()
        return cls._instance   

    def _load_all_translations(self):
        """Loads all translation files into memory and caches them. 

        Returns:
            _type_: returns a dictionary with language codes as keys and their corresponding translation dictionaries as values.
        """
        print("🔄 [SYSTEM] Loading translation files into memory...") 
        translations = {}   
        for lang in ['en', 'hi']:
            file_path = self.LOCALES_DIR / f"{lang}.json"
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    translations[lang] = json.load(f)
        return translations
    
    def get_text(self, key: str, lang: str = "en") -> str:
        """ Fetches the translated text for a given key and language. 
        If the translation for the specified language is not found, 
        it defaults to English.
        Args:
            key (str): _description_
            lang (str, optional): _description_. Defaults to "en".

        Returns:
            str: _description_
        """
        lang_dict = self.translations_cache.get(lang, self.translations_cache.get("en", {}))
        return lang_dict.get(key, key)
    
    def __str__(self):
        return f"TranslationManager(LOCALES_DIR='{self.LOCALES_DIR}')"
    
    def __repr__(self):
        return f"TranslationManager(LOCALES_DIR='{self.LOCALES_DIR}')"
    

