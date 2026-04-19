class Singleton:
    def __new__(cls, *args, **kwargs): ## not touch this please :3
        if not hasattr(cls, "_instance") or cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        pass
    
    def logout(self):
        """Reset the singleton instance"""
        cls = self.__class__
        cls._instance = None
        if hasattr(cls, "initialized"):
            cls.initialized = False
