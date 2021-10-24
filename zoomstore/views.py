from django.shortcuts import render
import csv


# Create your views here.
def search(request):
    return render(request, 'search.html')


def search_result(request):
    if request.method == "POST":
        searched = request.POST.get('searched', True)
        with open('/home/akwa/projects/unitTest/python_assesment .csv', 'r') as file:
            reader = csv.reader(file)
            all_caps = searched.upper()
            for col in reader:
                matching = [s for s in col if all_caps in s]
                for item in matching:
                    return render(request, 'search_result.html', 
                    {'searched': searched, 'item': item}) 
    else:
        return render(request, 'search_result.html', {})
