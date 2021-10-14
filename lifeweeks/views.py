from django.shortcuts import render, redirect
from .forms import AgeExpect

def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AgeExpect(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # get the form fields
            currentAge = int(request.POST['currentAge'])
            lifeExpentancy = int(request.POST['lifeExpentancy'])
            retireAge = int(request.POST['retireAge'])

            # process the form fields
            currentWeeks = (currentAge * 52)
            lifeInWeeks = (lifeExpentancy * 52)
            retireWeeks = (retireAge * 52)
            remainingweeks = (lifeInWeeks - currentWeeks)
            wksToRetire = (retireWeeks - currentWeeks)

            listweeks = []
            
            for i in range(1,lifeInWeeks + 1):

                if i < 936: # under 18
                    listweeks.append({'color':'#A6D3FF'})
                
                elif i < 1092: # under 21
                    listweeks.append({'color':'#FFC68C'})

                elif i <= currentWeeks:
                    listweeks.append({'color':'blue'})

                elif i < retireWeeks: # weeks until retirement
                    listweeks.append({'color':'#FF9C9C'})
                       
                else:
                    listweeks.append({'color':'#C8B5DA'})
                    
                
# to-do: implement bootstrap, add link to start over, add to notes!

            context = {'currentWeeks':currentWeeks,
                'lifeInWeeks':lifeInWeeks,
                'listweeks': listweeks,
                'remainingweeks':remainingweeks,
                'wksToRetire':wksToRetire,
                'lifeExpentancy':lifeExpentancy,
                'retireAge':retireAge}

        return render(request, 'lifeweeks/weeks.html', context)

    else:
        form = AgeExpect()
        return render(request, 'lifeweeks/home.html', {'form':form})
  


# Variables in weeks.html
# currentWeeks
# lifeInWeeks

# Variables in forms.py
# currentAge
# lifeExpentancy

# eighteen = 936 
# twentyone = 1092
# sixtyfive = 3380
# Working version