from colorama import Fore, Style

DEAD_END_PRINT = f'\n{Fore.LIGHTRED_EX}You got to a point where you can not find any other entrance and there is no ' \
                 f'way back because \nall ' \
                 f'the other dungeons have already been flooded. You start feeling the breath of death slowly\n' \
                 f'approaching towards your feet, you close your eyes trying to anticipate the amount of time left\n' \
                 f'for you before you will not be able to breathe ever again... \nHold on! What is it? Is it some' \
                 f'kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon entrance,' \
                 f'again! You slowly walk into this dungeon and hear water filling up the first room again... \n' \
                 f'it is time to keep going if you do not wanna end up like the last time!{Style.RESET_ALL}\n'

NO_TIME_PRINT = f"{Fore.LIGHTRED_EX}It seems like you have been awake for so long that you can't move on and you have " \
                f"to rest\n " \
                f"for a while, you put your head on the ground and close your eyes. While sleeping, you realise\n that " \
                f"there is too much water coming out of everywhere so you get up, try to escape this room\n but it's " \
                f"too late now and the water is getting closer and closer to your neck.\n You close your eyes for the " \
                f"last time thinking of everything you could have done if you did not get into this dungeon..." \
                f"\nHold on! What is it? Is it some" \
                f"kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon entrance," \
                f"again! You slowly walk into this dungeon and hear water filling up the first room again... \n" \
                f"it is time to keep going if you do not wanna end up like the last time!\n{Style.RESET_ALL}"

HATCH_FOUND_PRINT = f"{Fore.YELLOW}You've found a hatch! You can see the light coming out from the other side and you " \
                    f"fresh " \
                    f"air blowing into your face!\n Should you try to open it up? Do you think you are powerful " \
                    f"enough? \nYes/No{Style.RESET_ALL}"

TRY_OPEN_HATCH_PRINT = f'{Fore.LIGHTRED_EX}You are trying to open up the hatch and finally get out from ' \
                       f'this dungeon. However, you ' \
                       f'feel that you did not gain enough power and experience during this\n journey so you can not ' \
                       f'lift the lid, it is too heavy for you! You start feeling the breath of death slowly\n' \
                       f'approaching towards your feet, you close your eyes trying to anticipate the amount of ' \
                       f'time left\n ' \
                       f'for you before you will not be able to breathe ever again... \nHold on! What is it? Is it ' \
                       f'some ' \
                       f'kind of miracle? For some mysterious reason you open your eyes and see \nthe same dungeon ' \
                       f'entrance, ' \
                       f'again! You slowly walk into this dungeon and hear water filling up the first room ' \
                       f'again... \n ' \
                       f'it is time to keep going if you do not wanna end up like the last time!{Style.RESET_ALL}\n'

END_GAME_PRINT = f'{Fore.YELLOW}You managed to open up the hatch and get out from this dungeon! ' \
                 f'Congratulations!{Style.RESET_ALL}'

CLOSE_HATCH_CHOICE = f'{Fore.YELLOW}You decided to keep the hatch closed and stay in the dungeon forever... ' \
                     f'(Why Would you choose ' \
                     f'it?){Style.RESET_ALL}'
