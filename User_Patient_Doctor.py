class User:
	def __init__(self, name, surname, email, phone, city, username, password,birth, gender,age):
		self.name = name
		self.surname = surname
		self.email = email
		self.phone = phone
		self.city = city
		self.username = username
		self.password = password
		self.birth=birth
		self.gender=gender
		self.age=age

	def addRegistration():


	


class Doctor(User):
	def __init__(self, name, surname, email, phone, city, username, password,birth, gender,age, specialization, rank,cv,listOfDiplomas):
		User.__init__(self, name, surname, email, phone, city, username, password,birth, gender,age)
		self.specialization = specialization
		self.listOfPatients = {}
		self.rank = rank
		self.numOfPatients=0
		self.cv=cv
		self.listOfDiplomas=listOfDiplomas

	def completeForm():
	def doctorRegistration():
	def sendNotification():
	def selectPoint():
	def completeNotification():
	def searchPatient(name):
	def loadPatient(Patient):


class Patient(User):
	def __init__(self, name, surname, email, phone, city, weight, height, username, password,birth, gender,age):
		User.__init__(self, name, surname, email, phone, city, username, password,birth, gender,age)
		self.weight=weight
		self.height=height
		self.listOfDoctors= {}
		
	def patientRegistration():
	def completeForm1():
	def completeForm2():
	def insertData():
	def dataOptions():
	def checkChoice():
	def insertDiet(Diet):
	def createDiet():
	def insertExercise(Exercise):
	def createExercise():
	def insertMedicalReport(MedicalReport):
	def createMedicalReport():
	def insertMedicine(Medicine):
	def createMedicine():

