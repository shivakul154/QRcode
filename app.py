import pyqrcode
import png
link="https://www.linkedin.com/in/shivansh-kulshrestha"
qr_code=pyqrcode.create(link)
qr_code.png("shiva.png",scale=5)