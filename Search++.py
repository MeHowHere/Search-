import tkinter as tk
import webbrowser
import requests

def search():
    as_q = entry_1.get()
    as_epq = entry_2.get()
    as_oq = entry_3.get()
    as_eq = entry_4.get()
    as_nlo = entry_5.get()
    as_nhi = entry_6.get()
    lr = entry_7.get()
    cr = entry_8.get()
    as_sitesearch = entry_9.get()
    as_filetype = entry_10.get()
    tbs = entry_11.get()
    
    url = "https://www.google.com/search"
    payload = {
        "as_q": as_q,
        "as_epq": as_epq,
        "as_oq": as_oq,
        "as_eq": as_eq,
        "as_nlo": as_nlo,
        "as_nhi": as_nhi,
        "lr": lr,
        "cr": "country" + cr,
        "as_qdr": "all",
        "as_sitesearch": as_sitesearch,
        "as_occt": "any",
        "safe": "images",
        "as_filetype": as_filetype,
        "tbs": tbs
    }

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        full_url = response.url
        webbrowser.open(full_url, new=2)
    else:
        print("Failed to retrieve the page")
        
root = tk.Tk()
root.title("Google Search")

label_1 = tk.Label(root, text="Search")
label_1.grid(row=0, column=0, padx=5, pady=5)

entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1, padx=5, pady=5)

label_2 = tk.Label(root, text="as_epq")
label_2.grid(row=1, column=0, padx=5, pady=5)

entry_2 = tk.Entry(root)
entry_2.grid(row=1, column=1, padx=5, pady=5)

label_3 = tk.Label(root, text="as_oq")
label_3.grid(row=2, column=0, padx=5, pady=5)

entry_3 = tk.Entry(root)
entry_3.grid(row=2, column=1, padx=5, pady=5)

label_4 = tk.Label(root, text="as_eq")
label_4.grid(row=3, column=0, padx=5, pady=5)

entry_4 = tk.Entry(root)
entry_4.grid(row=3, column=1, padx=5, pady=5)

label_5 = tk.Label(root, text="as_nlo")
label_5.grid(row=4, column=0, padx=5, pady=5)

entry_5 = tk.Entry(root)
entry_5.grid(row=4, column=1, padx=5, pady=5)

label_6 = tk.Label(root, text="as_nhi")
label_6.grid(row=5, column=0, padx=5, pady=5)

entry_6 = tk.Entry(root)
entry_6.grid(row=5, column=1, padx=5, pady=5)

label_7 = tk.Label(root, text="language")
label_7.grid(row=6, column=0, padx=5, pady=5)

entry_7 = tk.Entry(root)
entry_7.grid(row=6, column=1, padx=5, pady=5)

label_8 = tk.Label(root, text="Country")
label_8.grid(row=7, column=0, padx=5, pady=5)

entry_8 = tk.Entry(root)
entry_8.grid(row=7, column=1, padx=5, pady=5)

label_9 = tk.Label(root, text="as_sitesearch")
label_9.grid(row=8, column=0, padx=5, pady=5)

entry_9 = tk.Entry(root)
entry_9.grid(row=8, column=1, padx=5, pady=5)

label_10 = tk.Label(root, text="as_filetype")
label_10.grid(row=9, column=0, padx=5, pady=5)

entry_10 = tk.Entry(root)
entry_10.grid(row=9, column=1, padx=5, pady=5)

label_11 = tk.Label(root, text="tbs")
label_11.grid(row=10, column=0, padx=5, pady=5)

entry_11 = tk.Entry(root)
entry_11.grid(row=10, column=1, padx=5, pady=5)

# add the remaining label and entry widgets for the other parameters

search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=15, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
