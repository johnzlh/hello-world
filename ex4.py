cars = 100  #总共的车辆数
space_in_a_car = 4  #每辆车能载客的人数
drivers = 30   #司机数
passengers = 90  #乘客数
cars_not_driven =cars - drivers  #不运行的车辆数=车辆总数-司机数
cars_driven = drivers   #运行的车辆数=司机数
carpool_capacity = cars_driven * space_in_a_car  #所有运行车辆的载客能力
average_passengers_per_car = passengers / cars_driven  #平均每辆车的载客数


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
