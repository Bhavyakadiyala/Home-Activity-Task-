from collections import defaultdict
import heapq
input_file=open("Input.txt","r")
slot_regid={} #stores the registration number of vehicle corresponding to the slot number
reg_no={} #stores registration_number and slot_number as key-value pairs
slot_age={}#Stores slot as key and age as value
ageList=defaultdict(list)#Stores slotnumbers for drivers of a particular age
slot_cnt=0
available_slots=[]
def CreateParkingLot(size):
  try:
    n=int(size)
    print("Created parking of",n,"slots")
  except:
    print("Invalid input,Size of parking lot must be a number")

def ParkCars(car_num,driver_age):
  global slot_cnt,size
  if available_slots:
    x=heapq.heappop(available_slots)
    reg_no[car_num]=x
    ageList[driver_age]+=[x]
    slot_regid[x]=car_num
    slot_age[x]=driver_age
    print("Car with vehicle registration number",car_num,"has been parked at slot number",x)
  else:
    #print(int(slot_cnt),int(size))
    if slot_cnt==size:
      print("Parking lot is full")
    else:
      slot_cnt+=1
      x=slot_cnt
      reg_no[car_num]=x
      ageList[driver_age]+=[x]
      slot_regid[x]=car_num
      slot_age[x]=driver_age
      print("Car with vehicle registration number",car_num,"has been parked at slot number",x)

def get_list_of_age(X):
  if ageList[X]:
    return ageList[X]
  else:
    print("There are no drivers with age =",X)
def vacate(slt_no):
  try:
    vehicle_number=slot_regid[slt_no]
    del slot_regid[slt_no]
    del reg_no[vehicle_number]
    driver_age=slot_age[slt_no]
    del slot_age[slt_no]
    ageList[driver_age].remove(slt_no)
    #print("Slot number",slt_no,"is vacated")
    print("Slot number",slt_no,"vacated, the car with vehicle registration number",vehicle_number,"left the space, the driver of the car was of age",driver_age)
    heapq.heappush(available_slots,slt_no)
  except:
    global size
    if slt_no>size:
      print(slt_no,"is beyond the size of parking lot")
    else:
      print("Slot already vacant")
def get_slot_number(car_num):
  try:
    print(reg_no[car_num])
  except:
    print("Car with given Registration number doesn't exist")

def get_registration_numbers(X):
  try:
    res=[]
    for i in ageList[X]:
      res.append(slot_regid[i])
  except:
    print("Driver with given age doesn't exist")
for line in input_file:
  inp_list=list(line.split())
  if inp_list[0]=="Create_parking_lot":
    size=int(inp_list[-1])
    CreateParkingLot(size)  #Creating a ParkingLot

  elif inp_list[0]=="Park":
    car_num=inp_list[1]
    driver_age=int(inp_list[-1])
    ParkCars(car_num,driver_age)

  elif inp_list[0]=="Slot_numbers_for_driver_of_age":
    driver_age=int(inp_list[-1])
    result=get_list_of_age(driver_age)
    if result:
      #print("Slot numbers having drivers of age",driver_age,"are",end=" ")
      print(*result,sep=",")
  
  elif inp_list[0]=="Slot_number_for_car_with_number":
    car_num=inp_list[-1]
    get_slot_number(car_num)

  elif inp_list[0]=="Leave":
    slt_no=int(inp_list[-1])
    #print(slot_age,available_slots)
    vacate(slt_no)
  
  elif inp_list[0]=="Vehicle_registration_number_for_driver_of_age":
    age=int(inp_list[-1])
    get_registration_numbers(age)
  else:
    print("Invalid Command")
  #print(ageList)