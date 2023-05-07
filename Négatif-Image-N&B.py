from PIL import Image
def negatif (coul) :
    neg_coul = 1 - coul
    return neg_coul
name = "(image-name).png"
image = Image.open (name)
colonnes,lignes = image.size
nouvelle_image = Image.new ('1',(colonnes,lignes))
for y in range (lignes) :
    for x in range (colonnes) :
        pixel = image.getpixel((x,y))
        couleur = pixel[0]
        neg_couleur = negatif (couleur)
        nouvelle_image.putpixel ((x,y), neg_couleur)
nouvelle_image.save ("Négatif_" + name)
print ("Programme terminé. Image Négatif_" + name + "créée")
