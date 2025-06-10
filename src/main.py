from extractionpipeline import extraction_database_notion
from transformationpipeline import execute_transformation_functions
from ingestionpipeline import ingestdatatopostgres
import time 


def run_full_pipeline():
    print("Iniciando o pipeline completo...")
    data_extracted_from_notion = extraction_database_notion()
    print("Extração concluída.")

        # 2. Transformação
    if len(data_extracted_from_notion) !=0 :
        transformed_data = execute_transformation_functions(data_extracted_from_notion)
        print("Transformação concluída.")
    else:
        print("Nenhum dado para transformar.")
        return
    
    if not transformed_data.empty:
        success = ingestdatatopostgres(transformed_data)
        if success:
            print("Ingestão concluída com sucesso!")
        else:
            print("Erro na ingestão.")

if __name__ == "__main__":
    while True:
        run_full_pipeline()
        time.sleep(86400)


