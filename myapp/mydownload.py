from django.http import HttpResponse
from  xlwt import *
from io import StringIO  #需要stringIO，这是python2中的，如果是python3，使用 from io import StringIO
# from .models import VInfoRegister
from models import VInfoRegister,NisUserInfo,VDataMonitor,ExperimentInfo,SubsysInfo

import os
def excel_export():
    """
    导出excel表格
    """
    list_obj = VInfoRegister.objects.all()
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, "id")
        w.write(0, 1, u"用户名")
        w.write(0, 2, u"发布时间")
        w.write(0, 3, u"内容")
        w.write(0, 4, u"来源")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj.id
            data_user = obj.username
            data_time = obj.time.strftime("%Y-%m-%d")[:10]
            data_content = obj.content
            dada_source = obj.source
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_time)
            w.write(excel_row, 3, data_content)
            w.write(excel_row, 4, dada_source)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio = StringIO()  #这里原博客是StringIO.StringIO()，发现有点问题
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=yourname.xls'
        response.write(sio.getvalue())
        return response

# if __name__=='__main__':
#     excel_export()

