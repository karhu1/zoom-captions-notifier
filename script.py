from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pyautogui, pytesseract, cv2, re
import pygame, time

# region=(775, 940, 350, 90) MIDDLE OF SCREEN


def screenshot():
  screenshot = pyautogui.screenshot(region=(300, 890, 350, 90))

  screenshot.save('screenshot.png')

def ocr_core(img):
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  text = pytesseract.image_to_string(img)
  return text

# MAKE GRAYSCALE
def get_grayscale(image):
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# NOISE REDUCTION
def remove_noise(image):
  return cv2.medianBlur(image, 5)

# THRESHOLDING
def thresholding(image):
  return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

while True:
  screenshot()
  img = cv2.imread('screenshot.png')
  img = get_grayscale(img)
  img = thresholding(img)
  # img = remove_noise(img)

  target_phrases = ['canvas', 'lecture post']
  matches = [phrase for phrase in target_phrases if re.search(phrase, ocr_core(img), re.IGNORECASE)]

  print(matches)

  for element in matches:
    pygame.mixer.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)

  time.sleep(5)