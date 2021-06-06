import pymssql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import * 
import tkinter.messagebox as messagebox 
from PIL import Image, ImageTk

#主界面
class StartPage:
	def __init__(self, parent_window):
		parent_window.destroy() 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('出版社信息管理系统')
		self.window.geometry('960x540+280+140')
		label = Label(self.window, text="出版社信息管理系统", font=("腾祥爱情体简", 30), width=30, height=2)
		label.place(x=480, y=100, anchor='center') 
 
		b1 = tk.Button(self.window, text="登陆", font=("腾祥爱情体简", 16), command=lambda: loginPage(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2 = tk.Button(self.window, text="关于", font=("腾祥爱情体简", 16), command=lambda: AboutPage(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b3 = tk.Button(self.window, text='退出', height=2, font=("腾祥爱情体简", 16), width=15, command=self.window.destroy,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b1.place(x=196, y=400, anchor='center')
		b2.place(x=480, y=400, anchor='center')
		b3.place(x=764, y=400, anchor='center')

		self.window.mainloop()
 
# 登陆界面
class loginPage:
	def __init__(self, parent_window):
		parent_window.destroy() 
 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('正在登陆')
		self.window.geometry('960x540+280+140')
 
		label = tk.Label(self.window, text='请选择登陆方式', font=('腾祥爱情体简', 30), width=30, height=2)
		label.place(x=480, y=50, anchor='center')
		b1 = tk.Button(self.window, text="管理员登陆", font=("腾祥爱情体简", 16), command=lambda: AdminPage(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2 = tk.Button(self.window, text="作者登陆", font=("腾祥爱情体简", 16), command=lambda: writer_login(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b3 = tk.Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b1.place(x=480, y=150, anchor='center')
		b2.place(x=480, y=250, anchor='center')
		b3.place(x=480, y=350, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()

	def back(self):
		StartPage(self.window)

# 管理员登陆界面
class AdminPage:
	def __init__(self, parent_window):
		parent_window.destroy() 
 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('管理员登陆页面')
		self.window.geometry('960x540+280+140')
 
		label = tk.Label(self.window, text='管理员登陆', font=('腾祥爱情体简', 30), width=30, height=2)
		label.place(x=480, y=50, anchor='center')
 
		l1 = Label(self.window, text='↓账号↓', font=("腾祥爱情体简", 14))
		l1.place(x=480, y=150, anchor='center')
		self.admin_username = tk.Entry(self.window, width=30, font=("腾祥爱情体简", 14), bg='Ivory')
		self.admin_username.place(x=480, y=200, anchor='center')
 
		l2 = Label(self.window, text='↓密码↓', font=("腾祥爱情体简", 14))
		l2.place(x=480, y=250, anchor='center')
		self.admin_pass = tk.Entry(self.window, width=30, font=("腾祥爱情体简", 14), bg='Ivory', show='*')
		self.admin_pass.place(x=480, y=300, anchor='center')
 
		b1 = Button(self.window, text="登陆", font=("腾祥爱情体简", 16), command=self.login, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2 = Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2.place(x=320, y=400, anchor='center')
		b1.place(x=640, y=400, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()
 
	def login(self):
		print(str(self.admin_username.get()))
		print(str(self.admin_pass.get()))
		admin_pass = None
 
		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy',charset='UTF-8')
		cursor = db.cursor()
		sql = "SELECT * FROM book_admin WHERE admin_id = '%s'" % (self.admin_username.get())
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				admin_id = row[0]
				admin_pass = row[1]
		except:
			messagebox.showinfo('ERROR', '用户名或密码不正确')
		db.close()
		if self.admin_pass.get() == admin_pass:
			AdminManage(self.window)
		else:
			messagebox.showinfo('ERROR', '用户名或密码不正确')
 
	def back(self):
		loginPage(self.window)

# 作者登陆界面
class writer_login:
	def __init__(self, parent_window):
		parent_window.destroy() 
 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('作者登陆页面')
		self.window.geometry('960x540+280+140')
 
		label = tk.Label(self.window, text='作者登陆', font=('腾祥爱情体简', 30), width=30, height=2)
		label.place(x=480, y=50, anchor='center')
 
		l1 = Label(self.window, text='↓作者姓名↓', font=("腾祥爱情体简", 14))
		l1.place(x=480, y=150, anchor='center')
		self.writer_username = tk.Entry(self.window, width=30, font=("腾祥爱情体简", 14), bg='Ivory')
		self.writer_username.place(x=480, y=200, anchor='center')
 
		l2 = Label(self.window, text='↓密码↓', font=("腾祥爱情体简", 14))
		l2.place(x=480, y=250, anchor='center')
		self.writer_pass = tk.Entry(self.window, width=30, font=("腾祥爱情体简", 14), bg='Ivory', show='*')
		self.writer_pass.place(x=480, y=300, anchor='center')
 
		b1 = Button(self.window, text="登陆", font=("腾祥爱情体简", 16), command=self.login, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2 = Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2.place(x=320, y=400, anchor='center')
		b1.place(x=640, y=400, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()

	def login(self):
		writer_pass = None

		file = open('name.txt', 'w')
		x = str(self.writer_username.get())
		file.write(x)
		file.close()

		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy',charset='UTF-8')
		cursor = db.cursor()
		sql = "SELECT * FROM book_writer WHERE writer_id = '%s'" % (self.writer_username.get())
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				writer_id = row[0]
				writer_pass = row[1]
		except:
			messagebox.showinfo('ERROR', '用户名或密码不正确')
		db.close()
		if self.writer_pass.get() == writer_pass:
			writerManage(self.window)
		else:
			messagebox.showinfo('ERROR', '用户名或密码不正确')

	def back(self):
		loginPage(self.window)

# 作者信息查询界面
class writerManage(writer_login):
	def __init__(self, parent_window):
		parent_window.destroy() 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		file = open("name.txt", "r")
		writer_username = file.read()
		file.close()

		self.window.title('作者信息显示')
		self.window.geometry('960x540+280+140')
		label2 = tk.Label(self.window, text='您好'+ writer_username + '，您的稿费信息为', font=('腾祥爱情体简', 30), width=30, height=2)
		label2.place(x=480, y=50, anchor='center')
		b3 = Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b3.place(x=480, y=400, anchor='center')

		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
		cursor = db.cursor()
		sql1 = "SELECT * FROM book where book.writer = '%s'" % (writer_username)
		try:
			cursor.execute(sql1)
			results = cursor.fetchall()
			for row in results:
				self.bno = row[0]
				self.bname =  row[1]
		except:
			messagebox.showinfo('ERROR', '数据查询失败')
		db.close()

		l3 = Label(self.window, text=self.bno, font=('腾祥爱情体简', 15))
		l4 = Label(self.window, text=self.bname, font=('腾祥爱情体简', 15))
		l3.place(x=540, y=200, anchor='center')
		l4.place(x=540, y=240, anchor='center')

		a = self.bno
		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
		cursor = db.cursor()
		sql2 = "SELECT * FROM sell where sell.bno = '%s'" % (a)
		try:
			cursor.execute(sql2)
			results = cursor.fetchall()
			for row in results:
				self.sellnum = row[1]
				self.sellcheck = row[2]
		except:
			messagebox.showinfo('ERROR', '数据查询失败')
		db.close()

		l5 = Label(self.window, text=self.sellnum, font=('腾祥爱情体简', 15))
		l6 = Label(self.window, text=self.sellcheck, font=('腾祥爱情体简', 15))
		l5.place(x=540, y=280, anchor='center')
		l6.place(x=540, y=320, anchor='center')

		l7 = Label(self.window, text='编号：', font=('腾祥爱情体简', 15))
		l8 = Label(self.window, text='图书名：', font=('腾祥爱情体简', 15))
		l9 = Label(self.window, text='销量：', font=('腾祥爱情体简', 15))
		l10 = Label(self.window, text='稿费：', font=('腾祥爱情体简', 15))
		l7.place(x=420, y=200, anchor='center')
		l8.place(x=420, y=240, anchor='center')
		l9.place(x=420, y=280, anchor='center')
		l10.place(x=420, y=320, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()

	def back(self):
		writer_login(self.window)

# 系统选择界面
class AdminManage:
	def __init__(self, parent_window):
		parent_window.destroy() 
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('系统选择页面')
		self.window.geometry('960x540+280+140')
		label = tk.Label(self.window, text='请选择要管理的系统', font=('腾祥爱情体简', 30), width=30, height=2)
		label.place(x=480, y=50, anchor='center')
		b1 = tk.Button(self.window, text="图书信息管理", font=("腾祥爱情体简", 16), command=lambda: AdminManage_book(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b2 = tk.Button(self.window, text="入库信息管理", font=("腾祥爱情体简", 16), command=lambda: AdminManage_ruku(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b3 = tk.Button(self.window, text='稿费信息管理', font=("腾祥爱情体简", 16), command=lambda: AdminManage_sell(self.window), width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b4 = tk.Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=15, height=2,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b1.place(x=196, y=250, anchor='center')
		b2.place(x=480, y=250, anchor='center')
		b3.place(x=764, y=250, anchor='center')
		b4.place(x=480, y=400, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()

	def back(self):
		loginPage(self.window)

# 图书信息操作界面
class AdminManage_book:
	def __init__(self, parent_window):
		parent_window.destroy()
		self.window = Tk()
		self.window.title('管理员操作界面')
		self.window.geometry('960x540+280+140')
		self.window.resizable(False, False)
		b1 = Label(self.window, text="图书信息管理", font=('腾祥爱情体简', 20))
		b1.place(x=480, y=30, anchor='center')
 
		self.frame_left_top = tk.Frame(width=600, height=200)
		self.frame_right_top = tk.Frame(width=300, height=200)
		self.frame_center = tk.Frame(width=500, height=700)
		self.frame_bottom = tk.Frame(width=650, height=0)

		self.columns = ("编号", "书名", "作者", "出版日期", "价格", "版次", "类型")
		self.tree = ttk.Treeview(self.frame_center, show="headings", height=7, columns=self.columns)
		self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.vbar.set)
 
		self.tree.column("编号", width=50, anchor='center')
		self.tree.column("书名", width=100, anchor='center')
		self.tree.column("作者", width=80, anchor='center')
		self.tree.column("出版日期", width=100, anchor='center')
		self.tree.column("价格", width=50, anchor='center')
		self.tree.column("版次", width=50, anchor='center')
		self.tree.column("类型", width=50, anchor='center')
 
		self.tree.grid(row=0, column=0, sticky=NSEW)
		self.vbar.grid(row=0, column=1, sticky=NS)
 
		self.bno = []
		self.bname = []
		self.writer = []
		self.chubandate = []
		self.price = []
		self.banci = []
		self.type = []

		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
		cursor = db.cursor()
		sql = "SELECT * FROM book"
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				self.bno.append(row[0])
				self.bname.append(row[1])
				self.writer.append(row[2])
				self.chubandate.append(row[3])
				self.price.append(row[4])
				self.banci.append(row[5])
				self.type.append(row[6])
		except:
			messagebox.showinfo('ERROR', '列表数据导入失败')
		db.close()
 
		for i in range(min(len(self.bno), len(self.bname), len(self.writer), len(self.chubandate), len(self.price), len(self.banci), len(self.type))): 
			self.tree.insert('', i, values=(self.bno[i], self.bname[i], self.writer[i], self.chubandate[i], self.price[i], self.banci[i], self.type[i]))
 
		for col in self.columns:
			self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
 
		# 左上信息
		self.left_top_frame = tk.Frame(self.frame_left_top)
		self.var_bno = StringVar()
		self.var_bname = StringVar()
		self.var_writer = StringVar()
		self.var_chubandate = StringVar()
		self.var_price = StringVar()
		self.var_banci = StringVar()
		self.var_type = StringVar()

		# 编号
		self.right_top_bno_label = Label(self.frame_left_top, text="编号", font=('腾祥爱情体简', 15))
		self.right_top_bno_entry = Entry(self.frame_left_top, textvariable=self.var_bno, font=('腾祥爱情体简', 15))
		self.right_top_bno_label.grid(row=1, column=0)
		self.right_top_bno_entry.grid(row=1, column=1)
		# 书名
		self.right_top_bname_label = Label(self.frame_left_top, text="书名", font=('腾祥爱情体简', 15))
		self.right_top_bname_entry = Entry(self.frame_left_top, textvariable=self.var_bname, font=('腾祥爱情体简', 15))
		self.right_top_bname_label.grid(row=2, column=0)
		self.right_top_bname_entry.grid(row=2, column=1)
		# 作者
		self.right_top_writer_label = Label(self.frame_left_top, text="作者", font=('腾祥爱情体简', 15))
		self.right_top_writer_entry = Entry(self.frame_left_top, textvariable=self.var_writer, font=('腾祥爱情体简', 15))
		self.right_top_writer_label.grid(row=3, column=0)
		self.right_top_writer_entry.grid(row=3, column=1)
		# 出版日期
		self.right_top_chubandate_label = Label(self.frame_left_top, text="出版日期", font=('腾祥爱情体简', 15))
		self.right_top_chubandate_entry = Entry(self.frame_left_top, textvariable=self.var_chubandate, font=('腾祥爱情体简', 15))
		self.right_top_chubandate_label.grid(row=4, column=0)
		self.right_top_chubandate_entry.grid(row=4, column=1)
		# 价格
		self.right_top_price_label = Label(self.frame_left_top, text="价格", font=('腾祥爱情体简', 15))
		self.right_top_price_entry = Entry(self.frame_left_top, textvariable=self.var_price, font=('腾祥爱情体简', 15))
		self.right_top_price_label.grid(row=5, column=0)
		self.right_top_price_entry.grid(row=5, column=1) 
		# 版次
		self.right_top_banci_label = Label(self.frame_left_top, text="版次", font=('腾祥爱情体简', 15))
		self.right_top_banci_entry = Entry(self.frame_left_top, textvariable=self.var_banci, font=('腾祥爱情体简', 15))
		self.right_top_banci_label.grid(row=6, column=0)
		self.right_top_banci_entry.grid(row=6, column=1)
		# 类型
		self.right_top_type_label = Label(self.frame_left_top, text="类型", font=('腾祥爱情体简', 15))
		self.right_top_type_entry = Entry(self.frame_left_top, textvariable=self.var_type, font=('腾祥爱情体简', 15))
		self.right_top_type_label.grid(row=7, column=0)
		self.right_top_type_entry.grid(row=7, column=1)

		# 操作按钮
		self.right_top_title = Label(self.frame_right_top, text="请选择操作", font=('腾祥爱情体简', 15))
		self.tree.bind('<Button-1>', self.click)
		self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建信息', width=20, command=self.new_row)
		self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新信息', width=20, command=self.updata_row)
		self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除信息', width=20, command=self.del_row)
		self.right_top_title.grid(row=1, column=0, pady=10)
		self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
		self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
		self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
 
		# 布局
		self.frame_left_top.grid(row=0, column=0, padx=60, pady=50)
		self.frame_right_top.grid(row=0, column=1, padx=0, pady=30)
		self.frame_center.grid(row=3, column=0, columnspan=2)
		self.frame_bottom.grid(row=2, column=0, columnspan=2)
 
		self.frame_left_top.grid_propagate(0)
		self.frame_right_top.grid_propagate(0)
		self.frame_center.grid_propagate(0)
		self.frame_bottom.grid_propagate(0)
 
		self.frame_left_top.tkraise()
		self.frame_right_top.tkraise()
		self.frame_center.tkraise()
		self.frame_bottom.tkraise()

		b4 = tk.Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=7, height=1,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b4.place(x=850, y=450, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)  
		self.window.mainloop()

	def back(self):
		AdminManage(self.window)

	def click(self, event):
		self.col = self.tree.identify_column(event.x)
		self.row = self.tree.identify_row(event.y)
 
		print(self.col)
		print(self.row)
		self.row_info = self.tree.item(self.row, "values")
		self.var_bno.set(self.row_info[0])
		self.var_bname.set(self.row_info[1])
		self.var_writer.set(self.row_info[2])
		self.var_chubandate.set(self.row_info[3])
		self.var_price.set(self.row_info[4])
		self.var_banci.set(self.row_info[5])
		self.var_type.set(self.row_info[6])
		self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_bno, font=('腾祥爱情体简', 15))
 
	def tree_sort_column(self, tv, col, reverse):
		l = [(tv.set(k, col), k) for k in tv.get_children('')]
		l.sort(reverse=reverse)
		for index, (val, k) in enumerate(l):
			tv.move(k, '', index)
		tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

	#添加数据
	def new_row(self):
		print(self.var_bno.get())
		print(self.bno)
		if str(self.var_bno.get()) in self.bno:
			messagebox.showinfo('ERROR', '该图书已存在')
		else:
			if self.var_bno.get() != '' and self.var_bname.get() != '' and self.var_writer.get() != '' and self.var_chubandate.get() != '' and self.var_price.get() != '' and self.var_banci.get() != '' and self.var_type.get() != '':
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "INSERT INTO book(bno, bname, writer, chubandate,price,banci,type) \
				       VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
					  (self.var_bno.get(), self.var_bname.get(), self.var_writer.get(), self.var_chubandate.get(), self.var_price.get(), self.var_banci.get(), self.var_type.get())
				try:
					cursor.execute(sql)
					db.commit()
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据修改失败')
				db.close()
 
				self.bno.append(self.var_bno.get())
				self.bname.append(self.var_bname.get())
				self.writer.append(self.var_writer.get())
				self.chubandate.append(self.var_chubandate.get())
				self.price.append(self.var_price.get())
				self.banci.append(self.var_banci.get())
				self.type.append(self.var_type.get())
				self.tree.insert('', len(self.bno) - 1, values=(
				self.bno[len(self.bno) - 1], self.bname[len(self.bno) - 1], self.writer[len(self.bno) - 1],
				self.chubandate[len(self.bno) - 1], self.price[len(self.bno) - 1], self.banci[len(self.bno) - 1], self.type[len(self.bno) - 1]))
				self.tree.update()
				messagebox.showinfo('恭喜', '插入成功')
			else:
				messagebox.showinfo('ERROR', '图书数据未成功填写')
	
	#更新数据
	def updata_row(self):
		res = messagebox.askyesnocancel('请确认', '是否更新所填数据？')
		if res == True:
			if self.var_bno.get() == self.row_info[0]:
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "UPDATE book SET bname = '%s', writer = '%s', chubandate = '%s', price = '%s', banci = '%s', type = '%s' \
				 WHERE bno = '%s'" % (self.var_bname.get(), self.var_writer.get(), self.var_chubandate.get(), self.var_price.get(), self.var_banci.get(), self.var_type.get(), self.var_bno.get())
				try:
					cursor.execute(sql)
					db.commit()
					messagebox.showinfo('恭喜', '更新成功')
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据更新失败')
				db.close()
 
				bno_index = self.bno.index(self.row_info[0])
				self.bname[bno_index] = self.var_bname.get()
				self.writer[bno_index] = self.var_writer.get()
				self.chubandate[bno_index] = self.var_chubandate.get()
				self.price[bno_index] = self.var_price.get()
				self.banci[bno_index] = self.var_banci.get()
				self.type[bno_index] = self.var_type.get()
 
				self.tree.item(self.tree.selection()[0], values=(
					self.var_bno.get(), self.var_bname.get(), self.var_writer.get(),
					self.var_chubandate.get(), self.var_price.get(), self.var_banci.get(), self.var_type.get()))
			else:
				messagebox.showinfo('ERROR', '不能修改图书编号')

	#删除数据
	def del_row(self):
		res = messagebox.askyesnocancel('请确认', '是否删除所选数据？')
		if res == True:
			print(self.row_info[0])
			print(self.tree.selection()[0])
			print(self.tree.get_children())
			db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
			cursor = db.cursor()
			sql1 = "DELETE FROM book WHERE bno = '%s'" % (self.row_info[0])
			sql2 = "DELETE FROM ruku WHERE bno = '%s'" % (self.row_info[0])
			sql3 = "DELETE FROM sell WHERE bno = '%s'" % (self.row_info[0])
			try:
				cursor.execute(sql1)
				cursor.execute(sql2)
				cursor.execute(sql3)
				db.commit()
				messagebox.showinfo('恭喜', '删除成功')
			except:
				db.rollback()
				messagebox.showinfo('ERROR', '数据删除失败')
			db.close()
 
			bno_index = self.bno.index(self.row_info[0])
			print(bno_index)
			del self.bno[bno_index]
			del self.bname[bno_index]
			del self.writer[bno_index]
			del self.chubandate[bno_index]
			del self.price[bno_index]
			del self.banci[bno_index]
			del self.type[bno_index]
			print(self.bno)
			self.tree.delete(self.tree.selection()[0])
			print(self.tree.get_children())

# 入库信息操作界面
class AdminManage_ruku:
	def __init__(self, parent_window):
		parent_window.destroy()
		self.window = Tk()
		self.window.title('管理员操作界面')
		self.window.geometry('960x540+280+140')
		self.window.resizable(False, False)
		b1 = Label(self.window, text="入库信息管理", font=('腾祥爱情体简', 20))
		b1.place(x=480, y=30, anchor='center')
 
		self.frame_left_top = tk.Frame(width=600, height=200)
		self.frame_right_top = tk.Frame(width=300, height=200)
		self.frame_center = tk.Frame(width=500, height=700)
		self.frame_bottom = tk.Frame(width=650, height=0)

		self.columns = ("编号", "入库日期", "入库数量", "仓库名称")
		self.tree = ttk.Treeview(self.frame_center, show="headings", height=7, columns=self.columns)
		self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.vbar.set)
 
		self.tree.column("编号", width=50, anchor='center')
		self.tree.column("入库日期", width=100, anchor='center')
		self.tree.column("入库数量", width=100, anchor='center')
		self.tree.column("仓库名称", width=100, anchor='center')
 
		self.tree.grid(row=0, column=0, sticky=NSEW)
		self.vbar.grid(row=0, column=1, sticky=NS)
 
		self.bno = []
		self.rukudate = []
		self.num = []
		self.depname = []

		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
		cursor = db.cursor()
		sql = "SELECT * FROM ruku"
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				self.bno.append(row[0])
				self.rukudate.append(row[1])
				self.num.append(row[2])
				self.depname.append(row[3])
		except:
			messagebox.showinfo('ERROR', '列表数据导入失败')
		db.close()
 
		for i in range(min(len(self.bno), len(self.rukudate), len(self.num), len(self.depname))): 
			self.tree.insert('', i, values=(self.bno[i], self.rukudate[i], self.num[i], self.depname[i]))
 
		for col in self.columns:
			self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
 
		# 左上信息
		self.left_top_frame = tk.Frame(self.frame_left_top)
		self.var_bno = StringVar()
		self.var_rukudate = StringVar()
		self.var_num = StringVar()
		self.var_depname = StringVar()

		# 编号
		self.right_top_bno_label = Label(self.frame_left_top, text="编号", font=('腾祥爱情体简', 15))
		self.right_top_bno_entry = Entry(self.frame_left_top, textvariable=self.var_bno, font=('腾祥爱情体简', 15))
		self.right_top_bno_label.grid(row=1, column=0)
		self.right_top_bno_entry.grid(row=1, column=1)
		# 入库时间
		self.right_top_rukudate_label = Label(self.frame_left_top, text="入库时间", font=('腾祥爱情体简', 15))
		self.right_top_rukudate_entry = Entry(self.frame_left_top, textvariable=self.var_rukudate, font=('腾祥爱情体简', 15))
		self.right_top_rukudate_label.grid(row=2, column=0)
		self.right_top_rukudate_entry.grid(row=2, column=1)
		# 入库数量
		self.right_top_num_label = Label(self.frame_left_top, text="入库数量", font=('腾祥爱情体简', 15))
		self.right_top_num_entry = Entry(self.frame_left_top, textvariable=self.var_num, font=('腾祥爱情体简', 15))
		self.right_top_num_label.grid(row=3, column=0)
		self.right_top_num_entry.grid(row=3, column=1)
		# 仓库名称
		self.right_top_depname_label = Label(self.frame_left_top, text="仓库名称", font=('腾祥爱情体简', 15))
		self.right_top_depname_entry = Entry(self.frame_left_top, textvariable=self.var_depname, font=('腾祥爱情体简', 15))
		self.right_top_depname_label.grid(row=4, column=0)
		self.right_top_depname_entry.grid(row=4, column=1)

		# 操作按钮
		self.right_top_title = Label(self.frame_right_top, text="请选择操作", font=('腾祥爱情体简', 15))
		self.tree.bind('<Button-1>', self.click)
		self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建信息', width=20, command=self.new_row)
		self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新信息', width=20, command=self.updata_row)
		self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除信息', width=20, command=self.del_row)
		self.right_top_title.grid(row=1, column=0, pady=10)
		self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
		self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
		self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
 
		# 布局
		self.frame_left_top.grid(row=0, column=0, padx=60, pady=50)
		self.frame_right_top.grid(row=0, column=1, padx=0, pady=30)
		self.frame_center.grid(row=3, column=0, columnspan=2)
		self.frame_bottom.grid(row=2, column=0, columnspan=2)
 
		self.frame_left_top.grid_propagate(0)
		self.frame_right_top.grid_propagate(0)
		self.frame_center.grid_propagate(0)
		self.frame_bottom.grid_propagate(0)
 
		self.frame_left_top.tkraise()
		self.frame_right_top.tkraise()
		self.frame_center.tkraise()
		self.frame_bottom.tkraise()

		b4 = tk.Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=7, height=1,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b4.place(x=850, y=450, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)  
		self.window.mainloop()

	def back(self):
		AdminManage(self.window)

	def click(self, event):
		self.col = self.tree.identify_column(event.x)
		self.row = self.tree.identify_row(event.y)
 
		print(self.col)
		print(self.row)
		self.row_info = self.tree.item(self.row, "values")
		self.var_bno.set(self.row_info[0])
		self.var_rukudate.set(self.row_info[1])
		self.var_num.set(self.row_info[2])
		self.var_depname.set(self.row_info[3])
		self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_bno, font=('腾祥爱情体简', 15))
 
	def tree_sort_column(self, tv, col, reverse):
		l = [(tv.set(k, col), k) for k in tv.get_children('')]
		l.sort(reverse=reverse)
		for index, (val, k) in enumerate(l):
			tv.move(k, '', index)
		tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

	#添加数据
	def new_row(self):
		print(self.var_bno.get())
		print(self.bno)
		if str(self.var_bno.get()) in self.bno:
			messagebox.showinfo('ERROR', '该图书已存在')
		else:
			if self.var_bno.get() != '' and self.var_rukudate.get() != '' and self.var_num.get() != '' and self.var_depname.get() != '':
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "INSERT INTO ruku(bno, rukudate, num, depname) \
				       VALUES ('%s', '%s', '%s', '%s')" % \
					  (self.var_bno.get(), self.var_rukudate.get(), self.var_num.get(), self.var_depname.get())
				try:
					cursor.execute(sql)
					db.commit()
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据修改失败')
				db.close()
 
				self.bno.append(self.var_bno.get())
				self.rukudate.append(self.var_rukudate.get())
				self.num.append(self.var_num.get())
				self.depname.append(self.var_depname.get())
				self.tree.insert('', len(self.bno) - 1, values=(self.bno[len(self.bno) - 1], self.rukudate[len(self.bno) - 1], self.num[len(self.bno) - 1],self.depname[len(self.bno) - 1]))
				self.tree.update()
				messagebox.showinfo('恭喜', '插入成功')
			else:
				messagebox.showinfo('ERROR', '图书数据未成功填写')
	
	#更新数据
	def updata_row(self):
		res = messagebox.askyesnocancel('请确认', '是否更新所填数据？')
		if res == True:
			if self.var_bno.get() == self.row_info[0]:
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "UPDATE ruku SET rukudate = '%s', num = '%s', depname = '%s' \
				 WHERE bno = '%s'" % (self.var_rukudate.get(), self.var_num.get(), self.var_depname.get(), self.var_bno.get())
				try:
					cursor.execute(sql)
					db.commit()
					messagebox.showinfo('恭喜', '更新成功')
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据更新失败')
				db.close()
 
				bno_index = self.bno.index(self.row_info[0])
				self.rukudate[bno_index] = self.var_rukudate.get()
				self.num[bno_index] = self.var_num.get()
				self.depname[bno_index] = self.var_depname.get()
 
				self.tree.item(self.tree.selection()[0], values=(self.var_bno.get(), self.var_rukudate.get(), self.var_num.get(), self.var_depname.get()))
			else:
				messagebox.showinfo('ERROR', '不能修改图书编号')

	#删除数据
	def del_row(self):
		res = messagebox.askyesnocancel('请确认', '是否删除所选数据？')
		if res == True:
			print(self.row_info[0])
			print(self.tree.selection()[0])
			print(self.tree.get_children())
			db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
			cursor = db.cursor()
			sql1 = "DELETE FROM book WHERE bno = '%s'" % (self.row_info[0])
			sql2 = "DELETE FROM ruku WHERE bno = '%s'" % (self.row_info[0])
			sql3 = "DELETE FROM sell WHERE bno = '%s'" % (self.row_info[0])
			try:
				cursor.execute(sql1)
				cursor.execute(sql2)
				cursor.execute(sql3)
				db.commit()
				messagebox.showinfo('恭喜', '删除成功')
			except:
				db.rollback()
				messagebox.showinfo('ERROR', '数据删除失败')
			db.close()
 
			bno_index = self.bno.index(self.row_info[0])
			print(bno_index)
			del self.bno[bno_index]
			del self.rukudate[bno_index]
			del self.num[bno_index]
			del self.depname[bno_index]
			print(self.bno)
			self.tree.delete(self.tree.selection()[0])
			print(self.tree.get_children())

# 稿费信息操作界面
class AdminManage_sell:
	def __init__(self, parent_window):
		parent_window.destroy()
		self.window = Tk()
		self.window.title('管理员操作界面')
		self.window.geometry('960x540+280+140')
		self.window.resizable(False, False)
		b1 = Label(self.window, text="稿费信息管理", font=('腾祥爱情体简', 20))
		b1.place(x=480, y=30, anchor='center')
 
		self.frame_left_top = tk.Frame(width=600, height=200)
		self.frame_right_top = tk.Frame(width=300, height=200)
		self.frame_center = tk.Frame(width=500, height=700)
		self.frame_bottom = tk.Frame(width=650, height=0)

		self.columns = ("编号", "销售数量", "稿费")
		self.tree = ttk.Treeview(self.frame_center, show="headings", height=7, columns=self.columns)
		self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.vbar.set)
 
		self.tree.column("编号", width=50, anchor='center')
		self.tree.column("销售数量", width=100, anchor='center')
		self.tree.column("稿费", width=100, anchor='center')
 
		self.tree.grid(row=0, column=0, sticky=NSEW)
		self.vbar.grid(row=0, column=1, sticky=NS)
 
		self.bno = []
		self.sellnum = []
		self.sellcheck = []

		db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
		cursor = db.cursor()
		sql = "SELECT * FROM sell"
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				self.bno.append(row[0])
				self.sellnum.append(row[1])
				self.sellcheck.append(row[2])
		except:
			messagebox.showinfo('ERROR', '列表数据导入失败')
		db.close()
 
		for i in range(min(len(self.bno), len(self.sellnum), len(self.sellcheck))): 
			self.tree.insert('', i, values=(self.bno[i], self.sellnum[i], self.sellcheck[i]))

		for col in self.columns:
			self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
 
		# 左上信息
		self.left_top_frame = tk.Frame(self.frame_left_top)
		self.var_bno = StringVar()
		self.var_sellnum = StringVar()
		self.var_sellcheck = StringVar()

		# 编号
		self.right_top_bno_label = Label(self.frame_left_top, text="编号", font=('腾祥爱情体简', 15))
		self.right_top_bno_entry = Entry(self.frame_left_top, textvariable=self.var_bno, font=('腾祥爱情体简', 15))
		self.right_top_bno_label.grid(row=1, column=0)
		self.right_top_bno_entry.grid(row=1, column=1)
		# 销售数量
		self.right_top_sellnum_label = Label(self.frame_left_top, text="销售数量", font=('腾祥爱情体简', 15))
		self.right_top_sellnum_entry = Entry(self.frame_left_top, textvariable=self.var_sellnum, font=('腾祥爱情体简', 15))
		self.right_top_sellnum_label.grid(row=3, column=0)
		self.right_top_sellnum_entry.grid(row=3, column=1)
		# 稿费
		self.right_top_sellcheck_label = Label(self.frame_left_top, text="稿费", font=('腾祥爱情体简', 15))
		self.right_top_sellcheck_entry = Entry(self.frame_left_top, textvariable=self.var_sellcheck, font=('腾祥爱情体简', 15))
		self.right_top_sellcheck_label.grid(row=4, column=0)
		self.right_top_sellcheck_entry.grid(row=4, column=1)

		# 操作按钮
		self.right_top_title = Label(self.frame_right_top, text="请选择操作", font=('腾祥爱情体简', 15))
		self.tree.bind('<Button-1>', self.click)
		self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建信息', width=20, command=self.new_row)
		self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新信息', width=20, command=self.updata_row)
		self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除信息', width=20, command=self.del_row)
		self.right_top_title.grid(row=1, column=0, pady=10)
		self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
		self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
		self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
 
		# 布局
		self.frame_left_top.grid(row=0, column=0, padx=60, pady=50)
		self.frame_right_top.grid(row=0, column=1, padx=0, pady=30)
		self.frame_center.grid(row=3, column=0, columnspan=2)
		self.frame_bottom.grid(row=2, column=0, columnspan=2)
 
		self.frame_left_top.grid_propagate(0)
		self.frame_right_top.grid_propagate(0)
		self.frame_center.grid_propagate(0)
		self.frame_bottom.grid_propagate(0)
 
		self.frame_left_top.tkraise()
		self.frame_right_top.tkraise()
		self.frame_center.tkraise()
		self.frame_bottom.tkraise()

		b4 = tk.Button(self.window, text="返回", font=("腾祥爱情体简", 16), command=self.back, width=7, height=1,
			   fg='black', bg='pink', activebackground='white', activeforeground='black')
		b4.place(x=850, y=450, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)  
		self.window.mainloop()

	def back(self):
		AdminManage(self.window)

	def click(self, event):
		self.col = self.tree.identify_column(event.x)
		self.row = self.tree.identify_row(event.y)
 
		print(self.col)
		print(self.row)
		self.row_info = self.tree.item(self.row, "values")
		self.var_bno.set(self.row_info[0])
		self.var_sellnum.set(self.row_info[1])
		self.var_sellcheck.set(self.row_info[2])
		self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_bno, font=('腾祥爱情体简', 15))
 
	def tree_sort_column(self, tv, col, reverse):
		l = [(tv.set(k, col), k) for k in tv.get_children('')]
		l.sort(reverse=reverse)
		for index, (val, k) in enumerate(l):
			tv.move(k, '', index)
		tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

	#添加数据
	def new_row(self):
		print(self.var_bno.get())
		print(self.bno)
		if str(self.var_bno.get()) in self.bno:
			messagebox.showinfo('ERROR', '该图书已存在')
		else:
			if self.var_bno.get() != '' and self.var_sellnum.get() != '' and self.var_sellcheck.get() != '':
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "INSERT INTO sell(bno, sellnum, sellcheck) \
				       VALUES ('%s', '%s', '%s')" % \
					  (self.var_bno.get(), self.var_sellnum.get(), self.var_sellcheck.get())
				try:
					cursor.execute(sql)
					db.commit()
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据修改失败')
				db.close()
 
				self.bno.append(self.var_bno.get())
				self.sellnum.append(self.var_sellnum.get())
				self.sellcheck.append(self.var_sellcheck.get())
				self.tree.insert('', len(self.bno) - 1, values=(self.bno[len(self.bno) - 1], self.sellnum[len(self.bno) - 1], self.sellcheck[len(self.bno) - 1]))
				self.tree.update()
				messagebox.showinfo('恭喜', '插入成功')
			else:
				messagebox.showinfo('ERROR', '图书数据未成功填写')
	
	#更新数据
	def updata_row(self):
		res = messagebox.askyesnocancel('请确认', '是否更新所填数据？')
		if res == True:
			if self.var_bno.get() == self.row_info[0]:
				db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
				cursor = db.cursor()
				sql = "UPDATE sell SET sellnum = '%s', sellcheck = '%s' \
				 WHERE bno = '%s'" % (self.var_sellnum.get(), self.var_sellcheck.get(), self.var_bno.get())
				try:
					cursor.execute(sql)
					db.commit()
					messagebox.showinfo('恭喜', '更新成功')
				except:
					db.rollback()
					messagebox.showinfo('ERROR', '数据更新失败')
				db.close()
 
				bno_index = self.bno.index(self.row_info[0])
				self.sellnum[bno_index] = self.var_sellnum.get()
				self.sellcheck[bno_index] = self.var_sellcheck.get()
 
				self.tree.item(self.tree.selection()[0], values=(self.var_bno.get(), self.var_sellnum.get(), self.var_sellcheck.get()))
			else:
				messagebox.showinfo('ERROR', '不能修改图书编号')

	#删除数据
	def del_row(self):
		res = messagebox.askyesnocancel('请确认', '是否删除所选数据？')
		if res == True:
			print(self.row_info[0])
			print(self.tree.selection()[0])
			print(self.tree.get_children())
			db = pymssql.connect('127.0.0.1', 'sa', 'azmiao', 'xxy', charset='UTF-8')
			cursor = db.cursor()
			sql1 = "DELETE FROM book WHERE bno = '%s'" % (self.row_info[0])
			sql2 = "DELETE FROM ruku WHERE bno = '%s'" % (self.row_info[0])
			sql3 = "DELETE FROM sell WHERE bno = '%s'" % (self.row_info[0])
			try:
				cursor.execute(sql1)
				cursor.execute(sql2)
				cursor.execute(sql3)
				db.commit()
				messagebox.showinfo('恭喜', '删除成功')
			except:
				db.rollback()
				messagebox.showinfo('ERROR', '数据删除失败')
			db.close()
 
			bno_index = self.bno.index(self.row_info[0])
			print(bno_index)
			del self.bno[bno_index]
			del self.sellnum[bno_index]
			del self.sellcheck[bno_index]
			print(self.bno)
			self.tree.delete(self.tree.selection()[0])
			print(self.tree.get_children())
 
 
# 关于
class AboutPage:
	def __init__(self, parent_window):
		parent_window.destroy()
		self.window = tk.Tk()
		self.window.resizable(False, False)
		C = Canvas(self.window, bg="blue", height=540, width=960) 
		filename = ImageTk.PhotoImage(file = "background.jpg") 
		background_label = Label(self.window, image=filename) 
		background_label.place(x=0, y=0, relwidth=1, relheight=1) 
		C.pack()

		self.window.title('关于')
		self.window.geometry('960x540+280+140')
		l1 = tk.Label(self.window, text='出版社信息管理系统', font=('腾祥爱情体简', 30), width=30, height=2)
		l2 = Label(self.window, text='作者：2018214520-夏星宇', font=('腾祥爱情体简', 18))
		l3 = Label(self.window, text='数据库课程设计', font=('腾祥爱情体简', 18))
		b1 = Button(self.window, text="返回首页", width=15, height=2, fg='black', bg='pink', activebackground='white', activeforeground='black', font=("腾祥爱情体简", 16), command=self.back)

		l1.place(x=480, y=100, anchor='center')
		l2.place(x=480, y=200, anchor='center')
		l3.place(x=480, y=300, anchor='center')
		b1.place(x=480, y=400, anchor='center')

		self.window.protocol("WM_DELETE_WINDOW", self.back)
		self.window.mainloop()
 
	def back(self):
		StartPage(self.window)
 
 
if __name__ == '__main__':
	try:
		window = tk.Tk()
		StartPage(window)
	except:
		messagebox.showinfo('ERROR', '数据库连接出错')