from src.constants import *


def __get_pit_numeric_code(row):
    pit_alpha_code = str(row['drill_pattern'])[0]
    return project_codes[pit_alpha_code][1]


def __get_project_number(row):
    pit_alpha_code = str(row['drill_pattern'])[0]
    return project_codes[pit_alpha_code][0]


def __get_bank_code(row):
    return str(row['drill_pattern']).split('_')[1]


def __get_polygon_code(row):
    raw_polygon_code = str(row['drill_pattern']).split('_')[2]
    if raw_polygon_code[-1] in ['a', 'b', 'c']:
        return raw_polygon_code[:-1]
    else:
        return raw_polygon_code


def __get_sample_sequential(row):
    return str(row['sample_seq'].zfill(4))


def __get_sampling_date(row):
    day_and_month = str(row['exec_code']).split('_')[1][:4]
    day = day_and_month[:2]
    month = day_and_month[2:]
    year = current_year
    return f"{day}/{month}/{year}"


def __get_sampler_code(row):
    raw_sampler_code = str(row['exec_code']).split('_')[1][4:6]
    return sampler_codes[raw_sampler_code]


def __get_sample_number(row):
    year = current_year[2:]
    pit = __get_pit_numeric_code(row)
    bank = __get_bank_code(row)
    polygon = __get_polygon_code(row)
    seq = __get_sample_sequential(row)
    return f"{year}_{pit}{bank}{polygon}-{seq}"


def __get_fire_plan(row):
    year = current_year[2:]
    pit = __get_pit_numeric_code(row)
    bank = __get_bank_code(row)
    polygon = __get_polygon_code(row)
    return f"{year}_{pit}{bank}{polygon}"
