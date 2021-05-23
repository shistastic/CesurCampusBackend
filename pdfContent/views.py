from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.decorators import api_view

from pdfContent.models import ContentFile


@api_view(['POST'])
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        content = ContentFile.objects.create(name=myfile.name, file=myfile)
        content.save()

        return Response(200)
    else:
        return Response(400)


@api_view(['GET'])
def show_image(request, id):
    media_path = settings.MEDIA_ROOT
    print(media_path)
    content = ContentFile.objects.get(id=id)

    image_data = open(media_path + "\\" + str(content.file), "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

# Create your views here.
# @csrf_exempt
# def downloadPDF(request):
#     seoma_domain = 'webmaster.digital'
#     seoma_info = 'info@webmaster.digital'
#     report_content = json.loads(request.body)
#     # print(report_content)
#
#     template_path = 'reports/custom_pdf.html'
#
#     context = {
#         'seoma_domain': seoma_domain,
#         'seoma_info': seoma_info,
#         'report_content': report_content,
#     }
#
#     response = HttpResponse(content_type='application/pdf')
#
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#
#     template = get_template(template_path)
#     html = template.render(context)
#
#     # print(context['report_content'])
#
#     # pisa_status = pisa.CreatePDF(html, dest=response)
#
#     # if pisa_status.err:
#     #     return HttpResponse("we have erros<pre>" + html + "</pre>")
#     return response
#
#     # print(report_url)
#     # return HttpResponse(200)
