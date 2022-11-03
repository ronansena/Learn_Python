import tkinter as tk
import subprocess
import threading
import sys
from functools import partial

# ### classes ####

class Redirect:
    
    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, textbox):
        self.widget.insert('end', textbox)
        if self.autoscroll:
            self.widget.see('end') # autoscroll

    def flush(self):
        pass


def run(textbox=None):
    threading.Thread(target=test, args=[textbox]).start()

def test(textbox=None):

    p = subprocess.Popen("python3 callfunction4.py".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    #p = subprocess.Popen("python2 call_function5.py".split(), stdout=subprocess.PIPE, bufsize=1, text=True,universal_newlines=True)
    
    while p.poll() is None:
        msg = p.stdout.readline().strip()  # read a line from the process output
        if msg:
            textbox.insert(tk.END, msg + "\n")
            #print (p.communicate("n\n")[0])
        
    # for stdout_line in iter(p.stdout.readline().strip()):
    #     yield stdout_line 
    # p.stdout.close()
    # return_code = p.wait()
    # if return_code:
    #     raise subprocess.CalledProcessError(return_code, "python2 call_function5.py".split())


if __name__ == "__main__":
    fenster = tk.Tk()
    fenster.title("My Program")
    textbox = tk.Text(fenster)
    textbox.grid()
    scrollbar = tk.Scrollbar(fenster, orient=tk.VERTICAL)
    scrollbar.grid()

    textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textbox.yview)

    start_button = tk.Button(fenster, text="Start", command=partial(run, textbox))
    start_button.grid()

    old_stdout = sys.stdout
    sys.stdout = Redirect(textbox)

    fenster.mainloop()
    sys.stdout = old_stdout