import os


name = input('Series Name: ')

total_seasons = int(input('Number of Seasons: '))

total_episodes = int(input('Number of Episodes: '))


for season in range(1, total_seasons+1):
    for episode in range(1, total_episodes+1):

        folder_name = name + '/S'

        if season < 10:
            folder_name += '0'

        folder_name += str(season) + '/E'

        if episode < 10:
            folder_name += '0'

        folder_name += str(episode)

        os.makedirs(folder_name)

