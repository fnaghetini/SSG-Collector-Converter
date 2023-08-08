from src.widgets import *
from src.button import generate_templates
import warnings
warnings.filterwarnings("ignore")


root = Tk()
root.title("Conversor Dados Coletora")
root.geometry("460x200")
root.configure(background='white')

######################################################################################
# ------------------------------ Definição dos Widgets ----------------------------- #
######################################################################################

txt_title = create_title_label(root, text="Conversor Dados Coletora - Vale Sossego")

btn_generate_templates = Button(root, text="Gerar Templates", width=30, height=2, justify=CENTER, cursor='hand2',
                                font=('Tahoma', '9', 'bold'), command=lambda: generate_templates())

# Versão do Aplicativo
txt_version = create_app_version_label(root, text="@Datamine Software v0.0.1")

######################################################################################
# ------------------------------- Posição dos Widgets ------------------------------ #
######################################################################################

txt_title.grid(row=0, column=0, columnspan=2, pady=10)
btn_generate_templates.grid(row=1, column=0, columnspan=2, pady=30)
txt_version.grid(row=2, column=1, sticky=E)

root.mainloop()
