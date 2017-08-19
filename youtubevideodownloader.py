import pytube
#fin des imports
print("Entrez le lien de votre video youtube")
lien = input()
youtube = pytube.YouTube(lien)
video = youtube.get_videos()

s = 1
for v in video:
	print(str(s)+". "+str(v))
	s += 1

print("Entrez la qualitée de votre video:")
n = int(input())
vid = video[n-1]

print("Entrez votre chemin:")	
chemin = input()
vid.download(chemin)

print(youtube.filename+"votre video a ete telechargee avec succes")