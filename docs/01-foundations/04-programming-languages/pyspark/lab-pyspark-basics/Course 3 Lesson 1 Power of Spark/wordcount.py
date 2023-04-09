# %%file is an Ipython magic function that saves the code cell as a file


from mrjob.job import MRJob # import the mrjob library

class MRSongCount(MRJob):
    
    # the map step: each line in the txt file is read as a key, value pair
    # in this case, each line in the txt file only contains a value but no key
    # _ means that in this case, there is no key for each line
    def mapper(self, _, song):
        # output each line as a tuple of (song_names, 1) 
        yield (song, 1)

    # the reduce step: combine all tuples with the same key
    # in this case, the key is the song name
    # then sum all the values of the tuple, which will give the total song plays
    def reducer(self, key, values):
        yield (key, sum(values))
        
if __name__ == "__main__":
    MRSongCount.run()