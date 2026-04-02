# Tạo lớp hàng hoá

class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.__gia = gia

    def matHang(self):
        return "Loại mặt hàng"

    def __str__(self):
        return (f"{self.matHang()}    |  {self.__ma_hang}")

    def hienThi(self):
        print(f"Mã hàng hoá            :    {self.__ma_hang:<5}\n"
              f"Tên hàng               :    {self.__ten_hang:<5}\n"
              f"Nhà sản xuất           :    {self.__nha_sx:<5}\n"
              f"Giá                    :    {self.__gia:<5}")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_bao_hanh = tg_bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def matHang(self):
        return "Hàng Điện Máy"
    
    def hienThi(self):
        hangDMay = "Hàng Điện Máy"
        print(hangDMay.center(30, "-"))
        super().hienThi()
        print(f"Thời gian bảo hành     :    {self.__tg_bao_hanh:<5}\n"
              f"Điện áp                :    {self.__dien_ap:<5}\n"
              f"Công suất              :    {self.__cong_suat:<5}")
        
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def matHang(self):
        return "Hàng Sành Sứ"
    
    def hienThi(self):
        hangSSu = "Hàng Sành Sứ"
        print(hangSSu.center(30, "-"))
        super().hienThi()
        print(f"Loại nguyên liệu       :    {self.__loai_nguyen_lieu:<5}")
        
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_san_xuat = ngay_san_xuat
        self.__ngay_het_han = ngay_het_han
    def matHang(self):
        return "Hàng Thực Phẩm"
    
    def hienThi(self):
        hangTPham = "Hàng Thực Phẩm"
        print(hangTPham.center(30, "-"))
        super().hienThi()
        print(f"Ngày sản xuất          :    {self.__ngay_san_xuat:<5}\n"
              f"Ngày hết hạn           :    {self.__ngay_het_han:<5}")

# Chương trình tạo mặt hàng

class DanhSachMatHang(HangDienMay,HangSanhSu,HangThucPham):
    def __init__(self):
        self.__danh_sach_mat_hang = []
    
    def themMatHang(self):
        print("\nNhững loại hàng hoá có thể thêm:\n"
              "1 - Hàng Điện Máy\n"
              "2 - Hàng Sành Sứ\n"
              "3 - Hàng Thực Phẩm")
        hang = int(input("Nhập mặt hàng cần thêm vào đây (1/2/3): ").strip())

        if hang not in (1, 2, 3):
            print(f"\nLựa chọn không hợp lệ!")
        
        else:
            nhapMatHang = "Nhập Mặt Hàng Mới"
            print(nhapMatHang.center(30, "="))

            ma_hang = input("Nhập mã hàng             : ")
            ten_hang = input("Nhập tên hàng hoá        : ")
            nha_sx = input("Nhập nhà sản xuất        : ")
            gia = int(input("Nhập giá hàng (VND)      : "))
            
            if hang == 1:
                tg_bao_hanh = input("Nhập thời gian bảo hành  : ")
                dien_ap = input("Nhập mức điện áp         : ")
                cong_suat = input("Nhập công suất chạy      : ")
                h_hoa = HangDienMay(ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap, cong_suat)

            elif hang == 2:
                loai_nguyen_lieu = input("Nhập loại nguyên liệu   : ")
                h_hoa = HangSanhSu(ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu)

            elif hang == 3:
                ngay_san_xuat = input("Ngày sản xuất (dd/mm/yy) : ")
                ngay_het_han = input("Ngày hết hạn (dd/mm/yy)  : ")
                h_hoa = HangThucPham(ma_hang, ten_hang, nha_sx, gia, ngay_san_xuat, ngay_het_han)

            self.__danh_sach_mat_hang.append(h_hoa)
            print(f"\nThêm mặt hàng thành công!")

    def hienDanhSach(self):
        if not self.__danh_sach_mat_hang:
            print(f"\nHiện không có mặt hàng nào.")
            return
        
        else:
            dsMH = "Danh Sách Hàng Hoá"
            print(dsMH.center(60,"="))
            for h_hoa in self.__danh_sach_mat_hang:
                h_hoa.hienThi()

    def trangChu(self):
        while True:
            menu = "[Danh Sách Hàng Hoá]"
            print("\n",menu.center(60,"="))
            print("1 - Thêm mặt hàng mới")
            print("2 - Hiển thị danh sách các mặt hàng hiện tại")
            print("0 - Thoát chương trình")
            luaChon = input("Nhập vào lựa chọn của bạn (1/2/0): ").strip()
            if luaChon == "1":
                self.themMatHang()
            elif luaChon == "2":
                self.hienDanhSach()
            elif luaChon == "0":
                print("\nTắt chương trình. Hẹn gặp lại!")
                break
            else:
                print("Lựa chọn không hợp lệ!")
                
            
if __name__ == "__main__":
    danhSachMatHang = DanhSachMatHang()
    danhSachMatHang.trangChu()