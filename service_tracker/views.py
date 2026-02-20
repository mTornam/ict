from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ServiceRecordForm
from .models import ServiceRecord
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    records = ServiceRecord.objects.all()
    
    # filtering
    status_filter = request.GET.get('status')
    received_by_filter = request.GET.get('received_by')
    office_filter = request.GET.get('office')
    
    if status_filter:
        if status_filter == 'resolved':
            records = records.filter(is_resolved=True)
        elif status_filter == 'unresolved':
            records = records.filter(is_resolved=False)
    
    if received_by_filter:
        records = records.filter(received_by__icontains=received_by_filter)
    
    if office_filter:
        records = records.filter(room_number__icontains=office_filter)
    
    # sorting
    sort_fields = {
        'received_at': 'Date',
        'requester_name': 'Name', 
        'is_resolved': 'Resolved',
        }
    sort = request.GET.get('s', '-received_at')
    direction = request.GET.get('d', 'dsc')

    if sort not in sort_fields:
        sort = 'received_at'
    if direction == 'dsc':
        sort = f'-{sort}'
    records = records.order_by(sort)

    # pagination
    paginator = Paginator(records, per_page=12, allow_empty_first_page=True)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    custom_range = page_obj.paginator.get_elided_page_range(
        number=page_obj.number, 
        on_ends=1
    )
    context = {
        'records': page_obj,
        'custom_range': custom_range,
        'sort_fields': sort_fields,
    }
    return render(request, 'service_tracker/index.html', context)

@login_required
def createJob(request):
    form = ServiceRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            form.instance.received_by = user
            form.save()
            return redirect('service_tracker:index')
    
    return render(request, 'service_tracker/create-job.html', {'form': form})

@login_required
def detail(request, pk):
    record = get_object_or_404(ServiceRecord, pk=pk)
    return render(request, 'service_tracker/detail.html', {'record': record})
    
@login_required
def updateJob(request, pk):
    record = get_object_or_404(ServiceRecord, pk=pk)
    form = ServiceRecordForm(request.POST or None, instance=record)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('service_tracker:detail', pk=record.pk)
    
    return render(request, 'service_tracker/update-job.html', {'form': form, 'record': record})

def markResolved(request, pk):
    record = get_object_or_404(ServiceRecord, pk=pk)
    if request.method == 'POST':
        record.is_resolved = True
        record.save()
        return redirect('service_tracker:detail', pk=record.pk)
    
    return redirect('service_tracker:detail', pk=record.pk)