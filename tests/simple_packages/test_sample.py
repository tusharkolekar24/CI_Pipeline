import numpy as np
class StandardScaler:
    def __init__(self,arrys:list)->list:
        self.__array = arrys
        self.__string_filter = [vals for vals in self.__array if ((vals!='') & (type(vals)!=str) & (vals!=None))
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

def null_hypothesis(condition,solution):
    
    output = StandardScaler(condition)
    
    output_vals = output.get_transform()

    if output_vals==solution:
       return True
    
    if output_vals==solution:
       return False


case1 = [1,1.2,1.3,1.5,8,10]
case2 = [1,1.2,1.3,1.5,8,'10']
case3 = [2,3,4,None,'1st',5,10,'last']
case4 = [2,3,5,np.nan,None,2,6,'p']

solution1 = [-0.7654241625116108, -0.7113942216284384, -0.684379251186852, -0.6303493103036796, 1.1256237683994275, 1.6659231772311527]
solution2 = [-0.5915386614343725, -0.517596328755076, -0.4806251624154277, -0.4066828297361311, 1.9964429823410073]
solution3 = [-1.0051414220648331, -0.6461623427559642, -0.28718326344709516, 0.07179581586177387, 1.866691212406119]
solution4 = [-0.9847319278346619, -0.36927447293799825, 0.8616404368553291, -0.9847319278346619, 1.4770978917519928]


# test condition1
def test_samplecode1():
    assert null_hypothesis(case1,solution1)

# test condition2
def test_samplecode2():
    assert null_hypothesis(case2,solution2)

# test condition3
def test_samplecode3():
    assert null_hypothesis(case3,solution3)

# test condition4
def test_samplecode4():
    assert null_hypothesis(case4,solution4)
