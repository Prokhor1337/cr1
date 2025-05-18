products = {
    "вишиванка": {"категорія": "одяг", "ціна": 1200},
    "лляна сукня": {"категорія": "одяг", "ціна": 1500},
    "мед": {"категорія": "їжа", "ціна": 200},
    "варення з ожини": {"категорія": "їжа", "ціна": 180},
    "глечик ручної роботи": {"категорія": "сувеніри", "ціна": 350},
    "дерев’яна іграшка": {"категорія": "сувеніри", "ціна": 250},
    "намисто з бісеру": {"категорія": "аксесуари", "ціна": 400}
}

def FilterProductsByCategory(category):
    return (name for name, info in products.items() if info["категорія"] == category)

def ShowAllProducts():
    print("\nУсі товари:")
    for name, info in products.items():
        print(f"- {name.title()} ({info['категорія']}) — {info['ціна']} грн")

def PlaceOrder():
    basket = []
    total = 0
    while True:
        choice = input("\nВведіть назву товару для додавання або 'стоп' для завершення: ").lower()
        if choice == "стоп":
            break
        elif choice in products:
            basket.append(choice)
            total += products[choice]["ціна"]
            print(f"Додано {choice.title()} до кошика.")
        else:
            print("Товар не знайдено. Спробуйте ще раз.")
    return basket, total

def RunShop():
    print("\nВіртуальна крамниця українських виробників")
    while True:
        print("\nОберіть дію:")
        print("1 — Показати всі товари")
        print("2 — Фільтрувати за категорією")
        print("3 — Оформити замовлення")
        print("4 — Вийти")
        command = input("Ваш вибір: ")
        if command == "1":
            ShowAllProducts()
        elif command == "2":
            category = input("Введіть назву категорії (одяг, їжа, сувеніри, аксесуари): ").lower()
            filtered = list(FilterProductsByCategory(category))
            if filtered:
                print(f"\nТовари у категорії '{category}':")
                for item in filtered:
                    print(f"- {item.title()} — {products[item]['ціна']} грн")
            else:
                print("Немає товарів у цій категорії.")
        elif command == "3":
            basket, total = PlaceOrder()
            if basket:
                print("\nВаше замовлення:")
                for item in basket:
                    print(f"- {item.title()} — {products[item]['ціна']} грн")
                print(f"Загальна сума: {total} грн")
            else:
                print("Замовлення не містить товарів.")
        elif command == "4":
            print("Дякуємо за візит!")
            break
        else:
            print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    RunShop()
