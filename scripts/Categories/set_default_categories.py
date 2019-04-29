import django

django.setup()

from apps.PostingOrganizer.models import Category

category_appliances = Category()
category_appliances.category_url_name = 'appliances'
category_appliances.display_name = 'Appliances'
category_appliances.craigslist_url_adder = 'appliances/search/ppa'
category_appliances.save()

category_athletic_equipment = Category()
category_athletic_equipment.category_url_name = 'athletic_equipment'
category_athletic_equipment.display_name = 'Athletic Equipment'
category_athletic_equipment.craigslist_url_adder = 'sporting-goods/search/sga'
category_athletic_equipment.save()

category_bikes = Category()
category_bikes.category_url_name = 'bikes'
category_bikes.display_name = 'Bikes'
category_bikes.craigslist_url_adder = 'bicycles/search/bia'
category_bikes.save()

category_clothing = Category()
category_clothing.category_url_name = 'clothing-accessories'
category_clothing.display_name = 'Clothing and Accessories'
category_clothing.craigslist_url_adder = 'clothing-accessories/search/cla'
category_clothing.save()

category_computers = Category()
category_computers.category_url_name = 'computers'
category_computers.display_name = 'Computers'
category_computers.craigslist_url_adder = 'computers/search/sya'
category_computers.save()

category_electronics = Category()
category_electronics.category_url_name = 'electronics'
category_electronics.display_name = 'Electronics'
category_electronics.craigslist_url_adder = 'electronics/search/ela'

category_musical_instruments = Category()
category_musical_instruments.category_url_name = 'musical_instruments'
category_musical_instruments.display_name = 'Musical Instruments'
category_musical_instruments.craigslist_url_adder = 'musical-instruments/search/msa'
category_musical_instruments.save()

category_tools = Category()
category_tools.category_url_name = 'tools'
category_tools.display_name = 'Tools'
category_tools.craigslist_url_adder = 'tools/search/tla'
category_tools.save()

category_vehicles = Category()
category_vehicles.category_url_name = 'vehicles'
category_vehicles.display_name = 'Vehicles'
category_vehicles.craigslist_url_adder = 'cars-trucks/search/cta'
category_vehicles.save()

category_video_gaming = Category()
category_video_gaming.category_url_name = 'video_gaming'
category_video_gaming.display_name = 'Video Gaming'
category_video_gaming.craigslist_url_adder = 'video-gaming/search/vga'
category_video_gaming.save()


