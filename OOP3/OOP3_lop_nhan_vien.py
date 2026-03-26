class NhanVien:
    LUONG_MAX = 10000000

    def __init__(self, tenNhanVien = str, luongCoBan = float, heSoLuong = float):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    @property
    def tenNhanVien(self):
        return self.__tenNhanVien
    
    @tenNhanVien.setter
    def tenNhanVien(self, value):
        if not value.strip():
            raise ValueError("Tên nhân viên không được để trống!")
        else:
            self.__tenNhanVien = value

    @property
    def luongCoBan(self):
        return self.__luongCoBan

    @luongCoBan.setter
    def luongCoBan(self, value):
        if value <= 0:
            raise ValueError("Lương cơ bản phải là một số dương.")
        else:
            self.__luongCoBan = value

    @property
    def heSoLuong(self):
        return self.__heSoLuong

    @heSoLuong.setter
    def heSoLuong(self, value):
        if value <= 0:
            raise ValueError("Hệ số lương phải lớn hơn 0.")
        else:
            self.__heSoLuong = value

    def tinh_luong(self) -> float:
        luong = self.__luongCoBan * self.__heSoLuong
        return luong

    def inTTin(self):
        luong = self.tinh_luong()
        print(f"""                      Thông Tin Nhân Viên:
              Tên Nhân Viên  : {self.__tenNhanVien:>23}
              Lương Cơ Bản   : {self.__luongCoBan:>20,.0f} VND
              Hệ Số Lương    : {self.__heSoLuong:>20.1f}
              Lương Hiện Tại : {luong:>20,.0f} VND""")
        
    def tang_luong(self, delta: float) -> bool:
        luong = (self.__luongCoBan + delta) * self.__heSoLuong
        if luong > NhanVien.LUONG_MAX:
            print(f"Mức lương mới vượt quá {NhanVien.LUONG_MAX:,.0f} VND. Không thể tăng lương!")
            return False
        else:
            self.__luongCoBan += delta
            print(f"Tăng lương thành công! Lương mới: {luong:,.0f} VND.")
            return True
        
nhanvien = NhanVien("Nguyen Van A", 2000000, 2.5)
nhanvien.inTTin()
nhanvien.tinh_luong()
nhanvien.tang_luong(500000)
nhanvien.tang_luong(15000000)