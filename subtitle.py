# ----------------------------------------------------------------- find function
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


# ----------------------------------------------------------------- generate pattern function
def get_pattern(number, extension):
    return '*E' + str(number).zfill(2) + '*.' + extension


# ----------------------------------------------------------------- find file function
def find_file(extension):
    arr = []
    episode_number = 1
    find_array = find(get_pattern(episode_number, extension), './')
    while len(find_array) > 0:
        if len(find_array) > 1:
            print('There is no unique file with this pattern: ' + get_pattern(episode_number, extension))
            break
        arr.append(find_array[0][0:-4])
        episode_number = episode_number + 1
        find_array = find(get_pattern(episode_number, extension), './')
    return arr


# ----------------------------------------------------------------- find video files
videoFiles = find_file('mkv')


# ----------------------------------------------------------------- find subtitle files
subtitleFiles = find_file('srt')


# ----------------------------------------------------------------- renaming
for i in range(len(subtitleFiles)):
    os.rename(subtitleFiles[i] + '.srt', videoFiles[i] + '.srt')
