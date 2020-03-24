
import xlwings as xw
app = xw.App(visible=True,add_book=False)
wb=app.books.open(r'e:\test1.xlsx')

wb.sheets['sheet1'].range('a1').value='苦短'
wb.save()
wb.close()
app.quit()
