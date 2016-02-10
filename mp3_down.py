import os 
import requests
import bs4

def song_parser(name):
			link2='https://mp3skull.yoga/mp3/'
			name=name.replace(' ','_')
			url=link2+name+'.html'
			r  = requests.get(url)
			data = r.text
			soup = bs4.BeautifulSoup(data,"html.parser")
			for link in soup.find_all("div",{ "class" : "download_button" }):
				for item in link.find_all("a"):
					temp_name=download_file(item.get('href'),name)
				break
				print(temp_name)

def download_file(url,local_filename):
				local_filename = local_filename+".mp3"
				temp_file=[]
				r = requests.get(url, stream=True)
				local_filename=list(local_filename)
				for item in local_filename:
					if item in ['*','?']:
						item='#'
					temp_file.append(item)
				local_filename=''.join(temp_file)
				with open(local_filename, 'wb') as f:
					for chunk in r.iter_content(chunk_size=1024): 
						if chunk: 
							f.write(chunk)
				return local_filename

def main():
	artist_name = input('Enter the name of the artist ')
	artist_url = 'http://www.top50songs.org/artist.php?artist='+artist_name
	if not os.path.exists(artist_name):
		os.makedirs(artist_name)
	current = os.getcwd()
	new=current+'\\'+artist_name
	os.chdir(new)

	r  = requests.get(artist_url)
	data = r.text
	soup = bs4.BeautifulSoup(data,"html.parser")
	for link in soup.find_all("li"):
		for item in link.find_all("a"):
			print(item.get('title'))
			song_parser(item.get('title'))

if __name__ == '__main__':
	main()
		
	

	

	
