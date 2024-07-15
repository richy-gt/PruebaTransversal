import csv
def menu():
	loop = True
	loop2 = True
	user1 = None
	user2 = None
	user3 = None
	contra1 = None
	contra2 = None
	contra3 = None
	diccionario = {}
	def menusecreto():
		menuSR = None
		while loop2 is True:
			try:
				print("")
				print("--------Menu Usuario--------")
				print("1. Multiplicar")
				print("2. Dividir")
				print("3. Crear Diccionario")
				print("4. Eliminar en el Diccionario")
				print("5. Buscar en el diccionario")
				print("6. Modificar el diccionario")
				print("7. Mostrar Diccionario Completo")
				print("8. Volver al menu principal")
				print("----------------------------")
				menuSR = int(input("Ingrese su respuesta: "))
				if menuSR == 1:
					def mult():
						try:
							nummult = int(input("Ingrese el primer numero a multiplicar: "))
							nummult2 = int(input("Ingrese el segundo numero a multiplicar: "))
							print("//////////////////////////////////////////////////////////")
							resultadomult = nummult * nummult2 
							print(resultadomult)
							print("//////////////////////////////////////////////////////////")
							print("")
						except ValueError:
							print("Ingrese valores numericos")
					mult()	
				elif menuSR == 2:
					def divi():
						try:
							errordivi = None
							dividir1 = int(input("Ingresar numero a dividir: "))
							dividir2 = int(input("Ingresar segundo numero a dividir: "))
							print("//////////////////////////////////////////////////////////")
							totaldivision = dividir1 // dividir2
							print(totaldivision)
							print("//////////////////////////////////////////////////////////")
							print("")
						except:
							errordivi = ValueError
							errordivi
							print("Ingrese valores numericos")
					divi()
				elif menuSR == 3:
					def agregar(diccionario):
						clave = input("Nombre de la clave para el diccionario: ")
						valor = input("Valor o nombre de lo que vas a agregar al diccionario: ")
						diccionario[clave] = valor
						print("//////////////////////////////////////////////////////////")
						print(diccionario)
						print("//////////////////////////////////////////////////////////")
						with open('Registro_diccionario.csv', 'w', newline='') as archivo_csv:
							escritor_csv = csv.writer(archivo_csv)
							escritor_csv.writerow(['|Clave', "|" , 'Valor|'])
							for clave, valor in diccionario.items():
								escritor_csv.writerow([clave, valor])	
							print("Datos guardados en Registro_diccionario.csv")
					agregar(diccionario)
				elif menuSR == 4:
					borrar = input("Ingrese el elemento a borrar: ")
					if borrar in diccionario:
						del diccionario[borrar]
						print(diccionario)
					else:
						print("No se encontro la clave buscada")
				elif menuSR == 5:
					search = input("Ingrese el nombre de la clave del diccionario: ").lower()
					diclave = {k.lower(): v for k, v in diccionario.items()}
					if search in diclave:
						clavedic = next(k for k in diccionario if k.lower() == search)
						print("Clave:", {clavedic}, "Valor:" ,{diccionario[clavedic]})
						print("//////////////////////////////////////////////////////////")
					else:
						print("No se encontro la clave ingresada")
						print("//////////////////////////////////////////////////////////")
				elif menuSR == 6:
					buscar = input("Ingrese el nombre de la clave a buscar: ")
					if buscar in diccionario:
						nuevonom = input("Ingrese el nuevo nombre de la clave: ")
						nuevoval = input("Ingrese el nuevo valor de la clave anterior: ")
						valor = diccionario.pop(buscar)
						diccionario[nuevonom] = nuevoval
						print(diccionario)
					else:
						print("No se encontro la clave ingresada")
				elif menuSR == 7:
					print(diccionario)
				elif menuSR == 8:
					print("Volviendo al menu principal..")
					break
			except ValueError:
				print("Ingrese un valor valido")
				continue
	while loop is True:
		try:
			print("--------Menu--------")
			print("1. Sumar")
			print("2. Restar")
			print("3. Registrar usuario")
			print("4. Iniciar sesion")
			print("5. Salir")
			print("----------------------")
			print("")
			menuR = int(input("Ingrese la opcion deseada: "))
			if menuR == 1:
				def suma():
					numsuma1 = int(input("Ingrese el primer numero a sumar: "))
					numsuma2 = int(input("Ingrese el segundo numero a sumar: "))
					print("//////////////////////////////////////////////////////////")
					totalsuma = numsuma1 + numsuma2
					print(totalsuma)
					print("//////////////////////////////////////////////////////////")
					print("")
				suma()
			elif menuR == 2:
				def resta():
					numresta1 = int(input("Ingrese el primer numero a restar: "))
					numresta2 = int(input("Ingrese el segundo numero a restar: "))
					print("//////////////////////////////////////////////////////////")
					totalresta = numresta1 - numresta2
					print(totalresta)
					print("//////////////////////////////////////////////////////////")
					print("")
				resta()
			elif menuR == 3:
				if user1 is None:
					user1 = input("Ingrese su nombre de usuario: ")
					contra1 = input("Ingrese su contraseña: ")
					print("Usuario 1 Creado!")
					print("")
				elif user2 is None:
					user2 = input("Ingrese su nonbre de usuario: ")
					contra2 = input("Ingrese su contraseña: ")
					print("Usuario 2 Creado!")
					print("")
				elif user3 is None:
					user3 = input("Ingrese su nombre de usuario: ")
					contra3 = input("Ingrese su contraseña: ")
					print("Usuario 3 creado!")
					print("")
				else:
					print("No hay usuarios disponibles")
					print("")
			elif menuR == 4:
					usuario = input("Ingrese su nombre de usuario: ")
					contraseña = input("Ingrese su contraseña: ")
					if usuario == user1 and contraseña == contra1:
						print("Bienvenido usuario ", user1,)
						menusecreto()
					elif usuario == user2 and contraseña == contra2:
						print("Bienvenido usuario ", user2,)
						menusecreto()
					elif usuario == user3 and contraseña == contra3:
						print("Bienvenido usuario ", user3,)
						menusecreto()
					else:
						print("Usuario o contraseña erroneos")
			elif menuR == 5:
				print("Saliendo del programa...")
				break
		except ValueError:
			print("Ingrese un valor valido")
			continue
print("//////////////////////////////////////////////////////////")
print("Bienvenido!")
print("EL siguiente menu le permite sumar y restar")
print("Si desea mas caracteristicas (como multiplicacion, division y el uso de diccionarios)")
print("Registrese e inicie sesion!")
print("//////////////////////////////////////////////////////////")
print("")
menu()