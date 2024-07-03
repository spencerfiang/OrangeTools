import core.process as process
import core.train

def c_main(path, num, ext):
    image_data = process.pre_process(path, num, ext)
    return image_data[1] + '.' + ext


def train_main(content_path,style_path,training_count,learning_rate):
    core.train.train(content_path,style_path,training_count,learning_rate)

if __name__ == '__main__':
    pass


