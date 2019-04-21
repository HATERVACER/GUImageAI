from imageai.Detection import VideoObjectDetection
from tkinter import *
from tkinter import filedialog as fd
import os

# Main variables
exec_path = os.getcwd()
root = Tk()

def start():
	ifp = entry_file_path.get()
	ofp = entry_file_path1.get()
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

root.title("Objecter")
root.resizable("False", "False")
root.geometry("200x150")

label1 = Label(root, text="Objecter")
entry_file_path = Entry(root)
entry_file_path.insert(END, "Input file name") 
entry_file_path1 = Entry(root, text="Output file name")
entry_file_path1.insert(END, "Output file name") 
recognit = Button(root, text="Start", command=start)

label1.pack()
entry_file_path.pack()
entry_file_path1.pack()
recognit.pack()
root.mainloop()