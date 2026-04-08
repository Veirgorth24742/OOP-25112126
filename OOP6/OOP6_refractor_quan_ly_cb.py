# Tạo các lớp Cán bộ

from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__("Độ tuổi đã nhập không hợp lệ (18 - 65)!")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        self.bac = bac
        super().__init__("Bậc không hợp lệ (1 - 10)!")

class CanBo:
    def __init__(self, ten = "", tuoi = int, gioi_tinh = "", dia_chi = ""):
        self.__ten = ten
        self.tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    @property
    def ten(self):
        return self.__ten

    @property
    def gioi_tinh(self):
        return self.__gioi_tinh
    
    @property
    def dia_chi(self):
        return self.__dia_chi
    
    @property
    def tuoi(self):
        return self.__tuoi    
    
    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass
           
    def __str__(self):
        return(f"  Tên cán bộ        :       {self.__ten:<5}\n"
               f"  Tuổi              :       {self.__tuoi:<5}\n"
               f"  Giới tính         :       {self.__gioi_tinh:<5}\n"
               f"  Địa chỉ           :       {self.__dia_chi:<5}\n"
               f"  {self.mo_ta()}")
    
    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__ten}', {self.__tuoi})")
    
    def __eq__(self, other):
        if not isinstance(other, CanBo):
            return NotImplemented
        return self.__ten == other.__ten and self.__tuoi == other.__tuoi

    def __lt__(self, other):
        return self.__ten < other.__ten
        
    def __hash__(self):
        return hash((self.__ten, self.__tuoi))
    
    def getTen(self):
        return self.__ten
        
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self.__bac
            
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value

    def mo_ta(self):
        return f"Công nhân bậc {self.__bac}"

class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"Kỹ sư {self.__nganh_dao_tao}"
 
class NhanVienSX(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên {self.__cong_viec}"

cb1 = CongNhan("Nguyễn Văn A", 30, "Nam", "Hà Nội", 5)
cb2 = KySu("Trần Thị B", 28, "Nữ", "HCM", "CNTT")
cb3 = NhanVienSX("Lê Văn C", 35, "Nam", "Đà Nẵng", "Kế toán")

danhsach =[cb1, cb2, cb3]
for cb in danhsach:
    print(cb)

print("\n---- Sắp xếp theo tên ----")
for cb in sorted(danhsach):
    print(f"  {cb.ten}")

print("\n---- Validation ----")
try:
    CongNhan("X", 15, "Nam", "HN", 5)
except TuoiKhongHopLe as e:
    print(f"  {e}")
try:
    CongNhan("Y", 25, "Nữ", "HN", 15)
except BacKhongHopLe as e:
    print(f"  {e}")

print("\n---- Lưu file ----")
with open("canbo.txt", "w", encoding="utf-8") as f:
    for cb in danhsach:
        f.write(str(cb) + "\n")
print(f"  Đã lưu {len(danhsach)} cán bộ")





# Tạo lớp quản lý cán bộ

# class QuanLyCanBo(CongNhan, KySu, NhanVienSX):
#     def __init__(self):
#         self.__danhSachCanBo = []

#     def themCanBo(self):
#         print("\nNhững nghề của cán bộ hiện có:\n"
#               "   1. Công Nhân\n"
#               "   2. Kỹ Sư\n"
#               "   3. Nhân Viên")
#         nghe = int(input("Nhập nghề vào đây (1/2/3): ").strip())

#         if nghe not in (1, 2, 3):
#             print("Lựa chọn không hợp lệ.")
#             return
        
#         nhapTTin = (" Thêm Cán Bộ ")
#         print("\n",nhapTTin.center(40, "="))

#         ten = input("Họ tên       : ")
#         tuoi = int(input("Tuổi         : "))
#         gioi_tinh = input("Giới Tính    : ")
#         dia_chi = input("Địa Chỉ      : ")

#         if nghe == 1:
#             bac = int(input("Nhập cấp bậc (1 - 10): "))
#             can_bo = CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)

#         elif nghe == 2:
#             nganhDTao = input("Nhập ngành đào tạo: ")
#             can_bo = KySu(ten, tuoi, gioi_tinh, dia_chi,nganhDTao)

#         elif nghe == 3:
#             cViec = input("Nhập công việc: ")
#             can_bo = NhanVienSX(ten, tuoi, gioi_tinh, dia_chi, cViec)
        
#         self.__danhSachCanBo.append(can_bo)
#         print(f"\n~> Thêm cán bộ mới thành công!")

#     def timKiem(self):
#         tenCanTim = input("\nNhập họ tên cần tìm: ").strip().lower()
#         ketQua = []
#         for can_bo in self.__danhSachCanBo:
#             if tenCanTim in can_bo.getTen().lower():
#                 ketQua.append(can_bo)

#         if ketQua:
#             print(f"\n~> Tìm thấy {len(ketQua)} cán bộ có tên \"{tenCanTim}\":")
#             for can_bo in ketQua:
#                 can_bo.hienThi()

#         else:
#             print(f"\n~> Không tìm thấy cán bộ nào mang tên \"{tenCanTim}\".")
#             return
        
#     def hienThongTin(self):
#         if not self.__danhSachCanBo:
#             print("\n~> Danh sách trống!")

#         else:
#             dsCB = "[Danh Sách Cán Bộ Hiện Tại]"
#             print("\n",dsCB.center(50, "="))
#             for can_bo in self.__danhSachCanBo:
#                 can_bo.hienThi()

#     def trangChu(self):
#         while True:
#             menu = "[Trang Chủ Danh Sách Quản Lý Cán Bộ]"
#             print("\n",menu.center(70,"="))
#             print("1 - Thêm mới cán bộ")
#             print("2 - Tìm kiếm cán bộ")
#             print("3 - Hiển thị danh sách cán bộ hiện tại")
#             print("0 - Thoát chương trình")

#             luaChon = input("Nhập vào lựa chọn của bạn (1/2/3/0): ").strip()
#             if luaChon == "1":
#                 self.themCanBo()
#             elif luaChon == "2":
#                 self.timKiem()
#             elif luaChon == "3":
#                 self.hienThongTin()
#             elif luaChon == "0":
#                 print("\nTắt chương trình. Hẹn gặp lại!")
#                 break
#             else:
#                 print("Lựa chọn không hợp lệ!")
#                 return

# if __name__ == "__main__":
    # qlcb = QuanLyCanBo()
    # qlcb.trangChu()