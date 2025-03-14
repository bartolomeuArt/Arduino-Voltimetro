from constante import *
from porta import *


#colocar porta que voce está usando no arduino
Arduino = serial.Serial("COM3" ,9600, timeout=1)


pygame.font.init()
my_font = pygame.font.SysFont('arial', 45)
my_font2 = pygame.font.SysFont('arial', 24)
my_font3 = pygame.font.SysFont('arial', 16)
text_surface = my_font.render('5V', False, (0, 0, 0))



#controle variaveis
running = True

r = getData(Arduino)
print(r)

#cria janela
screen = pygame.display.set_mode((WIDTH, HIGH))
pygame.display.set_caption('Voltietro') 
screen.fill(COR_BACKGROUND)

def getVolt():
    volt = getData(Arduino)
    print(volt)
    texto = str(volt) + " V"
    text_surface1 = my_font.render(texto, False, (0, 0, 0))
    text_rect = text_surface1.get_rect(center=(WIDTH/2, HIGH/2))
    screen.blit(text_surface1, text_rect)
    text_surface2 = my_font2.render("medir tensao DC, entre  0 < V < 30", False, (0, 0, 0))
    text_rect2 = text_surface2.get_rect(center=(WIDTH/2, 100))
    screen.blit(text_surface2, text_rect2)
    if volt<=0.0:
        text_surface3 = my_font3.render("*ver se polaridade esta invertida", False, (0, 0, 0))
        text_rect3 = text_surface3.get_rect(center=(WIDTH/2,  HIGH/2 + 100))
        screen.blit(text_surface3, text_rect3)



while running:
    getVolt()

    pygame.display.update()
    screen.fill(COR_BACKGROUND)
    
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

pygame.quit()

















