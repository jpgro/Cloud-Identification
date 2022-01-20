''' Proyecto: Identificación de nubes mediante serie de preguntas '''
INICIAR = str(input(
'Quieres INICIAR o repetir la identificación de nubes? Responde S para SI y,  N para NO: '))
while INICIAR == 'S':
    #1. Definición de tipos y descripción de nube
    tipos_nubes=[['Cumulonimbus (Cb)',  'Nube en forma de enorme torre,  a veces con yunque. \
    Posibilidad de tormenta.'],
    ['Cúmulus (Cu)',  'Nube acampanada y separada de otras nubes,  con contornos bien delimitados'],
    ['Stratus (St) ',  'Capa gris blanquecina en el nivel bajo,  que puede generar \
    llovizna o granizo blanco. Cuando el Sol o la Luna son visibles,  su contorno está definido. \
    Puede estar formado por elementos separados. '],
    ['Cirrostratus (Cs) ',  'Velo nuboso transparente,  de aspecto blanquecino \
    o fibroso (de cabellos),  que cubre total o parcialmente el cielo,  \
    dando lugar al fenómeno de halo.'],
    ['Altostratus (As) ',  'Capa nubosa alargada y uniforme,  que cubre el cielo,  \
    dejando ver el Sol \
    o la Luna vagamente,  como a través de un vidrio deslustrado. '],
    ['Nimbostratus (Ns) ',  'Nube oscura de lluvia o nube clara de nieve. \
    Suele producir precipitaciones continuas de lluvia,  nieve o gránulos de hielo. '],
    ['Cirrus (Ci) ',  'Ganchos,  plumas,  bandas o bancos con un brillo sedoso. '],
    ['Cirrocumulus (Cc) ',  'Capa delgada de pequeños gránulos u ondas,  sin sombras propias,  \
    situados en el nivel alto y de anchura inferior a un grado. ' ],
    ['Altocumulus (Ac) ',  'Banco,  manto o capa estructurado de nubes blancas o grises (de \
    torreta,  lenticulares o aborregadas),  con ondulaciones o rodillos. Anchura: entre 1 - 3°. '],
    ['Stratocumulus (Sc) ',  'Banco,  manto o capa de nubes grises o blanquecinas,  con contornos \
    redondeados y situados en el nivel bajo. Elementos dispuestos de forma armoniosa. \
    Anchura: 5-10° (5 dedos). ' ]]

    #2.Identificación de nubes:
    print('\nPorfavor conteste las siguientes preguntas. Responde S para SI,  y N para NO:  ')
    PREGUNTA_1=(str(input('\nSe ven rayos o se oyen truenos? ')))
    if PREGUNTA_1 == 'S':
        TIPO_NUBE = tipos_nubes[0][0]
        DESCRIPCION_NUBE = (tipos_nubes[0][1])
        print('\nLa nube que ves es un: ',  TIPO_NUBE)
        print(DESCRIPCION_NUBE)
        INICIAR = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
    elif PREGUNTA_1 == 'N':
        PREGUNTA_2=(str(input('\n¿Tiene protuberancias o forma de cúpula? ')))
        if PREGUNTA_2=='S':
            PREGUNTA_3=(str(input('\nEn el nivel alto de la nube,  ¿es nítido el contorno? ')))
            if PREGUNTA_3=='S':
                TIPO_NUBE=(tipos_nubes[0][0])
                DESCRIPCION_NUBE=(tipos_nubes[0][1])
                print('\nLa nube que ves es un: ',  TIPO_NUBE)
                print(DESCRIPCION_NUBE)
                INICIAR = str(input('\nQuieres repetir el proceso? \
                Responde S para SI y N para NO: '))
            elif PREGUNTA_3=='N':
                TIPO_NUBE=(tipos_nubes[1][0])
                DESCRIPCION_NUBE=(tipos_nubes[1][1])
                print('\nLa nube que ves es un: ',  TIPO_NUBE)
                print(DESCRIPCION_NUBE)
                INICIAR = str(input('\nQuieres repetir el proceso? \
                Responde S para SI y N para NO: '))
        elif PREGUNTA_2=='N':
            PREGUNTA_4=(str(input('\nSe observa una capa continua o discontinua,  \
            sin rodillos ni elementos distintivos? ')))
            if PREGUNTA_4=='S':
                PREGUNTA_5=(str(input('\nAparecen el Sol o la Luna en forma de halo? ')))
                if PREGUNTA_5=='S':
                    TIPO_NUBE=(tipos_nubes[3][0])
                    DESCRIPCION_NUBE=(tipos_nubes[3][1])
                    print('\nLa nube que ves es un: ',  TIPO_NUBE)
                    print(DESCRIPCION_NUBE)
                    INICIAR = str(input('\nQuieres repetir el proceso? \
                    Responde S para SI y N para NO: '))
                elif PREGUNTA_5=='N':
                    PREGUNTA_6=(str(input('\n¿Se observa una capa alta en forma de lámina y \
                    de color entre grisáceo o azulado y gris oscuro? ')))
                    if PREGUNTA_6=='S':
                        TIPO_NUBE=(tipos_nubes[4][0])
                        DESCRIPCION_NUBE=(tipos_nubes[4][1])
                        print('\nLa nube que ves es un: ',  TIPO_NUBE)
                        print(DESCRIPCION_NUBE)
                        INICIAR = str(input('\nQuieres repetir el proceso? \
                        Responde S para SI y N para NO: '))
                    elif PREGUNTA_6=='N':
                        PREGUNTA_7 = (str(input('\n¿Hay una capa baja densa y \
                        alargada poco definida que puede generar precipitaciones? ')))
                        if PREGUNTA_7=='S':
                            TIPO_NUBE=(tipos_nubes[5][0])
                            DESCRIPCION_NUBE=(tipos_nubes[5][1])
                            print('\nLa nube que ves es un: ',  TIPO_NUBE)
                            print(DESCRIPCION_NUBE)
                            INICIAR = str(input('\nQuieres repetir el proceso? \
                            Responde S para SI y N para NO: '))
                        elif PREGUNTA_7=='N':
                            TIPO_NUBE=(tipos_nubes[2][0])
                            DESCRIPCION_NUBE=(tipos_nubes[2][1])
                            print('\nLa nube que ves es un: ',  TIPO_NUBE)
                            print(DESCRIPCION_NUBE)
                            INICIAR = str(input('\nQuieres repetir el proceso? \
                            Responde S para SI y N para NO: '))
            elif PREGUNTA_4=='N':
                PREGUNTA_8=(str(input('\nHay filamentos o fibras blancos y finos? ')))
                if PREGUNTA_8=='S':
                    TIPO_NUBE=(tipos_nubes[6][0])
                    DESCRIPCION_NUBE=(tipos_nubes[6][1])
                    print('\nLa nube que ves es un: ',  TIPO_NUBE)
                    print(DESCRIPCION_NUBE)
                    INICIAR = str(input('\nQuieres repetir el proceso? \
                    Responde S para SI y N para NO: '))
                elif PREGUNTA_8=='N':
                    PREGUNTA_9=(str(input('\nSon todos los elementos \
                    más pequeños que un dedo (brazo estirado)? ')))
                    if PREGUNTA_9=='s':
                        TIPO_NUBE=(tipos_nubes[7][0])
                        DESCRIPCION_NUBE=(tipos_nubes[7][1])
                        print('\nLa nube que ves es un: ',  TIPO_NUBE)
                        print(DESCRIPCION_NUBE)
                        INICIAR = str(input('\nQuieres repetir el proceso? \
                        Responde S para SI y N para NO: '))
                    elif PREGUNTA_9=='N':
                        PREGUNTA_10=(str(input('\n¿Son todos los elementos \
                        redondos del tamaño de 1 a 3 dedos? ')))
                        if PREGUNTA_10=='S':
                            TIPO_NUBE=(tipos_nubes[8][0])
                            DESCRIPCION_NUBE=(tipos_nubes[8][1])
                            print('\nLa nube que ves es un: ',  TIPO_NUBE)
                            print(DESCRIPCION_NUBE)
                            INICIAR = str(input('\nQuieres repetir el proceso? \
                            Responde S para SI y N para NO: '))
                        elif PREGUNTA_10=='N':
                            TIPO_NUBE=(tipos_nubes[9][0])
                            DESCRIPCION_NUBE=(tipos_nubes[9][1])
                            print('\nLa nube que ves es un: ',  TIPO_NUBE)
                            print(DESCRIPCION_NUBE)
                            INICIAR = str(input('\nQuieres repetir el proceso? \
                            Responde S para SI y N para NO: '))
    if INICIAR == 'N':
        print('Muchas gracias por utilizar el programa.')
    