import django_filters
from .models import List

class ListFilter(django_filters.FilterSet):
	class Meta:
		model = List
		fields = {
			'patient' : ['icontains'],
			# 'claim_id' : ['icontains'],
			# 'ins' : ['icontains']
		}