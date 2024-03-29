from django.shortcuts import render
from .models import Bean
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# beanData = [
#     {'name': 'Pinto', 'origin': 'North America', 'description': 'Earthy, nutty flavor', 'cooking_time': '1-2 hours', 'image': ''},
#     {'name': 'Black', 'origin': 'South America', 'description': 'Slightly sweet, meaty texture', 'cooking_time': '1-2 hours', 'image': ''},
#     {'name': 'Chickpea', 'origin': 'Middle East', 'description': 'Nutty, buttery taste', 'cooking_time': '1.5-2 hours', 'image': ''},
#     {'name': 'Kidney', 'origin': 'Central America and Mexico', 'description': 'Mild, absorbent of flavors', 'cooking_time': '1-2 hours', 'image': ''},
#     {'name': 'Navy', 'origin': 'Americas', 'description': 'Mild, creamy texture', 'cooking_time': '1-2 hours', 'image': ''},
#     {'name': 'Lima', 'origin': 'South America', 'description': 'Buttery, starchy consistency', 'cooking_time': '1 hour', 'image': ''},
#     {'name': 'Adzuki', 'origin': 'East Asia', 'description': 'Sweet, nutty flavor', 'cooking_time': '1-1.5 hours', 'image': ''},
#     {'name': 'Cannellini', 'origin': 'Italy', 'description': 'Nutty, earthy taste', 'cooking_time': '1-1.5 hours', 'image': ''},
#     {'name': 'Garbanzo', 'origin': 'Middle East', 'description': 'Rich, nutty flavor', 'cooking_time': '1.5-2 hours', 'image': ''},
#     {'name': 'Great Northern', 'origin': 'North America', 'description': 'Delicate, nutty flavor', 'cooking_time': '1-1.5 hours', 'image': ''}
# ]


# Define the home view
def home(request):
  return render(request, 'home/index.html')

def about(request):
  return render(request, 'about/index.html')

def beans(request):
  beanData = Bean.objects.all()
  return render(request, 'beans/index.html', {
    'beans': beanData
  })

def bean_details(request, bean_id):
  beanData = Bean.objects.get(id=bean_id)
  return render(request, 'beans/details.html', {
    'bean': beanData
  })

class BeanCreate(CreateView):
  model = Bean
  fields = '__all__'

class BeanDelete(DeleteView):
  model = Bean
  success_url = '/beans'

class BeanUpdate(UpdateView):
  model = Bean
  fields = '__all__'

