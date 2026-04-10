import random
import statistics
datos=[random.randint(1,100) for _ in range(10)]
media=statistics.mean(datos)
mediana=statistics.median(datos)
valorMayor=max(datos)
valormenor=min(datos)
varianza=statistics.variance(datos)
desviacionEstandar=statistics.stdev(datos)
sumatotal=sum(datos)
print(f"Los datos son : {datos}\n"
      f"La media es : {media}\n"
      f"La mediana es : {mediana}\n"
      f"El valor Mayor es : {valorMayor}\n"
      f"El valor menor es : {valormenor}\n"
      f"La varianza es : {varianza:.2f}\n"
      f"La desviacion estandar es : {desviacionEstandar:.2f}\n"
      f"La suma total es de : {sumatotal}")