from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
data="""<table>
<tr><th>pid</th><th>pname</th><th>pcost</th></tr>
<tr><td>1001</td><td>book</td><td>1000.00</td></tr>
<tr><td>1002</td><td>pen</td><td>500.00</td></tr>
<tr><td>1003</td><td>phone</td><td>100000.00</td></tr>
<tr><td>1004</td><td>ac</td><td>50000.00</td></tr>
</table>"""
def htmldisplay(request):
    return HttpResponse(data,content_type="text/html")
def xmldisplay(request):
    return HttpResponse(data,content_type="application/xml")
def exceldisplay(request):
    return HttpResponse(data,content_type="application/vnd.ms-excel")