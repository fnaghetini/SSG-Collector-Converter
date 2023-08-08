from datetime import datetime

campaigns = [str(year) for year in list(range(2000, 2036))]
datum = ['UTM69-22S', 'SIRGAS2000:']
region_code = 'SSG'
medium_code = {'Plano de Fogo': 'PF',
               'Frente de Lavra': 'FL',
               'Pilha': 'TR'}

df_prog_input_cols = ['sample_seq', 'drill_pattern', 'elevation', 'eastwest_decimal', 'northsouth_decimal']
df_locd_input_cols = ['locd_code', 'sample_seq', 'elevation', 'eastwest_decimal', 'northsouth_decimal']
df_exec_input_cols = ['exec_code', 'sample_seq', 'elevation', 'eastwest_decimal', 'northsouth_decimal']
surface_samples_core_cols = ['sample_number', 'bank', 'project_number', 'fire_plan', 'drill_pattern']
surface_samples_exec_cols = ['sample_number', 'sampling_date', 'sampler_1']
sample_coordinate_cols = ['sample_number', 'coord_type_code', 'eastwest_decimal', 'northsouth_decimal', 'elevation']

current_year = str(datetime.now().year)

surface_samples_pk = 'sample_number'
sample_coordinate_pk = ['sample_number', 'coord_type_code']

project_codes = {'E': ['SEQ', '1'],
                 'O': ['SOS', '2'],
                 'P': ['PIS', '3'],
                 'M': ['MAT', '4']}


