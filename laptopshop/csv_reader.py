import csv
import os
import random
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laptopshop.settings")
import django
django.setup()

from laptop_app.models import *

with open('laptops.csv', 'rt', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        ssd = None
        hybrid = None
        hdd = None
        flash = None
        name = row[2]
        type = row[3]
        inches = row[4]
        resu = row[5]
        resu = re.search("\d+x\d+", resu).group()
        cpu = row[6]
        ram = row[7]
        ram = re.search('\d+',ram).group()
        memory = row[8]
        if '+' in memory:
            first_memory = memory.split('+')[0]
            if 'TB' in first_memory:
                memory_type = re.findall('[a-z,A-Z]+', first_memory)[1]
                memory_in_gb = int(re.search('\d+',first_memory).group()) * 1024
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid =  memory_in_gb
            else:
                memory_in_gb = int(re.search('\d+',first_memory).group())
                memory_type = re.findall('[a-z,A-Z]+', first_memory)[1]
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid = memory_in_gb

            second_memory = memory.split('+')[1].strip()

            if 'TB' in second_memory:
                memory_type = re.findall('[a-z,A-Z]+', second_memory)[1]
                memory_in_gb = int(re.search('\d+', second_memory).group()) * 1024
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid = memory_in_gb
            else:
                memory_in_gb = int(re.search('\d+', second_memory).group())
                memory_type = re.findall('[a-z,A-Z]+', second_memory)[1]
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid = memory_in_gb
        else:
            pass
            if 'TB' in memory:
                memory_in_gb = int(re.search('\d+', memory).group()) * 1024
                memory_type = re.findall('[a-z,A-Z]+', memory)[1]
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid = memory_in_gb
            else:
                memory_in_gb = int(re.search('\d+', memory).group())
                memory_type = re.findall('[a-z,A-Z]+', memory)[1]
                if memory_type == 'SSD':
                    ssd = memory_in_gb
                elif memory_type == 'HDD':
                    hdd = memory_in_gb
                elif memory_type == 'Flash':
                    flash = memory_in_gb
                elif memory_type == 'Hybrid':
                    hybrid = memory_in_gb
        gpu = row[9]
        opsys = row[10]
        weight = float(row[11][:-2])
        price = row[12]
        stock_amount = random.randint(1, 100)
        companies = Company.objects.all()
        companies_list = [company for company in companies]
        for company in companies_list:
            if company.name == row[1]:
                company_id = company
        new_laptop = Laptop(name=name,
                            type=type,
                            company=company_id,
                            inches=inches,
                            resolution=resu,
                            cpu=cpu,
                            ram=ram,
                            ssd=ssd,
                            hdd=hdd,
                            hybrid=hybrid,
                            flash_storage=flash,
                            gpu=gpu,
                            op_sys=opsys,
                            weight=weight,
                            price_euros=price,
                            stock_amount=stock_amount)
        new_laptop.save()