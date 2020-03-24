import xlwings as xw
app=xw.App(visible=True,add_book=False)
wb=app.books.open(r'e:\test6.xlsx')
wb.sheets['sheet2'].range('a2').value='world'
wb.save()
wb.close()
app.quit()