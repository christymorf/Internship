 #multiple inheritance
 class Subject:
	def __init__(self, subName):
		print (subName, "also handles different classes ")

		
 class Math(Subject):
	def __init__(self, mTeacher):
		print (mTeacher, "is my Math Teacher")
		super().__init__(mTeacher)

	
class Science(Subject):
	def __init__(self, sTeacher):
		print (sTeacher, "is my Science Teacher")
		super().__init__(sTeacher)

		
class English(Subject):
	def __init__(self, eTeacher):
		print(eTeacher, "is my English Teacher")
		super().__init__(eTeacher)

		
class Art(Subject):
	def __init__(self, aTeacher):
		print(aTeacher, "is my Art Teacher")
		super().__init__(aTeacher)

 
class Brown(Science, Art):
	def __init__(self):
		print("John Brown")
		super().__init__('Mr. Brown')

		
b = Brown()
k = Math('Ms. Sy')
a = English('Ms. Hanson')
