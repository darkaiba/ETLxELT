from ETL.ETL import ETL
from ELT.ELT import ELT

if __name__ == "__main__":

    json_enter = {
        "input_file": None,
        "reading": {
            "reading_mode": 'csv',
            "host": None,
            "user": None,
            "password": None,
            "path": 'C:\\Documents\\datasets',
            "filename": 'dados.csv',
            "database": None,
            "type_database": None
        },
        "transformer": {
            "nulos_nan_zero": None,
            "remove_nan_nulos": None,
            "remove_doubles": None,
            "add_column_default":{
                "key": None,
                "value": None
            },
            "conversor_type":{
                "colum": None,
                "type": None
            },
            "remove_columns":['col1', 'col2'],
            "add_colums":{
                "name_colum": None,
                "operation": None
            },
        },
        "delivery":{
            "host": None,
            "user": None,
            "password": None,
            "database": None,
            "type_database": None,
            "table": None,
            "delivery_path": None,
            "bucket_s3": None
        },
        "default": None
    }

    print("Iniciando o processo de ETL")
    ETL.run(json_enter)
    print("Iniciando o processo de ELT")
    ELT.run(json_enter)