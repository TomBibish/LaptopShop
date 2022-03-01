from django.db import connection


def get_top_laptops():
    with connection.cursor() as cursor:
        cursor.execute("""select l.id, l."name", avg(r.laptop_grade) as avrage_grade
                          from laptop_app_laptop l join laptop_app_reviews r on r.laptop_id = l.id
                          group by l."name",l.id
                          order by avrage_grade desc;""",)
        rows = cursor.fetchall()
        res_list = [{"laptop_id": row[0], "laptop_name": row[1], "avrage_grade": row[2]} for row in rows]
        return res_list


def get_stats_for_company():
    with connection.cursor() as cursor:
        cursor.execute("""select c."name", c.id, avg(r.laptop_grade) as avrage_grade, count(r) as reviews_count
                            from laptop_app_company c 
                            join laptop_app_laptop l on c.id = l.company_id
                            join laptop_app_reviews r on r.laptop_id = l.id 
                            group by c."name" , c.id
                            order by avrage_grade desc;""",)
        rows = cursor.fetchall()
        res_list = [{"company_name": row[0], "company_id": row[1], "avrage_grade": row[2], "reviews_count":row[3]}
                    for row in rows]
        return res_list


def best_customer_by_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""select c."name", count(r) as reviews_count  from laptop_app_customer c
                            join laptop_app_reviews r on r.customer_id = c.id
                            group by c."name" 
                            order by reviews_count desc limit 5;""",)
        rows = cursor.fetchall()
        res_list = [{"customer_name": row[0], "reviews_count":row[1]}
                    for row in rows]
        return res_list

def customers_reviewed_all():
    with connection.cursor() as cursor:
        cursor.execute("""with uniqe_items (customer_name, uniqe_items) as 
                            (select c."name", count(distinct oi) from laptop_app_customer c
                                join laptop_app_order o on o.customer_id = c.id 
                                join laptop_app_orderitem oi on oi.order_id = o.id 
                                group by c."name"),
                            uniqe_reviews (customer_name, uniqe_reviews) as 
                            (select c."name", count(distinct r.laptop_id) from laptop_app_customer c
                                join laptop_app_reviews r on r.customer_id = c.id 
                                group by c."name")
                            select uniqe_reviews.customer_name from uniqe_items 
                            join uniqe_reviews on uniqe_reviews.customer_name = uniqe_items.customer_name
                            where uniqe_reviews.uniqe_reviews = uniqe_items.uniqe_items;""",)
        rows = cursor.fetchall()
        res_list = [{"customer_name": row[0]}
                    for row in rows]
        return res_list


def cheapest_laptops_without_reviews():
    with connection.cursor() as cursor:
        cursor.execute("""select  l.id , l.name from laptop_app_laptop l
                                left join laptop_app_reviews r on r.laptop_id = l.id
                                where r.laptop_id is null 
                                and l.id is not null 
                                order by l.price_euros desc;""",)
        rows = cursor.fetchall()
        res_list = [{"laptop_name": row[1], "laptop_id":row[0]}
                    for row in rows]
        return res_list


def cheapest_laptops_highegst_avg():
    with connection.cursor() as cursor:
        cursor.execute("""select l.id, l.name, l.price_euros, avg(r.laptop_grade) as avrage_grade from laptop_app_laptop l
                                join laptop_app_reviews r on l.id = r.laptop_id
                                group by l.id
                                order by l.price_euros, avrage_grade desc;""",)
        rows = cursor.fetchall()
        res_list = [{"laptop_id": row[0], "laptop_name":row[1],"price":row[2], "avrage_grade":row[3] }
                    for row in rows]
        return res_list