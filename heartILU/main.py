import colorama
from colorama import Fore

colorama.init()

iloveYou = '\n'.join([''.join([('C'[(x-y)%len('C')] if
                                ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30, 30)])
                                for y in range(15, -15, -1)])

print(Fore.LIGHTMAGENTA_EX + iloveYou)
print("I love you!")