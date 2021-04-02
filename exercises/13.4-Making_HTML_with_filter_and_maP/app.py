all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
color = ""
def filter_colors(items):
    return items["sexy"] == True

def generate_li(items):
    return "<li>"+items["label"]+"</li>"
    
lista = list(filter(filter_colors, all_colors))
color = list(map(generate_li, lista))
x = ""
for i in color:
    x += i

print (x)