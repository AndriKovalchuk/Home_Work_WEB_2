from poetry_personal_assistant.main import DataEntryValidation, FolderOrganizer, PersonalAssistant


def main():
    validation = DataEntryValidation()
    sorter = FolderOrganizer()
    assistant = PersonalAssistant(validation, sorter)
    assistant.load()
    assistant.load_notes()
    assistant.run()


if __name__ == "__main__":
    main()
