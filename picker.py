import random

restaurants = {
    "Arby's":['American', 1, 'https://logos-world.net/wp-content/uploads/2021/08/Arbys-Logo.png'],
    "IHOP":['Breakfast', 3, 'https://media.wired.com/photos/59324b4d5c4fbd732b551ad4/master/w_1600%2Cc_limit/ihope-gallery-1.png'],
    'Midori':['Sushi', 5, 'https://media-cdn.tripadvisor.com/media/photo-s/0e/aa/85/e1/midori-sushi-martini.jpg']
}

def pick(cost=1, picks=1):
    food = list(restaurants.keys())
    weights = []
    
    for i in food:
        temp = restaurants[i][1]
        if temp < cost:
            temp = 100
        weights.append(10 / temp)
    
    outputs = random.choices(food, weights=weights, k=picks)
    return outputs[0]

def pull_info(pick):
    return restaurants[pick]
