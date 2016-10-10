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
pygame.font.init()

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 100)

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

# EXPLOSÃO DO FOGUETE
explosao_foguete = {
	'surface': pygame.image.load('kaban1.png').convert_alpha(),
	'position': [],
	'speed': {
		'x': 0,
		'y': 0
	},
	'rect': Rect(0, 0, 300, 300)
}

# COLISÃO COM CARGAS
cargas_conserva = {
	'surface': pygame.image.load('carga.png').convert_alpha(),
	'position': [],
	'speed': {
		'x': 0,
		'y': 0
	},
	'rect': Rect(0, 0, 300, 300)
}

# NOME DO JOGO: NAO SEI AINDA!
pygame.display.set_caption('SIMULADOR DE CARGA')

# CARGAS
def criaCarga():
	return {
		'surface': pygame.image.load('carga.png'),
		'position': [750, randrange(580)],
		'speed': randrange(7)
	}

listaDeCargas = []

def moverCargas():
	for carga in listaDeCargas:
		carga['position'][0] -= carga['speed']

def removeCarga():
	for carga in listaDeCargas:
		if carga['position'][0] > 750:
			listaDeCargas.remove(carga)

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


# DETECTAR COLISÕES: METEOROS E CARGAS
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

def cargaColisao():
	foguete_rect = get_rect(foguete)
	
	for carga in listaDeCargas:
		if foguete_rect.colliderect(get_rect(carga)):
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
collision_animation_count = 0
colisao_animation_carga = 0
velocidade_carga = 120
colisaoCarga = False

WINDOWWIDTH = 750
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)
	
font = pygame.font.SysFont(None, 30)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

while True:
	
	
	foguete['speed'] = {
	'x': 0,
	'y': 0
	}
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

			
	if not velocidade_meteoroA:
		velocidade_meteoroA = 120
		listaMeteoros.append(criarMeteoro())
	else:
		velocidade_meteoroA -= 1
		
		
	if not velocidade_carga:
		velocidade_carga = 120
		listaDeCargas.append(criaCarga())
	else:
		velocidade_carga -= 1
		
		
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
	
	# MOVIMENTO DO FOGUETE E DETECTAR COLISÕES
	
	
	if not collided:
		collided = foguete_colisao()
		
		foguete['position'][0] += foguete['speed']['x']
		foguete['position'][1] += foguete['speed']['y']
		tela.blit(foguete['surface'], foguete['position'])
		colisaoCarga = cargaColisao()
		
		if colisaoCarga:
			
			while True:
				if colisao_animation_carga == 2:
					
					colisaoCarga = cargaColisao()
					cargaInicial = conservacaoDeCargas(cargaInicial)
					print cargaInicial
					break
				else:
					cargas_conserva['rect'].x = colisao_animation_carga * 50
					cargas_conserva['position'] = foguete['position']
					
					colisao_animation_carga += 1		
				colisaoCarga = False
			colisao_animation_carga = 0
			
		
		drawText("Carga Inicial: 10.0 C", font, windowSurface, 10, 0)
		drawText("Carga apos colisao: %s C" % (cargaInicial), font, windowSurface, 10, 30)
		
		# NÃO ULTRAPASSAR A TELA
		if foguete['position'][0] > 550:
			foguete['position'][0] -= 10
			
		if foguete['position'][0] < 5:
			foguete['position'][0] += 10
			
		if foguete['position'][1] > 500:
			foguete['position'][1] -= 10
			
		if foguete['position'][1] < 10:
			foguete['position'][1] += 10
	else:
		if collision_animation_count == 3:
			text = game_font.render('GAME OVER', 1, (255, 0, 0))
			tela.blit(text, (150, 250))
			
		else:
			#FRAME DA EXPLOSÃO
			explosao_foguete['rect'].x = collision_animation_count * 300
			explosao_foguete['position'] = foguete['position']
			tela.blit(explosao_foguete['surface'], explosao_foguete['position'], explosao_foguete['rect'])
			collision_animation_count += 1
			print cargaInicial
			
	
	mover_meteoros()
	moverCargas()
	
	for meteoro in listaMeteoros:
		tela.blit(meteoro['surface'], meteoro['position'])
		
	for carga in listaDeCargas:
		tela.blit(carga['surface'], carga['position'])
	
	pygame.display.update()
	tempo = clock.tick(20)
	
	remove_meteoros()
	removeCarga()
