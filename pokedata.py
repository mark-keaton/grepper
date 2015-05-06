from __future__ import unicode_literals
from __future__ import print_function
from itertools import count
from pathlib import Path

import json

import pykemon
import requests

from pykemon.request import ResourceNotFoundError

base_path = Path('C:/pokemon/karston')
output_path = base_path / 'pokedata.txt'
image_path = base_path / 'images'


# def write_pokemon(name, moves, evolutions, types):
#     with output_path.open('a') as file_:
#         formatted_moves = ', '.join(moves)
#         formatted_evolutions = ', '.join(evolutions)
#         formatted_types = ', '.join(types)
#         args = (name, formatted_moves, formatted_evolutions, formatted_types)
#         print(*args, sep='\t', file=file_)
#
#
# def get_pokedata():
#     for i in count(1):
#         try:
#             mon = pykemon.get(pokemon_id=i)
#             name = mon.name
#             moves = mon.moves.keys()
#             evolutions = mon.evolutions.keys()
#             types = mon.types.keys()
#
#             write_pokemon(name, moves, evolutions, types)
#         except ResourceNotFoundError:
#             break


sprite_dict = dict()
def get_sprites():
    domain = 'http://pokeapi.co/'
    base_api_uri = domain + 'media/img/{}.png'
    for i in count(1):
        sprite_uri = base_api_uri.format(i)
        # json_response = requests.get(sprite_uri, stream=True)
        # sprite_dict = json.loads(json_response.text)
        # lower_name = sprite_dict.get('pokemon').get('name')
        # full_uri = domain + sprite_dict.get('image')
        response = requests.get(sprite_uri, stream=True)
        if response.ok:
            out_image_path = image_path / '{i}.png'.format(**locals())
            with out_image_path.open('wb') as file_:
                for chunk in response.iter_content():
                    file_.write(chunk)
            i += 1
        else:
            break



def main():
    # get_pokedata()
    get_sprites()

if __name__ == '__main__':
    main()