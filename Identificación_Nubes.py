iniciar = str(input('Quieres iniciar o repetir la identificación de nubes? Responde S para SI y N para NO: '))
while iniciar == 'S': 
    #1. Definición de tipos y descripción de nube
    tipos_nubes=[['Cumulonimbus (Cb)', 'Nube en forma de enorme torre, a veces con yunque. Posibilidad de tormenta.'], 
    ['Cúmulus (Cu)', 'Nube acampanada y separada de otras nubes, con contornos bien delimitados'], 
    ['Stratus (St) ', 'Capa gris blanquecina en el nivel bajo, que puede generar llovizna o granizo blanco. Cuando el Sol o la Luna son visibles, su contorno está definido. Puede estar formado por elementos separados. '], 
    ['Cirrostratus (Cs) ', 'Velo nuboso transparente, de aspecto blanquecino o fibroso (de cabellos), que cubre total o parcialmente el cielo, dando lugar al fenómeno de halo.'], 
    ['Altostratus (As) ', 'Capa nubosa alargada y uniforme, que cubre el cielo, dejando ver el Sol o la Luna vagamente, como a través de un vidrio deslustrado. '], 
    ['Nimbostratus (Ns) ', 'Nube oscura de lluvia o nube clara de nieve. Suele producir precipitaciones continuas de lluvia, nieve o gránulos de hielo. '], 
    ['Cirrus (Ci) ', 'Ganchos, plumas, bandas o bancos con un brillo sedoso. '], 
    ['Cirrocumulus (Cc) ', 'Capa delgada de pequeños gránulos u ondas, sin sombras propias, situados en el nivel alto y de anchura inferior a un grado. ' ], 
    ['Altocumulus (Ac) ', 'Banco, manto o capa estructurado de nubes blancas o grises (de torreta, lenticulares o aborregadas), con ondulaciones o rodillos. Anchura: entre 1 - 3°. '], 
    ['Stratocumulus (Sc) ', 'Banco, manto o capa de nubes grises o blanquecinas, con contornos redondeados y situados en el nivel bajo. Elementos dispuestos de forma armoniosa. Anchura: 5-10° (5 dedos). ' ]]
        

    #2.Identificación de nubes:
    print('\nPorfavor conteste las siguientes preguntas. Responde S para SI, y N para NO:  ')
    pregunta_1=(str(input('\nSe ven rayos o se oyen truenos? ')))
    if pregunta_1 == 'S': 
        tipo_nube = tipos_nubes[0][0]
        descripcion_nube = (tipos_nubes[0][1])
        print('\nLa nube que ves es un: ', tipo_nube)
        print(descripcion_nube)
        iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
    elif pregunta_1 == 'N':
        pregunta_2=(str(input('\n¿Tiene protuberancias o forma de cúpula? ')))
        if pregunta_2=='S':
            pregunta_3=(str(input('\nEn el nivel alto de la nube, ¿es nítido el contorno? ')))
            if pregunta_3=='S':
                tipo_nube=(tipos_nubes[0][0])
                descripcion_nube=(tipos_nubes[0][1])
                print('\nLa nube que ves es un: ', tipo_nube)
                print(descripcion_nube)
                iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
            elif pregunta_3=='N':
                tipo_nube=(tipos_nubes[1][0])
                descripcion_nube=(tipos_nubes[1][1])
                print('\nLa nube que ves es un: ', tipo_nube)
                print(descripcion_nube)
                iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
        elif pregunta_2=='N':
            pregunta_4=(str(input('\nSe observa una capa continua o discontinua, sin rodillos ni elementos distintivos? ')))
            if pregunta_4=='S':
                pregunta_5=(str(input('\nAparecen el Sol o la Luna en forma de halo? ')))
                if pregunta_5=='S':
                    tipo_nube=(tipos_nubes[3][0])
                    descripcion_nube=(tipos_nubes[3][1])
                    print('\nLa nube que ves es un: ', tipo_nube)
                    print(descripcion_nube)
                    iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                elif pregunta_5=='N':
                    pregunta_6=(str(input('\n¿Se observa una capa alta en forma de lámina y de color entre grisáceo o azulado y gris oscuro? ')))
                    if pregunta_6=='S':
                        tipo_nube=(tipos_nubes[4][0])
                        descripcion_nube=(tipos_nubes[4][1])
                        print('\nLa nube que ves es un: ', tipo_nube)
                        print(descripcion_nube) 
                        iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                    elif pregunta_6=='N':
                        pregunta_7 = (str(input('\n¿Hay una capa baja densa y alargada poco definida que puede generar precipitaciones? ')))
                        if pregunta_7=='S':
                            tipo_nube=(tipos_nubes[5][0])
                            descripcion_nube=(tipos_nubes[5][1])
                            print('\nLa nube que ves es un: ', tipo_nube)
                            print(descripcion_nube)
                            iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                        elif pregunta_7=='N':
                                tipo_nube=(tipos_nubes[2][0])
                                descripcion_nube=(tipos_nubes[2][1])
                                print('\nLa nube que ves es un: ', tipo_nube)
                                print(descripcion_nube)
                                iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
            elif pregunta_4=='N':
                pregunta_8=(str(input('\nHay filamentos o fibras blancos y finos? ')))
                if pregunta_8=='S':
                    tipo_nube=(tipos_nubes[6][0])
                    descripcion_nube=(tipos_nubes[6][1])
                    print('\nLa nube que ves es un: ', tipo_nube)
                    print(descripcion_nube)
                    iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                elif pregunta_8=='N':
                    pregunta_9=(str(input('\nSon todos los elementos más pequeños que un dedo (brazo estirado)? ')))
                    if pregunta_9=='s':
                        tipo_nube=(tipos_nubes[7][0])
                        descripcion_nube=(tipos_nubes[7][1])
                        print('\nLa nube que ves es un: ', tipo_nube)
                        print(descripcion_nube)
                        iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                    elif pregunta_9=='N':
                        pregunta_10=(str(input('\n¿Son todos los elementos redondos del tamaño de 1 a 3 dedos? ')))
                        if pregunta_10=='S':
                            tipo_nube=(tipos_nubes[8][0])
                            descripcion_nube=(tipos_nubes[8][1])
                            print('\nLa nube que ves es un: ', tipo_nube)
                            print(descripcion_nube)
                            iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
                        elif pregunta_10=='N':
                            tipo_nube=(tipos_nubes[9][0])
                            descripcion_nube=(tipos_nubes[9][1])
                            print('\nLa nube que ves es un: ', tipo_nube)
                            print(descripcion_nube)
                            iniciar = str(input('\nQuieres repetir el proceso? Responde S para SI y N para NO: '))
    if iniciar == 'N': 
        print('Muchas gracias por utilizar el programa.')
    
    