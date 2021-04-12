import ujson
import mysql.connector
from mysql.connector import errorcode
import argparse
import datetime
import os
import pathlib
import markdown


def parse_args():
    parser = argparse.ArgumentParser(description='Process input arguments.')
    parser.add_argument("-e", "--event", help="name of the event this memory belongs to", type=str)
    parser.add_argument("-d", "--date", help="date or start date of the event in format YYYY_MM_DD",
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    # TODO Almost; use datetime.date.fromisoformat(), not datetime.datetime.fromisoformat().
    # .. TODO You want a date object, not a datetime object
    parser.add_argument("-t", "--tag", help="mark your memory with tag(s)", type=str)
    parser.add_argument("-m", "--memory", help="describe your memory", type=str)

    args = parser.parse_args()
    print(args.memory)


class ProgramSettings:
    """
    TODO
    """
    def __init__(self):
        pass


class Memory:
    """
    TODO
    """
    def __init__(self):
        self.memory_name = None  # short name of event
        self.description = None  # formatted text (bolt text, odstavce, ...)
        self.tags_list = []
        self.start_date = None
        self.end_date = None
        self.path_to_preview_img = None
        self.path_to_gallery = None

    def set_memory_name(self, memory_name):
        self.memory_name = memory_name

    def set_description(self, description):
        self.description = description

    def add_tag(self, tag):
        if tag not in self.tags_list:
            self.tags_list.append(tag)

    def set_start_date(self, start_date):
        # TODO validate date
        self.start_date = start_date

    def set_end_date(self, end_date):
        # TODO validate date
        self.end_date = end_date

    def set_path_to_preview_img(self, path):
        """
        If Not set, first (random) gallery photo will be taken as preview image.
        :param path:
        :return:
        """
        self.path_to_preview_img = pathlib.Path(path)

    def set_path_to_gallery(self, path):
        self.path_to_gallery = pathlib.Path(path).name

    def format_as_dictionary(self):
        """
        TODO: misto tech local variables udeat local jen tuto a do ni to vse davat rovnou.
        """
        memory_dict = {}
        memory_dict["memory_name"] = self.memory_name
        memory_dict["description"] = self.description
        memory_dict["tags"] = self.tags_list
        memory_dict["start_date"] = self.start_date
        memory_dict["end_date"] = self.end_date
        memory_dict["path_to_preview_img"] = self.path_to_preview_img
        memory_dict["path_to_gallery"] = self.path_to_gallery
        return memory_dict


# def save_json(self, path):
#     # TODO path check, move into json module
#     file = open("JsonExample.json", "r")
#     SuperHeros = ujson.load(file)
#

# def load_json(self, path):
#     # TODO path check, move into json module
#     file = open("JsonExample.json", "r")
#         SuperHeros = ujson.load(file)


def insert_memory_to_db(memory_obj):
    """
    insert memory into db
    """
    pass


def convert_memory_to_json(memory_obj):
    output_json = ujson.dumps(memory_obj, indent=4)
    return output_json
    pass


def convert_json_to_memory(json_memory):
    """
    converts one memory retrieved from whole json into dictionary
    :param json_memory:
    :return:
    """
    output_memory = ujson.loads(json_memory)
    return output_memory


# class MemoryToJson:
#    def __init__(self):


if __name__ == "__main__":
    config = {
        'user': 'valgrut',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'MemoriesArchive',
        'raise_on_warnings': True
    }
    memories_db = ""
    try:
        memories_db = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Everything OK")

        parse_args()

        # TEST
        memory1 = Memory()
        memory1.set_memory_name("Prehrada v Krumsine")
        memory1.set_description("V Krumsine jsme s Davou u sudu u slepic vyhloubili malou prehradu a privod. \n Do nej jsme zahranovali cestu vode pomoci bridlicovych desticek a zkouseli, jestli nase opatreni vydrzi naval vody, ktery jsme vzdy lili z toho sudu.")
        memory1.add_tag("krumsin")
        memory1.add_tag("david")
        memory1.add_tag("hrani")
        memory1.add_tag("voda")
        memory1.set_start_date("2008-07-19")
        memory1.set_path_to_gallery("/home/valgrut/Pictures/Orlik")

        json_memory = convert_memory_to_json(memory1.format_as_dictionary())
        print(json_memory)
        print(convert_json_to_memory(json_memory))

        memories_db.close()
