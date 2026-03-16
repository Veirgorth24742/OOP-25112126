class ConCho:
    ten = str
    mauSac = str
    giong = str
    camXuc = str

    def __init__(self, ten, mauSac, giong, camXuc):
        self.ten = ten
        self.mauSac = mauSac
        self.giong = giong
        self.camXuc = camXuc

    def sua(self):
        print(f"{self.ten}: Gâu! Gâu!")

    def vay_duoi(self):
        print(f"{self.ten} đang vẫy đuôi. {self.ten} cảm thấy {self.camXuc}!")

    def an(self, doAn):
        print(f"{self.ten} đang ăn {doAn}.")

    def chay(self, tocDo):
        print(f"{self.ten} đang chạy với tốc độ {tocDo} km/h.")


class OTo:
    hangXe = str
    kichThuoc = int
    mau = str
    gia = int

    def __init__(self, hangXe, kichThuoc, mau, gia):
        self.hangXe = hangXe
        self.kichThuoc = kichThuoc
        self.mau = mau
        self.gia = gia

    def tang_toc(self, tocDo):
        print(f"{self.hangXe} đang tăng tốc lên {tocDo} km/h.")

    def giam_toc(self, tocDo):
        print(f"{self.hangXe} đang giảm tốc xuống {tocDo} km/h.")

    def dam(self, doiTuong):
        print(f"{self.hangXe} đã đâm trúng {doiTuong}!")


class TaiKhoan:
    tenTK = str
    soTK = int
    nganHang = str
    soDu = float
    
    def __init__(self, tenTK, soTK, nganHang, soDu):
        self.tenTK = tenTK
        self.soTK = soTK
        self.nganHang = nganHang
        self.soDu = soDu

    def rut_tien(self, soTien):
        if soTien > self.soDu:
            print(f"Số dư không đủ để rút {soTien} VND!")
        else:
            self.soDu -= soTien
            print(f"Đã rút {soTien} VND. Số dư hiện tại: {self.soDu} VND.")

    def gui_tien(self, soTien):
        self.soDu += soTien
        print(f"Đã gửi {soTien} VND. Số dư hiện tại: {self.soDu} VND.")

    def kiem_tra_so_du(self):
        print(f"Số dư hiện tại của tài khoản {self.tenTK} là: {self.soDu} VND.")


concho = ConCho("Malphite", "Vàng", "Golden Retriever", "vui vẻ")
concho.sua()
concho.vay_duoi()
concho.an("Xương")
concho.chay(20)

oto = OTo("Toyota", 5, "Đỏ", 500000000)
oto.tang_toc(100)
oto.giam_toc(50)
oto.dam("xe máy")

tk = TaiKhoan("Nguyen Van A", 100123456789, "Techcombank", 1000000)
tk.rut_tien(200000)
tk.gui_tien(500000)
tk.kiem_tra_so_du()