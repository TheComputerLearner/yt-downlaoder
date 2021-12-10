from pytube import YouTube
link = input('Enter the Link: ')

yt = YouTube(link)

print('Title: ',yt.title)

print('Number of View: ', yt.views)

print('thumbnail', yt.thumbnail_url )

print('Length of the video: ', yt.length,'seconds')

print("Description: ",yt.description)

print("Ratings: ",yt.rating)

print(yt.streams)

print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')
#ys.download()
ys.download('video')