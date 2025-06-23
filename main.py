import tkinter as tk
from tkinter import scrolledtext

# npc generates the NPCs 
from npc.npc import NPC 

def on_generate():
    # Generate a new NPC, then display it in the text area
    npc = NPC()
    text = str(npc)     # Convert NPC object to string
    
    # Clear previous output and insert new: 
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, text)
    output_area.config(state=tk.DISABLED)
    
def main():
    root = tk.Tk()
    root.title("NPC Generator")
    root.geometry("500x800")
    
    #Generate button
    generate_btn = tk.Button(root, text="Generate NPC", command=on_generate)
    generate_btn.pack(pady=10)
    
    #scrollable text area, read-only
    global output_area
    output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, state=tk.DISABLED)
    output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    root.mainloop()
    

if __name__ == "__main__":
    main()



#if __name__ == "__main__":
#    # Generate and print 5 NPCs
#    for i, _ in enumerate(range(5), start=1):
#        npc = NPC()
#        print(f"{i}) {npc}")
    