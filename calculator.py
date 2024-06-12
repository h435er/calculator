#Author: h435er
import customtkinter as ctk

def button_click(number):
    current_text = textbox.get()
    new_text = current_text + str(number)
    textbox.delete(0, ctk.END)
    textbox.insert(0, new_text)

def main():
    global textbox

    # create window
    app = ctk.CTk()
    app.geometry("300x700")
    ctk.set_appearance_mode("Dark")
    
    # textbox
    textbox = ctk.CTkEntry(app, border_width=1, border_color="gray", text_color="black",
                           fg_color="white", corner_radius=5, width=280, height=50)
    textbox.pack(padx=10, pady=10)

    # all functions
    def button_click_0():
        button_click(0)

    def button_click_1():
        button_click(1)

    def button_click_2():
        button_click(2)

    def button_click_3():
        button_click(3)

    def button_click_4():
        button_click(4)

    def button_click_5():
        button_click(5)

    def button_click_6():
        button_click(6)

    def button_click_7():
        button_click(7)

    def button_click_8():
        button_click(8)

    def button_click_9():
        button_click(9)

    def button_click_minus():
        button_click("-")
        
    def button_click_plus():
        button_click("+")
    
    def button_click_divide():
        button_click("/")

    def button_click_multiply():
        button_click("*")
    
    
    def calculate():
        result = eval(textbox.get())
        textbox.delete(0, ctk.END)
        textbox.insert(0, str(result))

    def clear():
        textbox.delete(0, ctk.END)
    
    def button_click_lbracket():
        button_click("(")
    
    def button_click_rbracket():
        button_click(")")



    # create buttons
    buttons_frame = ctk.CTkFrame(app)
    buttons_frame.pack(pady=10)

    # first row
    row1 = ctk.CTkFrame(buttons_frame)
    row1.pack()

    button7 = ctk.CTkButton(row1, text="7", command=button_click_7, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button7.pack(side=ctk.LEFT, padx=5,pady=5)

    button8 = ctk.CTkButton(row1, text="8", command=button_click_8, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button8.pack(side=ctk.LEFT, padx=5,pady=5)

    button9 = ctk.CTkButton(row1, text="9", command=button_click_9, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button9.pack(side=ctk.LEFT, padx=5,pady=5)
    minus= ctk.CTkButton(row1, text="-", command=button_click_minus, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    minus.pack(side=ctk.LEFT, padx=5,pady=5)

    # second row
    row2 = ctk.CTkFrame(buttons_frame)
    row2.pack()

    button4 = ctk.CTkButton(row2, text="4", command=button_click_4, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button4.pack(side=ctk.LEFT, padx=5,pady=5)

    button5 = ctk.CTkButton(row2, text="5", command=button_click_5, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button5.pack(side=ctk.LEFT, padx=5,pady=5)

    button6 = ctk.CTkButton(row2, text="6", command=button_click_6, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button6.pack(side=ctk.LEFT, padx=5,pady=5)
    plus= ctk.CTkButton(row2, text="+", command=button_click_plus, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    plus.pack(side=ctk.LEFT, padx=5,pady=5)

    # third row
    row3 = ctk.CTkFrame(buttons_frame)
    row3.pack()

    button1 = ctk.CTkButton(row3, text="1", command=button_click_1, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button1.pack(side=ctk.LEFT, padx=5,pady=5)

    button2 = ctk.CTkButton(row3, text="2", command=button_click_2, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button2.pack(side=ctk.LEFT, padx=5,pady=5)

    button3 = ctk.CTkButton(row3, text="3", command=button_click_3, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button3.pack(side=ctk.LEFT, padx=5,pady=5)
    divide= ctk.CTkButton(row3, text=":", command=button_click_divide, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    divide.pack(side=ctk.LEFT, padx=5,pady=5)

    # fourth row
    row4 = ctk.CTkFrame(buttons_frame)
    row4.pack()

    button0 = ctk.CTkButton(row4, text="0", command=button_click_0, border_width=1,
                           border_color="gray", fg_color="grey", corner_radius=5, width=70, height=70)
    button0.pack(side=ctk.LEFT, padx=5)
    lbracket= ctk.CTkButton(row4, text="(", command=button_click_lbracket, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    lbracket.pack(side=ctk.LEFT, padx=5,pady=5)
    rbracket= ctk.CTkButton(row4, text=")", command=button_click_rbracket, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    rbracket.pack(side=ctk.LEFT, padx=5,pady=5)
    multiply= ctk.CTkButton(row4, text="*", command=button_click_multiply, border_width=1,
                           border_color="gray", fg_color="green", corner_radius=5, width=70, height=70)
    multiply.pack(side=ctk.LEFT, padx=5,pady=5)

    

    
    

    
    # calculate and clear
    row5=ctk.CTkFrame(buttons_frame)
    row5.pack()
    equal= ctk.CTkButton(row5, text="=", command=calculate, border_width=1,
                           border_color="gray", fg_color="orange", corner_radius=5, width=70, height=70)
    equal.pack(side=ctk.LEFT, padx=5,pady=5)
    equal= ctk.CTkButton(row5, text="CLEAR", command=clear, border_width=1,
                           border_color="gray", fg_color="orange", corner_radius=5, width=70, height=70)
    equal.pack(side=ctk.LEFT, padx=5,pady=5)


    # start the app
    app.mainloop()

if __name__ == "__main__":
    main()
