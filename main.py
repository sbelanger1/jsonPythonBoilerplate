import json
# Declare file name with our sample JSON data
file_name = 'sampleData.json'


# Main function
def main():
    # Open the file
    file_contents = open(file_name)
    # Convert the file to a json string so python can work with it
    file_json = json.load(file_contents)
    # Print the content of the file
    print("Printing json file contents:")
    print(file_json)

    # Interacting directly with the json is pretty easy.
    # We can get at the nested objects data directly if we know exactly what we need from each object.
    # This will pull a bit of data from the first item in the array (array index 0)
    # Note that the JSON data type is just a number, which python won't print unless we string convert using str(data)
    print("Age of first actor is: " + str(file_json['Actors'][0]['age']))

    # We can also pull the same data from the second actor (array index 1)
    print("Age of second actor is: " + str(file_json['Actors'][1]['age']))

    # Let's loop through some JSON and see what we can pull.
    # Since "Actors" is an array, we need a loop to go through each actor sub-object so we can get at the contents.
    for actor in file_json['Actors']:
        # now each "actor" object contains the entirety of the json sub-object.
        # So 'actor' object contains something like this on the first loop:
        '''
        {
            "name": "Tom Cruise",
            "age": 56,
            "Born At": "Syracuse, NY",
            "Birthdate": "July 3, 1962",
            "photo": "https://jsonformatter.org/img/tom-cruise.jpg",
            "wife": null,
            "weight": 67.5,
            "hasChildren": true,
            "hasGreyHair": false,
            "children": [
                "Suri",
                "Isabella Jane",
                "Connor"
            ]
        }
        '''
        # We can reference values in our sub-object using the syntax actor['key']
        # For now let's print out the name:
        print("Actor Name is: " + actor['name'])

        # If there are sub-arrays in there we can add an additional loop to get at their contents one at a time:
        for child in actor['children']:
            print(actor['name'] + " has a child named: " + child)

        # alternatively we can just print out that whole array if we want, but we have to convert it to string
        # but this can be useful to just display some content for testing purposes.
        print("Actor " + actor['name'] + " has children named: " + str(actor['children']))

    # Close our file so it's not write locked some something dumb like that.
    file_contents.close()


# This code indicates that this is a script that should be run directly.  Usually we put these in the main script that
# starts our python program.  This lets other devs know that this is the starting point.  Other files that we import
# into this file don't need this line, only files that need to be run directly.
# See also: https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()

