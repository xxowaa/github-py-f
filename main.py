import tkinter as tk
import webview

# Function to create a web view
def create_web_view():
    # Create a separate window that loads the URL
    webview.create_window("Web Editor", "https://devjs-ruby.vercel.app/editor.html")
    webview.start()  # This line is critical to start the webview event loop

# Main function to create the Tkinter window
def main():
    root = tk.Tk()
    root.title("Tkinter WebView Example")

    # Create a button to open the URL
    open_button = tk.Button(root, text="Open Web Editor", command=create_web_view)
    open_button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()