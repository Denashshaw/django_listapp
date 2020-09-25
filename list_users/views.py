from django.shortcuts import render
from .models import List
from django.core.paginator import Paginator
from .filters import ListFilter
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	context = {}
	all_list = List.objects.all();
	filter_input = ListFilter(request.GET, queryset = all_list)

	count_per_page = 10
	paginated_list = Paginator(filter_input.qs, count_per_page)
	page_num = request.GET.get('page')	
	list_val = paginated_list.get_page(page_num)

	return render(request, 'index.html', {'filter_input': filter_input, 'list_val': list_val})

