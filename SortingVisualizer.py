from tkinter import *
import ttkbootstrap as tb
import random
from algorithms import Algorithms


class SortingVisualizer:

    # Constants
    WIDTH = 1380

    def __init__(self):


        # Choose theme for the window
        self.root = tb.Window(themename="darkly")
        self.root.title("Sorting Algorithm Visualizer")
        # Choose the dimensions of the window
        self.root.geometry("1400x800")

        # Initialize the Algorithms
        self.algorithms = Algorithms(self)

        # Create frames for the menu and canvas
        self.create_ui_frames()

        self.root.mainloop()

    def create_ui_frames(self):

        # Menu frame
        ui_frame = tb.Frame(self.root,
                            width=self.WIDTH,
                            height=90,
                            bootstyle="default")
        ui_frame.grid(row=0, column=0, padx=10, pady=5)

        # Call menu method to create interface
        self.menu()

        # Create canvas frame
        canvas_frame = tb.Frame(self.root,
                                width=self.WIDTH + 2,
                                height=682,
                                bootstyle="danger")
        canvas_frame.grid(row=1, column=0, padx=10, pady=5)

        # Create canvas
        self.canvas = Canvas(self.root,
                             width=self.WIDTH,
                             height=680,
                             bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

    def menu(self):

        # Hold value of the Combobox
        self.selected_alg = StringVar()

        # Frame for the interface
        pick_algo_frame = tb.Frame(self.root,
                                   width=200,
                                   height=50,
                                   bootstyle="default")
        pick_algo_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # "Algorithm: " label
        algo_label = tb.Label(pick_algo_frame,
                              text="Algorithm: ",
                              bootstyle="danger",
                              font=("Helvetica, 18"))
        algo_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Combobox with algorithm options
        algo_menu = tb.Combobox(pick_algo_frame,
                              bootstyle="danger",
                              textvariable=self.selected_alg,
                              values=["bubbleSort", "insertionSort", "mergeSort", "heapSort",
                                      "quickSort", "shellSort", "combSort", "exchangeSort"])
        algo_menu.grid(row=0, column=1, padx=5, pady=5)

        # Set current to the first option
        algo_menu.current(0)

        # generate array button
        gen_button = tb.Button(pick_algo_frame,
                               text="Generate Array",
                               command=self.generate,
                               bootstyle="danger, outline")
        gen_button.grid(row=0, column=2, padx=5, pady=5)

        # Choose the size of array slider
        self.size_slider = tb.Scale(pick_algo_frame,
                                    bootstyle="warning",
                                    length=800,
                                    from_=5,
                                    to=500,
                                    command=self.scaler)
        self.size_slider.grid(row=0, column=4, padx=5, pady=5)

        # Array size display
        self.slider_label = tb.Label(pick_algo_frame,
                                     text="5",
                                     bootstyle="danger",
                                     font=("Helvetica, 18"))
        self.slider_label.grid(row=0, column=5, padx=5, pady=5)

        # Initiate sorting button
        start_button = tb.Button(pick_algo_frame,
                                 text="Start",
                                 command=self.start_algorithm,
                                 bootstyle="success, outline")
        start_button.grid(row=0, column=3, padx=5, pady=5)


    # Generate array and shuffle it
    def generate(self):

        self.data = [i for i in range(1, int(self.size_slider.get())+1)]
        random.shuffle(self.data)
        self.draw_data(self.data, ["white" for x in range(len(self.data))])

    # Command: Display the size of the array
    def scaler(self, e):
        self.slider_label.config(text=f"{int(self.size_slider.get())}")

    #Command: Initiate sorting algorithm
    def start_algorithm(self):
        self.algorithms.start_algorithm(self.data)

    # Draw data on the canvas
    def draw_data(self, data, color):
        self.canvas.delete("all")

        # Canvas Size
        c_height = 680
        c_width = self.WIDTH - 20

        # Bar dimensions
        x_width = c_width / (len(data) + 1)
        offset = 10
        spacing = 1

        normalized_data = [i / max(data) for i in data]

        # Create bars that will fit on the screen
        for i, height in enumerate(normalized_data):

            # Top Left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 680
            # Bottom Right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

        self.root.update()

