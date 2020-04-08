from django.shortcuts import render


from django.shortcuts import render
from .models import NavMenuItems, AboutInfo, Experience, Education, LanguagesTools, Interests, Awards


#PageDetails, AboutInfo, BlogInfo


def landingpage(request):
    nav_bar_item_list = NavMenuItems.objects.all()
    about_info = AboutInfo.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    languages_tools = LanguagesTools.objects.all()
    interests = Interests.objects.all()
    awards = Awards.objects.all()
    context = {
        'nav_items': nav_bar_item_list,
        'about_info': about_info,
        'experience': experience,
        'education': education,
        'languages_tools': languages_tools,
        'interests': interests,
        'awards': awards,
    }
    return render(request, 'resumeApp/landingpage.html', context)