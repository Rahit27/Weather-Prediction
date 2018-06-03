from django.shortcuts import render
from .predictor import predictions



def homepage(request):


    predictions = predictions
    template_name = "Predictor/home.html"
    context = {
                "predictions":predictions

                }
    return render(request,template_name,context)
