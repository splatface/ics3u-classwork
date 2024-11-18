
def main():
    print("1. Butterfly")
    print("2. Elephant")
    print("3. Teddy Bear")
    print("4. Snake")

    choice = int(input("\nWhich animal to draw? "))
    print()

    if choice == 1:
        butterfly()
        butterfly()
        # will draw the butterfly twice now instead of once because it is called twice
    elif choice == 2:
        elephant()
    elif choice == 3:
        # write code here to call the function named 'teddybear' 
        teddybear()
    elif choice == 4:
        # write code here to call the function named 'snake'
        snake()
    else:
        print("Sorry, that wasn't one of the choices.")

    print("\nGoodbye!")
	
	
def butterfly():
    print("  .==-.                   .-==.     ")
    print("   \\()8`-._  `.   .'  _.-'8()/     ")
    print("   (88\"   ::.  \\./  .::   \"88)     ")
    print("    \\_.'`-::::.(#).::::-'`._/      ")
    print("      `._... .q(_)p. ..._.'         ")
    print("        \"\"-..-'|=|`-..-\"\"       ")
    print("        .\"\"' .'|=|`. `\"\".       ")
    print("      ,':8(o)./|=|\\.(o)8:`.        ")
    print("     (O :8 ::/ \\_/ \\:: 8: O)      ")
    print("      \\O `::/       \\::' O/       ")
    print("       \"\"--'         `--\"\"   hjw")
	
	
def elephant():
    print("       _..--\"\"-.                  .-\"\"--.._ ")
    print("   _.-'         \\ __...----...__ /         '-._")
    print(" .'      .:::...,'              ',...:::.      '.")
    print("(     .'``'''::;                  ;::'''``'.     )")
    print(" \\             '-)              (-'             /")
    print("  \\             /                \\             /")
    print("   \\          .'.-.            .-.'.          /")
    print("    \\         | \\0|            |0/ |         /")
    print("    |          \\  |   .-==-.   |  /          |")
    print("     \\          `/`;          ;`\\`          /")
    print("      '.._      (_ |  .-==-.  | _)      _..'")
    print("          `\"`\"-`/ `/'        '\\` \\`-\"`\"`")
    print("               / /`;   .==.   ;`\\ \\")
    print("         .---./_/   \\  .==.  /   \\ \\")
    print("        / '.    `-.__)       |    `\"")
    print("       | =(`-.        '==.   ;")
    print(" jgs    \\  '. `-.           /")
    print("         \\_:_)   `\"--.....-'")

	
def teddybear():
    print("            ___   .--. ")
    print("      .--.-\"   \"-' .- |")
    print("     / .-,`          .'")
    print("     \\   `           \\")
    print("      '.            ! \\")
    print("        |     !  .--.  |")
    print("        \\        '--'  /.____")
    print("       /`-.     \\__,'.'      `\\")
    print("    __/   \\`-.____.-' `\\      /")
    print("    | `---`'-'._/-`     \\----'    _")
    print("    |,-'`  /             |    _.-' `\\")
    print("   .'     /              |--'`     / |")
    print("  /      /\\              `         | |")
    print("  |   .\\/  \\      .--. __          \\ |")
    print("   '-'      '._       /  `\\         /")
    print("      jgs      `\\    '     |------'`")
    print("                 \\  |      |")
    print("                  \\        /")
    print("                   '._  _.'")
    print("                      ``")

	
def snake():
    print("         ,,'6''-,.")
    print("        <====,.;;--.")
    print("        _`---===. \"\"\"==__")
    print("      //\"\"@@-\\===\\@@@@ \"\"\\\\")
    print("     |( @@@  |===|  @@@  ||")
    print("      \\\\ @@   |===|  @@  //")
    print("        \\\\ @@ |===|@@@ //")
    print("         \\\\  |===|  //")
    print("___________\\\\|===| //_____,----\"\"\"\"\"\"\"\"\"\"-----,_")
    print("  \"\"\"\"---,__`\\===`/ _________,---------,____    `,")
    print("             |==||                           `\\   \\")
    print("            |==| |          pb                 )   |")
    print("           |==| |       _____         ______,--'   '")
    print("           |=|  `----\"\"\"     `\"\"\"\"\"\"\"\"         _,-'")
    print("            `=\\     __,---\"\"\"-------------\"\"\"''")
    print("                \"\"\"\"		")


if __name__ == "__main__":
    main()