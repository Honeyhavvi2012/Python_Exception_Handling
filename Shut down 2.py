def shutdown(user_input):
    if user_input == "Yes":
        return "Shutting down"
    elif user_input == "No":
        return "Abort shut down"
    else:
        return "Sorry"

def main():
    user_input = input("Do you want to shut down the system? (Yes/No): ")
    result = shutdown(user_input)
    print(result)

if __name__ == "__main__":
    main()
