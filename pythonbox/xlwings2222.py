#1.打开已保存的Excel文档
#导入xlwings模块，打开Excel程序，默认设置：程序可见，只打开不新建工作簿，屏幕更新关闭


import xlwings as xw
app = xw.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=False
#文件位置：filepath,打开test文档，然后保存，关闭，结束程序
filepath=r'e:\test.xlsx'
wb=app.books.open(filepath)
wb.save()
wb.close()
app.quit()