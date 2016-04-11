import csv
import os
import sys

class Movie:

    def __inti__(self, movie_id, mov_tittle, zhanra_1, zhanra_2, zhanra_3, zhanra_4, movie_rating, user_id):
        self.id = movie_id
        self.tittle = tittle
        self.zhanra_1 = zhanra_1
        self.zhanra_2 = zhanra_2
        self.zhanra_3 = zhanra_3
        self.zhanra_4 = zhanra_4
        self.movie_rating = movie_rating
        self.user_id = user_id


    def __str__(self):

        return ('{}: {}'.format(self.id, self.tittle))

class User:

    def __inti__(self, user_id, user_age, user_gender, user_occup, user_zip, user_mov_amt, user_rating, movie_id):

        self.user_id = user_id
        self.user_age = user_age
        self.user_gender = user_gender
        self.user_occup = user_occup
        self.user_zip = user_zip
        self.user_mov_amt = user_mov_amt
        self.user_rating = user_rating
        self.movie_id = movie_id


class MovieRatings:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    #def find_movie(self, dict_of_ratings):
    #    pass
#-----------------------------------------------

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

#-------------------------------------------

def catch_invalid_input(user_input_1, user_input_2):

    if user_input_1 != 0:
        if not user_input_1.isdigit() or int(user_input_1) > 4:
            input("Invalid input. Press enter to continue!... " )
            return True
        else:
            return False

    if user_input_2.isdigit():
        return user_input_2
    else:
        print('\n')
        input('Invalid entry..!!')
        return False



#-----------------------------

def get_ratings_by_movie_id(user_movie_id):

    again = False
    not_found = True

    while True:
        os.system('clear')
        if again:
            print('\n')
            user_movie_id = catch_invalid_input(0,input('Enter the movie ID: '))
            if not user_movie_id:
                return 0

        with open ('u.data') as ratings_file:

            reader = csv.DictReader(ratings_file, fieldnames=('user_id', 'movie_id', 'rating', ""), delimiter="\t")

            ratings_count = 0
            count_line = 4
            print_there(2,35,'----------------------------------------------')
            print_there(3,35,'No.  -  Movie Id  -  Movie Rating  -  User ID')
            print_there(4,35,'----------------------------------------------')

            sum_ratings = 0
            for row in reader:

                if user_movie_id == row['movie_id']:
                    ratings_count += 1
                    count_line += 1
                    info = str(ratings_count) + '        ' + row['movie_id'] + '              ' + row['rating'] + '            ' + row['user_id']
                    print_there(count_line,35, info)
                    info = ''
                    sum_ratings += float(row['rating'])
                    not_found = False


                if count_line == 23:
                    os.system('clear')
                    print_there(2,35,'----------------------------------------------')
                    print_there(3,35,'No.  -  Movie Id  -  Movie Rating  -  User ID')
                    print_there(4,35,'----------------------------------------------')
                    count_line = 4

        if not_found:
            print('\n')
            input('Movie not found..!!')


        elif not not_found:
            total_movie = str(ratings_count)
            ave_rating = str(round((sum_ratings / ratings_count),1))
            print_there(25,27,'|-----------------------------------------------------------|')
            print_there(26,27,'  Movie ID: ' + user_movie_id + '   Total ratings: ' + total_movie + '    ' + 'Average Rating: ' + ave_rating)
            print_there(27,27,'|-----------------------------------------------------------|')
            not_found = True

        print('\n')
        other_movie_again = input("Another Movie? Y/N..:").lower()
        os.system('clear')
        if other_movie_again == 'y':
            again = True
            continue
        else:
            return 0

#----------------------------------------------------------

def get_movie_name(user_movie_id):

    again = False
    not_found = True
    while True:
        os.system('clear')

        print_there(4,35,'---------------------------------------------------------------')
        print_there(5,42,'     Movie Id  -  Movie Name')
        print_there(6,35,'--------------------------------------------------------------')

        if again:
            print('\n')
            user_movie_id = catch_invalid_input(0,input('Enter the movie ID: '))
            if not user_movie_id:
                return 0

        with open ('u.item', encoding='latin_1') as movie_file:

            reader = csv.DictReader(movie_file, fieldnames=('movie_id', 'movie_tittle', ""), delimiter="|")

            for row in reader:

                if user_movie_id == row['movie_id']:
                    print_there(8,49, row['movie_id'] + '        ' + row['movie_tittle'])
                    not_found = False

        if not_found:
            print('\n')
            input('Movie not found..!!')
            not_found = True

        print('\n')
        other_movie_again = input("Another Movie? Y/N..:").lower()
        os.system('clear')
        if other_movie_again == 'y':
            again = True
            continue
        else:
            return 0

#-----------------------------------------------------------

def get_ratings_of_user(user_id):

    again = False
    not_found = True
    while True:
        os.system('clear')
        if again:
            print('\n')
            user_id = catch_invalid_input(0,input('Enter the User ID: '))
            if not user_id:
                return 0

        with open ('u.data') as ratings_file:

            reader = csv.DictReader(ratings_file, fieldnames=('user_id', 'movie_id', 'rating', ""), delimiter="\t")

            ratings_count = 0
            count_line = 4
            print_there(2,35,'----------------------------------------------')
            print_there(3,35,'No.  -  User Id  -  Movie Ratings  -  Movie ID')
            print_there(4,35,'----------------------------------------------')

            user_sum_ratings = 0
            for row in reader:

                if user_id == row['user_id']:
                    ratings_count += 1
                    count_line += 1
                    info = str(ratings_count) + '        ' + row['user_id'] + '              ' + row['rating'] + '            ' + row['movie_id']
                    print_there(count_line,35, info)
                    info = ''
                    user_sum_ratings += float(row['rating'])
                    not_found = False

                if count_line == 29:
                    os.system('clear')
                    print_there(2,35,'----------------------------------------------')
                    print_there(3,35,'No.  -  User Id  -  Movie Ratings  -  Movie ID')
                    print_there(4,35,'----------------------------------------------')
                    count_line = 4
        if not_found:
            print('\n')
            input('User not found..!!')


        elif not not_found:
            total_ratings = str(ratings_count)
            print_there(31,27,'|-----------------------------------------------------------|')
            print_there(32,27,'               User ID: ' + user_id + '   Total ratings: ' + total_ratings)
            print_there(33,27,'|-----------------------------------------------------------|')
            not_found = True


        print('\n')
        other_movie_again = input("Another User? Y/N..:").lower()
        os.system('clear')
        if other_movie_again == 'y':
            again = True
            continue
        else:
            return 0


#-----------------------------------------------------------

def get_menu_choices(choice):

    if catch_invalid_input(choice, 0):
        return 0

    # Find all ratings of a movie by mopvie ID and rating average
    elif int(choice) == 1:

        user_movie_id = catch_invalid_input(0,input('Enter the movie ID: '))

        if user_movie_id != False:
            return get_ratings_by_movie_id(user_movie_id)

    #Find a movie by ID
    elif int(choice) == 2:

        user_movie_id = catch_invalid_input(0,input('Enter the movie ID: '))

        return get_movie_name(user_movie_id)

    # Find all ratings of an user by User ID
    elif int(choice) == 3:

        user_id = catch_invalid_input(0,input('Enter the movie ID: '))
        return get_ratings_of_user(user_id)




#-----------------------------------------------------------

def main():

    while True:

        os.system('clear')
        print('WELCOME TO MOVIE_FLIX')
        print('\n\n')
        print('MAIN MENU:\n')
        print('1.) Find all ratings of a movie by movie ID its average rating \n')
        print('2.) Find a movie by ID\n')
        print('3.) Find all ratings of an user by User ID\n')
        print('4.) Quit Program\n\n\n')

        user_menu_choice = input("Choose a number option and press enter: ")

        if catch_invalid_input(user_menu_choice,0):
            continue
        else:
            if get_menu_choices(user_menu_choice) == 0:
                continue
            else:
                print('\n\n')
                print("Bye... Have a Nice Day!")
                print('\n\n')
                sys.exit()




if __name__ == '__main__':
    main()




















        #     #
        # print(count)
#         ratings_dict = (MovieRatings(row['user_id'], row['movie_id'], row['rating']))
#         movie_rartings_list.append(ratings_dict.movie_id)
#         movie_rartings_list.append(ratings_dict.rating)
#
# user_movie_id = input('Enter the movie ID: ')
# #print(ratings_dict.movie_id)
#input()
#
#
# count = 0
# for list_row in movie_rartings_list:
#     count += 1
#     print(movie_rartings_list)
#     input('hey')
#     print(len(movie_rartings_list))
#     input()
#     print(list_row)
#     print(len(list_row))
#     print(type(list_row))
#
#
#
#     input()
#     if user_movie_id == list_row:
#         print(list_row.movie_id, ' ', list_row.rating)
#         input()
#     #
# print(count)


# print(ratings_dict)
# #input()
#print(ratings_dict)
#print(ratings_dict.user_id, " ", ratings_dict.movie_id)
        #print(ratings_dict.user_id)


        #movies[movie_id] = movie
#print(ratings_dict)
#type(ratings_dict)
    #
    # movie_list = [movies[key] for key in movies]
    #
    # print(movie_list)
    #
    #
    # for movie in movies_list
    #     print(movie.tittle)
    #
    # user_input = input('Enter part of movie tittle: ').lower()
    #
    # for movie in movies_list
    #
    #     if user_input == movies_list.tittle.lower():
    #         print(movie)
    #
    #
    #
    # id = input("Enter your movie id: ")
    #





#
# with open (u.item, encoding='latin_1') as item_file :
#     reader = csv.reader(f)
#     #reader = csv.DictReader(item_file, delimiter="|", fieldname=['movie_i', 'tittle'])
#     headers = next(reader)
#     print(headers)
#     print('------')
#     for row in reader
#         movie = (Movie(row['movie_id'], row['tittle']))
#         movies[movie_id] = movie
#




#
# movie_list = [movies[key] for key in movies]
#
# print(movie_list)
#
#
# for movie in movies_list
#     print(movie.tittle)
#
# user_input = input('Enter part of movie tittle: ').lower()
#
# for movie in movies_list
#
#     if user_input == movies_list.tittle.lower():
#         print(movie)
#
#
#
# id = input("Enter your movie id: ")
#

#
#
#
# ____________________________
# for key in movies:
#      movies_list.append(movies[key])
#
#
#
#
# id = input("enter id: ")
#
#
# print(str(movies[id])
