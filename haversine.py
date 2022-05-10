from math import*
def haversine(raio, lat1, long1, lat2, long2):
  lat1 = radians(lat1) 
  lat2 = radians(lat2) 
  long1 = radians(long1) 
  long2 = radians(long2) 

  a = sin((lat2-lat1)/2)**2
  b = cos(lat1)*cos(lat2)
  c = sin((long2-long1)/2)**2 

  raiz = sqrt(a + (b*c))

  distancia = 2*raio*asin(raiz)

  return distancia