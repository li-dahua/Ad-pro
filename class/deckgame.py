from deck import DeckOfCards
deck_of_cards = DeckOfCards()
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

path = Path('.').joinpath('card_images')

figure,axes_list = plt.subplots(nrows=4, ncols=13)
figure.tight_layout()
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name =deck_of_cards.deal_card().image_name
    img =mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

deck_of_cards.shuffle()
g= plt.figure(1)
figure,axes_list =plt.subplots(nrows=4, ncols=13)
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name=deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
#g .show()
plt.show()
figure.tight_layout()

plt.close('all')