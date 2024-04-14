from django.shortcuts import render
from django.views import View
from django.db import connection
import pandas as pd

# Create your views here.

class Revenue_Products(View):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        users = cursor.execute("SELECT sum(a.quantity) as total_quantity, b.name, b.price FROM customer_orderitem a, customer_item b where a.product_id = b.id group by a.product_id")
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        print("Does not show column names")
        print(df)

        column_names = [desc[0] for desc in cursor.description]
        print(column_names)
        df.columns = column_names
        print("shows column names")
        print(df)
        df['sales_by_product'] = df.total_quantity * df.price
        df = df.sort_values('sales_by_product', ascending=False).iloc[:5]
        print(df)
        products = df['name'].tolist()
        sales_by_product = df['sales_by_product'].tolist()
        return render(request, 'store/revenue_by_products.html', {'products':products, 'sales_by_product':sales_by_product})

class Revenue_Categories(View):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        users = cursor.execute("select cat_name, sum(price*total_quantity) as total_by_category from (SELECT a.product_id, b.name, b.price as price, c.name as cat_name, sum(a.quantity) as total_quantity  FROM customer_orderitem a, customer_item b, customer_category c, customer_item_category d where a.product_id = b.id and b.id = d.item_id and c.id = d.category_id group by a.product_id, b.name, b.price, c.name) as s group by cat_name;")
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        print("Does not show column names")
        print(df)

        column_names = [desc[0] for desc in cursor.description]
        print(column_names)
        df.columns = column_names
        print("shows column names")
        print(df)
        
        df = df.sort_values('total_by_category', ascending=False).iloc[:5]
        print(df)
        categories = df['cat_name'].tolist()
        sales_by_category = df['total_by_category'].tolist()
        return render(request, 'store/revenue_by_categories.html', {'categories':categories, 'sales_by_category':sales_by_category})