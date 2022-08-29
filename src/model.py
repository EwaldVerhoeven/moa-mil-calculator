from typing import Literal

class Rifle:

    def __init__(self, 
                    caliber : str = None, 
                    rifle_brand : str = None, 
                    mount_type : str = None):
        self.caliber = caliber
        self.rifle_brand = rifle_brand
        self.mount_type = mount_type

class Scope(Rifle):

    def __init__(self,
                    caliber : str = None, 
                    rifle_brand : str = None, 
                    mount_type : str = None, 
                    scope_brand : str = None):
        super().__init__(caliber, rifle_brand, mount_type)
        self.scope_brand = scope_brand
        
class Calculation(Scope):

    def __init__(self, 
                    caliber : str = None, 
                    rifle_brand : str = None, 
                    mount_type : str = None, 
                    scope_brand : str = None, 
                    unit : Literal['metric','imperial'] = 'imperial', 
                    distance : int = 100):
        super().__init__(caliber, rifle_brand, mount_type, scope_brand)
        self.unit = unit
        self.distance = distance