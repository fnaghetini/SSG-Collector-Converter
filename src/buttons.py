from tkinter import messagebox
from src.constants import *
from src.file_io import __select_directory, __get_input_files_list, __get_path_leaf
from src.file_io import __read_txt, __read_csv, __save_as_csv
from src.data_handler import __generate_df_prog, __generate_df_locd, __generate_df_exec
from src.data_handler import __create_df_prog_columns, __create_df_locd_columns, __create_df_exec_columns
from src.data_handler import __generate_surface_samples_prog_template, __generate_sample_coordinate_prog_template
from src.data_handler import __generate_surface_samples_locd_exec_template, __generate_sample_coordinate_locd_exec_template


def generate_prog_templates(campaign_var, datum_var, medium_code_var):
    folder_path = __select_directory()
    all_txt_files = __get_input_files_list(folder_path, 'txt')
    valid_input_files = [file for file in all_txt_files
                         if '_samples.csv' not in file and '_coordinates.csv' not in file]
    if len(valid_input_files) == 0:
        messagebox.showerror('Erro', f"Não há nenhum arquivo .csv na pasta {folder_path}.")
        return
    else:
        for file in valid_input_files:
            file_name = __get_path_leaf(file)[:-4]
            df = __read_txt(file)

            df_prog = __generate_df_prog(df, file_name)
            df_prog = __create_df_prog_columns(df_prog, campaign_var)

            surface_samples = __generate_surface_samples_prog_template(medium_code[medium_code_var.get()],
                                                                       campaign_var.get(),
                                                                       df_prog)
            sample_coordinates = __generate_sample_coordinate_prog_template(datum_var.get(), df_prog)

            __save_as_csv(surface_samples, f'{file[:-5]}_prog_samples.csv')
            __save_as_csv(sample_coordinates, f'{file[:-5]}_prog_coordinates.csv')

        messagebox.showinfo('Processo Concluído',
                            f'Templates de amostras programadas gerados com sucesso na pasta {folder_path}.')


def generate_locd_exec_templates(campaign_var, datum_var, medium_code_var):
    folder_path = __select_directory()
    all_csv_files = __get_input_files_list(folder_path, 'csv')
    valid_input_files = [file for file in all_csv_files
                         if '_samples.csv' not in file and '_coordinates.csv' not in file]
    if len(valid_input_files) == 0:
        messagebox.showerror('Erro', f"Não há nenhum arquivo .csv na pasta {folder_path}.")
        return
    else:
        for file in valid_input_files:
            file_name = __get_path_leaf(file)[:-4]
            df = __read_csv(file)

            df_prog = __generate_df_prog(df, file_name)
            df_prog = __create_df_prog_columns(df_prog, campaign_var)

            df_locd = __generate_df_locd(df)
            df_locd = __create_df_locd_columns(df_locd, file_name, campaign_var)

            df_exec = __generate_df_exec(df)
            df_exec = __create_df_exec_columns(df_exec, file_name, campaign_var)

            surface_samples = __generate_surface_samples_locd_exec_template(medium_code[medium_code_var.get()],
                                                                            campaign_var.get(),
                                                                            df_prog,
                                                                            df_exec)

            sample_coordinates = __generate_sample_coordinate_locd_exec_template(datum_var.get(), df_locd, df_exec)

            # Exportação
            __save_as_csv(surface_samples, f'{file[:-5]}_samples.csv')
            __save_as_csv(sample_coordinates, f'{file[:-5]}_coordinates.csv')

        messagebox.showinfo('Processo Concluído',
                            f'Templates de amostras locadas e executadas gerados com sucesso na pasta {folder_path}.')
