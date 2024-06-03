import os
import time
import sys
import glob


files = []
numFilesInList = 50
showFullPath = False


def findItems(path):
    for root, folders, items in os.walk(path):
        for file in items:
            try:
                fileToShow = file

                #append the root to the fileToShow if fullpath flag set
                if showFullPath:
                    fileToShow = root + fileToShow
                    
                files.append((os.stat(root + os.sep + file).st_size, fileToShow))

            except(FileNotFoundError):
                continue

            except(OSError):
                continue


def main():
    global numFilesInList
    global showFullPath

    #cool banner
    banner = """
             _               _               _
            /\ \            /\ \            /\ \\
           /  \ \          /  \ \          /  \ \\
          / /\ \ \        / /\ \ \        / /\ \ \\
         / / /\ \_\      / / /\ \_\      / / /\ \_\\
        / / /_/ / /     / / /_/ / /     / / /_/ / /
       / / /__\/ /     / / /__\/ /     / / /__\/ /
      / / /_____/     / / /_____/     / / /_____/
     / / /\ \ \      / / /\ \ \      / / /\ \ \\
    / / /  \ \ \    / / /  \ \ \    / / /  \ \ \\
    \/_/    \_\/    \/_/    \_\/    \/_/    \_\/

    """
    print(banner, end='')
    print("\n", "-"*55)
    if len(sys.argv) <= 1 or "-h" in sys.argv:
        print("ex. python3 rrr.py /home/")
        print("ex. python3 rrr.py /home/ -f")
        print("-h for help")
        print("-f for full file path")
        print("-n for number of files to show (from biggest to smallest)")
        exit()

    #argument handling
    if "-f" in sys.argv:
        showFullPath = True
    try:
        found = sys.argv.index("-n")
        if found != -1:
            numFilesInList = int(sys.argv[found + 1])
    except(ValueError):
        pass

    #grab starting path
    startPath = sys.argv[1]
    print("Selected:", startPath, "\nThis may take a moment...")
    findItems(startPath)

    #sort files to get access
    files.sort()
    
    for i in range(len(files) - 1, len(files) - numFilesInList - 1, -1):
        try:
            print("\nName:", files[i][1], "\nSize in bytes:", files[i][0])
        except(IndexError):
            continue


if __name__ == "__main__":
    try:
        start = time.time()
        main()
        print("Finished in", time.time() - start)

    except(KeyboardInterrupt):
        exit()
