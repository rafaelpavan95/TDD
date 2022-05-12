class calculator:

    def add(self,x,y):

        if isinstance(x,str) or isinstance(y,str):
            
            raise TypeError('Can not be a string!')
        
        else: return x+y

    def subtract(self,x,y):

        if isinstance(x,str) or isinstance(y,str):
            
            raise TypeError('Can not be a string!')
        
        else: return x-y

    def multiply(self,x,y):

        if isinstance(x,str) or isinstance(y,str):

            raise TypeError('Can not be a string!')
        
        return x*y

    def divide(self,x,y):


        if isinstance(x,str) or isinstance(y,str):
            
            raise TypeError('Can not be a string!')
        
        else:
                
            if y == 0:
            
                raise ValueError('Can not divide by zero!')

            else: return x/y
