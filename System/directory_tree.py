#Author: Varnesh Gawde
#Date 9/9/2023
import os
import tkinter as tk
from tkinter import ttk, filedialog

def display_directory_tree(path, parent_node):
    """Recursively display directory tree in the given node."""
    for item in os.listdir(path):
        item_full_path = os.path.join(path, item)
        node = tree.insert(parent_node, 'end', text=item)
        if os.path.isdir(item_full_path):
            display_directory_tree(item_full_path, node)

def select_directory():
    """Open a directory chooser dialog and display the selected directory in the tree view."""
    path = filedialog.askdirectory()
    if not path:
        return

    tree.delete(*tree.get_children())  # Clear previous tree items
    root_node = tree.insert('', 'end', text=path)
    display_directory_tree(path, root_node)
    tree.item(root_node, open=True)  # Open the root node

app = tk.Tk()
app.title('Directory Tree Viewer')

frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tree = ttk.Treeview(frame)
tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

select_btn = ttk.Button(frame, text="Select Directory", command=select_directory)
select_btn.pack(pady=5)

app.geometry('500x500')
app.mainloop()
