

'''读Excel文件'''
# wb = xlrd.open_workbook(r"D:\Study_python\python 读取excel表格测试.xls")
# sheetname=wb.sheet_names()
# print(sheetname)
# sheet=wb.sheet_by_name(sheetname[0])
# print(sheet.nrows,sheet.ncols)
# print(sheet.cell_value(rowx=1,colx=2))
import xlrd
import random
import xlwt

'''写Excel文件'''
names=['Linda','Jack','Messi','Trump']
scores=[[random.randrange(60,101) for _ in range(3)] for _ in range(4)]
wb=xlwt.Workbook()
sheet=wb.add_sheet('九年五班')

'''调整单元格样式'''
header =xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern =xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 3
header.pattern=pattern


titles=('name','Chinese','Math','English')
for index,title in enumerate(titles):
    sheet.write(0,index,title,header)
for row in range(len(scores)):
    sheet.write(row+1,0,names[row])
    for col in range(len(scores[row])):
        sheet.write(row+1,col+1,scores[row][col])
wb.save(r'D:\Study_python\成绩单.xls')


'''调整字体'''
font = xlwt.Font()
font.name = '华文楷体'
font.height=20*18
font.bold=True
font.italic=True
font.colour_index =5
header.font=font

'''调整对齐方式'''
align =xlwt.Alignment()
align.vert = xlwt.Alignment.VERT_CENTER
align.horz = xlwt.Alignment.HORZ_CENTER
header.alignment =align

'''边框设置'''
borders= xlwt.Boders()
props = (
    ('top','top_colour'),('right','right_colour'),
    ('bottom','bottom_colour'),('left','left_colour')
)
for position,colour in props:
    setattr(borders,position,xlwt.Borders.DASHED)
    setattr(borders,colour,4)
header.borders =borders


'''单元格大小设置'''
sheet.row(0).set_style(xlwt.easyxf(f'front:height{20*40}'))

for index,tilte in enumerate(titles):
    sheet.col(index).width = 20*200 
    sheet.write(0,index,title,header)






