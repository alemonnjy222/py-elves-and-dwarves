from players.player import Player
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf
def calculate_team_total_rating(team: list[Player]):
    return sum(player.get_rating() for player in team)

def elves_concert(elfs: list[Elf]):
   for elf in elfs:
       elf.play_elf_song()
def feast_of_the_dwarves(dwarfs: list[Dwarf]):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()