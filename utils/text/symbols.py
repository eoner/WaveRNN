""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''

_pad = '_'
_punctuation = '!\'"(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_tr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÖÜÇŞĞİabcdefghijklmnopqrstuvwxyzöüçşğı'

# Export all symbols:
symbols_en = [_pad] + list(_special) + list(_punctuation) + list(_letters) 
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters_tr)