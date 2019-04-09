from datetime import datetime

def timestampToDate(timestamp):
    '''
    Convert a timestamp to readable date
    Params:
        timestamp: int
    Return:
        date and time in format 'YYYY-MM-DD HH:MM:SS': string
    '''
    date_pattern = '%Y-%m-%d %H:%M:%S'
    return str(datetime.utcfromtimestamp(int(timestamp)).strftime(date_pattern))

def fileToList(file):
    '''
    Read values of a file seperated by line breaks to list
    Params:
        file: string
    Return:
        list of values: list
    * alternative way, but does not close the file: list = [line.rstrip('\n') for line in open(file)] *
    '''
    with open(file) as f: 
        return [line.rstrip('\n') for line in f]

    
def listToFile(file, list):
    '''
    Write values of a list to file seperated by line breaks
    Params:
        file: string
        list of words: list
    '''
    with open(file, 'w') as f:
        for entry in list:
            f.write("%s\n" % entry)
