def convert(str):
   str = str.replace(":)","😀")
   str = str.replace(":(","☹️")
   return str
def main():
    x = input()
    print(convert(x))
main()