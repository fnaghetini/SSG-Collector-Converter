import pandas as pd
from src.constants import *
from src.columnsbuilder import __get_sample_number, __get_project_number, __get_bank_code, __get_fire_plan
from src.columnsbuilder import __get_sampling_date, __get_sampler_code


def __generate_df_prog(df, file_name):
    df_prog = df[df.loc[:, 1] == file_name]
    df_prog.columns = df_prog_input_cols
    return df_prog


def __generate_df_locd(df):
    df_locd = df[df.loc[:, 0].str.startswith('FL')]
    df_locd.columns = df_locd_input_cols
    return df_locd


def __generate_df_exec(df):
    df_exec = df[df.loc[:, 0].str.startswith('FE')]
    df_exec.columns = df_exec_input_cols
    return df_exec


def __create_df_prog_columns(df_prog, year):
    df_prog['sample_number'] = df_prog.apply(lambda row: __get_sample_number(row, year), axis=1)
    df_prog['project_number'] = df_prog.apply(lambda row: __get_project_number(row), axis=1)
    df_prog['coord_type_code'] = 'PROG'
    df_prog['bank'] = df_prog.apply(lambda row: __get_bank_code(row), axis=1)
    df_prog['fire_plan'] = df_prog.apply(lambda row: __get_fire_plan(row, year), axis=1)
    return df_prog


def __create_df_locd_columns(df_locd, file_name, year):
    df_locd['drill_pattern'] = file_name
    df_locd['sample_number'] = df_locd.apply(lambda row: __get_sample_number(row, year), axis=1)
    df_locd['project_number'] = df_locd.apply(lambda row: __get_project_number(row), axis=1)
    df_locd['coord_type_code'] = 'LOCD'
    df_locd['fire_plan'] = df_locd.apply(lambda row: __get_fire_plan(row, year), axis=1)
    return df_locd


def __create_df_exec_columns(df_exec, file_name, year):
    df_exec['drill_pattern'] = file_name
    df_exec['sample_number'] = df_exec.apply(lambda row: __get_sample_number(row, year), axis=1)
    df_exec['project_number'] = df_exec.apply(lambda row: __get_project_number(row), axis=1)
    df_exec['coord_type_code'] = 'EXEC'
    df_exec['fire_plan'] = df_exec.apply(lambda row: __get_fire_plan(row, year), axis=1)
    df_exec['sampling_date'] = df_exec.apply(lambda row: __get_sampling_date(row, year), axis=1)
    df_exec['sampler_1'] = df_exec.apply(lambda row: __get_sampler_code(row), axis=1)
    return df_exec


def __generate_surface_samples_template(sample_type, year, df_prog, df_exec):
    df_surface_samples = df_prog[surface_samples_core_cols]
    df_surface_samples = df_surface_samples.merge(df_exec[surface_samples_exec_cols], on=surface_samples_pk, how='left')
    df_surface_samples['campaign'] = year
    df_surface_samples['MEDIUM_CODE'] = sample_type
    df_surface_samples['REGION_CODE'] = region_code
    return df_surface_samples.sort_values(by=[surface_samples_pk])


def __generate_sample_coordinate_template(grid_type, df_prog, df_locd, df_exec):
    df_sample_coordinate = pd.concat([
        df_prog[sample_coordinate_cols],
        df_locd[sample_coordinate_cols],
        df_exec[sample_coordinate_cols]
    ])
    df_sample_coordinate['GRID_TYPE_CODE'] = grid_type
    return df_sample_coordinate.sort_values(by=sample_coordinate_pk)
