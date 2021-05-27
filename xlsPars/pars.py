from openpyxl import load_workbook

wb = load_workbook('./test.xlsx') 
sheet = wb.get_sheet_by_name('TDSheet')
surname = ['Астапов', 'Глотов', 'Заводчиков', 'Красулин', 'Перминов', 'Читайло']
end = ''
tname = ''
flag = 0
lst = []*3 
i = 0
while i < 2000:
    if sheet['C'+str(10+i)].value:
        print(str(sheet['C'+str(10+i)].value) +'/'+ str(sheet['L'+str(10+i)].value)+ '/' + str(tname))
        #lst.extend(str(sheet['C'+str(10+i)].value),str(sheet['L'+str(10+i)].value), str(name))
    else:  
        st = sheet['A'+str(10+i)].value
        name = st.split()[0].strip()
        for text in surname:
            if name in text:
                tname = name
    if sheet['A'+str(10+i)].value == 'Итого':
        print('End of file')
        break
    i = i+1       
