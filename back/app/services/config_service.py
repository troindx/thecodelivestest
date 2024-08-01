import os

from dotenv import load_dotenv

class ConfigError(Exception):
    pass

class ConfigService:
    def __init__(self):
        load_dotenv()
        self.MONGODB_PORT = int(os.getenv("MONGODB_PORT"))
        self.MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
        self.MONGODB_USER = os.getenv("MONGODB_USER")
        self.MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
        self.MONGODB_HOST = os.getenv("MONGODB_HOST")
        self.validate_config()

    def get(self, key):
        return getattr(self, key)
        
    
    def validate_config(self):
        errors = []
        
        if not isinstance(self.MONGODB_HOST, str):
            errors.append("MONGODB_HOST must be a string.")
        
        try:
            self.port = int(self.MONGODB_PORT)
        except (ValueError, TypeError):
            errors.append("MONGODB_PORT must be a number.")
        
        if not isinstance(self.MONGODB_DATABASE_NAME, str):
            errors.append("MONGODB_DATABASE_NAME must be a string.")
        
        if not isinstance(self.MONGODB_USER, str):
            errors.append("MONGODB_USER must be a string.")
        
        if not isinstance(self.MONGODB_PASSWORD, str):
            errors.append("MONGODB_PASSWORD must be a string.")
        
        if errors:
            raise ConfigError("\n".join(errors))
    
    def get_config(self):
        return {
            'mongodb_host': self.MONGODB_HOST,
            'mongodb_port': self.MONGODB_PORT,
            'mongodb_database_name': self.MONGODB_DATABASE_NAME,
            'mongodb_user': self.MONGODB_USER,
            'mongodb_password': self.MONGODB_PASSWORD
        }
