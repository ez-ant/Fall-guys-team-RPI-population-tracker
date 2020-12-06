import tkinter as tk
#set window
window = tk.Tk()
window.geometry("1000x700")
# to maximize window
#w, h = window.winfo_screenwidth(), window.winfo_screenheight()
#window.geometry("%dx%d+0+0" % (w, h))

class Building:
    def __init__(self, name, button):
        self.name = name
        self.button = button
        self.button.configure(highlightbackground = "yellow")
    def change_color(self, color):
        self.button.configure(highlightbackground = color)


class Building_Test:
    def test(self):
        # test 1: test case of creating a new Building successfully
        # create a Building class with name "Test" and a button and 
        # then check if it is created successfully
        button = tk.Button(text = "Button")
        test_building = Building("Test", button)
        # check if the building name is Test
        assert test_building.name == "Test"
        # check if the building contains a button with text "Button"
        assert test_building.button.cget("text") == "Button"
        # check if the button's color is yellow"
        assert test_building.button.cget("highlightbackground") == "yellow"
        print("Test Case 1 Pass")

        # test 2: test case of creating a new Building without Button (expect to fail)
        # create a Building class with name "Test" without button (expect to fail)
        try:
            # if test_building create successfully, this test case end in failure
            test_building = Building("Test", new_button)
            raise Exception ("Test Case 2 Fail")
        except:
            # success otherwise
            print("Test Case 2 Pass")

        # test 3: test function change_color() within Building class
        # create a Building class and then change its color to red
        button2 = tk.Button(text = "Button")
        test_building2 = Building("Test", button)
        test_building2.change_color("red")
        # check if the button's color change to red
        assert test_building.button.cget("highlightbackground") == "red"
        print("Test Case 3 Pass")

        # test 4: test function change_color() within Building class
        # create a Building class and then use change_color with empty string input
        button2 = tk.Button(text = "Button")
        test_building2 = Building("Test", button)
        try:
            # if change_color() works successfully, this test case end in failure
            test_building2.change_color("")
            raise Exception ("Test Case 4 Fail")
        except:
            # success otherwise
            print("Test Case 4 Pass")

        
        # test 5: test function change_color() within Building class
        # create a Building class and then use change_color with ambiguous string input(string that is not color)
        button3 = tk.Button(text = "Button")
        test_building3 = Building("Test", button)
        try:
            # if change_color() works successfully, this test case end in failure
            test_building3.change_color("hello")
            raise Exception ("Test Case 5 Fail")
        except:
            # success otherwise
            print("Test Case 5 Pass")


def read_database(a,b):
    return
def update_database(command):
    return

class update_database_test:
    def test(self):
        # regular case of updating data
        # update database: set west hall's capacity to 100
        command = "Updata building_database Set capacity = 100 where building = \"West\""
        update_database(command)
        # read the capacity of west hall from database
        assert read_database("capacity", "west") == 100
        print("Test Case 1 Pass")

        # error case of updating data
        # call update_database when command is null
        command = ""
        try:
            # if update_database() works successfully, this test case end in failure
            update_database(command)
            raise Exception ("Test Case 2 Fail")
        except:
            # success otherwise
            print("Test Case 2 Pass")

        # error case of updating data
        # call update_database when command contains syntax error
        command = "Hello World"
        try:
            # if update_database() works successfully, this test case end in failure
            update_database(command)
            raise Exception ("Test Case 3 Fail")
        except:
            # success otherwise
            print("Test Case 3 Pass")

        # error case of updating data
        # call update_database with incorrect/unreasonable number
        command = "Updata building_database Set capacity = -1 where building = \"West\""
        try:
            # if update_database() works successfully, this test case end in failure
            update_database(command)
            raise Exception ("Test Case 4 Fail")
        except:
            # success otherwise
            print("Test Case 4 Pass")

        # error case of updating data
        # call update_database with non-exist building
        command = "Updata building_database Set capacity = -1 where building = \"Google\""
        try:
            # if update_database() works successfully, this test case end in failure
            update_database(command)
            raise Exception ("Test Case 5 Fail")
        except:
            # success otherwise
            print("Test Case 5 Pass")



        

if __name__ == "__main__":
    test = Building_Test()
    test.test()


