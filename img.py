import os 
from PIL import Image 

folder_path =r"C:\Users\Khafiz\Downloads\Normal-20240602T024341Z-001\Normal" 

width = 224 
height = 224

for filename in os.listdir(folder_path):
  if filename.endswith((".png",".jpg",".jgeg",".gif")):

   image_path = os.path.join(folder_path,filename)
   image= Image.open(image_path)
   resized_image = image.resize ((width,height))
   resized_image.save(image_path)
   image.close()
