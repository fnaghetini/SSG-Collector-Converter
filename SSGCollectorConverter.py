from src.constants import *
from src.widgets import *
from src.buttons import generate_prog_templates, generate_locd_exec_templates
import warnings

warnings.filterwarnings("ignore")

root = Tk()
root.title("Vale Sossego - Curto Prazo")
root.geometry("495x337")
root.configure(background='white')

######################################################################################
# ------------------------------ Definição dos Widgets ----------------------------- #
######################################################################################

txt_title = create_title_label(root, text="Conversor de Dados da Coletora")

txt_campaign = Label(root, text="Ano:", width=30, bg='white', fg='black', justify=LEFT, anchor='w', padx=10)
campaign_var = StringVar(root)
campaign_var.set(str(datetime.now().year))
pkl_campaign = OptionMenu(root, campaign_var, *campaigns)
pkl_campaign.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

txt_datum = Label(root, text="Datum:", width=30, bg='white', fg='black', justify=LEFT, anchor='w', padx=10)
datum_var = StringVar(root)
datum_var.set(datum[0])
pkl_datum = OptionMenu(root, datum_var, *datum)
pkl_datum.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

txt_medium_code = Label(root, text="Tipo de Amostra:", width=30, bg='white', fg='black', justify=LEFT, anchor='w',
                        padx=10)
medium_code_var = StringVar(root)
medium_code_var.set(list(medium_code.keys())[0])
pkl_medium_code = OptionMenu(root, medium_code_var, *medium_code)
pkl_medium_code.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

btn_generate_prog_templates = Button(root, text="Gerar Templates (EXEC)", width=25, justify=CENTER,
                                     cursor='hand2', font=('Tahoma', '9', 'bold'), bg='#00939A', fg='white',
                                     command=lambda: generate_prog_templates(campaign_var,
                                                                             datum_var,
                                                                             medium_code_var)
                                     )

btn_generate_locd_exec_templates = Button(root, text="Gerar Templates (LOCD e EXEC)", width=25, justify=CENTER,
                                          cursor='hand2', font=('Tahoma', '9', 'bold'), bg='#00939A', fg='white',
                                          command=lambda: generate_locd_exec_templates(campaign_var,
                                                                                       datum_var,
                                                                                       medium_code_var)
                                          )

txt_version = create_app_version_label(root, text="@Datamine Software v0.0.1")

######################################################################################
# ------------------------------- Posição dos Widgets ------------------------------ #
######################################################################################

txt_title.grid(row=0, column=0, columnspan=2, pady=30)
txt_campaign.grid(row=1, column=0, pady=10, sticky=W)
pkl_campaign.grid(row=1, column=1)
txt_datum.grid(row=2, column=0, pady=10, sticky=W)
pkl_datum.grid(row=2, column=1)
txt_medium_code.grid(row=3, column=0, pady=10, sticky=W)
pkl_medium_code.grid(row=3, column=1)
btn_generate_prog_templates.grid(row=4, column=0, pady=30)
btn_generate_locd_exec_templates.grid(row=4, column=1, pady=30)
txt_version.grid(row=5, column=1, sticky=E)

root.mainloop()
