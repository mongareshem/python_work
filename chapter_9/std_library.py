from collections import OrderedDict

favorite_languages = OrderedDict()  # favorite_languages = {} (previously)
#Notice NO curly brackets, we have the class OrderedDict() instead; its instance

favorite_languages["shem"] = 'python'
favorite_languages["maal"] = 'ruby'
favorite_languages["victoria"] = 'javascript'
favorite_languages["david jesse"] = 'flutter'

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")