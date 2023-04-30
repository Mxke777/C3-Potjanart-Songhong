from tkinter import *
import tkinter as tk


class CurrencyConverterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("แปลงสกุลเงิน")
        self.window.geometry("560x620")
        #ตารางรับค่า-แปลงค่าอุณหภูมิ
        self.dollar_label = tk.Label(self.window, text="ดอลลาร์สหรัฐ(USD)")
        self.dollar_label.grid(row=0, column=0)
        self.thaibaht_label = tk.Label(self.window, text="บาท(THB)")
        self.thaibaht_label.grid(row=1, column=0)
        self.now_label = tk.Label(self.window, text="ราคา ณ วันที่ 30 เมษายน 2566")
        self.now_label.grid(row=2, column=1)
        self.dollar_entry = tk.Entry(self.window)
        self.dollar_entry.grid(row=0, column=1)
        self.thaibaht_entry = tk.Entry(self.window)
        self.thaibaht_entry.grid(row=1, column=1)
        
        #ปุ่มแปลงค่า
        self.convert_button = tk.Button(self.window, text="แปลงค่า", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=1)
        #ปุ่มล้างค่า
        self.reset_button = tk.Button(self.window, text="ล้างค่า", command=self.reset)
        self.reset_button.grid(row=3, column=1, columnspan=1)
        #ใส่รูป
        self.image = tk.PhotoImage(file="logocurrncy.png")
        self.image_label =tk.Label(self.window, image=self.image)
        self.image_label.grid(row=4,column=0 ,columnspan=2)

        self.window.mainloop()
    #ฟังก์ค่าเงิน
    def convert(self):
        dollar = 34.15
        dollar = float(self.dollar_entry.get())
        #แปลงค่าองศาเซลเซียสเป็นองศาฟาเรนไฮต์
        thaibaht = dollar * 34.15
        self.thaibaht_entry.delete(0, tk.END)
        self.thaibaht_entry.insert(0, thaibaht)

    #ฟังก์ชั่นปุ่มรีเซท
    def reset(self):
        self.dollar_entry.delete(0, tk.END)
        self.thaibaht_entry.delete(0, tk.END)
     

app = CurrencyConverterGUI()
