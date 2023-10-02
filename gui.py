import tkinter as tk
import main
import tkinter as tk
import main

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x500")

        self.gen = main.RandomPassword()

        # Password length input
        passwordLengthLabel = tk.Label(self.root, text="Password length:")
        passwordLengthLabel.pack()

        self.passwordLengthSlider = tk.Scale(self.root, from_=1, to=50, orient="horizontal", length=300)
        self.passwordLengthSlider.pack()

        # Buttons Function parameters
        buttomFrame = tk.Frame(self.root)
        buttomFrame.pack()

        self.upper_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        upperButton = tk.Checkbutton(buttomFrame, text="UpperCase", variable=self.upper_var)
        digitsButton = tk.Checkbutton(buttomFrame, text="Digits", variable=self.digits_var)
        specialButton = tk.Checkbutton(buttomFrame, text="Default special characters", variable=self.special_var)

        upperButton.pack(side=tk.LEFT)
        digitsButton.pack(side=tk.LEFT)
        specialButton.pack(side=tk.LEFT)

        # Custom character Parameter
        customCharacter = tk.Label(self.root, text="Custom characters")
        customCharacter.pack()

        self.customEntry = tk.Entry(self.root)
        self.customEntry.config(width=51)
        self.customEntry.pack()

        # Space
        space_label = tk.Label(self.root, text="")
        space_label.pack()

        # Generate password button
        generateButton = tk.Button(self.root, text="Generate Password", command=self.gerar_senha)
        generateButton.pack()

        self.passwordLabel = tk.Label(self.root, text="Password:")
        self.passwordLabel.config(height=2)
        self.passwordLabel.pack()

        self.passwordEntry = tk.Entry(self.root)
        self.passwordEntry.config(width=55)
        self.passwordEntry.pack()

    def gerar_senha(self):
        length = int(self.passwordLengthSlider.get())
        upper = self.upper_var.get()
        digits = self.digits_var.get()
        special = self.special_var.get()
        customCharacters = self.customEntry.get()

        password = self.gen.generate_password(
            length=length,
            upperLetters=upper,
            digits=digits,
            special_characters=special,
            custom_characters=customCharacters,
        )
        self.passwordEntry.delete(0, tk.END)
        self.passwordEntry.insert(0, password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
