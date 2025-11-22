print("""Welcome to image editor
******************
    1 for lighten
    2 for darken
    3 for quit
******************
    """)

choice = input("--->")
if choice == "3":
  quit()
filename = input("Please enter your file name(clue:skull): \n --->   ")
if filename[-4:] !="bmp.":
  filename = filename + ".bmp"

  print(filename)
value = int(input("Please enter a value you wish to change the image by\n --->   "))
file_name_append = ""

if choice == "1":
  file_name_append = "_lighten_"+str(value)
elif choice == "2":
  file_name_append = "_darken_"+str(value)
  value = 0 - value

########with open############
with open(filename,"rb") as ifile:
  #rb = read binary file
  data = ifile.read()
#######slice file ######
header = data[:54]
print(header)
 #b'BM~\x9f\xc0\x00\x00\   b = binary and \x = hexademical next two numbers
pixel_array = data[54:]
new_pixel_array = []
for pixel in pixel_array:
  new_pixel = pixel + value
  if new_pixel > 255:
    new_pixel = 255
  if new_pixel < 0:
    new_pixel = 0
  new_pixel_array.append(new_pixel)
###########convert new array into bytes##########
new_pixel_array = bytes(new_pixel_array)
##########make neew image file ################
new_image_data = header + new_pixel_array
new_file_name = filename[:-4] + file_name_append + ".bmp"
with open(new_file_name,"wb") as ifile:
  ifile.write(new_image_data)
print("finished updating image")



