#-*- codeing = utf-8 -*-

import xlwt

workBook = xlwt.Workbook(encoding="utf-8") # 创建workBook对象
workSheet = workBook.add_sheet("sheet1")# 创建工作表
workSheet.write(0,0,'hello') # 写入数据，第一个参数表示行，第二个参数表示列，第三个参数表示内容
workBook.save('student.xls') #保存数据表

# eg. 九九乘法表
workSheet2 = workBook.add_sheet("sheet2")
for i in range(1,10):
    for j in range(1,i+1):
        workSheet2.write(i-1,j-1,str(i) + "*" + str(j) + "=" + str(i*j))
        # workSheet2.write(i-1,j-1,"%d * %d = %d"%(i,j,i*j))

workBook.save('student.xls')