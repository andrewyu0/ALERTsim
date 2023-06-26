def load_case_laws(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        case_laws = file.readlines()

    return case_laws