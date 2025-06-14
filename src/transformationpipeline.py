import pandas as pd
from datetime import datetime

def Readjson(path):
    
    df = pd.read_json(path)
    df_properties = df['results']
    
    return df_properties

def ExplodeJsonDataframe(df_properties):
    df_properties = df_properties['properties']
    df_properties_exploded = pd.json_normalize(df_properties)
    return df_properties_exploded

def SelectOnlyRowsThatMatter(df_properties_exploded):
    
    columns = list(df_properties_exploded.columns)
    column_list = [element for element in columns if 'checkbox' in element or 'Created time.created_time' in element]
    df_habits_rows = df_properties_exploded.loc[:,column_list]

    return df_habits_rows

def PivotingDataFrame(df_habits_rows):
     
     df_habits_long = pd.melt(df_habits_rows,id_vars = 'Created time.created_time')  
     
     return  df_habits_long


def CleaningDataFrame(df_habits_long):
    
    df_habits_long_cleaned = df_habits_long.rename(columns = {'variable':"habit",
                                                              "Created time.created_time":"dt_habit"})
    df_habits_long_cleaned['habit'] = df_habits_long_cleaned['habit'].str.replace(".checkbox","").str.replace("properties.","")
    
    return df_habits_long_cleaned

def create_timestamp_column(df):
    today = datetime.now()
    df['dt_processed'] = today
    return df
    
def execute_transformation_functions(df):

    df_habits_long_cleaned = df.pipe(ExplodeJsonDataframe)\
        .pipe(SelectOnlyRowsThatMatter)\
            .pipe(PivotingDataFrame)\
                .pipe(CleaningDataFrame)\
                    .pipe(create_timestamp_column)
    
    return df_habits_long_cleaned




