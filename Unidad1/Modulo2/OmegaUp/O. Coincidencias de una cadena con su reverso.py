def contar_coincidencias(s):
    s_reverso = s[::-1] 
    coincidencias = 0
    
    for i in range(len(s)):
        if s[i].lower() == s_reverso[i].lower():  
            coincidencias += 1
    
    return coincidencias

s = input().strip()  

print(contar_coincidencias(s))
