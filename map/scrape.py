from .src.KoreaCDC import KoreaCovid
from .src.WorldCDC import WorldCovid
koreacovid = KoreaCovid()
worldcovid = WorldCovid()

def unroll_data(datarr : list) -> tuple:
    datarr = datarr.split('|')
    try:
        datarr = [int(float(dat)) for dat in datarr]
    except ValueError:
        dat=0
        pass
    # confirmed accumulated, increase, patients, recovered , deceased, ratio
    return tuple(datarr)

def csv_data():
    fieldnames, fieldvalues = koreacovid.read_csv_data()
    return fieldnames, fieldvalues
    
    
def parse_data():
    fieldnames, fieldvalues = csv_data()
    datarray_chart = []
    keys = [
        'City', 
        'Increase from day before', 
        'Total Patients', 
        'Total Quarantine', 
        'Total Recovered', 
        'Total Deceased', 
        'Increase to Patient Ratio'
    ]
    
    datarray = [[datarr[0],*unroll_data(datarr[-1])] for datarr in fieldvalues]
    print(f"Current date's status of Covid19:\n{datarray}")
    datarray.insert(0,keys)
    datarray_all = datarray
    
    for cnt, ele in enumerate(datarray):
        try:
            if(cnt==0):
                datarray_chart.append([ele[0],ele[2]])
            else:
                datarray_chart.append([ele[0],int(float(ele[2]))])
        except ValueError:
            if(cnt==0):
                datarray_chart.append([ele[0],ele[1]])
            else:
                datarray_chart.append([ele[0],int(str(ele[1]))])
    
    return datarray_all, datarray_chart
