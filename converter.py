from pyassimp import * 
from array import array
import struct

g_vertex_count = 3

def writeToFile(path):
  file = open(path, "wb")
  
  file.write(struct.pack('i', g_vertex_count))
  
  float_array = array('d', [3.14, 0.0, -1000.1])
  float_array.tofile(file)
  
  file.close()

def readFromFile(path):
  file = open(path, "rb")
  
  vertex_count = file.read(struct.calcsize('i'))        #read certain bytes and returns the bytes read
  real_count = struct.unpack('i', vertex_count)[0]  #convert the bytes read into string and get the number (which is the [0])
  print(real_count)
  print("")
  
  float_array = array('d')
  float_array.fromfile(file, real_count)
  for e in float_array:
    print(e)
  
  file.close()
  
def readElmFile(path):
  file = open(path, "rb")
  if file.closed == False:  #if open
    data = file.read(struct.calcsize('I'))
    geometries_count = struct.unpack('I', data)[0]
    print(geometries_count)
    
    vertices_count = 0
    normals_count = 0
    uvs_count = 0
    indices_count = 0
    
    vertices = []
    normals = []
    uvs = []
    indices = []
    
    for e in range(0, geometries_count):
      data = file.read(struct.calcsize('I'))
      vertices_count = struct.unpack('I', data)[0] 
      print("vertices_count: ")
      print(vertices_count)
      
      data = file.read(struct.calcsize('I'))
      normals_count = struct.unpack('I', data)[0]
      print("normals_count: ")
      print(normals_count)
      
      data = file.read(struct.calcsize('I'))
      uvs_count = struct.unpack('I', data)[0]
      print("uvs_count: ")
      print(uvs_count)
      
      data = file.read(struct.calcsize('I'))
      indices_count = struct.unpack('I', data)[0]
      print("indices_count: ")
      print(indices_count)
      
      
      for e in range(0, vertices_count):
        data = file.read(struct.calcsize('f'))
        vertices.append(struct.unpack('f', data)[0])
        
      for e in range(0, normals_count):
        data = file.read(struct.calcsize('f'))
        normals.append(struct.unpack('f', data)[0])
      
      for e in range(0, uvs_count): 
        data = file.read(struct.calcsize('f'))
        uvs.append(struct.unpack('f', data)[0])
        
      for e in range(0, indices_count): 
        data = file.read(struct.calcsize('I'))
        indices.append(struct.unpack('I', data)[0])
        
      data = file.read(struct.calcsize('I'))
      validity_check = struct.unpack('I', data)[0]
      print(validity_check)
    
    file.close()
  else:
    print("Failed to open " + path)
 
def main():
  print ("\nStart!\n")
  
  readElmFile("resources/suzanne.elm")
  
main()