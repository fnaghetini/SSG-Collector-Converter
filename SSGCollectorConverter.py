from src.constants import *
from src.widgets import *
from src.button import generate_templates
import warnings
warnings.filterwarnings("ignore")


root = Tk()
root.title("Vale Sossego - Curto Prazo")
root.geometry("495x270")
root.configure(background='white')

######################################################################################
# ------------------------------ Definição dos Widgets ----------------------------- #
######################################################################################

txt_title = create_title_label(root, text="Conversor de Dados da Coletora")

txt_datum = Label(root, text="Datum:", width=30, bg='white', fg='black', justify=LEFT, anchor='w', padx=10)
datum_var = StringVar(root)
datum_var.set(datum[0])
pkl_datum = OptionMenu(root, datum_var, *datum)
pkl_datum.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

txt_medium_code = Label(root, text="Tipo de Amostra:", width=30, bg='white', fg='black', justify=LEFT, anchor='w', padx=10)
medium_code_var = StringVar(root)
medium_code_var.set(list(medium_code.keys())[0])
pkl_medium_code = OptionMenu(root, medium_code_var, *medium_code)
pkl_medium_code.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

btn_generate_templates = Button(root, text="Gerar Templates", width=25, justify=CENTER,
                                cursor='hand2', font=('Tahoma', '9', 'bold'),
                                command=lambda: generate_templates(datum_var, medium_code_var))

# Versão do Aplicativo
txt_version = create_app_version_label(root, text="@Datamine Software v0.0.1")

######################################################################################
# ------------------------------- Posição dos Widgets ------------------------------ #
######################################################################################

txt_title.grid(row=0, column=0, columnspan=2, pady=20)
txt_datum.grid(row=1, column=0, pady=10, sticky=W)
pkl_datum.grid(row=1, column=1)
txt_medium_code.grid(row=2, column=0, pady=10, sticky=W)
pkl_medium_code.grid(row=2, column=1)
btn_generate_templates.grid(row=3, column=0, columnspan=2, pady=25)
txt_version.grid(row=4, column=1, sticky=E)

root.mainloop()
