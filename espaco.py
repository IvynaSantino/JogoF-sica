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


foguete = {
	'surface': pygame.image.load('foguete3.png').convert_alpha(),
	'position': [40, 300],
	'speed': {
		'x': 0,
		'y': 0
	}
}

# NOME DO JOGO: NAO SEI AINDA!
pygame.display.set_caption('SIMULADOR DE CARGA')


# MOVIMENTO DE METEOROS
def criarMeteoro():
	return {
		'surface': pygame.image.load("meteoroA.png"),
		'position': [750, randrange(600)],
		'speed': randrange(9)
	}
	
listaMeteoros = []

def mover_meteoros():
	for meteoro in listaMeteoros:
		meteoro['position'][0] -= meteoro['speed']


def remove_meteoros():
	for meteoro in listaMeteoros:
		if meteoro['position'][0] > 750:
			listaMeteoros.remove(meteoro)
			
velocidade_meteoroA = 120


# DETECTAR COLISÕES
def get_rect(obj):
	return Rect(obj['position'][0],
				obj['position'][1],
				obj['surface'].get_width(),
				obj['surface'].get_height())

def foguete_colisao():
	foguete_rect = get_rect(foguete)
	
	for meteoro in listaMeteoros:
		if foguete_rect.colliderect(get_rect(meteoro)):
			return True
	return False

# INICIANDO A CARGA DO FOGUETE
cargaInicial = 10.0
def conservacaoDeCargas(cargaInicial):
	
	cargaConservada = 0
	cargaLivre = randrange(0,50)
	
	cargaInicial = (cargaLivre + cargaInicial)/2.0 
	cargaConservada = cargaInicial
	return cargaConservada
	
	

# MOVIMENTAÇÃO DO JOGO
clock = pygame.time.Clock()
collided = False

while True:
	
	foguete['speed'] = {
	'x': 0,
	'y': 0
	}
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	print conservacaoDeCargas(cargaInicial)
			
	if not velocidade_meteoroA:
		velocidade_meteoroA = 120
		listaMeteoros.append(criarMeteoro())
	else:
		velocidade_meteoroA -= 1
		
		
	# COMANDOS ATRAVÉS DAS TECLAS
	pressed_keys = pygame.key.get_pressed()
	
	if pressed_keys[K_SPACE]:
		break
	
	if pressed_keys[K_UP]:
		foguete['speed']['y'] = -10
		
	elif pressed_keys[K_DOWN]:
		foguete['speed']['y'] = 10
		
	if pressed_keys[K_LEFT]:
		foguete['speed']['x'] = -10
		
	elif pressed_keys[K_RIGHT]:
		foguete['speed']['x'] = 10
		
	tela.blit(imagem_fundo, (0, 0))
	
	# MOVIMENTO DO FOGUETE
	if not collided:
		collided = foguete_colisao()
		foguete['position'][0] += foguete['speed']['x']
		foguete['position'][1] += foguete['speed']['y']
		tela.blit(foguete['surface'], foguete['position'])
		
		# NÃO ULTRAPASSAR A TELA
		if foguete['position'][0] > 550:
			foguete['position'][0] -= 10
			
		if foguete['position'][0] < 5:
			foguete['position'][0] += 10
			
		if foguete['position'][1] > 500:
			foguete['position'][1] -= 10
			
		if foguete['position'][1] < 10:
			foguete['position'][1] += 10
		
	# INICIAR FOGUETE NA POSIÇÃO 40 x 300 NA TELA
	#tela.blit(foguete['surface'], foguete['position'])
	mover_meteoros()
	
	for meteoro in listaMeteoros:
		tela.blit(meteoro['surface'], meteoro['position'])
		
	pygame.display.update()
	tempo = clock.tick(30)
	remove_meteoros()
