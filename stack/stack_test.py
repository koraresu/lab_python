from parenthesis import check_bracket
from tail import get_tail
import os

def test_checking():
	assert check_bracket('(()') == 2
	assert check_bracket(')()())') == 4
	assert check_bracket(')()())') ==  4
	assert check_bracket(')()())))') == 4
	assert check_bracket('(((())))))))))))))))))') == 8



file = (os.path.dirname(__file__))+'/pokemon_data.csv'

def test_tail():
	assert get_tail(file,3) == ['720,HoopaHoopa Confined,Psychic,Ghost,80,110,60,150,130,70,6,TRUE\n', '720,HoopaHoopa Unbound,Psychic,Dark,80,160,60,170,130,80,6,TRUE\n', '721,Volcanion,Fire,Water,80,110,120,130,90,70,6,TRUE\n']
	assert get_tail(file,10) == ['714,Noibat,Flying,Dragon,40,30,35,45,40,55,6,FALSE\n', '715,Noivern,Flying,Dragon,85,70,80,97,80,123,6,FALSE\n', '716,Xerneas,Fairy,,126,131,95,131,98,99,6,TRUE\n', '717,Yveltal,Dark,Flying,126,131,95,131,98,99,6,TRUE\n', '718,Zygarde50% Forme,Dragon,Ground,108,100,121,81,95,95,6,TRUE\n', '719,Diancie,Rock,Fairy,50,100,150,100,150,50,6,TRUE\n', '719,DiancieMega Diancie,Rock,Fairy,50,160,110,160,110,110,6,TRUE\n', '720,HoopaHoopa Confined,Psychic,Ghost,80,110,60,150,130,70,6,TRUE\n', '720,HoopaHoopa Unbound,Psychic,Dark,80,160,60,170,130,80,6,TRUE\n', '721,Volcanion,Fire,Water,80,110,120,130,90,70,6,TRUE\n']