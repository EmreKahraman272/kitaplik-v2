import sys
import pyautogui

x = 0
kitaplar = []
raflar = []
z = 1
k = 0
rafSay = 0
kitap = ""

pyautogui.alert(text='Programa Hoşgeldiniz ! \n Sürüm 0.2 \n UYARILAR!!! \n 1.Türkçe harfler kullanmayın.',
                title='KITAPLIK', button='TAMAM')

bps = int(pyautogui.prompt(text='Bir rafta kaç tane kitap bulunsun ?', title='BPS'))

i = "a"
while i != "finish":
    i = str(pyautogui.prompt(text="Kitap isimlerini giriniz.(Bittirmek için 'finish' yazınız.)", title='Kitaplar'))
    kitaplar.append(i)

sayilar = []
sayilar.extend(range((len(kitaplar))))
kitaplar.remove("finish")
kitaplar.sort()
kitaps = len(kitaplar)

if bps >= kitaps:
    rafSay = 1
elif bps < kitaps:
    raf = kitaps % bps
    if raf == 0:
        rafSay = kitaps / bps
    else:
        rafSay = kitaps / bps + 1

    print(int(rafSay))
    for k in range(int(rafSay)):
        try:
            print("Raf " + str(z) + ":")
            for f in range(bps):
                kitap += kitaplar[0]
                kitap += ", "

                # print(kitaplar[0])

                x += 1

                kitaplar.remove(kitaplar[0])




        except IndexError:
            sys.exit()
        finally:
            pyautogui.alert(text=kitap, title="Raf " + str(z), button="TAMAM")
            z += 1
            kitap = ""





