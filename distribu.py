print("Bienvenue dans notre simulation de distributeur")#ça sa dit Bienvenue pour le distributeur
#SAut a la ligne
distri = {#ça c pour stocker le stock
    "A1": {"nom": "Kinder Bueno", "stock": 2},#ça c lle kinder 
    "A2": {"nom": "Kinder Bueno White", "stock": 2},#ça c le kinder white 
    "A3": {"nom": "Twix", "stock": 3},# ça c le twix
    "A4": {"nom": "Mars", "stock": 3},# ça c le mars
    "A5": {"nom": "Snickers", "stock": 2},#ça les snickers
    "B1": {"nom": "Cola+", "stock": 9},#ça c le coca plus
    "B2": {"nom": "Fanta", "stock": 8},#ça c le fanta
    "B3": {"nom": "Sprite", "stock": 7},#ça c le sprite
    "B4": {"nom": "Ice Tea", "stock": 6},#ça ice tea
    "B5": {"nom": "Eau", "stock": 10},#ça eauuu
    "C1": {"nom": "Chips Nature", "stock": 4},#ça chips
    "C2": {"nom": "Chips Paprika", "stock": 4},#ça chips aussi mais avec du paprika
    "C3": {"nom": "Pringles", "stock": 3},#ça c le premieum du chips normal
    "C4": {"nom": "Doritos", "stock": 3},#ça c les chips normal mais americain
    "C5": {"nom": "Epstein", "stock": 2},#Attention le boug est dangereux
    "D1": {"nom": "Haribo", "stock": 5},#haribo c'est pour la vie pour les grands et les petits
    "D2": {"nom": "Dragibus", "stock": 5},#le bleu c'est le meilleur
    "D3": {"nom": "Tagada", "stock": 4},#comme le cheval ou quooi
    "D4": {"nom": "Skittles", "stock": 4},#personellemnt je troouve ça trres sucre
    "D5": {"nom": "M&M's", "stock": 3},#pue sa mere dit ethan tres en colere 
    "E1": {"nom": "Biscuit Chocolat", "stock": 3},#pas tres original chat gpt
    "E2": {"nom": "Camion citerne", "stock": 3},#tres utile au quotidien
    "E3": {"nom": "iphone 5+", "stock": 4},#go back to 2012
    "E4": {"nom": "Carte gold de trump", "stock": 2},#meme moi j'en veux pas 
    "E5": {"nom": "cable a paire torsades", "stock": 2}#big up a vivien
}#la on ferme le stock
choix = int(input("Tapez 1 pour voir le stock, tapez 2 pour acheter un produit : "))#la ça vous fait tapez pour soit voir le stock sois acheter
#ici ç'est un saut de ligne 
if choix == 1:#la c'est si tu tape 1 ca te fait faire le script en dessous
    for code in distri:#la on dit que chaqque truc dans la liste on l'appelle pouuuuurrr
        print(code, "-", distri[code]["nom"], ":", distri[code]["stock"])#iciiii ou cv afficher tout le stock
#encore un saut de ligne mais woow
elif choix == 2:#ici si tu a voulu acheter merci de la confiance
    code = input("Tu veux quoi").upper()#la c'est pour dire tvq et .lower va faire que si t'ecris en miniscule ou en maj cv rien changer
#UN SAUT DE LIGNE UN SAUT DE LIGNE UN SAUT DE LIGNE UN SAUT DE LIGNE UN SAUT DE LIGNE !!!!!
    if code in distri:#la on posee un if pour le choiix du produit attention boululu va venir
        if distri[code]["stock"] > 0:#la il check si y'as encore du stock
            distri[code]["stock"] -= 1#la il enleve si t'as bien taper le produit que tu voulais ahahahaha
            print("Produit acheté :", distri[code]["nom"])#la ça te confirme l'achat
            print("Stock restant :", distri[code]["stock"])#la ca montre combien il en reste
        else:#la c'est else il faitt peur au debut mais apres cv 
            print("Produit en rupture de stock")#deso va dans un autre distributeur y'as plus
    else:#encore else il est tres nice vous avez vu
        print("Code produit invalide")#la ta pas bien tape mon reuf
#SAAAAAAAAAAUUUUUUUUUUUUTTTTTTTTTT DEEEE LLLLLIIIIIIIIIIIGGGGNNNNNNNNNNEEEEEEEEEEEEE
else:#else else else else
    print("Choix invalide")#chosis les kinder c mieux

