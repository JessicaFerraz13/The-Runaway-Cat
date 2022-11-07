from graphics import *
import random

def main():

    win = GraphWin('The Runaway Cat', 1000, 600, autoflush = False)

    Fundo_inicio = Image(Point(500, 300), 'Inicio.png')
    Fundo_inicio.draw(win)

    Logo = Image(Point(500, 250), "The Runaway Cat.png")
    Logo.draw(win)

    Inicio = Image(Point(500, 450), 'Pressione.png')
    Inicio.draw(win)

    rate = 24

    movimento = 14
    movimento_carro = movimento*2.5
    
    while True:
        key = win.checkKey()

        if key != '':
            break

    Fundo = []
    
    for i in range(0, 8):
        Fundo.append(Image(Point(i * 4480 + 2240, 300), 'fundo.png'))
        Fundo[i].draw(win)

    Comprimento_do_fundo = len(Fundo) * 4480

    Fundo_inicio.undraw()
    Logo.undraw()
    Inicio.undraw()

    Menino_correndo = ['sprite_1.png', 'sprite_2.png', 'sprite_3.png', 'sprite_2.png', 'sprite_4.png']
    Menino_pulando = 'sprite_5.png'
    Menino_parado = ['sprite_1.png', 'sprite_1.png', 'sprite_1.png', 'sprite_1.png', 'sprite_1.png', 'sprite_1.png', 'sprite_1.1.png', 'sprite_1.1.png', 'sprite_1.1.png', 'sprite_1.1.png', 'sprite_1.1.png', 'sprite_1.1.png']
    Gato_sentado = ['Idle_cat_1.png', 'Idle_cat_1.png', 'Idle_cat_2.png', 'Idle_cat_2.png', 'Idle_cat_3.png', 'Idle_cat_3.png', 'Idle_cat_4.png', 'Idle_cat_4.png', 'Idle_cat_3.png', 'Idle_cat_3.png', 'Idle_cat_2.png', 'Idle_cat_2.png']
    Gato_levantando = ['gato_levantando_1.png', 'gato_levantando_2.png', 'gato_levantando_3.png', 'gato_levantando_4.png', 'gato_levantando_5.png', 'gato_levantando_6.png']
    Gato_correndo = ['gato_correndo_1.png', 'gato_correndo_2.png', 'gato_correndo_3.png', 'gato_correndo_4.png']
    Carro1 = ['Carro1.1.png', 'Carro1.2.png']
    Carro2 = ['Carro2.1.png', 'Carro2.2.png']
    Carro3 = ['Carro3.1.png', 'Carro3.2.png']
    Carro4 = ['Carro4.1.png', 'Carro4.2.png']
    Colisoes = ['colisao 1.png', 'colisao 1.png', 'colisao 2.png', 'colisao 2.png', 'colisao 3.png', 'colisao 3.png', 'colisao 4.png', 'colisao 4.png', 'colisao 5.png', 'colisao 5.png', 'colisao 6.png', 'colisao 6.png']
    Lista_de_carros = [Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4, Carro1, Carro2, Carro3, Carro4]

    cones = random.sample(range(1200, Comprimento_do_fundo - 1400, 500), 44)
    carros = random.sample(range(2000, int(Comprimento_do_fundo * 2.2), 1000), 40)

    Cones = []
    Carros = []

    for i in range(0, len(cones)):
        posicao_cones = random.randint(1, 2)

        if posicao_cones == 1:
            Cones.append(Image(Point(cones[i], 470), 'cone.png'))

        else:
            Cones.append(Image(Point(cones[i], 545), 'cone.png'))

        Cones[i].draw(win)

    for i in range(0, len(carros)):
        posicao_carros = random.randint(1, 2)

        if posicao_carros == 1:
            Carros.append(Image(Point(carros[i], 440), Lista_de_carros[i][0]))

        else:
            Carros.append(Image(Point(carros[i], 515), Lista_de_carros[i][0]))

        Carros[i].draw(win)

    Proxima_Imagem_Carro = 0

    def MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino):

        Proxima_Imagem = (Proxima_Imagem + 1) % len(Menino_parado)
        Menino.undraw()
        Menino = Image(Centro_do_menino, Menino_parado[Proxima_Imagem])
        Menino.draw(win)

        return Proxima_Imagem, Menino

    def GatoParado(Proxima_Imagem_Gato, Gato_sentado, Gato, Centro_do_gato):

        Proxima_Imagem_Gato = (Proxima_Imagem_Gato + 1) % len(Gato_sentado)
        Gato.undraw()
        Gato = Image(Centro_do_gato, Gato_sentado[Proxima_Imagem_Gato])
        Gato.draw(win)

        return Proxima_Imagem_Gato, Gato

    def MeninoCorrendo(Proxima_Imagem, Menino_correndo, Menino, Centro_do_menino):

        Proxima_Imagem = (Proxima_Imagem + 1) % len(Menino_correndo)
        Menino.undraw()
        Menino = Image(Centro_do_menino, Menino_correndo[Proxima_Imagem])
        Menino.draw(win)

        return Proxima_Imagem, Menino

    def GatoCorrendo(Proxima_Imagem_Gato, Gato_correndo, Gato, Centro_do_gato):

        Proxima_Imagem_Gato = (Proxima_Imagem_Gato + 1) % len(Gato_correndo)
        Gato.undraw()
        Gato = Image(Centro_do_gato, Gato_correndo[Proxima_Imagem_Gato])
        Gato.draw(win)

        return Proxima_Imagem_Gato, Gato

    def MeninoPulando(Menino, Centro_do_menino, Menino_pulando, Menino_em_cima, Fundo, Cones, movimento, Proxima_Imagem_Carro, Carros, Lista_de_carros, Posicao_no_fundo, rate, Colisoes):

        velocidade = 60
        Menino.undraw()
        Menino = Image(Centro_do_menino, Menino_pulando, )
        Menino.draw(win)

        while velocidade > 0:

            velocidade = velocidade - 10

            if Menino_em_cima:
                Menino.move(0, - velocidade)
                Centro_do_menino = Menino.getAnchor()
                Menino.undraw()
                Menino = Image(Centro_do_menino, Menino_pulando)
                Menino.draw(win)

            for i in range(0, len(Fundo)):
                Fundo[i].move(-movimento, 0)

            for i in range(0, len(Cones)):
                Cones[i].move(-movimento, 0)

            Proxima_Imagem_Carro = (Proxima_Imagem_Carro + 1) % len(Carro1)
                
            for i in range(0, len(Carros)):
                Carros[i].move(-movimento_carro, 0)
                Centro_do_carro = Carros[i].getAnchor()
                if Centro_do_carro.getX() > -200 and Centro_do_carro.getX() < 1200: 
                    Carros[i].undraw()
                    Carros[i] = Image(Centro_do_carro, Lista_de_carros[i][Proxima_Imagem_Carro])
                    Carros[i].draw(win)

            if not Menino_em_cima:
                Menino.move(0, - velocidade)
                Centro_do_menino = Menino.getAnchor()
                Menino.undraw()
                Menino = Image(Centro_do_menino, Menino_pulando)
                Menino.draw(win)

            Posicao_no_fundo = Posicao_no_fundo + movimento

            update(rate)

        while velocidade <= 50:

            if Menino_em_cima:
                Menino.move(0, velocidade)
                Centro_do_menino = Menino.getAnchor()
                Menino.undraw()
                Menino = Image(Centro_do_menino, Menino_pulando)
                Menino.draw(win)

                if velocidade == 50:
                    Proxima_Imagem = 0
                    Menino.undraw()
                    Menino = Image(Centro_do_menino, Menino_parado[0])
                    Menino.draw(win)

            for i in range(0, len(Fundo)):
                Fundo[i].move(-movimento, 0)

            for i in range(0, len(Cones)):
                Cones[i].move(-movimento, 0)

            Proxima_Imagem_Carro = (Proxima_Imagem_Carro + 1) % len(Carro1)
                
            for i in range(0, len(Carros)):
                Carros[i].move(-movimento_carro, 0)
                Centro_do_carro = Carros[i].getAnchor()
                if Centro_do_carro.getX() > -200 and Centro_do_carro.getX() < 1200: 
                    Carros[i].undraw()
                    Carros[i] = Image(Centro_do_carro, Lista_de_carros[i][Proxima_Imagem_Carro])
                    Carros[i].draw(win)

            if not Menino_em_cima:
                Menino.move(0, velocidade)
                Centro_do_menino = Menino.getAnchor()
                Menino.undraw()
                Menino = Image(Centro_do_menino, Menino_pulando)
                Menino.draw(win)

                if velocidade == 50:
                    Proxima_Imagem = 0
                    Menino.undraw()
                    Menino = Image(Centro_do_menino, Menino_parado[0])
                    Menino.draw(win)

            velocidade = velocidade + 10
                
            Posicao_no_fundo = Posicao_no_fundo + movimento

            colidiu, objeto, posicao, numero_do_carro = Colisao(Centro_do_menino, Carros, Cones)

            if colidiu:
                Menino = Animacao_colisao(Menino, Centro_do_menino, Colisoes, objeto, posicao, True)

                tempo = 0

                while tempo < 65:
                    tempo = tempo + 1
                    update(rate)

                Fim()

            update(rate)

        return Proxima_Imagem, Fundo, Cones, Menino, Proxima_Imagem_Carro, Carros, Posicao_no_fundo

    def Animacao_colisao(Menino, Centro_do_menino, Colisoes, objeto, posicao, pulando):

        Proxima_Imagem_Colisao = 0

        if objeto == 'carro':
            if pulando == True:
                colisao = Image(Point(Centro_do_menino.getX(), Centro_do_menino.getY() + 50), Colisoes[Proxima_Imagem_Colisao])
                colisao.draw(win)
                Centro_da_colisao = colisao.getAnchor()

                while Proxima_Imagem_Colisao < 11:
                    colisao.undraw()
                    Proxima_Imagem_Colisao = Proxima_Imagem_Colisao + 1

                    Menino.move(-22 + Proxima_Imagem_Colisao, -1 + (Proxima_Imagem_Colisao))
                    Centro_do_menino = Menino.getAnchor()
                    Menino.undraw()
                    Menino = Image(Centro_do_menino, 'sprite_9.png')
                    Menino.draw(win)

                    colisao = Image(Centro_da_colisao, Colisoes[Proxima_Imagem_Colisao])
                    colisao.draw(win)

                    update(rate)

                if posicao == True:
                    while Centro_do_menino.getY() < 440:
                        Proxima_Imagem_Colisao = Proxima_Imagem_Colisao + 1
                        Menino.move(-22 + Proxima_Imagem_Colisao, -1 + (Proxima_Imagem_Colisao))
                        Centro_do_menino = Menino.getAnchor()
                        Menino.undraw()
                        Menino = Image(Centro_do_menino, 'sprite_9.png')
                        Menino.draw(win)

                else:
                    while Centro_do_menino.getY() < 520:
                        Proxima_Imagem_Colisao = Proxima_Imagem_Colisao + 1
                        Menino.move(-22 + Proxima_Imagem_Colisao, -1 + (Proxima_Imagem_Colisao))
                        Centro_do_menino = Menino.getAnchor()
                        Menino.undraw()
                        Menino = Image(Centro_do_menino, 'sprite_9.png')
                        Menino.draw(win)


                Menino.undraw()
                Menino = Image(Point(Centro_do_menino.getX() - 30, Centro_do_menino.getY()), 'sprite_8.png')
                Menino.draw(win)

                colisao.undraw()

            else:
                colisao = Image(Point(Centro_do_menino.getX() + 20, Centro_do_menino.getY()), Colisoes[Proxima_Imagem_Colisao])
                colisao.draw(win)
                Centro_da_colisao = colisao.getAnchor()

                while Proxima_Imagem_Colisao < 5:
                    colisao.undraw()
                    Proxima_Imagem_Colisao = Proxima_Imagem_Colisao + 1

                    if Proxima_Imagem_Colisao == 5:
                        if Menino_em_cima:
                            Menino = Image(Point(Centro_do_menino.getX() - 30, Centro_do_menino.getY()), 'sprite_8.png')
                            Menino.draw(win)

                        if not Menino_em_cima: 
                            Menino = Image(Point(Centro_do_menino.getX() - 30, Centro_do_menino.getY()), 'sprite_8.png')
                            Carros[numero_do_carro].undraw()
                            Menino.draw(win) 
                            Carros[numero_do_carro].draw(win)

                    colisao = Image(Centro_da_colisao, Colisoes[Proxima_Imagem_Colisao])
                    colisao.draw(win)

                    update(rate)

                colisao.undraw()

        else:
            if pulando == True:
                colisao = Image(Point(Centro_do_menino.getX(), Centro_do_menino.getY() + 40), Colisoes[Proxima_Imagem_Colisao])
                colisao.draw(win)
                Centro_da_colisao = colisao.getAnchor()

            else:
                colisao = Image(Point(Centro_do_menino.getX() + 20, Centro_do_menino.getY()), Colisoes[Proxima_Imagem_Colisao])
                colisao.draw(win)
                Centro_da_colisao = colisao.getAnchor()

            while Proxima_Imagem_Colisao < 11:
                colisao.undraw()
                Proxima_Imagem_Colisao = Proxima_Imagem_Colisao + 1
                colisao = Image(Centro_da_colisao, Colisoes[Proxima_Imagem_Colisao])
                colisao.draw(win)

                if Proxima_Imagem_Colisao == 5:
                    if posicao == True:
                        Menino.undraw()
                        Menino = Image(Point(Centro_do_menino.getX() + 30, 450), 'sprite_6.png')
                        Carro_na_frente = False

                        for i in range(0, len(Carros)):
                            x_carro = (Carros[i].getAnchor()).getX()

                            if x_carro >= 50 and x_carro <= 550:
                                Carros[i].undraw()
                                Menino.draw(win)
                                Carros[i].draw(win)
                                Carro_na_frente = True

                        if not Carro_na_frente:
                            Menino.draw(win)

                    else:
                        Menino.undraw()
                        Menino = Image(Point(Centro_do_menino.getX() + 30 , 525), 'sprite_6.png')
                        Menino.draw(win)

                update(rate)

            colisao.undraw()         

        return Menino
    
    def Colisao(Centro_do_menino, Carros, Cones):
        
        x = Centro_do_menino.getX()
        y = Centro_do_menino.getY()

        for i in range(0, len(Carros)):
            x_carro = (Carros[i].getAnchor()).getX()
            y_carro = (Carros[i].getAnchor()).getY()

            if y_carro == 440:
                Carro_em_cima = True
            
            else:
                Carro_em_cima = False

            if x_carro >= -200 and x_carro <= 1200:
                if (Menino_em_cima and Carro_em_cima) or (not Menino_em_cima and not Carro_em_cima):
                    if (x + 20 > x_carro - 60 and x - 20 < x_carro + 165 and y + 40 > y_carro - 70 and y - 40 < y_carro + 55) or (x + 20 > x_carro - 165 and x - 20 < x_carro - 60 and y + 40 > y_carro - 15 and y - 40 < y_carro + 55):
                        Menino.undraw()
                        return True, 'carro', Carro_em_cima, i

        for i in range(0, len(Cones)):
            x_cone = (Cones[i].getAnchor()).getX()
            y_cone = (Cones[i].getAnchor()).getY()

            if y_cone == 470:
                Cone_em_cima = True
            
            else:
                Cone_em_cima = False

            if x_cone >= -50 and x_cone <= 1050:
                if (Menino_em_cima and Cone_em_cima) or (not Menino_em_cima and not Cone_em_cima):
                    if (x + 20 > x_cone - 25 and x - 20 < x_cone + 25 and y + 20 > y_cone - 9 and y - 20 < y_cone - 29):
                        Menino.undraw()
                        return True, 'cone', Cone_em_cima, None
        
        return False, None, None, None

    def Fim():

        Final = Image(Point(500, 300), 'Game Over.png')
        Final.draw(win)

        tempo = 0

        while tempo < 100:
            tempo = tempo + 1
            update(rate)

        Final.undraw()
        win.close()
        main()

    
    Menino = Image(Point(70, 450), Menino_parado[0])
    Menino.draw(win)
    Centro_do_menino = Menino.getAnchor()
    Menino_em_cima = True


    Gato = Image(Point(450, 477), Gato_sentado[0])
    Gato.draw(win)
    Centro_do_gato = Gato.getAnchor()

    tempo = 0
    Proxima_Imagem_Gato = 0
    Proxima_Imagem = 0
    
    while tempo > 5:

        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)
        
        Proxima_Imagem_Gato, Gato = GatoParado(Proxima_Imagem_Gato, Gato_sentado, Gato, Centro_do_gato)

        tempo = tempo + 1

        update(rate)

    x = 500
    y = 175
    proporcao = 1
     
    Informacoes = Rectangle(Point(x - 40, y + 15), Point(x + 40, y - 15))
    Informacoes.setFill('black')
    Informacoes.draw(win)

    while proporcao <= 9:

        Informacoes.undraw()
        proporcao = proporcao + 1
        Informacoes = Rectangle(Point(x - proporcao * 40, y + proporcao * 15), Point(x + proporcao * 40, y - proporcao * 15))
        Informacoes.setFill('black')
        Informacoes.draw(win)
        update(rate)

    Texto_informacoes = Text(Point(500, 175), 'Ajude Jéssica a pegar o seu gato que está fugindo.\n\nCuidado com os carros e obstáculos que encontrar pelo caminho!\n\n\nComandos:\n\n- Space: pula\n- Up: passa para a pista de cima\n- Down: passa para a pista de baixo\n\n\nQuando estiver pronto para começar pressione qualquer tecla!')
    Texto_informacoes.setFill('white')
    Texto_informacoes.setStyle('bold')
    Texto_informacoes.setFace('courier')
    Texto_informacoes.draw(win)
    
    key = ''

    while key == '':

        key = win.checkKey()

        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)

        Proxima_Imagem_Gato, Gato = GatoParado(Proxima_Imagem_Gato, Gato_sentado, Gato, Centro_do_gato)

        update(rate)

    Informacoes.undraw()
    Texto_informacoes.undraw()

    Gato.undraw()

    Gato = Image(Centro_do_gato, Gato_levantando[0])

    Proxima_Imagem_Gato = 0

    while Proxima_Imagem_Gato < 5:

        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)

        Proxima_Imagem_Gato = Proxima_Imagem_Gato + 1
        Gato.undraw()
        Gato = Image(Centro_do_gato, Gato_levantando[Proxima_Imagem_Gato])
        Gato.draw(win)

        update(rate)

    Gato.undraw()
    Gato = Image(Centro_do_gato, Gato_correndo[0])
    Gato.draw(win)
    Proxima_Imagem_Gato = 0

    while tempo < 40:

        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)

        Gato.move(movimento, 0)
        Centro_do_gato = Gato.getAnchor()
        Proxima_Imagem_Gato, Gato = GatoCorrendo(Proxima_Imagem_Gato, Gato_correndo, Gato, Centro_do_gato)

        tempo = tempo + 1

        update(rate)

    Proxima_Imagem = 0

    Posicao_no_fundo = Centro_do_menino.getX()

    while Posicao_no_fundo < 300:
        
        Menino.move(movimento, 0)
        Centro_do_menino = Menino.getAnchor()

        Proxima_Imagem, Menino = MeninoCorrendo(Proxima_Imagem, Menino_correndo, Menino, Centro_do_menino)
    
        Centro_do_menino = Menino.getAnchor()

        Posicao_no_fundo = Posicao_no_fundo + movimento
        
        Gato.move(movimento, 0)
        Centro_do_gato = Gato.getAnchor()
        Proxima_Imagem_Gato, Gato = GatoCorrendo(Proxima_Imagem_Gato, Gato_correndo, Gato, Centro_do_gato)

        update(rate)

    Gato.undraw()

    Menino.undraw()
    Menino = Image(Centro_do_menino, Menino_correndo[Proxima_Imagem])
    Menino.draw(win)
    
    while Posicao_no_fundo < Comprimento_do_fundo - 1375:

        key = win.checkKey()

        colidiu, objeto, posicao, numero_do_carro = Colisao(Centro_do_menino, Carros, Cones)

        if colidiu:
            Menino = Animacao_colisao(Menino, Centro_do_menino, Colisoes, objeto, posicao, False)

            while tempo < 65:
                tempo = tempo + 1
                update(rate)

            Fim()

        if key == 'space':
            Proxima_Imagem, Fundo, Cones, Menino, Proxima_Imagem_Carro, Carros, Posicao_no_fundo = MeninoPulando(Menino, Centro_do_menino, Menino_pulando, Menino_em_cima, Fundo, Cones, movimento, Proxima_Imagem_Carro, Carros, Lista_de_carros, Posicao_no_fundo, rate, Colisoes)

        if key == 'Up' and not Menino_em_cima:

            Menino.undraw()
            Menino = Image(Point(300, 450), Menino_parado[0])
            Proxima_Imagem = 0
            Menino.draw(win)
            Menino_em_cima = True
            Centro_do_menino = Menino.getAnchor()
       
        if key == 'Down' and Menino_em_cima:

            Menino.undraw()
            Menino = Image(Point(300, 525), Menino_parado[0])
            Proxima_Imagem = 0
            Centro_do_menino = Menino.getAnchor()
            colidiu, objeto, posicao, numero_do_carro = Colisao(Centro_do_menino, Carros, Cones)
            if not colidiu:
                Menino.draw(win) 
            Menino_em_cima = False
            

        else:

            if Menino_em_cima:
                Proxima_Imagem, Menino = MeninoCorrendo(Proxima_Imagem, Menino_correndo, Menino, Centro_do_menino)

            for i in range(0, len(Cones)):
                Cones[i].move(-movimento, 0)

            Proxima_Imagem_Carro = (Proxima_Imagem_Carro + 1) % len(Carro1)
            
            for i in range(0, len(Carros)):
                Carros[i].move(-movimento_carro, 0)
                Centro_do_carro = Carros[i].getAnchor()
                if Centro_do_carro.getX() > -200 and Centro_do_carro.getX() < 1200: 
                    Carros[i].undraw()
                    Carros[i] = Image(Centro_do_carro, Lista_de_carros[i][Proxima_Imagem_Carro])
                    Carros[i].draw(win)

            if not Menino_em_cima:
                Proxima_Imagem, Menino = MeninoCorrendo(Proxima_Imagem, Menino_correndo, Menino, Centro_do_menino)

            for i in range(0, len(Fundo)):
                Fundo[i].move(-movimento, 0)

            Posicao_no_fundo = Posicao_no_fundo + movimento

        update(rate)

    Menino.undraw()
    Menino = Image(Centro_do_menino, Menino_parado[0])
    Menino.draw(win)
    Proxima_Imagem = 0

    tempo = 0

    if Menino_em_cima:
        Balao = Image(Point(250, 350), 'balao.png')
        Balao.draw(win)

    else:
        Balao = Image(Point(250, 425), 'balao.png')
        Balao.draw(win)
    
    while tempo < 30:
        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)

        tempo = tempo + 1

        update(rate)

    Balao.undraw()

    Proxima_Imagem = 0
    Proxima_Imagem_Gato = 0
    
    if Menino_em_cima:
        Gato = Image(Point(1050, 477), Gato_sentado[0])
        Gato.draw(win)
        Centro_do_gato = Gato.getAnchor()

    else:
        Gato = Image(Point(1050, 552), Gato_sentado[0])
        Gato.draw(win)
        Centro_do_gato = Gato.getAnchor()
    
    while Posicao_no_fundo < Comprimento_do_fundo - 700:

        for i in range(0, len(Fundo)):
            Fundo[i].move(-movimento, 0)

        for i in range(0, len(cones)):
            Cones[i].undraw()
            Cones[i].move(-movimento, 0)
            Cones[i].draw(win)

        Proxima_Imagem, Menino = MeninoCorrendo(Proxima_Imagem, Menino_correndo, Menino, Centro_do_menino)

        Gato.move(-movimento, 0)
        Centro_do_gato = Gato.getAnchor()
        Proxima_Imagem_Gato, Gato = GatoParado(Proxima_Imagem_Gato, Gato_sentado, Gato, Centro_do_gato)

        Posicao_no_fundo = Posicao_no_fundo + movimento

        update(rate)

    tempo = 0
    Menino.undraw()
    Menino = Image(Centro_do_menino, Menino_parado[0])
    Menino.draw(win)
    Proxima_Imagem = 0

    Parabens = Image(Point(500, 300), 'Parabens.png')
    Parabens.draw(win)

    while tempo < 80:

        Proxima_Imagem, Menino = MeninoParado(Proxima_Imagem, Menino_parado, Menino, Centro_do_menino)

        Proxima_Imagem_Gato, Gato = GatoParado(Proxima_Imagem_Gato, Gato_sentado, Gato, Centro_do_gato)

        tempo = tempo + 1

        update(rate)

    x = 500
    y = 300
    proporcao = 1
     
    Informacoes_final = Rectangle(Point(x - 50, y + 30), Point(x + 50, y - 30))
    Informacoes_final.setFill('black')
    Informacoes_final.draw(win)

    while proporcao <= 9:

        Informacoes_final.undraw()
        proporcao = proporcao + 1
        Informacoes_final = Rectangle(Point(x - proporcao * 50, y + proporcao * 30), Point(x + proporcao * 50, y - proporcao * 30))
        Informacoes_final.setFill('black')
        Informacoes_final.draw(win)
        
        update(rate)

    Texto_final = Text(Point(225, 65), 'Desenvolvido por Jéssica Ferraz Rosario')
    Texto_final.setFill('white')
    Texto_final.setStyle('bold')
    Texto_final.setSize(15)
    Texto_final.draw(win)
    Texto_final2 = Text(Point(500, 250), 'Jogo elaborado como prosposta de atividade do terceiro bimestre da disciplina de Algoritmos\n\ne Estruturas de Dados I do curso de Engenharia da Computação da Universidade Federal do\n\nRio Grande - FURG')
    Texto_final2.setFill('white')
    Texto_final2.setStyle('bold')
    Texto_final2.draw(win)
    Menino_final = Image(Point(120, 450), 'Menino_frente.png')
    Menino_final.draw(win)
    Gato_final = Image(Point(200, 471), 'Gato_frente.png')
    Gato_final.draw(win)

    win.getMouse()    

main()   