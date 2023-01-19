class sinif:
    a = 5
    b = "ads"
    c = [1, 3, 5]

    def yazdir(self):
        d = 100
        print(d, self.b)

    def yazdir2(self, t):
        self.yazdir()
        print(t)


nesne = sinif()
nesne.yazdir()
nesne.yazdir2("gfdgfd")