def totalPrice(persons, breakfast = False):
    result = persons * 850 + breakfast * persons * 125
    return result
cena_vc_snidane = totalPrice(2, True)
cena_bez_snidane = totalPrice(2)
print(cena_vc_snidane)
print(cena_bez_snidane)


#def totalPrice(persons, breakfast=False):
  #if breakfast == True:
    #return persons * (850 + 125)
  #else:
    #return persons * 850

#cena_snidani = totalPrice(2, True)
#cena = totalPrice(2)


