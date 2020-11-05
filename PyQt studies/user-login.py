import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.gorsel()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS uyeler (eposta TEXT,parola TEXT,ad TEXT,"+
            "soyad TEXT,meslek TEXT,yaş TEXT,görevler TEXT)")

        self.baglanti.commit()

    def giris2(self):
        eposta1 = self.kullanici_eposta.text()
        parola1 = self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE eposta=? and parola=?", (eposta1, parola1))

        data = self.cursor.fetchall()

        if len(data) == 0:

            self.yazi_alani.setText("Kullanıcı e-posta veya parola hatalı")

        else:

            self.yazi_alani.setText("HOŞGELDİNİZ")

            Pencere2(self).show()

    def gorsel(self):

        self.kullanici_eposta = QtWidgets.QLineEdit()
        self.kullanici_eposta_yazi = QtWidgets.QLabel("e-posta")
        self.parola = QtWidgets.QLineEdit()
        self.parola_yazi = QtWidgets.QLabel("Parola  ")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.kayit_ol = QtWidgets.QPushButton("Kayıt Ol")
        self.yazi_alani = QtWidgets.QLabel(" yazi alani")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.kullanici_eposta_yazi)
        h_box.addWidget(self.kullanici_eposta)
        h_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.parola_yazi)
        h_box1.addWidget(self.parola)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.kayit_ol)
        h_box2.addStretch()
        h_box2.addWidget(self.giris)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addStretch()
        v_box.addLayout(h_box3)
        v_box.addStretch()
        v_box.addLayout(h_box2)

        self.setLayout(v_box)

        self.kullanici_eposta.setFixedSize(300, 25)
        self.parola.setFixedSize(300, 25)
        self.giris.setFixedSize(100, 25)
        self.kayit_ol.setFixedSize(100, 25)

        self.setWindowTitle("Kullanıcı girişi")

        self.setGeometry(700, 200, 800, 100)
        self.setFixedSize(400, 400)
        self.giris.clicked.connect(self.giris2)

        self.show()


class Pencere2(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.baglanti_olustur()
        self.gorsel()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS uyeler (eposta TEXT,parola TEXT,ad TEXT," +
            "soyad TEXT,meslek TEXT,yaş TEXT,görevler TEXT)")

        self.baglanti.commit()

    def gorsel(self):
        self.eposta = QtWidgets.QLabel("e-posta : ")
        self.ad = QtWidgets.QLabel("Ad : ")
        self.soyad = QtWidgets.QLabel("Soyad : ")
        self.meslek = QtWidgets.QLabel("Meslek : ")
        self.yas = QtWidgets.QLabel("Yaş : ")
        self.gorevler = QtWidgets.QLabel("Görevler : ")

        eposta1 = pencere.kullanici_eposta.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE eposta=?", (eposta1,))

        data = self.cursor.fetchall()
        eposta = data[0][0]
        ad = data[0][2]
        soyad = data[0][3]
        meslek = data[0][4]
        yas = data[0][5]
        gorevler = data[0][6]

        self.epostay = QtWidgets.QLabel("{}".format(eposta))
        self.ady = QtWidgets.QLabel("{}".format(ad))
        self.soyady = QtWidgets.QLabel("{}".format(soyad))
        self.mesleky = QtWidgets.QLabel("{}".format(meslek))
        self.yasy = QtWidgets.QLabel("{}".format(yas))
        self.gorevlery = QtWidgets.QLabel("{}".format(gorevler))

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.eposta)
        h_box.addWidget(self.epostay)
        h_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.ad)
        h_box1.addWidget(self.ady)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.soyad)
        h_box2.addWidget(self.soyady)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.meslek)
        h_box3.addWidget(self.mesleky)
        h_box3.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.yas)
        h_box4.addWidget(self.yasy)
        h_box4.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.gorevler)
        h_box5.addWidget(self.gorevlery)
        h_box5.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addStretch()

        self.setLayout(v_box)

        self.setWindowTitle("Bilgileriniz")



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
