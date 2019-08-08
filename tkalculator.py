#!/usr/bin/env python3
"""
A simple calculator
"""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst

# application name
app_name = "Tkalculator"
# application width
app_width = 650
# application height
app_height = 850

# base font size
font_size = 18
# file where to save
name_file = "tkalculator-saved.txt"
# thousands separator
t_sep = "'"

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.pack(fill="both", expand=True)
        
        self.create_widgets()
        
    def create_widgets(self):
        # how much characters in label
        label_width = 15
        # scrolledtext widget; height: lines - width:  characters
        self.main_text = tkst.ScrolledText(self, font=("Courier", font_size+4), height=12, state=tk.DISABLED)
        # text to right
        self.main_text.tag_configure("right", justify='right')
        self.main_text.pack(side="top")
        
        # font family and size
        self.s = ttk.Style(self.master)
        self.s.configure('.', font=('', font_size))
        
        # main label
        self.main_sv = tk.StringVar()
        self.main_sv.set("0")
        self.main_label = ttk.Label(self, width=label_width, font=("Courier", font_size+8), textvariable=self.main_sv, justify="right", anchor="e", background="light gray")
        self.main_label.pack(side="top", expand=True, fill="x")
        
        # optional label for numbers in memory
        self.opt_mem = tk.StringVar()
        self.opt_mem.set("0.0")
        self.opt_mem_label = ttk.Label(self, width=label_width, textvariable=self.opt_mem, justify="right", anchor="e", background="light gray")
        self.opt_mem_label.pack(side="top", expand=True, fill="x")
        
        # optional label for operators
        self.opt_sv = tk.StringVar()
        self.opt_sv.set("#")
        self.opt_label = ttk.Label(self, width=label_width, textvariable=self.opt_sv, justify="right", anchor="e", background="light gray")
        self.opt_label.pack(side="top", expand=True, fill="x")
        
        # save the content
        def fprint_btn():
            with open(name_file, "w") as f:
                save_text = self.main_text.get("1.0", tk.END).splitlines()
                for lline in save_text:
                    f.write('{:>30}\n'.format(lline))
        
        # grid
        self.grid = ttk.Frame(self)
        self.grid.pack(fill="both", expand=True)
        # 5 rows
        for rrow in range(5):
            tk.Grid.rowconfigure(self.grid, rrow+1, weight=1)
            # 6 columns
            for ccolumn in range(6):
                tk.Grid.columnconfigure(self.grid, ccolumn, weight=1)
        
        butt_width = 5
        ### buttons
        # memory
        self.butt_mc = ttk.Button(self.grid, text="MC", width=butt_width, command=lambda :self.fmbutton("MC"))
        self.butt_mc.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.butt_m1r = ttk.Button(self.grid, text="MR", width=butt_width, command=lambda :self.fmbutton("MR1"))
        self.butt_m1r.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.butt_m1p = ttk.Button(self.grid, text="M+", width=butt_width, command=lambda :self.fmbutton("M1+"))
        self.butt_m1p.grid(row=1, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.butt_m1m = ttk.Button(self.grid, text="M-", width=butt_width, command=lambda :self.fmbutton("M1-"))
        self.butt_m1m.grid(row=1, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        # print
        print_btn = ttk.Button(self.grid, text="Save", width=butt_width, command=fprint_btn)
        print_btn.grid(row=1, column=5, sticky=tk.N+tk.S+tk.E+tk.W)
        # first row
        self.butt_07 = ttk.Button(self.grid, text="7", width=butt_width, command=lambda :self.fbutton(7))
        self.butt_07.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('7', lambda e:self.fbutton(7))
        self.master.bind('<KP_7>', lambda e:self.fbutton(7))
        self.butt_08 = ttk.Button(self.grid, text="8", width=butt_width, command=lambda :self.fbutton(8))
        self.butt_08.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('8', lambda e:self.fbutton(8))
        self.master.bind('<KP_8>', lambda e:self.fbutton(8))
        self.butt_09 = ttk.Button(self.grid, text="9", width=butt_width, command=lambda :self.fbutton(9))
        self.butt_09.grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('9', lambda e:self.fbutton(9))
        self.master.bind('<KP_9>', lambda e:self.fbutton(9))
        self.diviso = ttk.Button(self.grid, text="/", width=butt_width, command=lambda :self.fbutton("/"))
        self.diviso.grid(row=2, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('/', lambda e:self.fbutton("/"))
        self.master.bind('<KP_Divide>', lambda e:self.fbutton("/"))
        self.canc_all = ttk.Button(self.grid, text="C", width=butt_width, command=lambda :self.fbutton("C"))
        self.canc_all.grid(row=1, column=4, sticky=tk.N+tk.S+tk.E+tk.W)
        # second row
        self.butt_04 = ttk.Button(self.grid, text="4", width=butt_width, command=lambda :self.fbutton(4))
        self.butt_04.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('4', lambda e:self.fbutton(4))
        self.master.bind('<KP_4>', lambda e:self.fbutton(4))
        self.butt_05 = ttk.Button(self.grid, text="5", width=butt_width, command=lambda :self.fbutton(5))
        self.butt_05.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('5', lambda e:self.fbutton(5))
        self.master.bind('<KP_5>', lambda e:self.fbutton(5))
        self.butt_06 = ttk.Button(self.grid, text="6", width=butt_width, command=lambda :self.fbutton(6))
        self.butt_06.grid(row=3, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('6', lambda e:self.fbutton(6))
        self.master.bind('<KP_6>', lambda e:self.fbutton(6))
        self.per = ttk.Button(self.grid, text="*", width=butt_width, command=lambda :self.fbutton("*"))
        self.per.grid(row=3, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('*', lambda e:self.fbutton("*"))
        self.master.bind('<KP_Multiply>', lambda e:self.fbutton("*"))
        self.canc_last = ttk.Button(self.grid, text="CE", width=butt_width, command=lambda :self.fbutton("CE"))
        self.canc_last.grid(row=2, column=4, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('<Delete>', lambda e:self.fbutton("C"))
        self.delete_last = ttk.Button(self.grid, text="<x", width=butt_width, command=lambda :self.fbutton("x"))
        self.delete_last.grid(row=3, column=4, sticky=tk.N+tk.S+tk.E+tk.W)
        # third row
        self.butt_01 = ttk.Button(self.grid, text="1", width=butt_width, command=lambda :self.fbutton(1))
        self.butt_01.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('1', lambda e:self.fbutton(1))
        self.master.bind('<KP_1>', lambda e:self.fbutton(1))
        self.butt_02 = ttk.Button(self.grid, text="2", width=butt_width, command=lambda :self.fbutton(2))
        self.butt_02.grid(row=4, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('2', lambda e:self.fbutton(2))
        self.master.bind('<KP_2>', lambda e:self.fbutton(2))
        self.butt_03 = ttk.Button(self.grid, text="3", width=butt_width, command=lambda :self.fbutton(3))
        self.butt_03.grid(row=4, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('3', lambda e:self.fbutton(3))
        self.master.bind('<KP_3>', lambda e:self.fbutton(3))
        self.meno = ttk.Button(self.grid, text="-", width=butt_width, command=lambda :self.fbutton("-"))
        self.meno.grid(row=4, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('-', lambda e:self.fbutton("-"))
        self.master.bind('<KP_Subtract>', lambda e:self.fbutton("-"))
        self.invert = ttk.Button(self.grid, text="1/x", width=butt_width, command=lambda :self.fbutton("1/x"))
        self.invert.grid(row=4, column=4, sticky=tk.N+tk.S+tk.E+tk.W)
        self.square = ttk.Button(self.grid, text="sqr", width=butt_width, command=lambda :self.fbutton("sqr"))
        self.square.grid(row=2, column=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.square_three = ttk.Button(self.grid, text="3_sqr", width=butt_width, command=lambda :self.fbutton("3_sqr"))
        self.square_three.grid(row=4, column=5, sticky=tk.N+tk.S+tk.E+tk.W)
        # fourth row
        self.butt_zero = ttk.Button(self.grid, text="0", width=butt_width, command=lambda :self.fbutton(0))
        self.butt_zero.grid(row=5, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('0', lambda e:self.fbutton(0))
        self.master.bind('<KP_0>', lambda e:self.fbutton(0))
        self.butt_decimali = ttk.Button(self.grid, text=",", width=butt_width, command=lambda :self.fbutton("."))
        self.butt_decimali.grid(row=5, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('.', lambda e:self.fbutton("."))
        self.master.bind('<KP_Decimal>', lambda e:self.fbutton("."))
        self.butt_result = ttk.Button(self.grid, text="=", width=butt_width, command=lambda :self.fbutton("="))
        self.butt_result.grid(row=5, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('<Return>', lambda e:self.fbutton("="))
        self.master.bind('<KP_Enter>', lambda e:self.fbutton("="))
        self.somma = ttk.Button(self.grid, text="+", width=butt_width, command=lambda :self.fbutton("+"))
        self.somma.grid(row=5, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.bind('+', lambda e:self.fbutton("+"))
        self.master.bind('<KP_Add>', lambda e:self.fbutton("+"))
        self.plus_minus = ttk.Button(self.grid, text="+/-", width=butt_width, command=lambda :self.fbutton("+-"))
        self.plus_minus.grid(row=5, column=4, sticky=tk.N+tk.S+tk.E+tk.W)
        self.powers_two = ttk.Button(self.grid, text="^2", width=butt_width, command=lambda :self.fbutton("^2"))
        self.powers_two.grid(row=3, column=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.powers_three = ttk.Button(self.grid, text="^3", width=butt_width, command=lambda :self.fbutton("^3"))
        self.powers_three.grid(row=5, column=5, sticky=tk.N+tk.S+tk.E+tk.W)

        # first temporary variable for operations
        self.temp_var1 = ""
        # second temporary variable for operations
        self.temp_var2 = ""
        # temporary variable for the current operator or equal 
        self.operation_var = ""
        # temporary variable for the previous operator or equal used
        self.prev_operation_var = ""
        # the total
        self.totale = 0.0
        # temporary variable in which to save the numbers memorized using M+
        self.mem_var = 0.0
    
    # add the thousands separator
    def thousand_separator(self, num):
        if '.' in num:
            integer, decimal = num.split('.')
            if decimal == '0':
                return str(format(int(integer), ',d').replace(",", t_sep))
            else:
                return str(format(int(integer), ',d').replace(",", t_sep))+'.'+decimal
        else:
            return str(format(int(num), ',d').replace(",", t_sep))
    
    def fbutton(self, btn):
        if btn in range(10):
            # 13 digits max
            if len(self.temp_var1) == 13:
                return
            
            if self.opt_sv.get() == "=":
                self.temp_var1 = ""
                self.temp_var2 = ""
                self.totale = 0.0
                self.opt_sv.set("#")
                self.prev_operation_var = ""
                self.operation_var = ""
            
            self.temp_var1 += str(btn)
            self.main_sv.set(self.temp_var1)
            #
        elif btn == ".":
            if "." in self.temp_var1:
                return
            if self.temp_var1 == "":
                self.temp_var1 = "0."
            else:
                self.temp_var1 += "."
        #
        elif btn in ["+","-","*","/"]:
            if self.temp_var1 == "":
                return
            if self.operation_var == "":
                self.operation_var = btn
            else:
                self.prev_operation_var = self.operation_var
                self.operation_var = btn
            self.opt_sv.set(btn)
            
            self.temp_var2 = self.temp_var1
            if self.prev_operation_var == "":
                self.totale += float(self.temp_var2)
            if self.prev_operation_var == "+":
                self.totale += float(self.temp_var2)
            elif self.prev_operation_var == "-":
                self.totale -= float(self.temp_var2)
            elif self.prev_operation_var == "*":
                self.totale *= float(self.temp_var2)
            elif self.prev_operation_var == "/":
                self.totale /= float(self.temp_var2)
            self.temp_var1 = ""
            self.main_text.configure(state=tk.NORMAL)
            value_with_thousand_separator = self.thousand_separator(self.temp_var2)
            
            self.main_text.insert(tk.END, value_with_thousand_separator+" "+btn+"\n")
            
            self.main_text.tag_add("right", 1.0, tk.END)
            self.main_text.see(tk.END)
            self.main_text.configure(state=tk.DISABLED)
            self.main_sv.set("0")
        elif btn == "+-":
            if self.operation_var == "=":
                self.totale = (-1)*self.totale
                if self.main_sv.get()[0] == "-":
                    self.temp_var1 = self.temp_var1[1:]
                    self.main_sv.set(self.main_sv.get()[1:])
                else:
                    self.temp_var1 = "-"+self.temp_var1
                    self.main_sv.set("-"+self.main_sv.get())
            else:
                if self.temp_var1 == "":
                    return
                first_char = self.temp_var1[0]
                if first_char == "-":
                    self.temp_var1 = self.temp_var1[1:]
                else:
                    self.temp_var1 = "-"+self.temp_var1
                self.main_sv.set(self.temp_var1)
        elif btn == "1/x":
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 == "":
                return
            self.temp_var1 = str(1/float(self.temp_var1))
            self.main_sv.set(self.temp_var1)
        elif btn == "sqr":
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 == "":
                return
            #
            try:
                self.temp_var1 = str(pow(float(self.temp_var1), 1/2))
                if "." in self.temp_var1:
                    integer, decimal = self.temp_var1.split(".")
                    if decimal == "0":
                        self.main_sv.set(integer)
                    else:
                        self.main_sv.set(self.temp_var1)
                else:
                    self.main_sv.set(self.temp_var1)
            except Exception as E:
                self.main_sv.set(str(E))
        elif btn == "^2":
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 == "":
                return
            #
            self.temp_var1 = str(float(self.temp_var1) * float(self.temp_var1))
            #
            if "." in self.temp_var1:
                integer, decimal = self.temp_var1.split(".")
                if decimal == "0":
                    self.main_sv.set(integer)
                else:
                    self.main_sv.set(self.temp_var1)
            else:
                self.main_sv.set(self.temp_var1)
        elif btn == "3_sqr":
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 == "":
                return
            #
            try:
                self.temp_var1 = str(pow(float(self.temp_var1), 1/3))
                if "." in self.temp_var1:
                    integer, decimal = self.temp_var1.split(".")
                    if decimal == "0":
                        self.main_sv.set(integer)
                    else:
                        self.main_sv.set(self.temp_var1)
                else:
                    self.main_sv.set(self.temp_var1)
            except Exception as E:
                self.main_sv.set(str(E))
        elif btn == "^3":
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 == "":
                return
            #
            self.temp_var1 = str(float(self.temp_var1) * float(self.temp_var1) * float(self.temp_var1))
            #
            if "." in self.temp_var1:
                integer, decimal = self.temp_var1.split(".")
                if decimal == "0":
                    self.main_sv.set(integer)
                else:
                    self.main_sv.set(self.temp_var1)
            else:
                self.main_sv.set(self.temp_var1)
        #
        elif btn == "=":
            if self.temp_var1 == "" or self.temp_var2 == "":
                return
            
            if self.operation_var == "":
                return
            
            if self.operation_var == "=":
                self.main_text.configure(state=tk.NORMAL)
                self.main_text.insert(tk.END, "###################\n\n")
                self.main_text.configure(state=tk.DISABLED)
                self.main_text.see(tk.END)
                return
            
            if self.temp_var1 == "0" and self.operation_var == "/":
                div_zero_message = "division by zero"
                self.main_sv.set(div_zero_message)
                #
                self.main_text.configure(state=tk.NORMAL)
                #
                self.main_text.insert(tk.END, self.temp_var1+"  "+"\n")
                #
                count_str = len(div_zero_message)
                str_nl = self.fcount_num(count_str, "-")
                self.main_text.insert(tk.END, str_nl+"\n")
                #
                self.main_text.insert(tk.END, div_zero_message+"\n")
                #
                str_nl = self.fcount_num(count_str, "=")
                self.main_text.insert(tk.END, str_nl+"\n")
                # 
                self.main_text.see(tk.END)
                self.main_text.configure(state=tk.DISABLED)
                # 
                self.opt_sv.set("#")
                self.temp_var1 = ""
                self.temp_var2 = ""
                self.totale = 0
                self.prev_operation_var = ""
                self.operation_var = ""
                return
            
            if self.operation_var == "+":
                self.totale += float(self.temp_var1)
                
            elif self.operation_var == "-":
                self.totale -= float(self.temp_var1)
            elif self.operation_var == "*":
                self.totale *= float(self.temp_var1)
            elif self.operation_var == "/":
                if self.temp_var1 == "0":
                    return
                self.totale /= float(self.temp_var1)
            
            self.main_text.configure(state=tk.NORMAL)
            self.main_text.insert(tk.END, self.thousand_separator(self.temp_var1)+"  "+"\n")
            value_with_thousand_separator = self.thousand_separator(str(self.totale))
            count_str = len(value_with_thousand_separator)
            str_nl = self.fcount_num(count_str, "-")
            self.main_text.insert(tk.END, str_nl+"\n")
            self.main_text.insert(tk.END, value_with_thousand_separator+" "+btn+"\n")
            str_nl = self.fcount_num(count_str, "=")
            self.main_text.insert(tk.END, str_nl+"\n\n")
            self.main_sv.set(value_with_thousand_separator)
            
            self.main_text.see(tk.END)
            self.main_text.configure(state=tk.DISABLED)
            self.operation_var = "="
            self.opt_sv.set("=")
            
            self.temp_var1 = str(self.totale)
            
        elif btn == "C":
            self.main_text.configure(state=tk.NORMAL)
            self.main_text.delete(1.0, tk.END)
            self.main_text.configure(state=tk.DISABLED)
            #
            self.main_sv.set("0")
            self.opt_sv.set("#")
            self.temp_var1 = ""
            self.temp_var2 = ""
            self.operation_var = ""
            self.prev_operation_var = ""
            self.totale = 0
        elif btn == "CE":
            if self.opt_sv.get() == "=":
                return
            self.main_sv.set("0")
            self.temp_var1 = ""
        elif btn == "x":
            if self.temp_var1 == "":
                return
            if self.opt_sv.get() == "=":
                return
            if self.temp_var1 != "":
                if len(self.temp_var1) > 1:
                    self.temp_var1 = self.temp_var1[0:-1]
                    self.main_sv.set(self.temp_var1)
                else:
                    self.temp_var1 = ""
                    self.main_sv.set("0")
    
    def fcount_num(self, num, nchar):
        str_nl = nchar*3
        for i in range(num):
            str_nl += nchar 
        return str_nl

    def fmbutton(self, butt):
        if butt == "MR1":
            if self.operation_var == "=":
                value_with_thousand_separator = self.thousand_separator(str(self.mem_var))
                self.temp_var1 = value_with_thousand_separator.replace(t_sep, "")
                self.main_sv.set(value_with_thousand_separator)
                self.totale = float(value_with_thousand_separator.replace(t_sep, ""))
            else:
                value_with_thousand_separator = self.thousand_separator(str(self.mem_var))
                self.temp_var1 = value_with_thousand_separator.replace(t_sep, "")
                self.main_sv.set(value_with_thousand_separator)
        elif butt == "M1+":
            self.mem_var += float(self.main_sv.get().replace(t_sep, ""))
            self.opt_mem.set(str(self.mem_var))
        elif butt == "M1-":
            self.mem_var -= float(self.main_sv.get().replace(t_sep, ""))
            self.opt_mem.set(str(self.mem_var))
        elif butt == "MC":
           self.mem_var = 0.0
           self.opt_mem.set(str(self.mem_var))

def main():
    root = tk.Tk()
    root.title(app_name)
    root.update_idletasks()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    width = app_width
    height = app_height
    root.geometry('{}x{}'.format(width, height))
    
    app = Application(master=root)
    app.mainloop()
    
if __name__ == "__main__":
    main()
