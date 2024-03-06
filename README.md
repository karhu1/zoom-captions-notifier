# Zoom Captions Notifier

This is a mini project I made in class because I wanted to create a program for capturing captions in a zoom meeting, reading them, and finding matches for keywords to notify me in case I needed to go to canvas for one of our attendance checks.

I'm using pyautogui and cv2 libraries for grabbing the screenshot, making the image clearer, and then finding matches with pytesseract and re.

Lastly I just play a super loud meow sound with pygame in the case that it is time for attendance, allowing me to have the zoom muted on my other monitor while I work on homework on the other. Very nice 👍

## Install

1. `pip3 install -r requirements.txt`
2. Download [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
3. Make sure the file path in `script.py` lines up with where your `Tesseract.exe` file is!
4. Mess around with the pixels to get your screenshot lined up properly.
5. You are done! You can run the script in the termianl with `py script.py`