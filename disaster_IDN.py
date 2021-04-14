# Function used here

def xlsxToCsv(sourceFile, targetFile):
    '''
    This function performs two stages:
    1. read 'xlsx' format obtained from original source
    2. convert it to csv for less memory use
    
    It takes two arguments (assigned prior to performing each xlsxToCsv):
    sourceFile = '.xlsx' original file
    targetFile = '.csv' file and where to put it
    
    '''
    read_file = pd.read_excel(sourceFile, engine='openpyxl', skiprows=1)
    return read_file.to_csv(targetFile, index = None, header=True)


def replaceValue (dfName, columnName, originalValue, targetValue):
    '''
    This function is to easily replace the value in certain column of dataframe
    It takes 4 arguments:
    dfName = the dataFrame Name
    columnName = column name to target
    OriginalValue = can be String, integer etc
    targetValue = value to replace
    '''
    return dfName[columnName].replace(originalValue,targetValue,inplace=True)