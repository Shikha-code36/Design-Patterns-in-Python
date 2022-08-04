class FrenchLocalizer:   
  
    """ it simply returns the french version """  
  
    def __init__(self):   
  
        self.translations = {"car": "voiture", "bike": "bicyclette",   
                            "cycle":"cyclette"}   
  
    def localize(self, msg):   
  
        """change the message using translations"""  
        return self.translations.get(msg, msg)   
  
class SpanishLocalizer:   
    """it simply returns the spanish version"""  
  
    def __init__(self):   
  
        self.translations = {"car": "coche", "bike": "bicicleta",   
                            "cycle":"ciclo"}   
  
    def localize(self, msg):   
  
        """change the message using translations"""  
        return self.translations.get(msg, msg)   
  
class EnglishLocalizer:   
    """Simply return the same message"""  
  
    def localize(self, msg):   
        return msg   
  
if __name__ == "__main__":   
  
    # main method to call others   
    fr = FrenchLocalizer()   
    en = EnglishLocalizer()   
    sp = SpanishLocalizer()   
  
    # list of strings   
    message = ["car", "bike", "cycle"]   
  
    for msg in message:   
        print(fr.localize(msg))   
        print(en.localize(msg))   
        print(sp.localize(msg))  

'''
O/P--

voiture
car
coche
bicyclette
bike
bicicleta
cyclette
cycle
ciclo
'''