class People:
    def __init__(self) -> None:
        self._people_names_list = []

    @property
    def people_names_list(self):
        return self._people_names_list

    def add_person(self, new_name: str) -> None:
        self._people_names_list.append(new_name)

    def __iter__(self) -> object:
        self.index = 0
        return self
    
    def __next__(self):
        if len(self.people_names_list) + 1 <= self.index + 1:
            del self.index
            raise StopIteration
        self.index += 1
        return self.people_names_list[self.index - 1]



def main():
    people = People()
    people.add_person("maya")
    people.add_person("koral")
    for person in people:
        print(person)

if __name__ == "__main__":
    main()