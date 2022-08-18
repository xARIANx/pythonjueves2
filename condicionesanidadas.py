#condiciones anidadas elif

sensorNivelAgua = int (input("digite el nivel de agua actual: "))

if(sensorNivelAgua >=0 and sensorNivelAgua <20):
    print(f'PELIGRO el nivel de agua {sensorNivelAgua} es peligroso')
elif(sensorNivelAgua >=20 and sensorNivelAgua<400):
    print(f'Nivel de la represa ESTABLE {sensorNivelAgua}')
elif(sensorNivelAgua >=400):
    print(f'PELIGRO el nivel del agua {sensorNivelAgua} es MUY PELIGROSO')
else:
    print("el nivel del agua esta valida")