
--1

select l.id, l."name", avg(r.laptop_grade) as avrage_grade
from laptop_app_laptop l join laptop_app_reviews r on r.laptop_id = l.id
group by l."name",l.id
order by avrage_grade desc;

--2

select c."name", c.id, avg(r.laptop_grade) as avrage_grade, count(r) as reviews_count
from laptop_app_company c
join laptop_app_laptop l on c.id = l.company_id
join laptop_app_reviews r on r.laptop_id = l.id
group by c."name" , c.id
order by avrage_grade desc;

--3

select c."name", count(r) as reviews_count  from laptop_app_customer c
join laptop_app_reviews r on r.customer_id = c.id
group by c."name"
order by reviews_count desc limit 2;

--4

with uniqe_items (customer_name, uniqe_items) as
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
	where uniqe_reviews.uniqe_reviews = uniqe_items.uniqe_items;

--=5
select  l.id , l.name from laptop_app_laptop l
left join laptop_app_reviews r on r.laptop_id = l.id
where r.laptop_id is null
and l.id is not null
order by l.price_euros desc;

---6
select l.id, l.name, l.price_euros, avg(r.laptop_grade) as avrage_grade from laptop_app_laptop l
join laptop_app_reviews r on l.id = r.laptop_id
group by l.id
order by l.price_euros, avrage_grade desc;
