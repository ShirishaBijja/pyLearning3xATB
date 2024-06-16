def allowed_to_attend_python_class(name):
    match name:
        case "Dell":
            print("Dell is allowed")

        case "Amit":
            print("Amit is allowed")
        case "Spim":
            print("Spim is allowed")
        case _:
            print("Not allowed")

allowed_to_attend_python_class("Dell")
