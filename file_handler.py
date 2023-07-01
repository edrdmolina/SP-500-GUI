from os import name, system, chmod, listdir, path, rename, scandir, stat
from natsort import natsorted
import shutil
import datetime
import time


class SP500DirHandler:

    def __init__(self, customer_initials, order_number, roll_number, roll_qty, order_notes, initial_dir, temp_dir, target_dir):
        self.customer_initials = customer_initials
        self.order_number = order_number
        self.roll_number = roll_number
        self.roll_qty = roll_qty
        self.order_notes = order_notes
        self.initial_dir = initial_dir
        self.temp_dir = temp_dir
        self.target_dir = target_dir

    @staticmethod
    def get_monday():
        """

        :return: Returns a string dictating the calendar date of the monday
        """
        today = datetime.date.today()
        days_since_monday = today.weekday()
        monday = today - datetime.timedelta(days=days_since_monday)
        return monday.strftime('%m-%d-%y')

    @staticmethod
    def move_directory(old_dir, new_dir):
        """
        This functions moves a directory to a target directory using shutil and ignoring certain errors
        :param old_dir: Path to the directory you are trying to move
        :param new_dir: Path to the location you are trying to move to
        """
        try:
            shutil.move(old_dir, new_dir)
        except OSError as e:
            if e.errno == 95:
                pass
            elif e.errno == 2:
                pass

    @staticmethod
    def get_order_rolls(initial_dir, roll_qty, reverse):
        """
        This function returns a list containing the most recent subdirectories in a specified initial directory
        :param initial_dir: Directory where all the files are located
        :param roll_qty: How many subdirectories will be moved
        :param reverse: Setting Reverse as True will return list in descending order.
        :return: returns a list of all the rolls in the order
        """

        subdirectories = [f.path for f in scandir(initial_dir) if f.is_dir()]
        sorted_subdirectories = sorted(subdirectories, key=lambda x: stat(x).st_ctime_ns, reverse=reverse)

        return sorted_subdirectories[:roll_qty]

    @staticmethod
    def update_file_name(roll, basename):
        counter = 1
        files = natsorted(listdir(roll))

        for file in files:
            extension = str(path.splitext(file)[1]).lower()
            if extension == ".jpg" or extension == ".jpeg":
                new_name = f"{basename}-{counter:03d}.jpg"
                rename(path.join(roll, file), path.join(roll, new_name))
                counter += 1
            elif extension == ".tiff" or extension == '.tif':
                new_name = f"{basename}-{counter:03d}.tiff"
                rename(path.join(roll, file), path.join(roll, new_name))
                counter += 1
            time.sleep(0.25)

    @staticmethod
    def create_formatted_name(customer_initials, order_number, roll_number):
        return f"{customer_initials}-{order_number}-{roll_number}"

    @staticmethod
    def create_file_with_string(file_path, string_to_write):
        with open(file_path, 'w') as file:
            file.write(string_to_write)

    def run(self):
        self.target_dir = path.join(self.target_dir, self.get_monday())

        initial_rolls = self.get_order_rolls(self.initial_dir, self.roll_qty, reverse=False)
        print(initial_rolls)

        for roll in initial_rolls:
            formatted_basename = self.create_formatted_name(self.customer_initials, self.order_number, self.roll_number)
            self.move_directory(roll, path.join(self.temp_dir, formatted_basename))
            time.sleep(0.25)
            self.roll_number = f"{(int(self.roll_number) + 1):04d}"

        rolls_in_temp = self.get_order_rolls(self.temp_dir, self.roll_qty, reverse=True)
        print(rolls_in_temp)

        for roll in rolls_in_temp:
            self.update_file_name(roll, path.basename(roll))
            time.sleep(0.25)
            # create a text file and add roll notes.
            if len(self.order_notes) > 0:
                self.create_file_with_string(path.join(roll, "Order Notes.txt"), self.order_notes)

            self.move_directory(roll, path.join(self.target_dir, path.basename(roll)))
            time.sleep(0.25)
