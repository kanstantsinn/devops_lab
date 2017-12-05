from t4_monitor import Monitor
import configparser
import time


def mon_system():
    Config = configparser.ConfigParser()
    Config.read('conf.ini')
    Output = Config['DEFAULT']['output']
    Interval = Config['DEFAULT']['interval']
    Snap = int(Config['SNAPSHOT']['number'])
    while True:
        snapshot = Monitor(Snap)
        snapshot.logging()
        Snap += 1
        Config['SNAPSHOT'] = {'number': "{}".format(Snap)}
        with open('conf.ini', 'w') as configfile:
            Config.write(configfile)
        time.sleep(int(Interval*60))
    return 0


mon_system()
