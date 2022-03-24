import datetime
def context(request):
    # stuff needed before defining context
    context = {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
        # any other context variables needed
    }

    return context

def footer_year(request):
    return{'year':datetime.datetime.now().year}



    