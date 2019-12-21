import os

name = input('Series Name: ')
n_seasons = int(input('Number of Seasons: '))
n_episodes = int(input('Number of Episodes: '))

folders = [
	os.makedirs(f'{name}/S{season:02d}/E{episode:02d}')
	for season in range(1, n_seasons+1)
	for episode in range(1, n_episodes+1)
]
