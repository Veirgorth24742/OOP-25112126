LUONG_CO_BAN = 10000000

class NhanVienPhongBan:
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.__ma_nhan_vien = ma_nhan_vien
        self.__ho_ten = ho_ten
        self.__nam_sinh = nam_sinh
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
        self.__he_so_luong = he_so_luong if he_so_luong > 0 else 1.0
        self.__luong_toi_da = luong_toi_da 
    
    def tinhLuong(self):
        return LUONG_CO_BAN * self.__he_so_luong
    
    def hienThi(self):
        print(f" Mã nhân viên          :       {self.__ma_nhan_vien:<5}\n"
              f" Họ tên                :       {self.__ho_ten:<5}\n"
              f" Năm sinh              :       {self.__nam_sinh:<5}\n"
              f" Giới tính             :       {self.__gioi_tinh:<5}\n"
              f" Địa chỉ               :       {self.__dia_chi:<5}\n"
              f" Hệ số lương           :       {self.__he_so_luong:<5}\n"
              f" Lương                 :       {self.tinhLuong():<5,.0f} VNĐ")
        
class CongTacVien(NhanVienPhongBan):
    HAN_HOP_DONG = ["3 tháng", "6 tháng", "1 năm"]
    
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, 
                 he_so_luong, luong_toi_da, han_hop_dong, phu_cap_ld):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        if han_hop_dong not in CongTacVien.HAN_HOP_DONG:
            raise ValueError(f"Thời hạn hợp đồng phải là {CongTacVien.HAN_HOP_DONG}!")
        self.__han_hop_dong = han_hop_dong
        self.__phu_cap_ld = phu_cap_ld

    def tinhLuong(self):
        return super().tinhLuong() + self.__phu_cap_ld

    def hienThi(self):
        congTacVien = " Cộng Tác Viên "
        print(congTacVien.center(50, "-"))
        super().hienThi()
        print(f" Thời hạn hợp đồng     :       {self.__han_hop_dong:<5}\n"
              f" Phụ cấp lao động      :       {self.__phu_cap_ld:<5,.0f} VNĐ\n")
              
class NhanVienChinhThuc(NhanVienPhongBan):
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh,
                dia_chi, he_so_luong, luong_toi_da, vi_tri_cv):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        self.__vi_tri_cv = vi_tri_cv

    def hienThi(self):
        nvChinhThuc = " Nhân Viên Chính Thức "
        print(nvChinhThuc.center(50, "-"))
        super().hienThi()
        print(f" Vị trí công việc      :       {self.__vi_tri_cv:<5}\n")
        
class TruongPhong(NhanVienPhongBan):
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh,
                dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        self.__ngay_bat_dau_ql = ngay_bat_dau_ql
        self.__phu_cap_ql = phu_cap_ql

    def tinhLuong(self):
        return super().tinhLuong() + self.__phu_cap_ql

    def hienThi(self):
        truongPhong = " Trưởng Phòng "
        print(truongPhong.center(50, "-"))
        super().hienThi()
        print(f" Ngày bắt đầu quản lý  :       {self.__ngay_bat_dau_ql:<5}\n"
              f" Phụ cấp quản lý       :       {self.__phu_cap_ql:<5,.0f} VNĐ\n")


#Test run code
ctv = CongTacVien("25", "Liêm", "2000", "Nam", "HN", 0.25, "", "6 tháng", 1000000)
nvct = NhanVienChinhThuc("63", "Huê", "2003", "Nữ", "LC", 0.6, "", "Kế Toán")
tp = TruongPhong("10", "Thông", "1996", "Nam", "HN", 0.85, "", "20/03/2014", 3000000)
ctv.hienThi()
nvct.hienThi()
tp.hienThi()
        
