import tkinter as tk
import time
root = tk.Tk()
# width=width chars, height=lines text
text = tk.Text(root, width=20, height=1, bg='white')
text.place(x=850,y=50)
# use a proportional font to handle spaces correctly
text.config(fg="blue",font=('courier', 24, 'bold'))
s1 = "सोनहिरा रेल प्रवासी आरक्षण मध्ये आपले सहर्ष स्वागत आहे "
# pad front and end with 20 spaces
s2 = ' ' * 10
s = s2 + s1 + s2
for k in range(len(s)):
    # use string slicing to do the trick
    ticker_text = s[k:k+100]
    text.insert("1.1", ticker_text)
    root.update()
    # delay by 0.15 seconds
    time.sleep(0.15)
root.mainloop()
