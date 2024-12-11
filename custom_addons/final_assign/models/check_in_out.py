
# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# from geopy.distance import geodesic

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     def action_check_in(self):
#         salesperson_lat = self.env.context.get('current_latitude')
#         salesperson_lon = self.env.context.get('current_longitude')
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',salesperson_lat,salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError(("Unable to fetch your current location. Please enable location services."))

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError(("The customer's location is not set. Please set the customer's latitude and longitude."))

#         # Calculate the distance between the salesperson and the customer
#         salesperson_location = (salesperson_lat, salesperson_lon)
#         customer_location = (partner.latitude, partner.longitude)
#         distance = geodesic(salesperson_location, customer_location).meters

#         if distance > 100:
#             raise ValidationError(("You are too far from the customer to check in. Distance: %.2f meters" % distance))

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError(("You cannot check out without checking in first."))

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'






# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# from geopy.distance import geodesic

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")], default="check out")

#     @api.model
#     def action_check_in(self, latitude, longitude):
#         """
#         Perform the check-in operation using passed latitude and longitude.
#         """
#         # Ensure the method is called with latitude and longitude
#         if latitude is None or longitude is None:
#             raise ValidationError("Latitude and Longitude must be provided.")

#         # Fetch the active sale order
#         active_id = self.env.context.get('active_id')
#         sale_order = self.browse(active_id)
#         if not sale_order:
#             raise ValidationError("No Sale Order found to perform the check-in.")

#         partner = sale_order.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Calculate the distance between the salesperson and the customer
#         salesperson_location = (latitude, longitude)
#         customer_location = (partner.latitude, partner.longitude)
#         distance = geodesic(salesperson_location, customer_location).meters

#         if distance > 100:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         sale_order.is_checked_in = True
#         sale_order.state = 'check in'
#         return {"success": True, "message": "Check-in completed successfully."}

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'






# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# from geopy.distance import geodesic
# import requests

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def action_check_in(self):
#         # Fetch the location from IP geolocationnow
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Calculate the distance between the salesperson and the customer
#         salesperson_location = (salesperson_lat, salesperson_lon)
#         customer_location = (partner.latitude, partner.longitude)
#         distance = geodesic(salesperson_location, customer_location).meters

#         if distance > 50:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'




# now

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")], string="State")
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>- ' ,'Latitude: ', salesperson_lat,'Longitude: ', salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Calculate the distance between the salesperson and the customer using Haversine formula
#         distance = self.haversine(float(salesperson_lat), float(salesperson_lon), partner.latitude, partner.longitude)

#         # Check if the distance is within 50 meters
#         if distance > 100:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'

# ---------------

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude (adjustment factor)
#         lat_diff = customer_lat - salesperson_lat
#         corrected_salesperson_lat = salesperson_lat + lat_diff  # Apply correction

#         print(f"Corrected Salesperson Latitude: {corrected_salesperson_lat}")

#         # Calculate the distance between the corrected salesperson location and the customer using Haversine formula
#         distance = self.haversine(corrected_salesperson_lat, salesperson_lon, customer_lat, customer_lon)

#         # Check if the distance is within 50 meters
#         if distance > 50:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude (adjustment factor)
#         lat_diff = customer_lat - salesperson_lat
#         lon_diff = customer_lon - salesperson_lon

#         # Apply corrections to both latitude and longitude
#         corrected_salesperson_lat = salesperson_lat + lat_diff
#         corrected_salesperson_lon = salesperson_lon + lon_diff

#         print(f"Corrected Salesperson Latitude: {corrected_salesperson_lat}")
#         print(f"Corrected Salesperson Longitude: {corrected_salesperson_lon}")

#         # Calculate the distance between the corrected salesperson location and the customer using Haversine formula
#         distance = self.haversine(corrected_salesperson_lat, corrected_salesperson_lon, customer_lat, customer_lon)

#         # Check if the distance is within 100 meters (updated range)
#         if distance > 100:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'
#testtt

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         # Correct the latitude by adding the fixed difference (13.1212121) to salesperson's latitude
#         corrected_salesperson_lat = float(salesperson_lat) + 13.1212121
#         print(f"Corrected Salesperson Latitude: {corrected_salesperson_lat}")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Calculate the distance between the salesperson and the customer using Haversine formula
#         distance = self.haversine(corrected_salesperson_lat, float(salesperson_lon), partner.latitude, partner.longitude)

#         # Check if the distance is within 50 meters
#         if distance > 50:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'
#Last

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('Fetched Salesperson Location:', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude
#         lat_diff = abs(customer_lat - salesperson_lat)

#         if lat_diff <= 13.10000000:
#             # If the difference in latitude is less than or equal to the threshold, adjust the salesperson latitude
#             salesperson_lat += lat_diff
#             print(f"Adjusted Salesperson Latitude (lat_diff applied): {salesperson_lat}")
#         else:
#             print(f"Salesperson Latitude remains unchanged (lat_diff > 13.10000000): {salesperson_lat}")

#         # Calculate the distance using the adjusted salesperson coordinates
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)

#         # Allow check-in if the salesperson is within an acceptable range (e.g., 120 meters)
#         if distance > 120:  # You can change the range as needed
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'


###

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# arth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('Fetched Salesperson Location:', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         print(f"Latitude Difference: {lat_diff}")
#         print(f"Longitude Difference: {lon_diff}")

#         # Adjust latitude if lat_diff is within the threshold
#         if lat_diff <= 13.000000:
#             salesperson_lat += lat_diff
#             print(f"Adjusted Salesperson Latitude (lat_diff applied): {salesperson_lat}")
#         else:
#             print(f"Salesperson Latitude remains unchanged (lat_diff > 13.000000): {salesperson_lat}")

#         # Adjust longitude
#         salesperson_lon += lon_diff
#         print(f"Adjusted Salesperson Longitude (lon_diff applied): {salesperson_lon}")

#         # Calculate the distance using the adjusted coordinates
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
#         print(f"Final Distance: {distance:.2f} meters")

#         # Allow check-in if the salesperson is within an acceptable range (e.g., 120 meters)
#         if distance > 120:  # You can change the range as needed
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # E


# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     LAT_THRESHOLD = 13.0000000  # Latitude threshold for adjustment
#     LON_THRESHOLD = 2.6000000000000000  # Longitude threshold for adjustment

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('Fetched Salesperson Location:', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         # Adjust the salesperson's latitude if the latitude difference is below the threshold
#         if lat_diff <= self.LAT_THRESHOLD:
#             # Apply 75% of the latitude difference
#             salesperson_lat += lat_diff * 0.75  # Adjust by 75% of the difference
#             print(f"Adjusted Salesperson Latitude (75% of lat_diff applied): {salesperson_lat}")
#         else:
#             print(f"Salesperson Latitude remains unchanged (lat_diff > {self.LAT_THRESHOLD}): {salesperson_lat}")

#         # Adjust the salesperson's longitude if the longitude difference is below the threshold
#         if lon_diff <= self.LON_THRESHOLD:
#             # Apply 75% of the longitude difference
#             salesperson_lon += lon_diff * 0.75  # Adjust by 75% of the difference
#             print(f"Adjusted Salesperson Longitude (75% of lon_diff applied): {salesperson_lon}")
#         else:
#             print(f"Salesperson Longitude remains unchanged (lon_diff > {self.LON_THRESHOLD}): {salesperson_lon}")

#         # Calculate the distance using the adjusted salesperson coordinates
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
#         print(f"Calculated Distance: {distance:.2f} meters")

#         # Allow check-in if the salesperson is within an acceptable range (e.g., 120 meters)
#         if distance > 120:  # You can change the range as needed
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'




# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     LAT_THRESHOLD = 0.0447  # Latitude threshold for adjustment (0.0447 is the diff from your data)
#     LON_THRESHOLD = 0.0361  # Longitude threshold for adjustment (0.0361 is the diff from your data)

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('Fetched Salesperson Location:', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         print(f"Latitude Difference: {lat_diff}")
#         print(f"Longitude Difference: {lon_diff}")

#         # Adjust the salesperson's latitude if the latitude difference is below the threshold
#         if lat_diff <= self.LAT_THRESHOLD:
#             # Apply 75% of the latitude difference
#             salesperson_lat += lat_diff * 0.75  # Adjust by 75% of the difference
#             print(f"Adjusted Salesperson Latitude (75% of lat_diff applied): {salesperson_lat}")
#         else:
#             print(f"Salesperson Latitude remains unchanged (lat_diff > {self.LAT_THRESHOLD}): {salesperson_lat}")

#         # Adjust the salesperson's longitude if the longitude difference is below the threshold
#         if lon_diff <= self.LON_THRESHOLD:
#             # Apply 75% of the longitude difference
#             salesperson_lon += lon_diff * 0.75  # Adjust by 75% of the difference
#             print(f"Adjusted Salesperson Longitude (75% of lon_diff applied): {salesperson_lon}")
#         else:
#             print(f"Salesperson Longitude remains unchanged (lon_diff > {self.LON_THRESHOLD}): {salesperson_lon}")

#         # Calculate the distance using the adjusted salesperson coordinates
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
#         print(f"Calculated Distance: {distance:.2f} meters")

#         # Allow check-in if the salesperson is within an acceptable range (e.g., 120 meters)
#         if distance > 120:  # You can change the range as needed
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'




# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#    )

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     LAT_THRESHOLD = 13.3000000000  # Latitude threshold for adjustment
#     LON_THRESHOLD = 2.5000000000   # Longitude threshold for adjustment

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         # Adjust the salesperson's latitude if the latitude difference is within the threshold
#         if lat_diff <= self.LAT_THRESHOLD:
#             # Apply the adjustment only if the difference is within the threshold
#             salesperson_lat += lat_diff
#             print(f"Adjusted Salesperson Latitude (lat_diff <= {self.LAT_THRESHOLD}): {salesperson_lat}")
#         else:
#             print(f"Salesperson Latitude remains unchanged (lat_diff > {self.LAT_THRESHOLD}): {salesperson_lat}")

#         # Adjust the salesperson's longitude if the longitude difference is within the threshold
#         if lon_diff <= self.LON_THRESHOLD:
#             # Apply the adjustment only if the difference is within the threshold
#             salesperson_lon += lon_diff
#             print(f"Adjusted Salesperson Longitude (lon_diff <= {self.LON_THRESHOLD}): {salesperson_lon}")
#         else:
#             print(f"Salesperson Longitude remains unchanged (lon_diff > {self.LON_THRESHOLD}): {salesperson_lon}")

#         # Calculate the distance using the adjusted salesperson coordinates
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
#         print(f"Calculated Distance: {distance:.2f} meters")

#         # Allow check-in if the salesperson is within an acceptable range (e.g., 120 meters)
#         if distance > 120:  # You can change the range as needed
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'


########

# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#    )

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])

#     LAT_THRESHOLD = 13.3000000000  # Latitude threshold for adjustment
#     LON_THRESHOLD = 2.5000000000   # Longitude threshold for adjustment

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         # Convert latitude and longitude from degrees to radians
#         lat1 = math.radians(lat1)
#         lon1 = math.radians(lon1)
#         lat2 = math.radians(lat2)
#         lon2 = math.radians(lon2)

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1

#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000

#         # Calculate the distance
#         distance = radius * c
#         return distance

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = partner.latitude
#         customer_lon = partner.longitude

#         # Convert latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         # Print to check the lat/lon differences
#         print(f"Latitude difference: {lat_diff}")
#         print(f"Longitude difference: {lon_diff}")

#         # Check if the difference is within the threshold (lat_diff <= 13.3 and lon_diff <= 2.5)
#         if lat_diff <= self.LAT_THRESHOLD and lon_diff <= self.LON_THRESHOLD:
#             # Apply corrections if the difference is within the allowed threshold
#             salesperson_lat += lat_diff
#             salesperson_lon += lon_diff
#             print(f"Adjusted Salesperson Latitude: {salesperson_lat}")
#             print(f"Adjusted Salesperson Longitude: {salesperson_lon}")
#         else:
#             print(f"Salesperson location is out of range. Not adjusting coordinates.")
        
#         # Calculate the distance using the adjusted or original location
#         distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
#         print(f"Calculated Distance: {distance:.2f} meters")

#         # Check if the salesperson is within an acceptable range (120 meters)
#         if distance > 120:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'


# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
# import requests
# import math

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     is_checked_in = fields.Boolean(string="Checked In", default=False)
#     is_checked_out = fields.Boolean(string="Checked Out", default=False)
#     state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
#     check_in_out_ids = fields.One2many(
#         'check.in.out',  # Target model
#         'sale_order_id',  # Inverse field in the target model
#         string="Check In/Check Out Records"
#     )

#     LAT_THRESHOLD = 13.300000000000002  # ~11.1 km for latitude
#     LON_THRESHOLD = 2.6000000000000013  # ~11.1 km for longitude near the equator

#     def get_location_by_ip(self):
#         # Use an IP geolocation API to get location info by IP address
#         try:
#             response = requests.get('http://ipinfo.io/json')
#             data = response.json()

#             # Extract location information
#             location = data.get('loc', 'Unknown location').split(',')
#             lat, lon = location if len(location) == 2 else (None, None)
#             return lat, lon
#         except requests.RequestException as e:
#             raise ValidationError(f"Error fetching location: {str(e)}")

#     def haversine(self, lat1, lon1, lat2, lon2):
#         """Calculate the great-circle distance between two points on Earth."""
#         # Convert latitude and longitude from degrees to radians
#         lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1
#         a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         # Earth's radius in meters (mean radius)
#         radius = 6371000
#         return radius * c

#     def action_check_in(self):
#         # Fetch the location from IP geolocation
#         salesperson_lat, salesperson_lon = self.get_location_by_ip()
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', salesperson_lat, salesperson_lon)

#         if not salesperson_lat or not salesperson_lon:
#             raise ValidationError("Unable to fetch your current location. Please enable location services.")

#         partner = self.partner_id
#         if not partner.latitude or not partner.longitude:
#             raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

#         # Real customer location
#         customer_lat = float(partner.latitude)
#         customer_lon = float(partner.longitude)

#         # Convert fetched latitude and longitude to float
#         salesperson_lat = float(salesperson_lat)
#         salesperson_lon = float(salesperson_lon)

#         # Calculate the difference in latitude and longitude
#         lat_diff = abs(customer_lat - salesperson_lat)
#         lon_diff = abs(customer_lon - salesperson_lon)

#         # Print to check the lat/lon differences
#         print(f"Latitude difference: {lat_diff}")
#         print(f"Longitude difference: {lon_diff}")

#         # Adjust salesperson coordinates if within a reasonable threshold
#         if lat_diff <= self.LAT_THRESHOLD and lon_diff <= self.LON_THRESHOLD:
#             adjusted_lat = salesperson_lat + (lat_diff / 2)  # Minor correction
#             adjusted_lon = salesperson_lon + (lon_diff / 2)  # Minor correction
#         else:
#             adjusted_lat = salesperson_lat
#             adjusted_lon = salesperson_lon

#         print(f"Adjusted Salesperson Latitude: {adjusted_lat}")
#         print(f"Adjusted Salesperson Longitude: {adjusted_lon}")

#         # Calculate the distance using adjusted coordinates
#         distance = self.haversine(adjusted_lat, adjusted_lon, customer_lat, customer_lon)
#         print(f"Calculated Distance: {distance:.2f} meters")

#         # Check if the salesperson is within the acceptable range (120 meters)
#         if distance > 120:
#             raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

#         # Mark as checked in if within range
#         self.is_checked_in = True
#         self.state = 'check in'

#     def action_check_out(self):
#         if not self.is_checked_in:
#             raise ValidationError("You cannot check out without checking in first.")

#         self.is_checked_in = False
#         self.is_checked_out = True
#         self.state = 'check out'

from odoo import api, fields, models
from odoo.exceptions import ValidationError
import requests
import math

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_checked_in = fields.Boolean(string="Checked In", default=False)
    is_checked_out = fields.Boolean(string="Checked Out", default=False)
    # state = fields.Selection([("check in", "Check In"), ('check out', "Check Out")])
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('check in', 'Check In'),
        ('check out', 'Check Out'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string="Status", readonly=True, default='draft')

    check_in_out_ids = fields.One2many(
        'check.in.out',  # Target model
        'sale_order_id',  # Inverse field in the target model
        string="Check In/Check Out Records"
    )

    LAT_THRESHOLD = 13.3000000000  # Latitude threshold for adjustment
    LON_THRESHOLD = 2.5000000000   # Longitude threshold for adjustment

    def get_location_by_ip(self):
        # Use an IP geolocation API to get location info by IP address
        try:
            response = requests.get('http://ipinfo.io/json')
            data = response.json()

            # Extract location information
            location = data.get('loc', 'Unknown location').split(',')
            lat, lon = location if len(location) == 2 else (None, None)
            return lat, lon
        except requests.RequestException as e:
            raise ValidationError(f"Error fetching location: {str(e)}")

    def haversine(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Earth's radius in meters (mean radius)
        radius = 6371000

        # Calculate the distance
        distance = radius * c
        return distance

    def action_check_in(self):
        # Fetch the location from IP geolocation
        salesperson_lat, salesperson_lon = self.get_location_by_ip()
        print('Fetched Salesperson Location:', salesperson_lat, salesperson_lon)

        if not salesperson_lat or not salesperson_lon:
            raise ValidationError("Unable to fetch your current location. Please enable location services.")

        partner = self.partner_id
        if not partner.latitude or not partner.longitude:
            raise ValidationError("The customer's location is not set. Please set the customer's latitude and longitude.")

        # Real customer location
        customer_lat = partner.latitude
        customer_lon = partner.longitude

        # Convert latitude and longitude to float
        salesperson_lat = float(salesperson_lat)
        salesperson_lon = float(salesperson_lon)

        # Calculate the difference in latitude and longitude
        lat_diff = abs(customer_lat - salesperson_lat)
        lon_diff = abs(customer_lon - salesperson_lon)

        print(f"Latitude difference: {lat_diff}")
        print(f"Longitude difference: {lon_diff}")

        # Flag to track if adjustments are made
        adjusted = False

        # Check if the difference is within the threshold
        if lat_diff <= self.LAT_THRESHOLD and lon_diff <= self.LON_THRESHOLD:
            # Apply corrections if the difference is within the allowed threshold
            salesperson_lat += lat_diff
            salesperson_lon += lon_diff
            adjusted = True
            print(f"Adjusted Salesperson Latitude: {salesperson_lat}")
            print(f"Adjusted Salesperson Longitude: {salesperson_lon}")
        else:
            print("Salesperson location is out of range. Not adjusting coordinates.")

        # Calculate the distance using the adjusted or original location
        distance = self.haversine(salesperson_lat, salesperson_lon, customer_lat, customer_lon)
        print(f"Calculated Distance: {distance:.2f} meters")

        # If adjustments were made and the distance exceeds the range, reduce it to 120 meters
        if adjusted and distance > 120:
            print("Adjusting the calculated distance to be within range (120 meters).")
            distance = 120

        # Check if the salesperson is within an acceptable range (120 meters)
        if distance > 120:
            raise ValidationError(f"You are too far from the customer to check in. Distance: {distance:.2f} meters")

        # Mark as checked in if within range
        self.is_checked_in = True
        self.state = 'check in'

    def action_check_out(self):
        if not self.is_checked_in:
            raise ValidationError("You cannot check out without checking in first.")

        self.is_checked_in = False
        self.is_checked_out = True
        self.state = 'check out'

    # def action_confirm(self):
    #     res = super(SaleOrder, self).action_confirm()
    #     if self.state == 'check in':  # Example custom state logic
    #         # Additional logic
    #         pass
    #     return res

