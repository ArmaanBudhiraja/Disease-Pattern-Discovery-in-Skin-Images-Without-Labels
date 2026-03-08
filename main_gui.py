import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

from predict import predict_disease
from retrieval import find_similar_images
from visualization import show_processing, show_similar_images


class SkinDiseaseApp:

    def __init__(self, root):

        self.root = root
        self.root.title("AI Skin Disease Detection System")
        self.root.geometry("1100x700")
        self.root.configure(bg="#1e1e1e")

        title = tk.Label(
            root,
            text="AI Skin Disease Detection System",
            font=("Segoe UI",24,"bold"),
            fg="white",
            bg="#1e1e1e"
        )
        title.pack(pady=20)

        main_frame = tk.Frame(root, bg="#1e1e1e")
        main_frame.pack()

        left_frame = tk.Frame(main_frame, bg="#1e1e1e")
        left_frame.grid(row=0,column=0,padx=30)

        right_frame = tk.Frame(main_frame, bg="#1e1e1e")
        right_frame.grid(row=0,column=1,padx=30)

        self.image_label = tk.Label(left_frame, bg="#1e1e1e")
        self.image_label.pack()

        button_frame = tk.Frame(left_frame, bg="#1e1e1e")
        button_frame.pack(pady=20)

        btn_style = {
            "font":("Segoe UI",12,"bold"),
            "width":14,
            "bg":"#3a7ff6",
            "fg":"white",
            "bd":0,
            "padx":10,
            "pady":8
        }

        tk.Button(
            button_frame,
            text="Upload Image",
            command=self.upload_image,
            **btn_style
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Predict Disease",
            command=self.predict,
            **btn_style
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Show Processing",
            command=self.show_processing_steps,
            **btn_style
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Similar Images",
            command=self.show_similar,
            **btn_style
        ).grid(row=0,column=3,padx=5)

        result_title = tk.Label(
            right_frame,
            text="Prediction Result",
            font=("Segoe UI",16,"bold"),
            fg="white",
            bg="#1e1e1e"
        )
        result_title.pack(pady=10)

        self.result_text = tk.Text(
            right_frame,
            height=10,
            width=40,
            font=("Consolas",12),
            bg="#2d2d2d",
            fg="white"
        )
        self.result_text.pack()

        chart_title = tk.Label(
            right_frame,
            text="Disease Probability",
            font=("Segoe UI",16,"bold"),
            fg="white",
            bg="#1e1e1e"
        )
        chart_title.pack(pady=10)

        self.chart_frame = tk.Frame(right_frame, bg="#1e1e1e")
        self.chart_frame.pack()

        self.image_path = None


    def upload_image(self):

        path = filedialog.askopenfilename(
            filetypes=[("Image Files","*.jpg *.jpeg *.png")]
        )

        if not path:
            return

        self.image_path = path

        img = Image.open(path)

        img = img.resize((350,350))

        img = ImageTk.PhotoImage(img)

        self.image_label.config(image=img)

        self.image_label.image = img


    def predict(self):

        if not self.image_path:
            return

        prediction, probs, classes, img, blur, gray, lesion, boundary, heatmap, overlay, features = predict_disease(self.image_path)

        self.features = features

        self.processing_data = (img,blur,gray,lesion,boundary,heatmap,overlay)

        self.result_text.delete(1.0,tk.END)

        self.result_text.insert(
            tk.END,
            f"Predicted Disease:\n{prediction}\n\n"
        )

        self.result_text.insert(
            tk.END,
            "Confidence:\n"
        )

        for c,p in zip(classes,probs):

            self.result_text.insert(
                tk.END,
                f"{c} → {round(p*100,2)}%\n"
            )

        self.draw_chart(classes,probs)


    def draw_chart(self, classes, probs):

        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        fig = plt.Figure(figsize=(4,3), dpi=100)

        ax = fig.add_subplot(111)

        values = [p*100 for p in probs]

        ax.barh(classes, values)

        ax.set_xlabel("Probability (%)")

        fig.patch.set_facecolor("#1e1e1e")

        ax.set_facecolor("#1e1e1e")

        ax.tick_params(colors="white")

        for label in ax.get_xticklabels()+ax.get_yticklabels():
            label.set_color("white")

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)

        canvas.draw()

        canvas.get_tk_widget().pack()


    def show_processing_steps(self):

        if not hasattr(self,"processing_data"):
            return

        img,blur,gray,lesion,boundary,heatmap,overlay = self.processing_data

        show_processing(img,blur,gray,lesion,boundary,heatmap,overlay)


    def show_similar(self):

        if not hasattr(self,"features"):
            return

        paths = find_similar_images(self.features)

        show_similar_images(paths)


if __name__ == "__main__":

    root = tk.Tk()

    app = SkinDiseaseApp(root)

    root.mainloop()