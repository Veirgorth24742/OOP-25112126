from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá {gia} không hợp lệ! Giá phải > 0!")

class MaHangTrungLap(Exception):
    def __init__(self, ma_hang, ten):
        self.ma_hang = ma_hang
        self.ten = ten
        super().__init__(f"Mã hàng hoá {ma_hang} - {ten} bị trùng lặp giữa các sản phẩm! Vui lòng sử dụng một mã khác.")

class HangHoa(ABC):
    maHangDaDung = set()

    def __init__(self, ma_hang, ten, nha_sx, gia):
        self.__ten = ten
        self.__nha_sx = nha_sx
        self.ma_hang = ma_hang
        self.gia = gia

    @property
    def ma_hang(self):
        return self.__ma_hang

    @property
    def ten(self):
        return self.__ten
    
    @property
    def ngay_sx(self):
        return self.__nha_sx
    
    @property
    def gia(self):
        return self.__gia
    
    @gia.setter
    def gia(self, value):
        if value <= 0:
            raise GiaKhongHopLe(value)
        self.__gia = value

    @ma_hang.setter
    def ma_hang(self, value):
        if getattr(self, 'HangHoa__ma_hang', None) == value:
            return
        
        if value in HangHoa.maHangDaDung:           #Phát hiện trùng lặp mã hàng
            raise MaHangTrungLap(value, self.__ten)
        
        old_value = getattr(self, 'HangHoa__ma_hang', None)
        if old_value is not None:
            HangHoa.maHangDaDung.discard(old_value)
        HangHoa.maHangDaDung.add(value)
        self.__ma_hang = value
    
    @abstractmethod
    def loaiHang(self):
        pass

    def hienThi(self):
        return (f"[{self.loaiHang()}]  Mã hàng hoá: {self.__ma_hang}  |  Tên hàng: {self.__ten}  |"
                f"  Nhà sản xuất: {self.__nha_sx}  |  Giá: {self.__gia:,.0f} VNĐ")
        
    def __str__(self):
        return self.hienThi()
    
    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__ma_hang}', "
                f"'{self.__ten}', '{self.__nha_sx}', {self.__gia})")
    
    def __eq__(self, other):
        if not isinstance(other, HangHoa):
            return NotImplemented
        return self.__ma_hang == other.__ma_hang

    def __lt__(self, other):
        return self.__gia < other.__gia
        
    def __hash__(self):
        return hash(self.__ma_hang)

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten, nha_sx, gia)
        self.__bao_hanh = bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def loaiHang(self):
        return "Điện Máy "
    
    def hienThi(self):
        return (f"{super().hienThi()}  |  Thời gian bảo hành: {self.__bao_hanh}  |"
                f"  Điện áp: {self.__dien_ap} V |  Công suất: {self.__cong_suat} W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten, nha_sx, gia)
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def loaiHang(self):
        return " Sành Sứ "
    
    def hienThi(self):
        return (f"{super().hienThi()}  |  Loại nguyên liệu: {self.__loai_nguyen_lieu}")
    
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten, nha_sx, gia, ngay_sx, ngay_hh):
        super().__init__(ma_hang, ten, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hh = ngay_hh

    def loaiHang(self):
        return "Thực Phẩm"
    
    def hienThi(self):
        return (f"{super().hienThi()}  |  Ngày sản xuất: {self.__ngay_sx}"
                f"  |  Ngày hết hạn: {self.__ngay_hh}")
    
sp1 = HangDienMay("DM1", "Tủ Lạnh", "LG", 11_000_000, "24 tháng", 220, 150)
sp2 = HangSanhSu("SS1", "Bát Sứ", "Bát Tràng", 400_000, "Sứ cao cấp")
sp3 = HangThucPham("TP1", "CocaCola", "PepsiCola", 10_000, "2025-01-01", "2026-07-01")

kho = [sp1, sp2, sp3]
for sp in kho:
    print(sp)

print("\n---- Sắp xếp theo giá ----")
for sp in sorted(kho):
    print(f"  {sp.gia:>12,.0f}đ | {sp.ten}")

print("\n---- So sánh / Loại trùng ----")
try:
    sp1_copy = HangDienMay("DM01", "Tủ Lạnh", "LG", 12_000_000, 24, 220, 150)
    print(f"  sp1 == sp1_copy? {sp1 == sp1_copy}")
    print(f"  Set loại trùng: {len([sp1, sp2, sp1_copy])} -> {len(set([sp1, sp2, sp1_copy]))}")
except MaHangTrungLap as e:
    print(f"  Bắt lỗi trùng lặp: {e}")

print("\n---- Validation ----")
try:
    sp_loi = HangDienMay("DM99", "Test", "X", -5000, 12, 220, 50)
except GiaKhongHopLe as e:
    print(f"  Bắt lỗi: {e}")

try:
    h = HangHoa("X", "Test", "Y", 100)
except TypeError as e:
    print(f"  ABC: {e}")

print("\n---- Lưu file ----")
with open("kho_hang.txt", "w", encoding="utf-8") as f:
    for sp in kho:
        f.write(repr(sp) + "\n")
print(f"  Đã lưu {len(kho)} sản phẩm") 