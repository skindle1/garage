def main():
	class vehicle:
		def setVehicle_Make (self, make):
			self.vehicle_make = make 
		def setVehicle_Model (self, model):
			self.vehicle_model = model 
		def displayOption (self):
			print (f"The vehicle make is: {self.vehicle_make}")
			print (f"The vehicle model is: {self.vehicle_model}")
	class car(vehicle):
		def setcar_door (self, door):
			self.car_door = door 
		def displayOption(self):
			print (f"The vehicle make is: {self.vehicle_make}")
			print (f"The vehicle model is: {self.vehicle_model}")
			print (f"This vehicle has {self.car_door} doors.")
	class truck(vehicle):
		def setbed_length (self, length):
			self.bed_length = length 
		def displayOption(self):
			print (f"The vehicle make is: {self.vehicle_make}")
			print (f"The vehicle model is: {self.vehicle_model}")
			print (f"The truck's bed length is : {self.bed_length}")
	print ("Welcome to my garage.")
	number = input ("Press 1 for car or 2 for truck:")
	number = int(number)
	if number == 1:
		input_make = input("Enter the car's make: ")
		input_model = input("Enter the car's model: ")
		input_door = input("How many doors does the car have?: ")
		new_car = car()
		new_car.setVehicle_Make(input_make)
		new_car.setVehicle_Model(input_model)
		new_car.setcar_door(input_door)
		new_car.displayOption()
	if number == 2:
		input_make = input("Enter the truck's make: ")
		input_model = input("Enter the truck's model: ")
		input_bed = input("How long is the truck's bed?: ")
		new_truck = truck()
		new_truck.setVehicle_Make(input_make)
		new_truck.setVehicle_Model(input_model)
		new_truck.setbed_length(input_bed)
		new_truck.displayOption()
	print ("This vehicle has been added to the garage.")
	restart = input("Would you like to enter another vehicle? Press 1 for yes, 2 for no: ")
	restart = int(restart)
	if restart == 1:
		main()
	else:
		print("Thank you for adding your vehicle.")
		exit
main()
