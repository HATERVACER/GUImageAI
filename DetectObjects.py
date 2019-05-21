import pip
try:
	from imageai.Detection import VideoObjectDetection
	from imageai.Detection import ObjectDetection
	from tkinter import filedialog as fd
	from tkinter import *
	import wget
	import os
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
		from imageai.Detection import VideoObjectDetection
		from imageai.Detection import ObjectDetection
		from tkinter import *
		from tkinter import filedialog as fd
		import os
		import wget


# Main variables
exec_path = os.getcwd()
root = Tk()

def vftrue():
	global vf
	vf = True
	print(vf)

def vffalse():
	global vf
	vf = False
	print(vf)

def start():
	global vf
	ifp = entry_file_path.get()
	ofp = entry_file_path1.get()
	if vf == True:
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
	elif vf == False: 
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

root.title("Objecter")
root.resizable("False", "False")
root.geometry("200x200")

label1 = Label(root, text="Choose file type")
choose = Button(root, text="Video", command=vftrue)
choose1 = Button(root, text="Photo", command=vffalse)
entry_file_path = Entry(root)
entry_file_path.insert(END, "Input file name") 
entry_file_path1 = Entry(root, text="Output file name")
entry_file_path1.insert(END, "Output file name") 
recognit = Button(root, text="Start", command=start)

label1.pack()
choose.pack()
choose1.pack()
entry_file_path.pack()
entry_file_path1.pack()
recognit.pack()
root.mainloop()
