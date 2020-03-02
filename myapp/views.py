from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import VInfoRegister,NisUserInfo,VDataMonitor,ExperimentInfo,SubsysInfo,DataProcessIpc,UserMediaFile
from .forms import VInforRegister_form,RawVinforresiger_form,NisUserInfo_form,RawUserInfo_form,ExperimentInfo_form
import json
# class Registertest(View):
#     def get(self, request):
#         # 表单渲染注册界面
#         form = RegisterForm()
#         return render(request, 'mywebsite/register_2.html',context={
#             'form':form,
#         })
#     def post(self, request):
#         # 表单校验数据
#         form = RegisterForm(request.POST)
#         # 如果数据正确
#         if form.is_valid():
#             return HttpResponse('注册成功')
#
#         # 若校验失败，则渲染注册界面
#         return render(request, 'mywebsite/register_2.html', context={
#             'form': form,
#         })
#

##能够直接form.forms的表单进行
# def register(request):
#     my_form = NisUserInfo_form(request.GET)
#     print('we are hehre')
#     if request.method == "POST":
#         my_form = RawUserInfo_form(request.GET)
#         my_form.save()
#     context = {
#         'form':my_form
#
#     }
#     return  render(request,'mywebsite/register_2.html',context)
def  registersave(request):
    print('we at resigster save')
    form = NisUserInfo_form(request.POST or None)
    if form.is_valid():
        form.save()
        print('this is valid')
        return HttpResponseRedirect( '/index/')

    context = {
        'form':form,

    }
    return  render(request,'mywebsite/register.html',context)


def regist(request):
    if request.method == 'POST':
        regi_form = NisUserInfo_form(request.POST)  #包含用户名和密码
        if regi_form.is_valid():
            #获取表单数据
            username = regi_form.cleaned_data['username']  #cleaned_data类型是字典，里面是提交成功后的信息
            password = regi_form.cleaned_data['password']
            phone = regi_form.cleaned_data['password']
            #添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            registAdd = NisUserInfo.objects.create(username=username, password=password,phone=phone)
            # print registAdd
            if registAdd == False:

                print('注册失败')
                return render(request,'share1.html', {'registAdd': registAdd, 'username': username})

            else:
                print('注册成功')
                # return HttpResponse('ok')
                return render(request,'share1.html', {'registAdd': registAdd})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        regi_form = NisUserInfo_form(request.POST or None)
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request,'mywebsite/register.html', {'form': regi_form})



# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print username,password
#         re = auth.authenticate(username=username,password=password)  #用户认证
#         if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
#             auth.login(request,re)   #登陆成功
#             return redirect('/',{'user':re})    #跳转--redirect指从一个旧的url转到一个新的url
#         else:  #数据库里不存在与之对应的数据
#             return render(request,'login.html',{'login_error':'用户名或密码错误'})  #注册失败
#     return render(request,'login.html')
#
#


def login(request):
    print('we are login 1')

    if request.method == "POST":
        print('we are login 2')

        username = request.POST.get('username')
        password = request.POST.get('password')
        # if username=='游客':
        #     print('我是游客')
        #     return render(request, 'mywebsite/login_2.html')
        #
        # else:
        #     print('quit界面的username',username)
        #     print('return quit 界面')
        #     # return HttpResponseRedirect(request, 'mywebsite/log_out/',{'username':username})
        #
        #



        list = NisUserInfo.objects.filter(username = username)
        if len(list)==0:
            print('该用户不存在')
        else:
            if list[0].password==password:
                print('登录成功',username)
                request.session['username']=username
                print(request.session['username'])
                return HttpResponseRedirect("/index/")
            else:
                print('密码输入错误')
                # request.session['username']=username
                # return render(request,'login.html',)
                return render(request,"mywebsite/login.html",{'msg':'密码错误'})
        print(type(list))
        print(list.values)
        print('username',username)
        print('password',password)
    if request.method == "GET":
        username = request.session.get('username')
        print(username)
        if username is None:
            print('username is none')
            return render(request, 'mywebsite/login.html')

        else:

            print('return quit 界面')
            return render(request,'mywebsite/log_out.html',{'username':username})
            # return HttpResponseRedirect(request, 'mywebsite/log_out/',{'username':username})


    # else:
        return render(request, 'mywebsite/login.html')

        # username=request.POST.get('username','login')

def logout(request):
    # 1. 将session中的用户名、昵称删除
    request.session.flush()
    # 2. 重定向到 登录界面
    username=request.session.get('username','login')
    print('username',username)

    return HttpResponseRedirect("/index/")
    # return render(request, 'mywebsite/index.html',{'username':username})


def checkPassword(cp,pwd):
    list = VInfoRegister.objects.filter(phone = cp,password = pwd)
    print('查询结果:',list)
    if len(list)==0:
        print()
        return False
    else:
        return True



    pass
















'''
一个实现实时数据到界面上的方案：

'''
# def  RawVInfoRegisterview(request):
#     my_form = RawVinforresiger_form(request.GET)
#     if request.method == "POST":
#         my_form = RawVinforresiger_form(request.POST)
#     context = {
#         'form':my_form
#
#         }
#     return  render(request, '../static/../templates/mywebsite/register_info_create.html', context)



def  VInfoRegisterview(request):
    form = VInforRegister_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form

    }
    return  render(request,'../templates/mywebsite/register_info_create.html',context)











def test(request):

    s=VInfoRegister.objects.all()

    mycontext={
        "my_text":"this is about us",
        "my_number":123,
        "register":s
    }


    return render(request,"test.html",mycontext)


def main(request):
    return render(request, 'main.html')
def index(request):
    username=request.session.get('username','neww')
    print('username',username)

    return render(request, 'mywebsite/index.html',{'username':username})
def dataview(request):


    #历史数据筛选
    # data=gascontrol(request)
    expriments = ExperimentInfo.objects.all()
    V_registerinfos=VInfoRegister.objects.all()
    subsysid_registerid=[]
    v_register_name=[]


    exp_ids=[]
    exp_managers=[]
    start_times=[]
    exp_description=[]
    for expriment in expriments:
        exp_ids.append(expriment.exp_id)
        exp_managers.append(expriment.exp_managername)
        start_times.append(expriment.start_time)
        exp_description.append(expriment.exp_description)
    for registerinfo in V_registerinfos:
        subsysid_registerid.append((registerinfo.subsys_id,registerinfo.register_id))
        v_register_name.append(registerinfo.v_name)

    expinforegister_form = ExperimentInfo_form(request.POST or None)


    datatoreturn={
        'exp_ids':exp_ids,
        'exp_managers':exp_managers,
        'start_times':start_times,
        'exp_descriptions':exp_description,

        'subsysid_registerid':subsysid_registerid,
        'v_register_name':v_register_name,
        'expinfo_register_form': expinforegister_form,

    }
    # print('we are in data to return part  dataview')
    print(datatoreturn)

    # return HttpResponseRedirect("dataview/")
    return render(request, 'mywebsite/dataview.html',datatoreturn)
def dataviewsearch(request):
    print(request.GET.get('namechoose'))





    #前台传送的数据内容
    # data=gascontrol(request)

    #前台数据打印
    print('request.GET.get name choose ', request.GET.get('namechoose'))
    print('打印实验id',request.GET.get('expid'))




    v_data_values=[]
    v_data_times=[]
    subsysid_registerid=[]
    v_register_name=[]
    v_data_xy=[]


    expriment_id=request.GET.get('expid');
    expriment = ExperimentInfo.objects.get(exp_id=expriment_id)

    exp_id=expriment.exp_id
    exp_managers=expriment.exp_managername
    start_time=expriment.start_time
    exp_description=expriment.exp_description




    v_names_datas=[]
    names=json.loads(request.GET.get('namechoose'));
    print('打印names',names)
    # print(names[0],names[1],names[2])
    for v_name in names :
        print(v_name)
        v_monitor=VInfoRegister.objects.get(v_name=v_name)
        v_data_moninitors=VDataMonitor.objects.filter(subsys_id=v_monitor.subsys_id,register_id=v_monitor.register_id,exp_id=expriment_id)

        for v_data_moninitor in v_data_moninitors:
            v_data_values.append(v_data_moninitor.v_data)
            # str1 = .strftime('%Y-%m-%d %H:%M:%S')
            v_data_times.append(str(v_data_moninitor.v_data_time.strftime('%Y-%m-%d %H:%M:%S.%f')))

            v_data_xy.append([str(v_data_moninitor.v_data_time.strftime('%Y-%m-%d %H:%M:%S.%f')),v_data_moninitor.v_data])

        v_name_data={
            'v_name':v_name,
            'v_data_times':v_data_times,
            'v_data_values':v_data_values,
        }
        v_data_times=[]
        v_data_values=[]
        v_names_datas.append(v_name_data)

    print(v_names_datas)

    datatoreturn={
            'exp_ids':exp_id,
            'exp_managers':exp_managers,
            'exp_descriptions':exp_description,

            'subsysid_registerid':subsysid_registerid,
            'v_names_datas':v_names_datas,

        }
    a= json.dumps(datatoreturn)
    print('we are in data to return part, to return is that okayh')
    # print(datatoreturn)

    return HttpResponse(a)
    # return HttpResponseRedirect("dataview/")
    # return render(request, 'mywebsite/dataview.html',datatoreturn)


def dataviewredirect(request):  #从头开始跳转
    return HttpResponseRedirect("/dataview/")
    # return render(request, 'mywebsite/dataview.html')

def teststatic(request):
    return render(request, 'mywebsite/teststatic.html')
def indexredirect(request):  #从头开始跳转
    return HttpResponseRedirect("/index/")
    # return render(request, 'mywebsite/dataview.html')



def search(request):
    a=VInfoRegister.objects.all()[0:2]


    print('hello world')
    my_data={
        'name':request.POST['q'],
        'value':12.5,
        'VRegisterInfo':a
    }
    return render(request,'main.html',my_data)
    # return HttpResponse('name')  #这个相当于一个简易的界面，直接进行跳转的


def search2(request):
    a = VInfoRegister.objects.all()[0:1]

    print('hello world')
    my_data = {
        'name2':'hha',
        'value2':14.25,
        'VRegisterInfo': a
    }
    print('this ia  a bnew')
    return render(request, 'main.html', my_data)
def auto_flush(request):
    # return render(request,'main.html')

    return HttpResponse('我们点击了这个按钮')



def  gascontrol(request):
    table = VDataMonitor.objects.all()
    print('we arer in gascontrol la')
    subsysid=[]
    registerid=[]
    expid=[]
    v_data=[]
    v_data_time=[]
    for obj in table:
        subsysid.append(obj.subsys_id)
        registerid.append(obj.register_id)
        expid.append(obj.exp_id)
        v_data.append(obj.v_data)
        v_data_time.append(obj.v_data_time)
    datatoreturn={
        'subsysid':subsysid,
        'registerid':registerid,
        'expid':expid,
        'v_data':v_data,
        'v_data_time':v_data_time
    }



def data_add(request):
    pass


from django.http import StreamingHttpResponse


def big_file_download(request):
    # do something...
    print('we are at big file down load part')

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                print(c)
                if c:
                    yield c
                else:
                    break

    the_file_name = "test2.txt"
    response = HttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response


def file_download(request):
    print('file download function')
    file = open('test2.txt', 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="example.txt"'
    print(response)
    return response

from xlwt import *
from io import StringIO,BytesIO
import os
def data_download(request):
    """
    导出excel表格
    """
    #获取要筛选的条件

    numerofdata=request.GET.get('expid')
    print('request.get',numerofdata)


    print('we are at data download')
    print(request.content_type)
    list_obj = VInfoRegister.objects.filter()
    # print(len(list_obj[0:int(numerofdata)]))
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, "subsys_id")
        w.write(0, 1, u"register_id")
        w.write(0, 2, u"v_name")
        w.write(0, 3, u"ip_port")
        w.write(0, 4, u"created_time")
        w.write(0, 5, u"created_manager")
        w.write(0, 6, u"v_type")
        w.write(0, 7, u"v_discription")
        w.write(0, 8, u"v_status")




        # 写入数据
        excel_row = 1
        for obj in list_obj:

            w.write(excel_row, 0, obj.subsys_id)
            w.write(excel_row, 1, obj.register_id)
            w.write(excel_row, 2, obj.v_name)
            w.write(excel_row, 3, obj.ip_port)
            w.write(excel_row, 4, obj.created_time.strftime("%Y-%m-%d"))
            w.write(excel_row, 5, obj.created_manager)
            w.write(excel_row, 6, obj.v_type)
            w.write(excel_row, 7, obj.v_description)
            w.write(excel_row, 8, obj.v_status)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio =BytesIO()  # 这里原博客是StringIO.StringIO()，发现有点问题
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=yourname.xls'
        response.write(sio.getvalue())
        return response

import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse,StreamingHttpResponse,JsonResponse

@csrf_exempt
def Export_excel(request):  # 生成EXCEL表格
    if request.method == 'POST':
        try:
            now = datetime.datetime.now()
            expid = request.POST.get('expid')
            print('request.get', expid)
            # print(type(numerofdata))
            registernames =json.loads(request.POST.get("namechoose"))

            print("registernames:",registernames)
            registerids=[]
            filename='IDs'
            for name in registernames:
                temp_registerid=VInfoRegister.objects.get(v_name=name).register_id
                temp_subsys = VInfoRegister.objects.get(v_name=name).subsys_id
                filename = filename +str(temp_subsys)+str(temp_registerid)
                registerids.append(temp_registerid)
                print(registerids)
            file_path = os.path.join(r'static/excel/', '%s.xls' % (now.strftime("%Y-%m-%d-%H-%M-%S")+filename))
            #

            print('we are at data download')
            print(request.content_type)
            list_obj=[]
            for registerid in registerids:
                list_obj.extend(VDataMonitor.objects.filter(exp_id=expid,register_id=registerid))
            # list_obj =list_obj [0:int(numerofdata)]
            # print(list_obj[0].register_id)


            if list_obj:
                # 创建工作薄
                ws = Workbook(encoding='utf-8')
                w = ws.add_sheet(u"数据报表第一页")
                w.write(0, 0, "subsys_id")
                w.write(0, 1, u"register_id")
                w.write(0, 2, u"exp_id")
                w.write(0, 3, u"v_data")
                w.write(0, 4, u"v_data_time")

                # 写入数据
                excel_row = 1
                for obj in list_obj:
                    w.write(excel_row, 0, obj.subsys_id)
                    w.write(excel_row, 1, obj.register_id)
                    w.write(excel_row, 2, obj.exp_id)
                    w.write(excel_row, 3, obj.v_data)
                    w.write(excel_row, 4, obj.v_data_time.strftime("%Y-%m-%d %H:%M:%S.%f"))
                    excel_row += 1
                # 检测文件是够存在
                # 方框中代码是保存本地文件使用，如不需要请删除该代码
                ###########################
                # exist_file = file_path+'test.xls'
                # if exist_file:
                #     os.remove(r"test.xls")
                ws.save(file_path)
                print('file_path',file_path)
                print('we have saved the file ')
            return JsonResponse({'code': 0, 'data': file_path})  # 将路径返回到前台
        except Exception as e:
            print(e)
            return JsonResponse({'code': 1, 'data': '导出表格失败!'})
    elif request.method == 'GET':
        print('we are at get method part')
        excel_download(request)


def excel_download(request):
    try:
        filename = request.GET.get('data',None)
        def file_iterator(file_name):
            with open(file_name, 'rb')as f:
                while True:
                    c = f.read(512)
                    if c:
                        yield c
                    else:
                        break
        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename={0}".format(filename.split('/')[2])#这里改成自己需要的文件名
        return response
    except Exception as e:
        print (e)

def process_status_update(request):
    processobjs =DataProcessIpc.objects.all()
    process_statuses=[]
    process_names=[]
    process_updatetimes=[]


    for process in processobjs:
        process_statuses.append(process.process_status)
        process_names.append(process.process_name)
        process_updatetimes.append(process.update_time.strftime('%Y-%m-%d %H:%M:%S'))

    datatoreturn={
        'process_names':process_names,
        'process_statuses':process_statuses,
        'process_updateimes':process_updatetimes
    }
    a= json.dumps(datatoreturn)
    print('we are in data to return part, to return is that okay update')
    # print(datatoreturn)

    return HttpResponse(a)
def upload_fileRedirect(request):
    print("we are in redirect ")
    return HttpResponseRedirect("/upload/")
def upload_filehtml(request):
    print("file file fjiel")
    return render(request, 'mywebsite/upload.html')

def upload_file(request):
    if request.method == 'POST':

        username = request.session['username']
        myFile = request.FILES.get("myfile",None)
        print(myFile,'++++++++++++++++++++++')
        if not myFile:
            return HttpResponse('no files for upload!')

        # Product.objects.filter(id=uid).update(image=myFile.name,jad_address=myFile)
        #这个是存在的是本地的
        destination = open(os.path.join("/home/scottar/Desktop/nis_website/nis_website/uploadFile/", myFile.name), 'wb+')

        for chunk in myFile.chunks():
            destination.write(chunk)
            print(destination,'----------------------')
        destination.close()

        #完成了数据的上传,此时,将用户的id,并且将上传的文件的名称和类型保存到数据库表格当中
        print(myFile.name)
        print(type(myFile))
        name = myFile.name

        print(username)
        if name[-4] == '.':
            print('3个点',name)
            # filetype = name[-3:]
        elif name[-5] == '.':
            filetype = name[-4:]
            # print('5ge dian'name[-4:])
        else:
            print('othiers')


        # #---------表中插入数据方式一
        # # info={"username":u,"sex":e,"email":e}
        # # models.UserInfor.objects.create(**info)
        #
        # #---------表中插入数据方式二
        UserMediaFile.objects.create(
            username=username,
            filename=name,
            filetype=filetype
        )

        # info_list=models.UserInfor.objects.all()
        #
        # return render(req,"userInfor.html",{"info_list":info_list})






    print("we are in upload file")
    # return HttpResponseRedirect("/dataview/")
    return render(request, 'mywebsite/upload.html')

def download_fileRedirect(request):
    print("we are in redirect ")
    return HttpResponseRedirect("/download/")
def download_filehtml(request):
    print("file file fjielaaaaaa")
    userfileobjs =UserMediaFile.objects.filter(username=request.session['username'])
    filenames = []
    for userfile in userfileobjs:
        filenames.append(userfile.filename)
    # print('打印当前的filename',filenames)
    my_data = {
        'filenames':filenames
    }


    return render(request, 'mywebsite/download.html',my_data)

def download_file(request,filename,filetype):

    print("we are in download file",filename)
    print("filetype",filetype)
####可以实现多种格式的文件的下载###########
    # field = request.GET.get('field')
    # name = request.GET.get('name')
    # print('filed',field)
    # print('name',name)
    file = open("/home/scottar/Desktop/nis_website/nis_website/uploadFile/"+filename+'.'+filetype,'rb')
    response =FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename='+filename+'.'+filetype
###################################################
    # if request.method == "GET":
    #     file = open('/home/scottar/Desktop/nis_website/api.pdf', 'rb')
    #     response = HttpResponse(file)
    #     response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    #     response['Content-Disposition'] = 'attachment;filename="api.pdf"'





    return  response


    # return HttpResponseRedirect("/dataview/")
    # return render(request, 'mywebsite/download.html')




def expinfo_register(request):
    form = ExperimentInfo_form(request.POST or None)

    if request.method=="GET":
        print('we are at get info')
        pass
    else:
        if form.is_valid():
            print('this is vilid')
            form.save()
            return HttpResponseRedirect("/dataview/")

    context = {
        'expinfo_register_form':form,

    }
    return render(request, 'mywebsite/dataview.html',context)


    pass


