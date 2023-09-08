import configparser
import json


def main():
    # Q3
    with open('my_file.txt', 'r') as file:
        print(file.read())
    with open('my_file.txt', 'w') as file:
        file.write("Hello world")
    
    #  Q4
    config = configparser.ConfigParser()
    config.add_section('section')
    config.set('section', 'data', 'hello world')
    config.set('section', 'silent', 'True')
    with open(f"configfile.txt", 'w') as configfile:
        config.write(configfile)
    config.read("configfile.txt") 
    data_value = config.get('section', 'data')
    silent_value = config.get('section', 'silent')
    config.set('section', 'data', data_value.upper())
    if silent_value == "True":
        print(data_value.upper())
    
    # Q6
    with open('my_json.txt') as json_file:
        json_dict = json.load(json_file)
    print(json_dict)
    json_dict["name"] = "Maya"  
    json_dict["age"] = "19"
    json_dict["city"] = "Shoham"
    with open('my_new_json.txt', 'w') as json_file:
        json.dump(json_dict, json_file)
    
if __name__ == "__main__":
    main()