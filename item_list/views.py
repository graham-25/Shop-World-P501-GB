from django.shortcuts import render

# Create your views here.
def get_item_list(request):
    return render(request, 'item_list/item_list.html')
