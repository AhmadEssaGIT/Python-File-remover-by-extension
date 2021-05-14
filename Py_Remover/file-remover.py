import os 
from os import path

class FileRemover:
	def __init__(self, dir, *args) :
		 self.files_extensions = args
		 self.files = []
		 self.dir = str(dir)
		 self.accepted = ['yes' , 'y' , 'Yes' , 'Y']
	def remove(self):
		if path.isdir(self.dir) and not self.dir == '' :
			self.files = os.listdir(self.dir)			
			if self.files == [] :
				print("No Files In the Folder")
				exit("Exit With code 44" )
				
			else :
				print("Current files will be deleted : \n")
				for file in self.files:
					if file.endswith(self.files_extensions[0]):
						print(file)

				accept = str(input("{}\nPlease Choose option to delete ! (yes\\no)".format(20*'-')))
			 
				if (accept in self.accepted ):
					for file in self.files:
						os.remove(path.join(self.dir , file))
						print("delete {}".format(file))
				else:
					print("Not Permited")
					exit("Exit With code 1 , No Permision" )

		else : 
			print("Path \"%s\" is not a directory ! Please be sure. " % self.dir)

def main():


	Remover = FileRemover('/home/ahmad/Desktop/Folder Deleteion', ('exe','js'))
	Remover.remove()
	exit("Exit With code 0 " )

if __name__=="__main__":main()
