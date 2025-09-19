from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Simulated database
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1200, 'description': 'High-performance laptop for professionals'},
    {'id': 2, 'name': 'Mouse', 'price': 25, 'description': 'Ergonomic wireless mouse'},
    {'id': 3, 'name': 'Keyboard', 'price': 75, 'description': 'Mechanical gaming keyboard'},
]

@csrf_exempt
def product_view(request):
    global products

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            new_id = max([p['id'] for p in products]) + 1 if products else 1
            products.append({
                'id': new_id,
                'name': request.POST['name'],
                'price': int(request.POST['price']),
                'description': request.POST['description']
            })

        elif action == 'edit':
            product_id = int(request.POST['id'])
            for p in products:
                if p['id'] == product_id:
                    p['name'] = request.POST['name']
                    p['price'] = int(request.POST['price'])
                    p['description'] = request.POST['description']

        elif action == 'delete':
            product_id = int(request.POST['id'])
            products = [p for p in products if p['id'] != product_id]

        return redirect('/')

    return render(request, 'products/product_page.html', {'products': products})
