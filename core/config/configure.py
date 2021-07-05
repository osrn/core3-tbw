import configparser

class Configure:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.static(config)
        self.delegate(config)
        self.payment(config)
        self.experimental(config)
        
        
    def static(self, config):
        self.atomic = config.get('static', 'atomic')
        print(atomic)
    
    
    def delegate(self):
        pass
    
    
    def payment(self):
        pass
    
    
    def experimental(self):
        pass
