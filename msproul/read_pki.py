from secrets_dev import pki_name
from django.http import HttpResponse

def read_file(request):
    f = open('../ssl/' + pki_name, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")