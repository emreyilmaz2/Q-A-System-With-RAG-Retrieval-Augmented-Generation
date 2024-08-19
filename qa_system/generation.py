import random
from datetime import datetime, timedelta

# Ürün listesi
products = [
    {"name": "apple", "category": "fruit", "price": 1.00},
    {"name": "banana", "category": "fruit", "price": 0.50},
    {"name": "orange", "category": "fruit", "price": 1.20},
    {"name": "milk", "category": "dairy", "price": 2.50},
    {"name": "bread", "category": "bakery", "price": 1.80},
    {"name": "cheese", "category": "dairy", "price": 3.00},
    {"name": "butter", "category": "dairy", "price": 2.80},
    {"name": "chocolate", "category": "snack", "price": 1.50},
    {"name": "coffee", "category": "beverage", "price": 4.00},
    {"name": "tea", "category": "beverage", "price": 2.00},
    {"name": "yogurt", "category": "dairy", "price": 1.20},
    {"name": "egg", "category": "dairy", "price": 0.20},
    {"name": "chicken", "category": "meat", "price": 5.00},
    {"name": "beef", "category": "meat", "price": 7.00},
    {"name": "pasta", "category": "pantry", "price": 1.50},
    {"name": "rice", "category": "pantry", "price": 2.00},
    {"name": "potato", "category": "vegetable", "price": 0.80},
    {"name": "tomato", "category": "vegetable", "price": 1.00},
    {"name": "cucumber", "category": "vegetable", "price": 1.20},
    {"name": "onion", "category": "vegetable", "price": 0.70},
    {"name": "garlic", "category": "vegetable", "price": 0.50},
    {"name": "carrot", "category": "vegetable", "price": 0.90},
    {"name": "lettuce", "category": "vegetable", "price": 1.00},
    {"name": "spinach", "category": "vegetable", "price": 1.50},
    {"name": "peppers", "category": "vegetable", "price": 1.80},
    {"name": "mushrooms", "category": "vegetable", "price": 2.00},
    {"name": "beans", "category": "pantry", "price": 1.00},
    {"name": "lentils", "category": "pantry", "price": 1.20},
    {"name": "nuts", "category": "snack", "price": 3.00},
    {"name": "honey", "category": "sweetener", "price": 4.00},
    {"name": "jam", "category": "sweetener", "price": 2.50},
    {"name": "peanut butter", "category": "spread", "price": 3.50},
    {"name": "cereal", "category": "breakfast", "price": 2.50},
    {"name": "oatmeal", "category": "breakfast", "price": 1.80},
    {"name": "sugar", "category": "sweetener", "price": 1.00},
    {"name": "salt", "category": "seasoning", "price": 0.50},
    {"name": "pepper", "category": "seasoning", "price": 1.00},
    {"name": "vinegar", "category": "condiment", "price": 1.20},
    {"name": "oil", "category": "condiment", "price": 2.50},
    {"name": "soy sauce", "category": "condiment", "price": 1.80},
    {"name": "ketchup", "category": "condiment", "price": 2.00},
    {"name": "mustard", "category": "condiment", "price": 1.50},
    {"name": "mayonnaise", "category": "condiment", "price": 2.00},
    {"name": "spaghetti sauce", "category": "condiment", "price": 2.50},
    {"name": "soup", "category": "pantry", "price": 1.80},
    {"name": "crackers", "category": "snack", "price": 2.00},
    {"name": "chips", "category": "snack", "price": 2.50},
    {"name": "cookies", "category": "snack", "price": 3.00},
    {"name": "cake", "category": "dessert", "price": 4.00},
    {"name": "ice cream", "category": "dessert", "price": 3.50},
    {"name": "frozen vegetables", "category": "frozen", "price": 2.00},
    {"name": "frozen fruit", "category": "frozen", "price": 3.00},
    {"name": "pizza", "category": "frozen", "price": 5.00},
    {"name": "frozen meat", "category": "frozen", "price": 6.00},
    {"name": "fish", "category": "meat", "price": 4.50},
    {"name": "pita bread", "category": "bakery", "price": 2.00},
    {"name": "tortillas", "category": "bakery", "price": 2.50},
    {"name": "bagels", "category": "bakery", "price": 3.00},
    {"name": "croissants", "category": "bakery", "price": 2.80},
    {"name": "muffins", "category": "bakery", "price": 3.20},
    {"name": "canned tomatoes", "category": "pantry", "price": 1.50},
    {"name": "canned beans", "category": "pantry", "price": 1.20},
    {"name": "canned tuna", "category": "pantry", "price": 1.80},
    {"name": "canned soup", "category": "pantry", "price": 2.00},
    {"name": "baking powder", "category": "baking", "price": 1.00},
    {"name": "baking soda", "category": "baking", "price": 0.80},
    {"name": "flour", "category": "baking", "price": 2.00},
    {"name": "rice vinegar", "category": "condiment", "price": 1.50},
    {"name": "sesame oil", "category": "condiment", "price": 2.50},
    {"name": "sriracha", "category": "condiment", "price": 2.00},
    {"name": "olive oil", "category": "condiment", "price": 3.00},
    {"name": "balsamic vinegar", "category": "condiment", "price": 2.50},
    {"name": "cream cheese", "category": "dairy", "price": 2.80},
    {"name": "sour cream", "category": "dairy", "price": 1.50},
    {"name": "buttermilk", "category": "dairy", "price": 2.00},
    {"name": "croutons", "category": "snack", "price": 1.80},
    {"name": "granola", "category": "breakfast", "price": 3.00},
    {"name": "trail mix", "category": "snack", "price": 3.50},
    {"name": "energy bars", "category": "snack", "price": 2.50},
    {"name": "dried fruit", "category": "snack", "price": 4.00}
]

# Rastgele bir IP adresi oluşturma
def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Rastgele bir zaman damgası oluşturma
# Rastgele bir zaman damgası oluşturma
def generate_timestamp():
    # Son bir ay içinde rastgele bir gün seç
    random_days = random.randint(0, 30)  # 0-30 gün arası
    random_date = datetime.now() - timedelta(days=random_days)
    
    # Bugünün başından itibaren rastgele bir zaman seç
    random_seconds = random.randint(0, 86400)  # 0-24 saat arası
    random_time = random_date.replace(hour=0, minute=0, second=0) + timedelta(seconds=random_seconds)
    return random_time.strftime("%d/%b/%Y:%H:%M:%S +0000")


# Rastgele bir HTTP yöntemi ve ürün path'i oluşturma
def generate_request():
    methods = ["GET", "POST"]
    action = random.choice(["view", "add-to-cart", "search", "filter", "checkout"])
    
    if action == "view":
        product = random.choice(products)
        path = f"/products/{product['name']}.html"
        status = 200  # Görüntüleme için 200 OK
    elif action == "add-to-cart":
        product = random.choice(products)
        path = f"/cart/add/{product['name']}"
        status = 201  # Sepete ekleme için 201 Created
    elif action == "search":
        query = random.choice(products)
        path = f"/search?q={query['name']}"
        status = 200  # Arama için 200 OK
    elif action == "filter":
        category = random.choice(["fruit", "dairy", "bakery", "snack", "beverage"])
        path = f"/products?category={category}"
        status = 200  # Filtreleme için 200 OK
    elif action == "checkout":
        path = "/checkout"
        status = 200  # Ödeme için 200 OK

    method = random.choice(methods)
    return f'"{method} {path} HTTP/1.1"', status
    method = random.choice(methods)
    return f'"{method} {path} HTTP/1.1"', status

# Rastgele bir yanıt boyutu oluşturma
def generate_size():
    return random.randint(200, 2000)

# Komple bir log satırı oluşturma
def generate_log_line():
    ip = generate_ip()
    timestamp = generate_timestamp()
    request, status = generate_request()
    size = generate_size()
    log_line = f'{ip} - - [{timestamp}] {request} {status} {size}'
    return log_line

# Bir log dosyası oluşturma
def generate_log_file(filename, num_lines=100):
    with open(filename, "w") as file:
        for _ in range(num_lines):
            log_line = generate_log_line()
            file.write(log_line + "\n")

# 100 satırlık bir log dosyası oluşturma
generate_log_file("market_logs.txt", num_lines=2000)

print("Log dosyası oluşturuldu: market_logs.txt")
