 #multiple inheritance
 class Subject:
	def __init__(self, subj_name):
		print (subj_name, "also handles different classes ")

		
 class Math(Subject):
	def __init__(self, math_teacher):
		print (math_teacher, "is my Math Teacher")
		super().__init__(math_teacher)

	
class Science(Subject):
	def __init__(self, science_teacher):
		print (science_teacher, "is my Science Teacher")
		super().__init__(science_teacher)

		
class English(Subject):
	def __init__(self, english_teacher):
		print(english_teacher, "is my English Teacher")
		super().__init__(english_teacher)

		
class Art(Subject):
	def __init__(self, art_teacher):
		print(art_teacher, "is my Art Teacher")
		super().__init__(art_teacher)

 
class Brown(Science, Art):
	def __init__(self):
		print("John Brown")
		super().__init__('Mr. Brown')

		
b = Brown()
k = Math('Ms. Sy')
a = English('Ms. Hanson')
