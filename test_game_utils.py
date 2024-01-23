import words_game_utils.py as wg
from colorama import Fore


def test_check_guess():
    assert wg.check_guess("Prone", "Prneo") == [2, 2, 1, 1, 1]
    assert wg.check_guess("Query", "xxxxx") == [0, 0, 0, 0, 0]
    assert wg.check_guess("Poops", "Poops") == [2, 2, 2, 2, 2]
  
    assert wg.check_guess("whats", "thwsa") == [1, 1, 1, 1, 1]
    assert wg.check_guess("xxxxx", "Pxxxrneo") == None
    
    
def test_color_string():
    assert wg.color_string([2, 2, 2, 2, 2], 'Point') == Fore.GREEN + '[P]' + '[o]' + '[i]' + '[n]' + '[t]'
    assert wg.color_string([2, 0, 2, 0, 2], 'Point') == Fore.GREEN + '[P]' + Fore.RED + 'o' + Fore.GREEN + '[i]' + Fore.RED + 'n' + Fore.GREEN + '[t]'
    assert wg.color_string([1, 2, 1, 0, 2], 'Point') == Fore.YELLOW + '(P)' + Fore.GREEN + '[o]' + Fore.YELLOW + '(i)' + Fore.RED + 'n' + Fore.GREEN + '[t]'
    assert wg.color_string([1, 1, 1, 1, 1], 'Point') == Fore.YELLOW + '[P]' + '[o]' + '[i]' + '[n]' + '[t]'
    assert wg.color_string([0, 0, 0, 0, 0], 'Point') == Fore.RED + '[P]' + '[o]' + '[i]' + '[n]' + '[t]'
    

def test_collection_menu():
    assert wg.collection_menu([("idk1", {"value": 0}), ("idk2", {"iuyfuy": 0})]) == "Collections\n1   idk1\n2    idk2"
    assert wg.collection_menu([("idk1", {"value": 0}), ("idk2", {"iuyfuy": 0}), ("idk3", {"iuyfuy": 0})]) == "COLLECTIONS\n1    idk1\n2    idk2\n3    idk3"
    assert wg.collection_menu([("idk1", {"value": 0})]) == "COLLECTIONS\n1    idk1"
    assert wg.collection_menu([("idk1", {"value": 0}), ("idk2", {"iuyfuy": 0})]) == "Collections\n1   idk1\n2    idk2"
    