import tkinter

window = tkinter.Tk()
window.geometry("400x300")


def calculate():
    if(weight.get() != "" and height.get() != ""):
        try:
            powerOfTwoOfHeight = (int(height.get()) / 100) ** 2
            calculation = (int(weight.get()) / powerOfTwoOfHeight)
            if calculation < 18.5:
                result.config(text=f"Boyunuza göre zayıfsınız")
            elif calculation >= 18.5 and calculation < 25:
                result.config(text="İdeal kilodasınız")
            elif calculation >= 25 and calculation < 30:
                result.config(text="Birinci Obezite sınıfı")
            elif calculation >= 30 and calculation < 40:
                result.config(text="İkinci Obezite sınıfı")
            else:
                result.config(text="Üçüncü Obezite sınıfı")

        except:
            result.config(text="Lütfen geçerli değerler girin!")
    else:
        result.config(text="Lütfen değerleri boş bırakmayın!")


tkinter.Label(window, text="Kilonuz (kg)",font=("Arial", 16,"bold")).pack()
weight = tkinter.Entry(window, font=("Arial",16, "normal"), justify="center", width=10)
weight.pack()
tkinter.Label(window, text="Boyunuz (cm)", font=("Arial", 16, "bold")).pack()
height = tkinter.Entry(window, font=("Arial",16,"normal"), justify="center", width=10)
height.pack()
calculateButton = tkinter.Button(window, text="Hesapla", command=calculate)
calculateButton.pack()
result = tkinter.Label(window, text="", font=("Arial", 16, "bold"), justify="center")
result.pack()


window.mainloop()