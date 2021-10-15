from service_coordinator import run_service_coordinator
def main():
    '''
    This function allows the user to start the app
    with or without debug mode, and put the ip and port
    of the coordinator app
    '''
    host = '0.0.0.0'
    port = 5000
    run_service_coordinator(host, port)

if __name__ == '__main__':
    main()
    pass
