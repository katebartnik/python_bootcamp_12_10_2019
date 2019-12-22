from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from maths.forms import MathForm
from maths.models import Math


def calculate(request, op, a, b):
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y,
    }
    try:
        result = operations[op](a, b)
    except ZeroDivisionError:
        result = "Działanie niedozwolone"
    Math.objects.create(
        operation=op,
        a=a,
        b=b,
        result=result
    )
    return HttpResponse(result)


def history(request):
    maths = Math.objects.all()
    template = get_template("maths/math_history.html")
    context = {"maths": maths, "text": "Ala ma kota"}
    return HttpResponse(template.render(context=context))


def history2(request):
    maths = Math.objects.all()
    context = {"maths": maths, "text": "Ala ma kota"}
    return render(
        request=request,
        template_name="maths/math_history.html",
        context=context
    )


def history_detail(request, id):
    m = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/math_detail.html",
        context={"math": m}
    )


def do_math(request):
    if request.method == "POST":
        # print("To jest POST")
        # a = request.POST['a']
        # b = request.POST['b']
        # op = request.POST['operation']
        form = MathForm(data=request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/maths/")
    else:
        form = MathForm()
        return render(
            request=request,
            template_name="maths/do_math.html",
            context={'form': form}
        )
