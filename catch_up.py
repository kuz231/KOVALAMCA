from pygame import *
window = display.set_mode((700, 500)) #500 px yükseklik ve 700 px lik boyutlara sahip boş pencere
display.set_caption("Kovalamaca") #pencere başlığı
background = transform.scale(image.load("background.png"), (700, 500))
#arkaplan görselinin aktarılması ve ekrana boyutlandırılması

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100)) #karakter 1'in ekrana yerleştirilmesi
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100)) #karakter 2'nin ekrana yerleştirilmesi
speed = 10

#Oyun döngüsü:
run = True
clock = time.Clock() #bir tane clock nesnesi oluşturduk. Oyun döngümüz saniyede kaç defa tekrarlayacak
FPS = 60 #döngü tekrar hızı için oluşturuldu

while run:
    window.blit(background, (0, 0)) #ekrana arkaplanı yerleştiriyoruz 
    window.blit(sprite1, (x1, y1)) #ekrana karakteri i yerleştiriyoruz
    window.blit (sprite2, (x2, y2)) #ekrana karakter ikiyi yerleştiriyoruz

    for e in event.get(): #burada event.get listesi içerisindeki tüm öğeler tek tek kontrol edilir if
        if e.type == QUIT: #eğer bu listedeki değerlerden bir tanesi QUIT'e eşitse yani x e basılmışsa
            run = False #oyunu sonlandırdık

    keys_pressed = key.get_pressed() #key_pressed değişkenine tuşlara basılma olaylarını atadik


#karakter1
    if keys_pressed [K_LEFT] and x1 > 5: #eğer sol ok tuşuna basılmışsa ve x1 konumu 5'ten büyükse
        x1 -= speed #sola git

    if keys_pressed [K_RIGHT] and x1 < 595: #eğer sağ ok tuşuna basılmışsa ve x1 konumu 595'ten küçükse
        x1 += speed #sağa git

    if keys_pressed [K_UP] and y1 > 5: #eğer yukarı ok tuşuna basılmışsa ve y1 konumu 5'ten büyükse
        y1 -=speed #yukarı git

    if keys_pressed [K_DOWN] and y1 < 395: #eğer aşağı ok tuşuna basılmışsa ve y1 konumu 595'ten küçükse
        y1 += speed #aşağı git

#karakter2
    if keys_pressed [K_a] and x2 > 5: #eğer a tuşuna basılmışsa ve x2 konumu 5'ten büyükse
        x2 -= speed #sola git

    if keys_pressed [K_d] and x2 < 595: #eğer d tuşuna basılmışsa ve x2 konumu 595'ten küçükse
        x2 += speed #sağa git

    if keys_pressed [K_w] and y2 > 5: #eğer w tuşuna basılmışsa ve y2 konumu 5'ten büyükse
        y2 -= speed #aşağı git

    if keys_pressed [K_s] and y2 < 395: #eğer s tuşuna basılmışsa ve y2 konumu 595'ten küçükse
        y2 += speed #aşağı git

    display.update() #pencereyi döngü her çalıştığında günceller
    clock.tick(FPS)