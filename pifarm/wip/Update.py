from subprocess import check_call as run

#setlocal
# set DEPOT=https://github.com/fringebits/PiFarm.git

def main():

    run('git fetch --all --tags')
    run('git checkout release')

if __name__ == "__main__":
    main()