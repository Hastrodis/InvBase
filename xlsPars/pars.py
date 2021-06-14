from InvBase.settings import ALLOWED_HOSTS
from openpyxl import load_workbook
from SaveBase.models import Techn



def pars(techsp):
    flag = 1 
    alltech = []
    wb = load_workbook('./test.xlsx') 
    sheet = wb.get_sheet_by_name('TDSheet')
    #surname = ['Астапов', 'Глотов', 'Заводчиков', 'Красулин', 'Перминов', 'Читайло']
    tname = ''
    i = 0
    n = 1
    while i < n:
        if (sheet['C'+str(10+i)].value):
            alltech.append({
                'invnomer': str(sheet['L'+str(10+i)].value),
                'name': str(sheet['C'+str(10+i)].value),
                'podot': str(tname),
            })
            print(str(sheet['C'+str(10+i)].value) +'/'+ str(sheet['L'+str(10+i)].value)+ '/' + str(tname))
        #lst.extend(str(sheet['C'+str(10+i)].value),str(sheet['L'+str(10+i)].value), str(name))
        else:  
            st = sheet['A'+str(10+i)].value
            name = st.split()[0].strip()
            for text in techsp:
                if name in text.values():
                    tname = name
                    flag = 1
                else: 
                    flag = 0
        if sheet['A'+str(10+i)].value == 'Итого':
            print('End of file')
            n = 0
        i = i+1
        n = n+1
   
    return(alltech[1].values())