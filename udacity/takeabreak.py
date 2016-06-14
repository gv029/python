import time
import webbrowser

print "Program started on "+ time.ctime()
for i in range(3):
    time.sleep(2*60*60)
    print("Take a break!")
    webbrowser.open("https://www.wikipedia.org/");
    
