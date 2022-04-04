

class ConvertToDollar():
	
	@classmethod
	def dolarizar(self, number) -> str:
		numero=number
		numero=round(numero,2)
		numero=str(numero)
		numeroFormateado=""
		if numero[-2] == ".":
			numero=numero+"0"
		insertar=len(numero)-7
		for i in numero:
			if i == ".":
				i=","
			numeroFormateado+=i
		numero=numeroFormateado
		numeroFormateado=""
		while insertar > -1:
			contador=0
			for i in numero:
				if str(contador) == str(insertar):
					i=i+"."
					insertar=insertar-3
				numeroFormateado+=i
				contador+=1
			numero=numeroFormateado
			numeroFormateado=""
		resultadousd = numero
		return f'$ {resultadousd}'
	





		
		
