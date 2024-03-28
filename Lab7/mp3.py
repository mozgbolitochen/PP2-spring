import pygame
import os
playing = False

def play_song(ind,this = False):
    global playing
    if this:
        if playing:
            pygame.mixer.music.pause()
            playing = not playing
        else:
            pygame.mixer.music.unpause()
            playing = not playing
    else:
        pygame.mixer.music.load(songs[ind])
        pygame.mixer.music.play()
        playing = True


pygame.init()


HEIGHT, WEIGHT = 600, 600
screen = pygame.display.set_mode((HEIGHT, WEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("My first game")


f = pygame.font.Font(None, 36)
text1 = f.render('PLAY - Space', True, (0, 0, 0))
text2 = f.render('STOP - s', True, (0, 0, 0))
text3 = f.render('NEXT - n', True, (0, 0, 0))
text4 = f.render('PREVIOUS - p', True, (0, 0, 0))
text5 = f.render('START - q', True, (0, 0, 0))


screen.blit(text1, (10, 50))
screen.blit(text2, (10, 100))
screen.blit(text3, (10, 150))
screen.blit(text4, (10, 200))
screen.blit(text5, (10, 250))

pygame.display.update()
songs = []
ind = 0
directory = r"/home/ruslan/Music"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.mp3'):
        songs.append(f)
print(songs)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_song(ind,True)
            if event.key == pygame.K_q:
                play_song(ind)
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False
            if event.key == pygame.K_n:
                if ind < len(songs) - 1:
                    ind += 1
                    if playing:
                        play_song(ind)

                else:
                    ind = 0
                    if playing:
                        play_song(ind)
            if  event.key == pygame.K_p:
                if ind > 0:
                    ind -= 1
                    if playing:
                        play_song(ind)
                else:
                    ind = len(songs)-1
                    if playing:
                        play_song(ind)
            if event.key == pygame.K_ESCAPE:
                running = False
