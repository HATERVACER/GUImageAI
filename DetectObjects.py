import pip
try:
	from imageai.Detection import VideoObjectDetection
	from imageai.Detection import ObjectDetection
	from tkinter import filedialog as fd
	from tkinter import *
	import wget
	import os
	import face_recognition
	from PIL import Image, ImageDraw

except ModuleNotFoundError:
		def install(package):
		    if hasattr(pip, 'main'):
		        pip.main(['install', package])
		    else:
		        pip._internal.main(['install', package])
		install('tensorflow')
		install('https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl')
		install('keras')
		install('h5py')
		install('matplotlib')
		install('pillow')
		install('opencv-python')
		install('numpy')
		install('scipy')
		install('wget')
		install('face_recognition')
		from imageai.Detection import VideoObjectDetection
		from imageai.Detection import ObjectDetection
		from tkinter import *
		from tkinter import filedialog as fd
		import os
		import wget
		import face_recognition


# Main variables
exec_path = os.getcwd()
root = Tk()
k = True
s = True 	

def vftrue():
	global vf
	vf = 0
	print(vf)

def vffalse():
	global vf
	vf = 1
	print(vf)

def vfwtf():
	global vf
	vf = 2
	print(vf)

def clear_search(*iloveminecraft):
	global k
	if k:
		entry_file_path.delete(0, END)
	k = False

def clear_search1(*iloveminecraftvol2):
	global s
	if s:
		entry_file_path1.delete(0, END)
	s = False

def start():
	global vf
	ifp = entry_file_path.get()
	ofp = entry_file_path1.get()
	if vf == 0:
		try:
			print("Starting to render video")
			detector = VideoObjectDetection()
			detector.setModelTypeAsYOLOv3()
			detector.setModelPath(os.path.join(exec_path, "yolo.h5"))
			detector.loadModel()
		except:
			wget.download("https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5")
			print("Starting to render video")
			detector = VideoObjectDetection()
			detector.setModelTypeAsYOLOv3()
			detector.setModelPath(os.path.join(exec_path, "yolo.h5"))
			detector.loadModel()
			list = detector.detectObjectsFromVideo(
				input_file_path=os.path.join(exec_path, ifp),
				output_file_path=os.path.join(exec_path, ofp),
				frames_per_second=20
			)
		label = Label(root, text="Succeful!", fg="green")
		label.pack()
	elif vf == 1: 
		try:
			print("Starting to render photo")
			detector = ObjectDetection()
			detector.setModelTypeAsRetinaNet()
			detector.setModelPath(os.path.join(exec_path, "resnet50_coco_best_v2.0.1.h5"))
			detector.loadModel()
		except OSError:
			wget.download("https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5")
			print("Starting to render photo")
			detector = ObjectDetection()
			detector.setModelTypeAsRetinaNet()
			detector.setModelPath(os.path.join(exec_path, "resnet50_coco_best_v2.0.1.h5"))
			detector.loadModel()
			list = detector.detectObjectsFromImage(
				input_image=os.path.join(exec_path, ifp),
				output_image_path=os.path.join(exec_path, ofp),
				display_percentage_probability=True,
				display_object_name=True
			)
		label = Label(root, text="Succeful!", fg="green")
		label.pack()
	elif vf == 2:
		image = face_recognition.load_image_file(exec_path + "/" + ifp)
		face_landmarks_list = face_recognition.face_landmarks(image)
		pil_image = Image.fromarray(image)
		d = ImageDraw.Draw(pil_image)
		for face_landmarks in face_landmarks_list:
			for facial_feature in face_landmarks.keys():
				d.line(face_landmarks[facial_feature], width=5)
		pil_image.show()

root.title("Objecter")
root.resizable("False", "False")
root.geometry("200x200")

label1 = Label(root, text="Choose file type")
choose = Button(root, text="Video", command=vftrue)
choose1 = Button(root, text="Photo", command=vffalse)
choose2 = Button(root, text="Face recognit", command=vfwtf)
entry_file_path = Entry(root)
entry_file_path.insert(END, "Input file name") 
entry_file_path1 = Entry(root, text="Output file name")
entry_file_path1.insert(END, "Output file name") 
recognit = Button(root, text="Start", command=start)

label1.pack()
choose.pack()
choose1.pack()
choose2.pack()
entry_file_path.pack()
entry_file_path1.pack()
recognit.pack()

entry_file_path.bind("<Button-1>", clear_search) 
entry_file_path1.bind("<Button-1>", clear_search1) 

root.mainloop()