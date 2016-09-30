#coding: utf-8

#################################################################
#																#
#		PRIMEIRO ESTÁGIO: FÍSICA CLÁSSICA						#
#		ALUNAS: IVYNA ALVES E ALICE SILVA						#
#		SIMULAÇÃO DA QUESTÃO TAL DO LIVRO TEXTO HALLIDAY 3		#
#																#
#################################################################

import pygame
from pygame.locals import *
from sys import exit
from random import randrange
from random import randrange

# INICIANDO O JOGO
pygame.init()

# DETALHES DA TELA: LARGURA E ALTURA
LARGURA = 750 
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA),0,32)
imagem_fundo = pygame.image.load("espacoFormat.jpg")


foguete_imagem = "foguete3.png"
foguete = pygame.image.load(foguete_imagem).convert_alpha()

foguete_posicao = [40, 300]

# NOME DO JOGO: NAO SEI AINDA!
pygame.display.set_caption('SIMULADOR DE CARGA')


# MOVIMENTO DE METEOROS
def criarMeteoro():
	return {
		'surface': pygame.image.load("meteoroA.png"),
		'position': [750, randrange(600)],
		'speed': randrange(9)
	}
	
mAmarelo = []

def mover_meteoros():
	for meteoro in mAmarelo:
		meteoro['position'][0] -= meteoro['speed']


def remove_meteoros():
	for meteoro in mAmarelo:
		if meteoro['position'][0] > 750:
			mAmarelo.remove(meteoro)
			
velocidade_meteoroA = 120


# MOVIMENTAÇÃO DO JOGO
clock = pygame.time.Clock()

while True:
	velocidade = {
	'x': 0,
	'y': 0
	}
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	if not velocidade_meteoroA:
		velocidade_meteoroA = 120
		mAmarelo.append(criarMeteoro())
	else:
		velocidade_meteoroA -= 1
		
		
	# COMANDOS ATRAVÉS DAS TECLAS
	pressed_keys = pygame.key.get_pressed()
	
	if pressed_keys[K_SPACE]:
		break
	
	if pressed_keys[K_UP]:
		velocidade['y'] = -10
		
	elif pressed_keys[K_DOWN]:
		velocidade['y'] = 10
		
	if pressed_keys[K_LEFT]:
		velocidade['x'] = -10
		
	elif pressed_keys[K_RIGHT]:
		velocidade['x'] = 10
		
	tela.blit(imagem_fundo, (0, 0))
	
	# MOVIMENTO DO FOGUETE
	foguete_posicao[0] += velocidade['x']
	foguete_posicao[1] += velocidade['y']
	
	# NÃO ULTRAPASSAR A TELA
	if foguete_posicao[0] > 550:
		foguete_posicao[0] -= 10
		
	if foguete_posicao[0] < 5:
		foguete_posicao[0] += 10
		
	if foguete_posicao[1] > 500:
		foguete_posicao[1] -= 10
		
	if foguete_posicao[1] < 10:
		foguete_posicao[1] += 10
		
		
	tela.blit(foguete, foguete_posicao)
	
	mover_meteoros()
	
	for meteoro in mAmarelo:
		tela.blit(meteoro['surface'], meteoro['position'])
		
	pygame.display.update()
	tempo = clock.tick(30)
