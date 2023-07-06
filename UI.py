import tkinter as tk
from file_handler import SP500DirHandler


class FileHandlerGUI:

    def __init__(self, initial_dir, temp_dir, target_dir):
        self.initial_dir = initial_dir
        self.temp_dir = temp_dir
        self.target_dir = target_dir

    @staticmethod
    def create_gui(self):
        def reset_form():
            customer_initials_entry.delete(0, len(customer_initials_entry.get()))
            order_num_entry.delete(0, len(order_num_entry.get()))
            roll_number_start_entry.delete(0, len(roll_number_start_entry.get()))
            roll_qty_entry.delete(0, len(roll_qty_entry.get()))
            order_notes_entry.delete(1.0, 'end')

        def loading_widget(parent):
            widget = tk.Toplevel(parent)
            widget.title('Loading')
            widget.geometry('100x50')
            label = tk.Label(widget, text='Loading...')
            label.pack(pady=15)

            return widget

        def start():
            # Functionality when start button is clicked
            customer_initials = customer_initials_entry.get().strip().upper()
            order_number = order_num_entry.get().strip().upper()
            roll_number = roll_number_start_entry.get().strip().upper()
            roll_qty = int(roll_qty_entry.get().strip())
            order_notes = order_notes_entry.get(1.0, 'end').strip()

            loading = loading_widget(root)

            file_handler = SP500DirHandler(customer_initials, order_number, roll_number, roll_qty,
                                           order_notes, self.initial_dir, self.temp_dir, self.target_dir)
            file_handler.run()

            loading.destroy()

            reset_form()

        root = tk.Tk()
        root.geometry("800x400")
        root.title("SP-500 File Organizer")

        font = ('Courier New', 18)

        # customer initials order text input
        customer_initials_label = tk.Label(root, text="Customer Initials:", font=font, padx=20, pady=10)
        customer_initials_label.grid(row=0, column=0, sticky='W')
        customer_initials_entry = tk.Entry(root, width=35)
        customer_initials_entry.grid(row=0, column=1, sticky='W')

        # Order number text input
        order_num_label = tk.Label(root, text="Order Number:", font=font, padx=20, pady=10)
        order_num_label.grid(row=1, column=0, sticky='W')
        order_num_entry = tk.Entry(root, width=35)
        order_num_entry.grid(row=1, column=1, sticky='W')

        # Roll Number text input
        roll_number_start_label = tk.Label(root, text="First Roll Number:", font=font, padx=20, pady=10)
        roll_number_start_label.grid(row=3, column=0, sticky='W')
        roll_number_start_entry = tk.Entry(root, width=35)
        roll_number_start_entry.grid(row=3, column=1, sticky='W')

        # Qty of rolls text input
        roll_qty_label = tk.Label(root, text="Number of Rolls:", font=font, padx=20, pady=10)
        roll_qty_label.grid(row=4, column=0, sticky='W')
        roll_qty_entry = tk.Entry(root, width=35)
        roll_qty_entry.insert(1, "1")
        roll_qty_entry.grid(row=4, column=1, sticky='W')

        # Order notes
        order_notes_label = tk.Label(root, text="Order Notes:", font=font, padx=20, pady=10)
        order_notes_label.grid(row=5, column=0, sticky='W')
        order_notes_entry = tk.Text(root, height=5, width=46)
        order_notes_entry.grid(row=5, column=1, sticky='W')

        # Create start button
        start_button = tk.Button(root, text="Start", command=start, height=2, width=4)
        start_button.grid(row=6, column=0, columnspan=3)

        return root

    def run(self):
        root = self.create_gui(self)
        root.mainloop()
