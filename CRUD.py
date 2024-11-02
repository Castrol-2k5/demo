import pandas as pd
from tkinter import messagebox, simpledialog
class Patient:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy file. Vui lòng kiểm tra đường dẫn.")
            
    def read(self):
            return self.df
        
    def save(self):
        try:
            self.df.to_csv(self.file_path, index=False)
            messagebox.showinfo("Thành công", "Lưu dữ liệu thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")    
    
    def create(self):
        # Lấy dữ liệu cho từng cột từ người dùng
        new_data = {}
        for column in self.df.columns:
            value = simpledialog.askstring("Nhập dữ liệu", f"Nhập giá trị cho '{column}':")
            new_data[column] = value
        
        # Thêm dữ liệu mới vào DataFrame
        self.df = self.df.append(new_data, ignore_index=True)
        messagebox.showinfo("Thành công", "Dữ liệu mới đã được thêm vào!")  
        self.save()
        
    def update(self):
         # Yêu cầu người dùng nhập Person ID để tìm hàng cần cập nhật
        person_id = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Person ID của hàng cần cập nhật:")

        # Ép kiểu của `person_id` từ người dùng sao cho khớp với kiểu dữ liệu trong DataFrame
        if pd.api.types.is_integer_dtype(self.df['Person ID']):
            person_id = int(person_id)
        elif pd.api.types.is_float_dtype(self.df['Person ID']):
            person_id = float(person_id)

        if person_id not in self.df['Person ID'].values:
            messagebox.showinfo("Thông báo", f"Không tìm thấy Person ID '{person_id}'. Thêm mới dữ liệu.")
            self.create()  # Gọi hàm "create" để thêm mới dữ liệu
            return

        #cập nhật
        updates = {}
        for column in self.df.columns:
            if column != 'Person ID':  
                new_value = simpledialog.askstring("Cập nhật dữ liệu", f"Nhập giá trị mới cho '{column}' (bỏ qua nếu không thay đổi):")
                if new_value:
                    updates[column] = new_value

        
        for column_name, new_value in updates.items():
            try:
            
                if pd.api.types.is_integer_dtype(self.df[column_name]):
                    new_value = int(new_value)
                elif pd.api.types.is_float_dtype(self.df[column_name]):
                    new_value = float(new_value)
                self.df.loc[self.df['Person ID'] == person_id, column_name] = new_value
            except ValueError:
                messagebox.showerror("Lỗi", f"Giá trị không hợp lệ cho cột '{column_name}'")

        messagebox.showinfo("Thành công", "Cập nhật dữ liệu thành công!")
        self.save()
    
    def delete(self):
        row_id = simpledialog.askstring("Xóa dữ liệu", "Nhập Person ID của hàng cần xóa:")
        
        
        if pd.api.types.is_integer_dtype(self.df['Person ID']):
            row_id = int(row_id)
        elif pd.api.types.is_float_dtype(self.df['Person ID']):
            row_id = float(row_id)

        if row_id not in self.df['Person ID'].values:
            messagebox.showerror("Lỗi", f"Không tìm thấy hàng nào có Person ID '{row_id}'")
            return

        # Xóa hàng theo Person ID
        self.df.drop(self.df[self.df['Person ID'] == row_id].index, inplace=True)
        messagebox.showinfo("Thành công", "Hàng đã được xóa thành công!")
        self.save()
        
    def get_column(self, column_name):
        # Trả về dữ liệu của một cột cụ thể
        if column_name in self.df.columns:
            return self.df[column_name]
        else:
            return f"Cột '{column_name}' không tồn tại trong dữ liệu."

file_path = 'do_an/Sleep_health_and_lifestyle_dataset.csv'
patient = Patient(file_path)

# ví dụ get_column

for i in range(10):
    print(patient.get_column("Occupation")[i])