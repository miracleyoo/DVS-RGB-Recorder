import aedat

decoder = aedat.Decoder(r'D:\Dataset\DVS\dv_data\dvSave-2021_10_20_11_06_43.aedat4')
print(decoder.id_to_stream())

for packet in decoder:
    print(packet['stream_id'], end=': ')
    if 'events' in packet:
        print('{} polarity events'.format(len(packet['events'])))
    elif 'frame' in packet:
        print('{} x {} frame'.format(packet['frame']['width'], packet['frame']['height']))
    elif 'imus' in packet:
        print('{} IMU samples'.format(len(packet['imus'])))
    elif 'triggers' in packet:
        print('{} trigger events'.format(len(packet['triggers'])))
    break