import pygame

## init
pygame.init()

# membuat display surface object
window = pygame.display.set_mode((600, 600))

# object game
# posisi
x = 250
y = 250

# ukuran
lebar = 30
panjang = 30

# kecepatan gerak
speed = 5

isRun = True
while isRun:
    pygame.time.delay(10)

    ## user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil arrow kiri
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
      
    # ambil arrow kanan
    if keys[pygame.K_RIGHT] and x < 595 - lebar:
        x += speed
    
    # ambil arrow atas
    if keys[pygame.K_UP] and y > 5:
        y -= speed

    # ambil arrow bawah
    if keys[pygame.K_DOWN] and y < 590 - panjang:
        y += speed
          
    ## update asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,50,50), (x,y,lebar,panjang), border_radius=2)

    ## render ke display
    pygame.display.update()

pygame.quit()
