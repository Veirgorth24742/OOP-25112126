class NhanVien:
    LUONG_MAX = 10000000
    
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def getTenNhanVien(self):
        return self.__tenNhanVien
    def setTenNhanVien(self, value: str):
        if value.strip() == "":
            raise ValueError("Tên nhân viên không được để trống!")
        else: self.__tenNhanVien = value

    def getLuongCoBan(self):
        return self.__luongCoBan
    def setLuongCoBan(self, value: float):
        if value <= 0:
            raise ValueError("Lương cơ bản phải là một số dương!")
        else: self.__luongCoBan = value

    def getHeSoLuong(self):
        return self.__heSoLuong
    def setHeSoLuong(self, value: float):
        if value <= 0:
            raise ValueError("Hệ số lương phải là một số dương.")
        else: self.__heSoLuong = value

    def tinhLuong(self) -> float:
        luong = self.__luongCoBan * self.__heSoLuong
        return luong
    
    def inTTin(self):
        luong = self.tinhLuong()
        print(f"""                      Thông Tin Nhân Viên:
              Tên Nhân Viên  : {self.__tenNhanVien:>23}
              Lương Cơ Bản   : {self.__luongCoBan:>20,.0f} VND
              Hệ Số Lương    : {self.__heSoLuong:>20.1f}
              Lương Hiện Tại : {luong:>20,.0f} VND""")

    def tangLuong(self, multi: float) -> bool:
        luongMoi = self.__luongCoBan * (self.__heSoLuong + multi)
        if luongMoi > NhanVien.LUONG_MAX:
            print(f"Lương mới vượt quá {NhanVien.LUONG_MAX:,.0f} VND. Không thể tăng lương!")
            return False
        else:
            self.__heSoLuong += multi
            print(f"Tăng lương thành công. Mức lương hiện tại: {luongMoi:,.0f} VND")
            return True
    

# Test code
nhanvien = NhanVien("Nguyen Van A", 5000000, 1.5)
nhanvien.inTTin()
nhanvien.tangLuong(0.5)
