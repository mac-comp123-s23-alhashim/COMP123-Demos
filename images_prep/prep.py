from imageTools import *
import PIL

# font = pickAFont()
font = ImageFont.truetype("Demo_ConeriaScript.ttf", 300)

mac_logo = Picture("mac-logo.png")
mac_logo.drawText(mac_logo.getWidth()/2, mac_logo.getHeight()/2, "Mac",
                  "yellow", font)
mac_logo.show()

input()
