#!/usr/bin/env python
'''
Get details of recent earthquakes occurred in Nepal.
Author: Amit Chaudhary
'''
from datetime import date

sheet_id = '1eeIOB58Dn5qRNWTySqrL35U8xY3JjZ7yhg5Dpxvbz8s'
sheet_url = 'https://docs.google.com/spreadsheets/u/0/d/{}/export?format=csv'


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def normalize(data):
    details = data.split('\n')
    details.pop(0)
    details.pop(5)
    details.pop(5)
    details = map(lambda x: x.strip(',\r'), details)
    return details


def create_dictionary(datas):
    result = []
    for data in datas:
        fields = data.split(',')
        result.append({'date': fields[0],
                       'time': fields[1],
                       'magnitude': fields[4],
                       'location': fields[6]})
    return sorted(result, key=lambda r: r.get('date'), reverse=True)


def main():
    data = get_page(sheet_url.format(sheet_id))

    if data:
        details = normalize(data)
        details = create_dictionary(details)
        today = date.today()
        print "Today's date: {}".format(today)
        year, month, day = map(int, details[0]['date'].split('/'))
        last_quake = date(year, month, day)
        delta = (today - last_quake).days
        print 'Last Earthquake: {} days ago'.format(delta)
        print
        headers = ['Date', 'Time', 'Magnitude', 'Location']
        print '{:>15s} {:>15s} {:>15s} {:>15s}'.format(*headers)
        for detail in details:
            fields = (detail['date'], detail['time'],
                      detail['magnitude'], detail['location'])
            print '{:>15s} {:>15s} {:>15s} {:>15s}'.format(*fields)
    else:
        print "Please check your internet connection."

if __name__ == '__main__':
    main()