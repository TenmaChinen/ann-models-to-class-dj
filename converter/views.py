from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from staticfiles.generators.keras_model_data_manager import get_model_data
from staticfiles.generators.python import generator as gen_py
# from staticfiles.generators.javascript import generator as gen_js
import json
import pdb
import h5py

class Lang:
  Python = "0"
  JavaScript = "1"


def index(request):
  context = {}
  return render(request,'converter/index.html',context)

# TODO : Check if h5 already contains full model & Keras Version
def check_file(request):
  pass

def convert(request):
  if request.method == 'POST':
    language = request.POST['lang']
    d_files = request.FILES
    file_json = d_files.get('fileJson')
    file_h5 = d_files.get('fileH5')

    model_json = None

    if file_h5:
      # file_h5_content = h5py.File(file_h5)
      pass

    if file_json:
      model_json = json.load(file_json)
    
    l_layers_objs = get_model_data(file_h5,model_json)
    code_model = gen_py.get_model_code(l_layers_objs)

    # pdb.set_trace()
    return JsonResponse({'model':code_model})

  return HttpResponse()