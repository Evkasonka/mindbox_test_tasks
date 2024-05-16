from pyspark.sql import SparkSession

# Создаем сессию Spark
spark = SparkSession.builder.getOrCreate()

# Создаем датафрейм для продуктов
# Каждый продукт имеет уникальный идентификатор и имя
products_data = [('p1', 'Product1'), ('p2', 'Product2'), ('p3', 'Product3')]
df_products = spark.createDataFrame(products_data, ['ProductID', 'ProductName'])


# Создаем датафрейм для категорий
# Каждая категория связана с идентификатором продукта
categories_data = [('p1', 'Category1'), ('p1', 'Category2'), ('p2', 'Category3')]
df_categories = spark.createDataFrame(categories_data, ['ProductID', 'CategoryName'])


# Объединяем два датафрейма по идентификатору продукта
# Используем 'left' join, чтобы сохранить все продукты, даже те, у которых нет категорий
df_joined = df_products.join(df_categories, on='ProductID', how='left')

# Создаем новый датафрейм, который содержит все пары «Имя продукта – Имя категории»
df_pairs = df_joined.select('ProductName', 'CategoryName')

# Создаем новый датафрейм, который содержит имена всех продуктов, у которых нет категорий
df_no_category = df_joined.filter(df_joined.CategoryName.isNull()).select('ProductName')

# Выводим результаты
print("Пары «Имя продукта – Имя категории»:")
df_pairs.show()

print("Продукты без категорий:")
df_no_category.show()