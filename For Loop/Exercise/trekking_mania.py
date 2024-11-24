trekking_group_count = int(input())

trekking_musala_peoples = 0
trekking_montblanc_peoples = 0
trekking_kilimanjaro_peoples = 0
trekking_k2_peoples = 0
trekking_everest_peoples = 0



for i in range (0, trekking_group_count):
    trekking_group_peoples = int(input())
    if trekking_group_peoples <= 5:
        trekking_musala_peoples += trekking_group_peoples
    elif 5 < trekking_group_peoples <= 12:
        trekking_montblanc_peoples += trekking_group_peoples
    elif 12 < trekking_group_peoples <= 25:
        trekking_kilimanjaro_peoples += trekking_group_peoples
    elif 25 < trekking_group_peoples <= 40:
        trekking_k2_peoples += trekking_group_peoples
    elif trekking_group_peoples > 40:
        trekking_everest_peoples += trekking_group_peoples

trekking_peoples = trekking_musala_peoples + trekking_montblanc_peoples + trekking_kilimanjaro_peoples + trekking_k2_peoples + trekking_everest_peoples
musala_percent = trekking_musala_peoples * 100 / trekking_peoples
montblanc_percent = trekking_montblanc_peoples * 100 / trekking_peoples
kilimanjaro_percent = trekking_kilimanjaro_peoples * 100 / trekking_peoples
k2_percent = trekking_k2_peoples * 100 / trekking_peoples
everest_percent = trekking_everest_peoples * 100 / trekking_peoples

print(f'{musala_percent:.2f}%')
print(f'{montblanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

