class SieuNhan:
    ten = str
    vu_khi = str
    mau_sac = str

    def __init__(self, ten="", vu_khi="", mau_sac=""):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    
    def __str__(self):
        return"Siêu nhân %s, Vũ khí %s, Màu %s" % (self.ten, self.vu_khi, self.mau_sac)

sieunhanA = SieuNhan("A", "Kiếm", "Xanh")
sieunhanB = SieuNhan("B", "Khiên", "Đỏ")

print(sieunhanA,"\n",sieunhanB)