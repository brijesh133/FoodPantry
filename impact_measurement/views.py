from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import checkout


# Create your views here.
@login_required(login_url='/')
def impact_measurement(request):
    total_check = 0
    total_amount = 0
    total_products = 0
    unique_id = []
    raw_data = checkout.objects.all()

    chart_values = calculatevalues(raw_data)

    
    for x in raw_data:
        total_check = total_check + 1
        total_amount = total_amount + x.price
        total_products = total_products + x.quantity
        if x.student_id not in unique_id:
            unique_id.append(x.student_id)


    quantity_by_student = calculate(unique_id)

    average = 0
    sumofquant = 0
    sumofstud = 0
    for key in quantity_by_student:
        sumofstud = sumofstud + 1
        sumofquant = sumofquant + quantity_by_student[key]

    average = sumofquant / sumofstud

    page_data = {"Total_Checkouts" : total_check, "Unique" : len(unique_id), "Total_Amount": total_amount, "Total_Quantity": total_products, "dat": quantity_by_student, "average": average, "dat2" : chart_values}

    print(page_data)

    return render(request, "impact_measurement/impact.html", context=page_data)



def calculate(unique_id):
    page_data_d = {}
    for x in unique_id:
        raw_data = checkout.objects.filter(student_id = x)
        quant = 0
        for y in raw_data:
            quant = quant + y.quantity
        page_data_d[x] = quant
    return page_data_d


# calculates highest item quantity donated item and respective items
def calculatevalues(raw_data):

    page_data_chartist = {}
    page_data_chartist_ret = {}

    for x in raw_data:
        page_data_chartist.setdefault(x.item_name, 0)


    for x in raw_data:
        page_data_chartist[x.item_name] = page_data_chartist[x.item_name] + x.quantity


    print(page_data_chartist)

    j = 0
    l1 = []
    l2 = []
    for w in sorted(page_data_chartist, key=page_data_chartist.get, reverse=True):
        page_data_chartist_ret[w] = page_data_chartist[w]
        if j == 10:
            break
        j = j + 1

    return page_data_chartist_ret