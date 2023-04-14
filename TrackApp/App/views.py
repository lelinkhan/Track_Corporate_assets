from django.shortcuts import render
from .models import Company, Employee, Device, DeviceLog


def index(request):
    all_list = DeviceLog.objects.all()
    context = {'emp': all_list}
    return render(request, 'index.html', context)


def all_company(request):
    all_comp = Company.objects.all()
    context = {'all_comp': all_comp}
    return render(request, 'company.html', context)


def company_details(request, company_id):
    company = Company.objects.get(id=company_id)
    employee = Employee.objects.filter(company=company)
    context = {'company': company, 'employees': employee}
    return render(request, 'company_details.html', context)


def all_device(request):
    all_dev = Device.objects.all()
    context = {'all_dev': all_dev}
    return render(request, 'device.html', context)


def device_details(request, device_id):
    device = Device.objects.get(id=device_id)
    deviceLog = DeviceLog.objects.filter(device=device)
    context = {'device': device, 'deviceLog': deviceLog}
    return render(request, 'device_details.html', context)
