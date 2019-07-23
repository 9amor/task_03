from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [
            {
                "restaurant_name":"Al Baik",
                "food_type":"chicen",
            },
            {
                "restaurant_name":"Fire grill",
                "food_type":"casadia",
            },
            {
                "restaurant_name":"Baskin Robins",
                "food_type":"Choclate icecreem",
            },
        ],
    }

    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_list": {
                "restaurant_name":"Baskin Robins",
                "food_type":"Choclate icecreem",
                },
    }
    return render(request, 'detail.html', context)
