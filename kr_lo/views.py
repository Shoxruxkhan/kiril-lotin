from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def krill(request):
    kiril=["ю","Ю","я","Я","ё","Ё","ш","Ш","ч","Ч","ў","Ў",
        "қ","Қ","ғ","Ғ","ц","Ц","й","Й","у","У","к","К",
        "е","Е","н","Н","г","Г","щ","Щ","з","З","х","Х",
        "э","Э","ж","Ж","д","Д","л","Л","о","О","р","Р",
        "п","П","а","А","в","В","ф","Ф","с","С","м","М",
        "и","И","т","Т","б","Б","қ","Қ","ҳ","Ҳ","ғ","Ғ","ь","Ы","ы"]

    lot=["yu","Yu","ya","Ya","yo","Yo","sh","Sh","ch","Ch","o'","O'",
        "q","Q","g'","G'","ts","Ts","y","Y","u","U","k","K","e","E",
        "n","N","g","G","sh","Sh","z","Z","x","X","e","E","j","J",
        "d","D","l","L","o","O","r","R","p","P","a","A","v","V","f",
        "F","s","S","m","M","i","I","t","T","b","B","q","Q","h","H",
        "g'","G'","`","I","i"]
    context = request.POST.get('data')
    matn = str(context)
    for i in range(len(kiril)):
        matn = matn.replace(kiril[i],lot[i])
    return render(request, 'krill-lotin.html',{'matn':matn})

def lotin(request):
    kiril=["ю","Ю","я","Я","ё","Ё","ш","Ш","ч","Ч","ў","Ў",
        "қ","Қ","ғ","Ғ","ц","Ц","й","Й","у","У","к","К",
        "е","Е","н","Н","г","Г","щ","Щ","з","З","х","Х",
        "э","Э","ж","Ж","д","Д","л","Л","о","О","р","Р",
        "п","П","а","А","в","В","ф","Ф","с","С","м","М",
        "и","И","т","Т","б","Б","қ","Қ","ҳ","Ҳ","ғ","Ғ","ь","Ы","ы"]

    lot=["yu","Yu","ya","Ya","yo","Yo","sh","Sh","ch","Ch","o'","O'",
        "q","Q","g'","G'","ts","Ts","y","Y","u","U","k","K","e","E",
        "n","N","g","G","sh","Sh","z","Z","x","X","e","E","j","J",
        "d","D","l","L","o","O","r","R","p","P","a","A","v","V","f",
        "F","s","S","m","M","i","I","t","T","b","B","q","Q","h","H",
        "g'","G'","`","I","i"]
    context = request.POST.get('data')
    matn = str(context)
    for i in range(len(lot)):
        matn = matn.replace(lot[i],kiril[i])
    return render(request, 'lotin-kiril.html',{'matn':matn})