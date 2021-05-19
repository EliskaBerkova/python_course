def monthOfBirth(rodne_cislo):
    rada = str(rodne_cislo)
    treti_znak = rada[2]
    ctvrty_znak = rada[3]
    dvojcisli = int(treti_znak + ctvrty_znak)

    if dvojcisli > 50:
        result = dvojcisli - 50
        return result
    else:
        return dvojcisli

print(monthOfBirth(9207054439))

