video_1_title = "Concrete Candle Holder How To Make"
video_1_link = "Z_8Ss94fgZc"

video_2_title = "How To Make a Concrete Fire Bowl"
video_2_link = "uSSp3X07Vls"

video_3_title = "Diy LED Desk Lamp With Concrete Base"
video_3_link = "a5yiMhJaGCo"

playlist_1_title = "Работа по дереву"
playlist_2_title = "Литье"
playlist_3_title = "Оборудование мастерской"

tags = "concrete, table, wood, furniture, accessorizes, metal"


print('''Приложение в разработке.
Введите ”videos” чтобы посмотреть список видео. 
Введите “tags” чтобы посмотреть список тегов. 
Введите “playlists” чтобы посмотреть список тегов. 
Введите “about” чтобы получить информацию.
''')

cmd = input()

if cmd == 'videos':
    print('У нас есть 3 видео:')
    print()
    print(f'{video_1_title}: youtu.be/{video_1_link}')
    print(f'{video_2_title}: youtu.be/{video_2_link}')
    print(f'{video_3_title}: youtu.be/{video_3_link}')

elif cmd == 'tags':
    print(f'У нас есть 6 тегов: {tags}')

elif cmd == 'playlists':
    print(f'У нас есть 3 плейлиста: {playlist_1_title}, {playlist_2_title}, {playlist_3_title}')

elif cmd == 'about':
    print('Stepik Media – О приложении. Это – кинотеатр полезных видео про DIY (или другая, ваша тема)')

else:
    print('К сожалению, ничего не понятно!')