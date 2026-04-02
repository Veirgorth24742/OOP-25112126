# Tạo các lớp Cán bộ

class CanBo:
    def __init__(self, ten = "", tuoi = int, gioi_tinh = "", dia_chi = ""):
        self.__ten = ten
        self.__tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    def loaiCanBo(self):
        return "Cán Bộ"
    
    def hienThi(self):
        print(f"  Tên cán bộ        :       {self.__ten:<5}\n"
              f"  Tuổi              :       {self.__tuoi:<5}\n"
              f"  Giới tính         :       {self.__gioi_tinh:<5}\n"
              f"  Địa chỉ           :       {self.__dia_chi:<5}")
        
    def __str__(self):
        return(f"{self.loaiCanBo():<10s}   |  {self.__ten}")

    def getTen(self):
        return self.__ten
        
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc phải nằm trong giá trị từ 1 đến 10!")
        self.__bac = bac

    def loaiCanBo(self):
        return "Công Nhân"

    def hienThi(self):
        congNhan = " Công Nhân "
        print(congNhan.center(36, "-"))
        super().hienThi()
        print(f"  Cấp Bậc           :       {self.__bac:<5}")

class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao

    def loaiCanBo(self):
        return "Kỹ Sư"

    def hienThi(self):
        kySu = " Kỹ Sư "
        print(kySu.center(36, "-"))
        super().hienThi()
        print(f"  Ngành Đào Tạo     :       {self.__nganh_dao_tao:<5}")
 
class NhanVienSX(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def loaiCanBo(self):
        return "Nhân Viên"

    def hienThi(self):
        nhanVien = " Nhân Viên "
        print(nhanVien.center(36, "-"))
        super().hienThi()
        print(f"  Công Việc         :       {self.__cong_viec:<5}")

# Tạo lớp quản lý cán bộ

class QuanLyCanBo(CongNhan, KySu, NhanVienSX):
    def __init__(self):
        self.__danhSachCanBo = []

    def themCanBo(self):
        print("\nNhững nghề của cán bộ hiện có:\n"
              "   1. Công Nhân\n"
              "   2. Kỹ Sư\n"
              "   3. Nhân Viên")
        nghe = int(input("Nhập nghề vào đây (1/2/3): ").strip())

        if nghe not in (1, 2, 3):
            print("Lựa chọn không hợp lệ.")
            return
        
        nhapTTin = (" Thêm Cán Bộ ")
        print("\n",nhapTTin.center(40, "="))

        ten = input("Họ tên       : ")
        tuoi = int(input("Tuổi         : "))
        gioi_tinh = input("Giới Tính    : ")
        dia_chi = input("Địa Chỉ      : ")

        if nghe == 1:
            bac = int(input("Nhập cấp bậc (1 - 10): "))
            can_bo = CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)

        elif nghe == 2:
            nganhDTao = input("Nhập ngành đào tạo: ")
            can_bo = KySu(ten, tuoi, gioi_tinh, dia_chi,nganhDTao)

        elif nghe == 3:
            cViec = input("Nhập công việc: ")
            can_bo = NhanVienSX(ten, tuoi, gioi_tinh, dia_chi, cViec)
        
        self.__danhSachCanBo.append(can_bo)
        print(f"\n~> Thêm cán bộ mới thành công!")

    def timKiem(self):
        tenCanTim = input("\nNhập họ tên cần tìm: ").strip().lower()
        ketQua = []
        for can_bo in self.__danhSachCanBo:
            if tenCanTim in can_bo.getTen().lower():
                ketQua.append(can_bo)

        if ketQua:
            print(f"\n~> Tìm thấy {len(ketQua)} cán bộ có tên \"{tenCanTim}\":")
            for can_bo in ketQua:
                can_bo.hienThi()

        else:
            print(f"\n~> Không tìm thấy cán bộ nào mang tên \"{tenCanTim}\".")
            return
        
    def hienThongTin(self):
        if not self.__danhSachCanBo:
            print("\n~> Danh sách trống!")

        else:
            dsCB = "[Danh Sách Cán Bộ Hiện Tại]"
            print("\n",dsCB.center(50, "="))
            for can_bo in self.__danhSachCanBo:
                can_bo.hienThi()

    def trangChu(self):
        while True:
            menu = "[Trang Chủ Danh Sách Quản Lý Cán Bộ]"
            print("\n",menu.center(70,"="))
            print("1 - Thêm mới cán bộ")
            print("2 - Tìm kiếm cán bộ")
            print("3 - Hiển thị danh sách cán bộ hiện tại")
            print("0 - Thoát chương trình")

            luaChon = input("Nhập vào lựa chọn của bạn (1/2/3/0): ").strip()
            if luaChon == "1":
                self.themCanBo()
            elif luaChon == "2":
                self.timKiem()
            elif luaChon == "3":
                self.hienThongTin()
            elif luaChon == "0":
                print("\nTắt chương trình. Hẹn gặp lại!")
                break
            else:
                print("Lựa chọn không hợp lệ!")
                return

if __name__ == "__main__":
    qlcb = QuanLyCanBo()
    qlcb.trangChu()