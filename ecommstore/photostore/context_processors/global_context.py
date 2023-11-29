from photostore.models import Product
import random

def global_context(request):

	# collect all themes
	theme_choices = Product.THEME_CHOICES
	theme_codes = [theme[0] for theme in theme_choices]
	theme_names = [theme[1] for theme in theme_choices]
	
	# 'Theme of the Day' section
	# Random Theme label
	theme_index = random.choice(range(len(theme_choices)))
	theme_label = theme_names[theme_index]

	# Randomized pictures based on chosen theme_label and random_theme_inds
	total_theme_images = 9    
	theme_set = Product.objects.filter(theme=theme_codes[theme_index])   
	random_theme_inds = random.choices(range(theme_set.count()), k=total_theme_images)
	random_theme_pics = [theme_set[ind] for ind in random_theme_inds]    


	# randomize themes for 'Photo' and 'Art' of the day pictures
	# filter by categoy
	photos = Product.objects.filter(category='PH')
	art = Product.objects.filter(category='ART')
	
	# randomize and pick image
	random_photo_ind = random.choice(range(photos.count()))
	random_photo = photos[random_photo_ind]

	random_art_ind = random.choice(range(art.count()))
	random_art = art[random_art_ind]
	
	context = {
		"random_photo" : random_photo,
        "random_art" : random_art,
        "theme_label" : theme_label,
        "theme_pictures" : random_theme_pics,		
        	}
	
	return context 