from tkinter import *
import random
import copy

class LiveModel:
	__word_original = [ "B", "O", "N", "J", "O", "U", "R"]

	def __init__(self):
		self.__word = copy.copy(self.__word_original)

	def get_word(self):
		"""
		Retourne les données sous forme de liste
		"""
		return self.__word

	def modify_word(self, index ):
		code = ord(self.__word[index])
		new_letter = chr(code+1)
		self.__word[index] = new_letter

	def reset_word(self):
		self.__word = copy.copy(self.__word_original)


class LiveView:

	def __init__(self, controller):
		self.window = Tk()

		b1 = Button(self.window, text='Go!', command=controller.gui_go)  # référence !
		b1.pack(side=LEFT, padx=3, pady=3)

		# b2 = Button(fen1, text='Display')
		# b2.bind( "<Click>", lambda event: controller.gui_display())
		b2 = Button(self.window, text='Display', command=controller.gui_display)
		b2.pack(side=LEFT, padx=3, pady=3)

		b3 = Button(self.window, text='Modify', command=controller.gui_modify)
		b3.pack(side=LEFT, padx=3, pady=3)

		b4 = Button(self.window, text='Reset', command=controller.gui_reset)
		b4.pack(side=LEFT, padx=3, pady=3)

		entree = Entry(self.window)
		entree.bind("<Return>", lambda event: controller.gui_change_vit(entree.get()))
		entree.pack(side=RIGHT)

		chaine = Label(self.window)
		chaine.configure(text="Attente entre chaque étape (ms) :")
		chaine.pack(side=RIGHT)

	def display_word(self, data):
		str = "/".join(data)
		print(str)

	def mainloop(self):
		self.window.mainloop()


class LiveController:

	def __init__(self):
		self.model = LiveModel()
		self.view = LiveView(self)
		self.view.mainloop()

	def gui_go(self):
		print("button go pressed")

	def gui_change_vit(self, new_speed):
		"""fonction pour changer la vitesse(l'attente entre chaque étape)"""
		# global vitesse
		# vitesse = int(eval(entree.get()))
		print(new_speed)

	def gui_display(self):
		"""
		1) Récupère le contenu de Model
		2) L'envoie à  View pour affichage
		"""
		word_l = self.model.get_word()
		# print(word_l)
		self.view.display_word(word_l)

	def gui_modify(self):
		word_l = self.model.get_word()
		i_alea = random.randrange(len(word_l))
		self.model.modify_word(i_alea)
		print("mot modifié")

	def gui_reset(self):
		self.model.reset_word()
		print("mot resetté")


# programme "principal"
if __name__ == "__main__":
	LiveController()

# fin de l'application
