import time 
from plyer import notification
##
if __name__ == '__main__':
    
    while True:
      notification.notify(
          title= 'Notification',
          message = 'this is my message for notification',
          app_name = 'news notify',
          app_icon = "News_icon.png",
          timeout =10
          )
      time.sleep(15)
