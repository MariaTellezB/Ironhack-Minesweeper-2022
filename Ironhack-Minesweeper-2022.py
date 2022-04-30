import numpy as np
import random
import os



#función para abrir cumulos de ceros------------------------------------------------------------------------------
def abrir_ceros(fila_usu,col_usu):#función que abrirá el tablero cuando toque aglomeración de ceros
    abrir_casilla(fila_usu,col_usu)#Abre la casilla que fue la primera seleccionada
    ar,ab,iz,de,arf,abf,izf,derf=revisar_casillas(col_usu,fila_usu)#llama a la función para revisar si existen casillas arriba, abajo, der, iz
    
    
    if ar == True:#Si existe casilla ariiba
        if arf=='C':#Si la casilla se encuentra cerrada en las flags
            if board[fila_usu-1][col_usu]!='0' and board[fila_usu-1][col_usu]!='x'  :#Si el número  es [1-8] 
                abrir_casilla(fila_usu-1,col_usu)#abir la casilla
            else:
                abrir_ceros(fila_usu-1,col_usu)

    if ab == True:#Si existe casilla abajo
        if abf=='C':#Si la casilla se encuentra cerrada en las flags
            if board[fila_usu+1][col_usu]!='0' and board[fila_usu+1][col_usu]!='x' :#Si el número  es [1-8]  
                abrir_casilla(fila_usu+1,col_usu)#abrir la casilla
            else:
                abrir_ceros(fila_usu+1,col_usu)    
                
                
                
    if iz == True:#Si existe casilla izquierda
        if izf=='C':#Si la casilla se encuentra cerrada en las flags
            if board[fila_usu][col_usu-1]!='0' and board[fila_usu][col_usu-1]!='x' :#Si el número  es [1-8] 
                abrir_casilla(fila_usu,col_usu-1)#abrir la casilla
            else:
                abrir_ceros(fila_usu,col_usu-1)   
                
                
                
    if de == True:#Si existe casilla derecha
        if derf=='C':#Si la casilla se encuentra cerrada en las flags
            if board[fila_usu][col_usu+1]!='0' and board[fila_usu-1][col_usu+1]!='x' :#Si el número  es [1-8]  
                abrir_casilla(fila_usu,col_usu+1)#abrir la casilla
            else:
                abrir_ceros(fila_usu,col_usu+1)
#-----------------------------------------------------------------------------------------------------------------

#funciones que revisan si nos encontramos dentro de indices para abrir tablero------------------------------------
def revisar_casilla_arriba(col_usu,fila_usu):#Revisa si la casilla arriba de la selección se encuentra en unn indica válido
    if (fila_usu-1)>=0:
        return True
    
def revisar_casilla_abajo(col_usu,fila_usu):#---abajo---
    if fila_usu+1<=tamaño-1:
        return True
    
def revisar_casilla_derecha(col_usu,fila_usu):#---derecha---
    if col_usu+1<=tamaño-1:
        return True
    
def revisar_casilla_izquierda(col_usu,fila_usu):#---izqueirda---
    if col_usu-1>=0:
        return True
#------------------------------------------------------------------------------------------------------------------

#función que revisar las 4 direcciones para asegurar indices existentes y status en el tablero de banderas---------
def revisar_casillas(col_usu,fila_usu):
    ar=revisar_casilla_arriba(col_usu,fila_usu)
    if ar == True:#si la casilla de arriba se encuentra en un indice válido
        arf=board_flags[fila_usu-1][col_usu] 
    else:
        arf='v'
    ab=revisar_casilla_abajo(col_usu,fila_usu)
    if ab ==True:
        abf=board_flags[fila_usu+1][col_usu]
    else:
        abf='v'
    iz=revisar_casilla_izquierda(col_usu,fila_usu)
    if iz == True:
        izf=board_flags[fila_usu][col_usu-1]
    else:
        izf='v'
    de=revisar_casilla_derecha(col_usu,fila_usu)
    if de == True:
        derf=board_flags[fila_usu][col_usu+1]
    else:
        derf='v'
    return(ar,ab,iz,de,arf,abf,izf,derf)
#------------------------------------------------------------------------------------------------------------------

#Función para abrir casillas individuales y cambiar bandera en board_flags------------------------------------------
def abrir_casilla(fila_usu,col_usu): #función abrir una casilla
    board_player[fila_usu][col_usu]=board[fila_usu][col_usu]#Mostrar el valor de board[fila_usu][col_usu] en board_flags[fila_usu][col_usu]
    board_flags[fila_usu][col_usu]='A'#Cambiar el estado de la bandera a Abierto (A)
    os.system('cls||clear')#limpiar terminal
#--------------------------------------------------------------------------------------------------------------------

#funciónes para hacer el conteo de las minas que rodean a cada casilla---------------------------------------------
def contar_mina_arriba(fila, col):
    if board[fila-1][col]=='x':
        return 1
    else:
        return 0
    
    
#abajo
def contar_mina_abajo(fila, col):
    if board[fila+1][col]=='x':
        return 1
    else:
        return 0
    

#derecha
def contar_mina_derecha(fila, col):
    if board[fila][col+1]=='x':
        return 1
    else:
        return 0
    

#izquierda
def contar_mina_izquierda(fila, col):
    if board[fila][col-1]=='x':
        return 1
    else:
        return 0
    
    
    
#arriba derecha
def contar_mina_arriba_derecha(fila, col):
    if board[fila-1][col+1]=='x':
        return 1
    else:
        return 0
    
    
    
    
#arriba izquierda
def contar_mina_arriba_izquierda(fila, col):
    if board[fila-1][col-1]=='x':
        return 1
    else:
        return 0
    
    
    
#abajo derecha
def contar_mina_abajo_derecha(fila, col):
    if board[fila+1][col+1]=='x':
        return 1
    else:
        return 0
    
    
    
    
#abajo izquierda
def contar_mina_abajo_izquierda(fila, col):
    if board[fila+1][col-1]=='x':
        return 1
    else:
        return 0
#--------------------------------------------------------------------------------------------------------------------

#Función para perder la partida-------------------------------------------------------------------------------------
def perder_partida():
    global ref
    global stop_in#referencia de apoyo para dejar de pedir inputs global
    stop_in=False#cambiamos el valor de la referencia, para que deje de pedir inputs porque perdimos
    os.system('cls||clear')
    print('You Died')
    re=play_again()
    if re==1:
        ref=True
    else:
        ref=False
#------------------------------------------------------------------------------------------------------------------

#Función para inicializar tablero-----------------------------------------------------------------------------------
def iniciar_tablero(tamaño, minas):
    #
#####

    minas_col=[]#arreglo vacio para coordenadas x de minas que se ponran en el tablero
    minas_fil=[]#arreglo vacio para coordenadas y de minas que se ponran en el tablero
    for mm in range(minas):#for de 0 hasta el número asignado para minas al elegir dificultad
        colu = random.randint(0, tamaño-1)#creación de número random para coordenada x
        filas = random.randint(0, tamaño-1)#creación de número random para coordenada y
        minas_col.append(colu)#Añadimos la coordenada x a la lista de coordenadas
        minas_fil.append(filas)#Añadimos la coordenada y a la lista de coordenadas
    lista_minas=[]#Creamos una lista que contendrá las listas de coordenadas
    for m in range (minas):#Para cda una de las minas creadas
        coordenadas=[minas_col[m],minas_fil[m]]#Crear una lista aux que se formará de [coordx.coordy]
        lista_minas.append(coordenadas)#añadir la lista a la lista de minas
    #print(lista_minas)
    #print(lista_minas)   

    for mines in range (0,minas):#Para cada una de las minas
        board[lista_minas[mines][1]][lista_minas[mines][0]]='x'#Coloca minas en el tablero board
       # print(f'minas colocadas en {minas_x[mines]},{[minas_y[mines]]}')
    #print(board)
    #contminas=0
    #for fila in range(0,tamaño): 
    #    for col in range (0,tamaño):
    #        if board[fila][col]=='x':
    #            contminas=contminas+1            
    #print(contminas)

    #Cuenta el números de minas rodeando a cada casilla--------------------------------------------------------------
    #--------Parte central---------------------------------------
    for fila in range(1,tamaño-1): 
        for col in range (1,tamaño-1):
            cont=0
            if board[fila][col]=='-':
                aux=contar_mina_arriba(fila,col)
                cont=cont+aux

                aux=contar_mina_abajo(fila,col)
                cont=cont+aux

                aux=contar_mina_derecha(fila,col)
                cont=cont+aux

                aux=contar_mina_izquierda(fila,col)
                cont=cont+aux

                aux=contar_mina_arriba_derecha(fila,col)
                cont=cont+aux

                aux=contar_mina_arriba_izquierda(fila,col)
                cont=cont+aux

                aux=contar_mina_abajo_derecha(fila,col)
                cont=cont+aux

                aux=contar_mina_abajo_izquierda(fila,col)
                cont=cont+aux

                board[fila][col]=str(cont)
    #----------4 Esquinas-------------------------------------
    if board[0][0]=='-':
        cont_esquina=0
        cont_esquina=cont_esquina+contar_mina_derecha(0,0)
        cont_esquina=cont_esquina+contar_mina_abajo(0,0)
        cont_esquina=cont_esquina+contar_mina_abajo_derecha(0,0)
        board[0][0]=str(cont_esquina)

    if board[tamaño-1][0]=='-':
        cont_esquina=0
        cont_esquina=cont_esquina+contar_mina_arriba(tamaño-1,0)
        cont_esquina=cont_esquina+contar_mina_derecha(tamaño-1,0)
        cont_esquina=cont_esquina+contar_mina_arriba_derecha(tamaño-1,0)
        board[tamaño-1][0]=str(cont_esquina)

    if board[0][tamaño-1]=='-':
        cont_esquina=0
        cont_esquina=cont_esquina+contar_mina_izquierda(0,tamaño-1)
        cont_esquina=cont_esquina+contar_mina_abajo(0,tamaño-1)
        cont_esquina=cont_esquina+contar_mina_abajo_izquierda(0,tamaño-1)
        board[0][tamaño-1]=str(cont_esquina)


    if board[tamaño-1][tamaño-1]=='-':
        cont_esquina=0
        cont_esquina=cont_esquina+contar_mina_izquierda(tamaño-1, tamaño-1)
        cont_esquina=cont_esquina+contar_mina_arriba(tamaño-1, tamaño-1)
        cont_esquina=cont_esquina+contar_mina_arriba_izquierda(tamaño-1, tamaño-1)
        board[tamaño-1][tamaño-1]=str(cont_esquina)
    #-----------Perimetro arriba y abajo-----------
    ladoshor=[0,tamaño-1]
    for index in ladoshor:
        for lado1 in range (1,tamaño-1): #lado arriba
            if index==0:
                if board[index][lado1]=='-':
                    contlado=0
                    contlado=contlado+contar_mina_izquierda(index,lado1)
                    contlado=contlado+contar_mina_derecha(index,lado1)
                    contlado=contlado+contar_mina_abajo(index, lado1)
                    contlado=contlado+contar_mina_abajo_derecha(index, lado1)
                    contlado=contlado+contar_mina_abajo_izquierda(index, lado1)
                    board[index][lado1]=str(contlado)
            else:
                if board[index][lado1]=='-':
                    contlado=0
                    contlado=contlado+contar_mina_izquierda(index,lado1)
                    contlado=contlado+contar_mina_derecha(index,lado1)
                    contlado=contlado+contar_mina_arriba(index, lado1)
                    contlado=contlado+contar_mina_arriba_derecha(index, lado1)
                    contlado=contlado+contar_mina_arriba_izquierda(index, lado1)
                    board[index][lado1]=str(contlado)
    #--------------Perimetro derecha e izquierda-------------
    ladoshor=[0,tamaño-1]
    for lado1 in range (1,tamaño-1):
        for index in ladoshor:
            if index==0:
                if board[lado1][index]=='-':
                    contlado=0
                    contlado=contlado+contar_mina_arriba(lado1,index)
                    contlado=contlado+contar_mina_abajo(lado1,index)
                    contlado=contlado+contar_mina_derecha(lado1,index)
                    contlado=contlado+contar_mina_abajo_derecha(lado1,index)
                    contlado=contlado+contar_mina_arriba_derecha(lado1,index)
                    board[lado1][index]=str(contlado)
            else:
                if board[lado1][index]=='-':
                    contlado=0
                    contlado=contlado+contar_mina_arriba(lado1,index)
                    contlado=contlado+contar_mina_abajo(lado1,index)
                    contlado=contlado+contar_mina_izquierda(lado1,index)
                    contlado=contlado+contar_mina_abajo_izquierda(lado1,index)
                    contlado=contlado+contar_mina_arriba_izquierda(lado1,index)
                    board[lado1][index]=str(contlado)
    print(board)
    print('\n')
    print(board_player)
    #print('\n')
    #print(board_flags)
    return lista_minas
#llenado del tablero terminado, toda la info está en el tablero board------------------------------------------------

#Función para abrir tablero-----------------------------------------------------------------------------------------
def abrir_tab(fila_usu, col_usu):
    if (board[fila_usu][col_usu]!='0' and board[fila_usu][col_usu]!='x'): #Si la selección no es ni un cero ni una mina (numeros entre el 1 y 8)
        #print('No es 0 ni x')#print de ayuda, se eliminará
        if board_flags[fila_usu][col_usu]=='C':#Si la selección, tiene un status de cerrado (C) en board_flags
            abrir_casilla(fila_usu,col_usu) #llama a funcion abir_casilla fila, col
        else:#Si la casilla ya tiene el estatus abierto (A) en borad_flags
            #print('esa casilla ya fue abierta')#La casilla ya fue abierta
            pass
    else:#caso si es 0 en el tablero board, 0 minas en las casilas , deberá abrir todos los 0 adyacentes(recursivo a todos los 0 que encuentre) caso si es x, metodo perder
        if board[fila_usu][col_usu]=='x':#Si es mina, llamar a la funcion terminar juego, permios el juego
            board_player[fila_usu][col_usu]=board[fila_usu][col_usu]#Mostrar la mina que nos hizo perder
            perder_partida()#Llamar a función perder partida
        elif board[fila_usu][col_usu]=='0':#Si la casilla seleccionada tiene un 0
            #revisar si la casilla está abierta o no
            if board_flags[fila_usu][col_usu]=='A':#Si la casilla ya fue abierte
                board_player[fila_usu][col_usu]=board[fila_usu][col_usu]#Solo volver a pasar el valo de board a board_player
            elif board_flags[fila_usu][col_usu]=='C':#Si la casilla se encuentra cerrada en board_flags
                abrir_ceros(fila_usu,col_usu)#llamamos  a la función para abrir ceros


    #print(board)
    #print('\n')
    print(board_player)
    #print('\n')
    #print(board_flags)
    
    return;
#------------------------------------------------------------------------------------------------------------------

#función de selección de dificultad-----------------------------------------------------------------------------
def seleccion_dif():
    dif=input('Choose your dificulty: 1:7x7 | 2:14x14 | 3:20x20: ')#selección de dificultad
    if dif not in ['1','2','3']:
        return seleccion_dif()
    return dif
#.................................................................................................................

#función de selección de marcar o abrir-----------------------------------------------------------------------------
def mark_open():
    action=input('To open a square: 1  |  To mark a mine:2  |  To desmark all mines:3:  ')#selección de acción
    if action not in ['1','2','3']:
        return mark_open()
    return action
#.................................................................................................................

#Función para verificar si ya se ganó------------------------------------------------------------------------------
def verificar_ganar(lista_minas_limpia, lista_minas_usu):
    global stop_in#referencia global para dejar de pedir inputs
    global ref
    if lista_minas_usu==lista_minas_limpia:#Si la lista limpia de minas es igual a la lista del usuario
        stop_in=False#cambiar referencia para dejar de pedir inputs
        os.system('cls||clear')
        print('You Win')
        re=play_again()
        if re==1:
            ref=True
        else:
            ref=False
    return;
#------------------------------------------------------------------------------------------------------------------

#voler a jugar----------------------------------------------------------------------------------------------------
def play_again():
    play=input('Do you want to play again? 1-Yes 2-No:'  )#selección de acción
    if play not in ['1','2']:
        return play_again()
    return int(play)
#------------------------------------------------------------------------------------------------------------------





ref=True
while ref==True:
    print('Welcome to IronHack Minesweeper 2022\n')# mensaje de bienvenida

    dif=seleccion_dif()
    dif=int(dif)#convertimos la dif a un enter
    if dif==1:#si dif ==1
        tamaño=7#tamaño del tablero 7x7
        minas=8#número de minas
    elif dif==2:#si dif==2
        tamaño=14#tamaño del tablero 14x14
        minas=30#Número de minas
    elif dif==3:#Si dif==3
        tamaño=20#Tamaño del tablero 20x20
        minas=63#número de minas
    board=np.full((tamaño, tamaño), '-')#Se crea un tablero "vacio", este se llenará de minas y números pero no se muestra al jugador
    board_player=np.full((tamaño, tamaño), '-')#Tablero vacio que se muestra al jugador, mientras se juegue se mostrará las partes abiertas al jugador
    board_flags=np.full((tamaño, tamaño), 'C')#Tablero de banderas, indica si una posición del tablero está Abierta(A) o cerrada(C) a la vista del jugador    

    lista_minas=iniciar_tablero(tamaño, minas)#Función para crear tablero
    lista_minas=sorted(lista_minas)#ordenar la lista de minas para hacer la comparación más facil



    lista_minas_limpia = []
    for item in lista_minas:
        if item not in lista_minas_limpia:
            lista_minas_limpia.append(item)

    print(lista_minas_limpia)

    stop_in=True#Valor de referencia para seguir pidiendo inputs
    lista_minas_usu=[]
    while stop_in==True:#lo hará mientras el valor de referencia no cambie

        action=int(mark_open())#Definir la acción del jugador: 1-marcar mina 2-abrir tablero

        if action==1:
            col_usu=input('Columna de la casilla a abrir: ')#columna
            col_usu=int(col_usu)-1

            fila_usu=input('Fila de la casilla a abrir: ')#fila
            fila_usu=int(fila_usu)-1

            abrir_tab(fila_usu,col_usu)
        elif action==2:
            colm_usu=int(input('Columna de la mina a marcar: '))#columna
            filam_usu=int(input('Fila de la mina a marcar: '))#fila   
            board_player[filam_usu-1][colm_usu-1]='P'
            board_flags[filam_usu-1][colm_usu-1]='A'
            print(board_player)
            lista_coord_in=[colm_usu-1,filam_usu-1]
            lista_minas_usu.append(lista_coord_in)
            lista_minas_usu=sorted(lista_minas_usu)
            verificar_ganar(lista_minas_limpia, lista_minas_usu)
            print(f'lista minas usu{lista_minas_usu}')
        else:
            for jlista in (lista_minas_usu):
            #    print(board_player[jlista[1]][jlista[0]])
                board_player[jlista[1]][jlista[0]]='-'
                board_flags[jlista[1]][jlista[0]]='C'
            lista_minas_usu=[]    
          #  print(f'lista minas usu{lista_minas_usu}')        
