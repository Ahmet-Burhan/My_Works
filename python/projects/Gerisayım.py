import time
import datetime
print("Merhaba Geleceğin VERİ BİLİMCİLERİ!!!\n(Geri Sayımdan çıkmak için 'Interrupt the Kernel')\n")
try: 
    def countdown(stop):
        while True:
            difference = stop - datetime.datetime.now()
            count_hours, rem = divmod(difference.seconds, 3600)
            count_minutes, count_seconds = divmod(rem, 60)
            print('DATA SCIENCE Introya '
                  + str(difference.days) + " gün "
                  + str(count_hours) + " saat "
                  + str(count_minutes) + " dakika "
                  + str(count_seconds) + " saniye kaldı "
                  )
            time.sleep(1)
    end_time = datetime.datetime(2021, 9, 3, 19, 0, 0)
    countdown(end_time)
    
except KeyboardInterrupt:
    print('\n3 EYLÜL Cuma 19.00 (TR) de görüşmek üzere...')