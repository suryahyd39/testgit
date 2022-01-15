def user_data(name,age,**kwargs):
     
    if kwargs.items():
        k_list=[]
        v_list=[]
        for k,v in kwargs.items():
            k_list.append(k)
            v_list.append(v)
        details=f'his name is {name} and his age is {age} and rest of the details are ',k ,v
        return details
    else:
        details=f'his name is {name} and his age is {age}'
        return details
        
            
            
         
        
        
    
details=user_data('surya',39,hometown='Hyd')

print(details)

details1=user_data('teja',20)
print(details1)