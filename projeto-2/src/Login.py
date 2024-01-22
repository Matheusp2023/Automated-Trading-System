import customtkinter as ctk
import DataBase
from tkinter import *
from tkinter import messagebox
from PIL import Image

window = ctk.CTk()

class Login():
    def __init__(self):
        self.window = window
        self.theme()
        self.login_window_config()
        self.login_window_screen()
        window.mainloop()

    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def login_window_config(self):
        window.geometry("700x400")
        window.title("Sistema de login")
        window.iconbitmap("../assets/icon.ico")
        window.resizable(False, False)
    
    def login_window_screen(self):
        img_path = "../assets/log.png"
        img = ctk.CTkImage(light_image=Image.open(img_path), dark_image=Image.open(img_path), size=(343,332))
        label_img = ctk.CTkLabel(master=window, image=img, text="")
        label_img.place(x=3, y=65)

        label_tt = ctk.CTkLabel(master=window, text="Entre na sua conta e acesse\n a plataforma!", font=("Roboto", 18), text_color="#00B0F0")
        label_tt.place(x=60, y=10)

        login_frame = ctk.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 20), text_color=("black", "white"))
        label.place(x=25, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
        username_entry.place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo nome de usuário é obrigatório.", text_color="green", font=("Roboto",8))
        username_label.place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do usuário", width=300, font=("Roboto", 14), show="*")
        password_entry.place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo senha do usuário é obrigatório.", text_color="green", font=("Roboto",8))
        password_label.place(x=25, y=205)

        password_checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar da minha senha")
        password_checkbox.place(x=25, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300)
        login_button.place(x=25, y=285)

        def check_information_usuary_register(username_entry, email_entry, password_entry, confirm_password_entry, usuary_terms_checkbox_entry):
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            usuary_terms_checkbox = usuary_terms_checkbox_entry.get()

            db = DataBase.DataBase()
            if db.verify_username(username):
                return False
            elif len(password) < 4:
                return False
            elif db.verify_email(email):
                return False
            elif password != confirm_password:
                return False
            elif not bool(usuary_terms_checkbox):
                return False
            else:
                return True

        def screen_register():
            login_frame.pack_forget()
            rg_frame = ctk.CTkFrame(master=window, width=350, height=396)
            rg_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=rg_frame, text="Registre-se!", font=("Roboto", 20), text_color=("black", "white"))
            label.place(x=25, y=5)

            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
            username_entry.place(x=25, y=105)

            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de usuário", width=300, font=("Roboto", 14))
            email_entry.place(x=25, y=145)

            password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show="*")
            password_entry.place(x=25, y=185)

            confirm_password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirmar senha", width=300, font=("Roboto", 14), show="*")
            confirm_password_entry.place(x=25, y=225)

            usuary_terms_checkbox_entry = ctk.CTkCheckBox(master=rg_frame, text="Eu concordo com os termos de usuário")
            usuary_terms_checkbox_entry.place(x=25, y=265)

            def back():
                rg_frame.pack_forget()
                login_frame.pack(side=RIGHT)

            def save():
                username = username_entry.get()
                email = email_entry.get()
                password = password_entry.get()

                if check_information_usuary_register(username_entry, email_entry, password_entry, confirm_password_entry, usuary_terms_checkbox_entry):
                    db = DataBase.DataBase()
                    db.add_user(username, password, email)
                    back()
                else:
                    span_label = ctk.CTkLabel(master=rg_frame, text="Por favor, preencha todos os campos corretamente.", font=("Roboto", 10), text_color="red")
                    span_label.place(x=25, y=75)

            back_button = ctk.CTkButton(master=rg_frame, text="VOLTAR", width=145, fg_color="gray", hover_color="#202020", command=back)
            back_button.place(x=25, y=300)
            save_button = ctk.CTkButton(master=rg_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="#014B05", command=save)
            save_button.place(x=180, y=300)
      
        register_span = ctk.CTkLabel(master=login_frame, text="Não tem uma conta?")
        register_span.place(x=25, y=325)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=169, fg_color="green", hover_color="#2D9334", command=screen_register)
        register_button.place(x=156, y=325)

if __name__ == "__main__":
    Login()