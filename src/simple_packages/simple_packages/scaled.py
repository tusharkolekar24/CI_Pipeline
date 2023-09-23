import numpy as np
class StandardScaler:
    def __init__(self,arrys:list)->list:
        self.__array = arrys
        self.__string_filter = [vals for vals in self.__array 
                                if ((vals!='') & (type(vals)!=str) & (vals!=None))
                               ]

        self.__remove_null   = [vals for vals in self.__string_filter 
                                if not((str(vals).lower()=='nan') & (type(vals)==float))
                               ]
        
    def get_transform(self):
        standard_deviation = np.array(self.__remove_null).std()
        mean_value         = np.array(self.__remove_null).mean()

        scaled_dataset =[ 
                        (vals-mean_value)/standard_deviation 
                        for vals in self.__remove_null
                        ]    
        
        return scaled_dataset